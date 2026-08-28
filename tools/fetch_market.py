#!/usr/bin/env python3
"""每天抓一次市場資料，存進 data/。

資料源全部免費、無需 API key：
  月營收   證交所 / 櫃買中心 OpenAPI
  估值     證交所 BWIBBU_ALL / 櫃買中心本益比分析
  新聞     Google News RSS

用法：
    python3 tools/fetch_market.py            抓全部
    python3 tools/fetch_market.py --no-news  跳過新聞（比較快）
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import date, datetime
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watchlist import COMPANIES, OFF_CHAIN  # noqa: E402

KB = Path(__file__).resolve().parent.parent
DATA = KB / "data"
LOG = DATA / "fetch.log"

RETRIES = 3
BACKOFF = 5
TIMEOUT = 30
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh) KnowledgeBase/1.0"}

SOURCES = {
    "revenue_twse": "https://openapi.twse.com.tw/v1/opendata/t187ap05_L",
    "revenue_tpex": "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O",
    "valuation_twse": "https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL",
    "valuation_tpex": "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis",
}


def log(msg: str) -> None:
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line)
    DATA.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def get(url: str, parse_json: bool = True):
    """抓一個網址，失敗重試 3 次。全部失敗就拋例外，不回半殘資料。"""
    last = None
    for attempt in range(1, RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            resp.raise_for_status()
            return resp.json() if parse_json else resp.text
        except Exception as exc:  # noqa: BLE001
            last = exc
            log(f"⚠️  第 {attempt}/{RETRIES} 次失敗：{url} — {exc}")
            if attempt < RETRIES:
                time.sleep(BACKOFF)
    raise RuntimeError(f"{url} 重試 {RETRIES} 次仍失敗：{last}")


def _num(value):
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return None


def _roc_to_iso(roc: str) -> str:
    """民國日期 1150827 → 2026-08-27。"""
    roc = str(roc).strip()
    if len(roc) == 7 and roc.isdigit():
        return f"{int(roc[:3]) + 1911}-{roc[3:5]}-{roc[5:]}"
    return roc


def fetch_revenue(codes: set) -> dict:
    rows = get(SOURCES["revenue_twse"]) + get(SOURCES["revenue_tpex"])
    out, period = {}, None
    for r in rows:
        code = r.get("公司代號")
        if code not in codes:
            continue
        period = period or r.get("資料年月")
        out[code] = {
            "name": r.get("公司名稱"),
            "industry": r.get("產業別"),
            "period": r.get("資料年月"),
            "revenue": _num(r.get("營業收入-當月營收")),
            "mom_pct": _num(r.get("營業收入-上月比較增減(%)")),
            "yoy_pct": _num(r.get("營業收入-去年同月增減(%)")),
            "cum_revenue": _num(r.get("累計營業收入-當月累計營收")),
            "cum_yoy_pct": _num(r.get("累計營業收入-前期比較增減(%)")),
            "note": (r.get("備註") or "").strip(),
        }
    return {"period": period, "companies": out}


def fetch_valuation(codes: set) -> dict:
    out, as_of = {}, None
    for r in get(SOURCES["valuation_twse"]):
        code = r.get("Code")
        if code in codes:
            as_of = as_of or _roc_to_iso(r.get("Date"))
            out[code] = {
                "name": r.get("Name"),
                "per": _num(r.get("PEratio")),
                "pbr": _num(r.get("PBratio")),
                "yield_pct": _num(r.get("DividendYield")),
            }
    for r in get(SOURCES["valuation_tpex"]):
        code = r.get("SecuritiesCompanyCode")
        if code in codes:
            as_of = as_of or _roc_to_iso(r.get("Date"))
            out[code] = {
                "name": r.get("CompanyName"),
                "per": _num(r.get("PriceEarningRatio")),
                "pbr": _num(r.get("PriceBookRatio")),
                "yield_pct": _num(r.get("YieldRatio")),
            }
    return {"as_of": as_of, "companies": out}


def fetch_news(code: str, name: str, limit: int = 5) -> list:
    """Google News RSS。日後要換 Perplexity 只需改這個函式。"""
    query = urllib.parse.quote(f"{name} {code}")
    url = f"https://news.google.com/rss/search?q={query}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    try:
        xml = get(url, parse_json=False)
        root = ET.fromstring(xml)
    except Exception as exc:  # noqa: BLE001
        log(f"⚠️  {code} {name} 新聞抓取失敗：{exc}")
        return []
    items = []
    for item in root.findall(".//item")[:limit]:
        title = (item.findtext("title") or "").strip()
        source = item.findtext("{*}source") or ""
        items.append({
            "title": re.sub(r"\s+-\s+[^-]+$", "", title),
            "publisher": source or title.rsplit(" - ", 1)[-1],
            "link": (item.findtext("link") or "").strip(),
            "published": (item.findtext("pubDate") or "").strip(),
        })
    return items


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)  # 先寫暫存再換名，避免中途失敗留下半殘檔案


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-news", action="store_true", help="跳過新聞抓取")
    args = parser.parse_args()

    codes = set(COMPANIES) | set(OFF_CHAIN)
    today = date.today().isoformat()
    log(f"=== 開始抓取（{len(codes)} 檔）===")

    try:
        valuation = fetch_valuation(codes)
        write_json(DATA / "valuation" / f"{today}.json", valuation)
        log(f"✅ 估值 {len(valuation['companies'])} 檔（資料日 {valuation['as_of']}）")

        revenue = fetch_revenue(codes)
        period = revenue["period"]
        if period:
            iso = f"{int(period[:3]) + 1911}-{period[3:]}"
            write_json(DATA / "revenue" / f"{iso}.json", revenue)
            log(f"✅ 月營收 {len(revenue['companies'])} 檔（{iso}）")
        else:
            log("⚠️  月營收無資料")
    except Exception as exc:  # noqa: BLE001
        log(f"❌ 抓取中止：{exc}")
        return 1

    if not args.no_news:
        news, missing = {}, []
        for code, (name, _) in COMPANIES.items():
            items = fetch_news(code, name)
            news[code] = items
            if not items:
                missing.append(code)
            time.sleep(0.6)  # 對 Google 客氣一點，避免被擋
        write_json(DATA / "news" / f"{today}.json", {"date": today, "companies": news})
        log(f"✅ 新聞 {len(news) - len(missing)}/{len(news)} 檔有結果"
            + (f"，無結果：{','.join(missing)}" if missing else ""))

    log("=== 抓取完成 ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
