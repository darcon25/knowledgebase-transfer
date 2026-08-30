#!/usr/bin/env python3
"""回補歷史月營收。

證交所／櫃買的 OpenAPI 只給當期快照，抓不到過去。歷史資料要從公開資訊
觀測站的月報表 HTML 解析（Big5 編碼）。

用法：
    python3 tools/backfill_revenue.py            回補過去 12 個月
    python3 tools/backfill_revenue.py --months 6
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watchlist import COMPANIES, OFF_CHAIN  # noqa: E402

KB = Path(__file__).resolve().parent.parent
DATA = KB / "data" / "revenue"
BASE = "https://mopsov.twse.com.tw/nas/t21/{market}/t21sc03_{roc}_{month}_0.html"


def fetch_html(market: str, roc: int, month: int) -> str:
    url = BASE.format(market=market, roc=roc, month=month)
    result = subprocess.run(["curl", "-sS", "--fail", "--max-time", "40", url],
                            capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(f"下載失敗 {url}")
    return result.stdout.decode("big5", errors="ignore")


def _num(text: str):
    text = text.replace(",", "").strip()
    try:
        return float(text)
    except ValueError:
        return None


def parse(html: str, codes: set) -> dict:
    out = {}
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        cells = [re.sub("<[^>]+>", "", c).replace("&nbsp;", " ").strip()
                 for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        if len(cells) < 8 or cells[0] not in codes:
            continue
        cur, last, last_year = _num(cells[2]), _num(cells[3]), _num(cells[4])
        cum, cum_last = _num(cells[6]), _num(cells[7])
        out[cells[0]] = {
            "name": cells[1],
            "revenue": cur,
            # 這兩個成長率官方 HTML 沒給完整，用原始數字自己算
            "mom_pct": round((cur / last - 1) * 100, 2) if cur and last else None,
            "yoy_pct": round((cur / last_year - 1) * 100, 2) if cur and last_year else None,
            "cum_revenue": cum,
            "cum_yoy_pct": round((cum / cum_last - 1) * 100, 2) if cum and cum_last else None,
            "note": "",
            "source": "MOPS 歷史月報表",
        }
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--months", type=int, default=12, help="往回補幾個月")
    args = parser.parse_args()

    codes = set(COMPANIES) | set(OFF_CHAIN)
    today = date.today()
    done, skipped = 0, 0

    for back in range(1, args.months + 1):
        total = today.year * 12 + today.month - 1 - back
        year, month = total // 12, total % 12 + 1
        iso = f"{year}-{month:02d}"
        path = DATA / f"{iso}.json"
        if path.exists():
            skipped += 1
            continue
        roc = year - 1911
        companies = {}
        for market in ("sii", "otc"):
            try:
                companies.update(parse(fetch_html(market, roc, month), codes))
            except Exception as exc:  # noqa: BLE001
                print(f"⚠️  {iso} {market} 失敗：{exc}")
        if not companies:
            print(f"⚠️  {iso} 無資料，跳過")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(
            {"period": f"{roc}{month:02d}", "companies": companies,
             "source": "backfill"}, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✅ {iso}：{len(companies)} 檔")
        done += 1

    print(f"\n完成：新增 {done} 個月，已存在跳過 {skipped} 個月")
    return 0


if __name__ == "__main__":
    sys.exit(main())
