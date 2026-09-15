#!/usr/bin/env python3
"""從公開資訊觀測站（MOPS）回補歷史季度損益表。

為什麼需要：`fetch_market.py` 抓的 `t187ap17_L` **只有最新一季**，
所以 `data/margin/` 長期只有一個檔，看不出毛利率趨勢——
而毛利率是漲價循環的**領先指標**（營收 YoY 還撐著時，毛利率會先反轉）。
2026-09-15 做 CCL 成長持續性檢驗時，這就是最大的資料缺口。

資料來源：MOPS 綜合損益表 `ajax_t163sb04`（上市 sii／上櫃 otc），一次回傳全市場。
民國年制：西元 2026 = 民國 115。

用法：
    python3 tools/fetch_financials.py                 # 回補最近 8 季
    python3 tools/fetch_financials.py --quarters 12   # 回補 12 季
    python3 tools/fetch_financials.py --year 115 --season 2   # 只抓單季
"""
import argparse
import html
import json
import re
import sys
import time
from pathlib import Path

import requests

KB = Path(__file__).resolve().parent.parent
OUT = KB / "data" / "financials"
sys.path.insert(0, str(KB / "tools"))
from watchlist import COMPANIES, OFF_CHAIN  # noqa: E402

URL = "https://mopsov.twse.com.tw/mops/web/ajax_t163sb04"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36",
}
PAUSE = 3          # MOPS 會擋太密集的請求
TIMEOUT = 60

WANTED = set(COMPANIES) | set(OFF_CHAIN)


def log(m):
    print(m, flush=True)


def fetch(typek: str, year: int, season: int) -> str:
    """typek: sii=上市 otc=上櫃"""
    data = {
        "encodeURIComponent": "1", "step": "1", "firstin": "1", "off": "1",
        "isQuery": "Y", "TYPEK": typek, "year": str(year), "season": f"{season:02d}",
    }
    r = requests.post(URL, headers=HEADERS, data=data, timeout=TIMEOUT)
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text


def to_num(t: str):
    t = t.replace(",", "").strip()
    if t in ("--", "", "-"):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def parse(page: str) -> dict:
    """抽出觀察名單公司的損益數字。

    欄位順序（實測 2026-09-15）：
      [0]代號 [1]名稱 [2]營業收入 [3]營業成本 [6]營業毛利 … [-1]基本每股盈餘
    ⚠️ 中間欄位會因產業別（金融業另有表格）而不同，所以只取頭尾這幾個可靠的。
    """
    out = {}
    for m in re.finditer(r"<tr[^>]*>(.*?)</tr>", page, re.S):
        cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
                 for c in re.findall(r"<td[^>]*>(.*?)</td>", m.group(1), re.S)]
        if len(cells) < 10:
            continue
        code = cells[0]
        if code not in WANTED:
            continue
        rev, cost, gross = to_num(cells[2]), to_num(cells[3]), to_num(cells[6])
        eps = to_num(cells[-1])
        if rev is None:
            continue
        rec = {"name": cells[1], "revenue": rev, "cost": cost, "gross_profit": gross, "eps": eps}
        if gross is not None and rev:
            rec["gross_margin"] = round(gross / rev * 100, 2)
        out[code] = rec
    return out


def quarters_back(n: int):
    """從最近『已公布』的一季往回數 n 季。

    ⚠️ 財報有公布時程：Q1 約 5 月、Q2 約 8 月、Q3 約 11 月、Q4（年報）約隔年 3 月。
    所以「當下季度」通常還沒有資料，要往回退。
    """
    from datetime import date
    d = date.today()
    y, mth = d.year - 1911, d.month
    if mth >= 11:       season = 3
    elif mth >= 8:      season = 2
    elif mth >= 5:      season = 1
    else:               y, season = y - 1, 4
    res = []
    for _ in range(n):
        res.append((y, season))
        season -= 1
        if season == 0:
            y, season = y - 1, 4
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quarters", type=int, default=8)
    ap.add_argument("--year", type=int)
    ap.add_argument("--season", type=int)
    ap.add_argument("--force", action="store_true", help="已存在也重抓")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    targets = ([(args.year, args.season)] if args.year and args.season
               else quarters_back(args.quarters))

    done = skipped = 0
    for y, s in targets:
        path = OUT / f"{y + 1911}Q{s}.json"
        # ⚠️ 不能只看檔案存在就跳過——觀察名單擴編後，舊檔的公司數會不足。
        #    backfill_revenue.py 就是這樣讓 23 家新公司補不到歷史的。
        if path.exists() and not args.force:
            try:
                have = len(json.loads(path.read_text(encoding="utf-8"))["companies"])
            except Exception:
                have = 0
            if have >= len(WANTED) * 0.8:
                log(f"⏭  {path.name} 已有 {have} 家，跳過")
                skipped += 1
                continue
            log(f"♻️  {path.name} 只有 {have} 家（名單 {len(WANTED)} 家），重抓")

        merged = {}
        for typek, label in (("sii", "上市"), ("otc", "上櫃")):
            try:
                page = fetch(typek, y, s)
            except Exception as e:
                log(f"   ❌ {y}Q{s} {label} 抓取失敗：{e}")
                continue
            got = parse(page)
            merged.update(got)
            log(f"   {label} {len(got)} 家")
            time.sleep(PAUSE)

        if not merged:
            log(f"❌ {y + 1911}Q{s} 無資料（可能尚未公布）")
            continue
        path.write_text(json.dumps(
            {"period": f"{y}Q{s}", "roc_year": y, "season": s, "companies": merged},
            ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        log(f"✅ {path.name}：{len(merged)} 家")
        done += 1

    log(f"\n完成：新增/更新 {done} 季，跳過 {skipped} 季")
    return 0


if __name__ == "__main__":
    sys.exit(main())
