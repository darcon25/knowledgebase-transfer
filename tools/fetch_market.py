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
import subprocess
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
    "margin_twse": "https://openapi.twse.com.tw/v1/opendata/t187ap17_L",
    "margin_tpex": "https://www.tpex.org.tw/openapi/v1/mopsfin_187ap17_O",
}


def log(msg: str) -> None:
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line)
    DATA.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def _curl(url: str) -> str:
    """用 curl 取代 requests。

    櫃買中心（tpex.org.tw）用的 TWCA 憑證缺 Subject Key Identifier，
    新版 OpenSSL 會直接拒絕，但 curl 走 macOS 系統信任庫可以驗過。
    這是備援路徑，**憑證仍然有驗證**，不是關掉檢查。
    """
    result = subprocess.run(
        ["curl", "-sS", "--fail", "--max-time", str(TIMEOUT), "-A", HEADERS["User-Agent"], url],
        capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"curl 失敗：{result.stderr.strip()[:200]}")
    return result.stdout


def get(url: str, parse_json: bool = True):
    """抓一個網址，失敗重試 3 次。全部失敗就拋例外，不回半殘資料。"""
    last = None
    for attempt in range(1, RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            resp.raise_for_status()
            return resp.json() if parse_json else resp.text
        except requests.exceptions.SSLError as exc:
            log(f"ℹ️  {url} 憑證驗證失敗，改用 curl 備援")
            try:
                text = _curl(url)
                return json.loads(text) if parse_json else text
            except Exception as curl_exc:  # noqa: BLE001
                last = curl_exc
                log(f"⚠️  第 {attempt}/{RETRIES} 次失敗（curl 備援也失敗）：{curl_exc}")
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


def fetch_margin(codes: set) -> dict:
    """季度營益分析：毛利率、營業利益率、稅前／稅後純益率。

    月營收看不出漲價有沒有吃到獲利，毛利率才看得出來。季度資料，比月營收慢。
    """
    out, period = {}, None
    for r in get(SOURCES["margin_twse"]):
        code = r.get("公司代號")
        if code in codes:
            period = period or f"{r.get('年度')}Q{r.get('季別')}"
            out[code] = {
                "name": r.get("公司名稱"),
                "period": f"{r.get('年度')}Q{r.get('季別')}",
                "revenue_mn": _num(r.get("營業收入(百萬元)")),
                "gross_margin": _num(r.get("毛利率(%)(營業毛利)/(營業收入)")),
                "op_margin": _num(r.get("營業利益率(%)(營業利益)/(營業收入)")),
                "pretax_margin": _num(r.get("稅前純益率(%)(稅前純益)/(營業收入)")),
                "net_margin": _num(r.get("稅後純益率(%)(稅後純益)/(營業收入)")),
            }
    for r in get(SOURCES["margin_tpex"]):
        code = r.get("SecuritiesCompanyCode")
        if code in codes:
            period = period or f"{r.get('Year')}Q{r.get('季別')}"
            out[code] = {
                "name": r.get("CompanyName"),
                "period": f"{r.get('Year')}Q{r.get('季別')}",
                "revenue_mn": _num(r.get("營業收入百萬元")),
                "gross_margin": _num(r.get("毛利率")),
                "op_margin": _num(r.get("營業利益率")),
                "pretax_margin": _num(r.get("稅前純益率")),
                "net_margin": _num(r.get("稅後純益率")),
            }
    return {"period": period, "companies": out}


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

        margin = fetch_margin(codes)
        if margin["period"]:
            roc = margin["period"]                      # 例：115Q2
            iso = f"{int(roc[:3]) + 1911}{roc[3:]}"     # 例：2026Q2
            write_json(DATA / "margin" / f"{iso}.json", margin)
            log(f"✅ 毛利率 {len(margin['companies'])} 檔（{iso}）")
        else:
            log("⚠️  毛利率無資料")
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
