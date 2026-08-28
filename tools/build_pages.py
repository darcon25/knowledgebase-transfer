#!/usr/bin/env python3
"""用 data/ 的資料產生／更新 wiki/investing/ 的頁面。

原則：程式只寫 <!-- AUTO:START --> 到 <!-- AUTO:END --> 之間的內容，
其餘（你的論點、觀察指標、筆記）永遠不動。
"""
import json
import re
import sqlite3
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watchlist import (COMPANIES, OFF_CHAIN, SEGMENT_DESC, SEGMENT_ORDER,  # noqa: E402
                       companies_in, name_of, neighbours, peers)

KB = Path(__file__).resolve().parent.parent
DATA = KB / "data"
INV = KB / "wiki" / "investing"
TRADES_DB = Path("/Users/mmfamily/Maxtrading Review/data/trades.db")

AUTO_START = "<!-- AUTO:START 由 tools/build_pages.py 產生，此區塊會被覆寫 -->"
AUTO_END = "<!-- AUTO:END -->"


def latest(folder: str):
    files = sorted((DATA / folder).glob("*.json"))
    if not files:
        return None, None
    return json.loads(files[-1].read_text(encoding="utf-8")), files[-1].stem


def load_positions() -> dict:
    """唯讀讀取 Maxtrading Review 的持倉，判斷持有／曾交易／觀察。"""
    if not TRADES_DB.exists():
        return {}
    con = sqlite3.connect(f"file:{TRADES_DB}?mode=ro", uri=True)
    try:
        held = {
            row[0]: {"quantity": row[1], "avg_price": row[2], "unrealized": row[3]}
            for row in con.execute(
                "SELECT code, quantity, avg_price, unrealized_pnl FROM positions "
                "WHERE date = (SELECT MAX(date) FROM positions)")
        }
        traded = {row[0] for row in con.execute(
            "SELECT DISTINCT code FROM trades WHERE date >= date('now','-365 day')")}
    finally:
        con.close()
    out = {}
    for code in set(held) | traded:
        out[code] = {"status": "持有" if code in held else "曾交易", **held.get(code, {})}
    return out


def fmt_period(roc_period) -> str:
    """民國年月 11507 → 2026-07。"""
    roc = str(roc_period or "")
    if len(roc) == 5 and roc.isdigit():
        return f"{int(roc[:3]) + 1911}-{roc[3:]}"
    return roc or "—"


def fmt_yi(thousand_ntd) -> str:
    """千元 → 億元。"""
    if thousand_ntd is None:
        return "—"
    return f"{thousand_ntd / 100000:,.2f} 億"


def fmt_pct(value) -> str:
    if value is None:
        return "—"
    return f"{value:+.1f}%"


def fmt_x(value) -> str:
    return "—" if value is None else f"{value:.1f}x"


def write_auto(path: Path, auto_body: str, fresh_template: str) -> str:
    """更新 AUTO 區塊；檔案不存在才用範本建立。回傳 created / updated。"""
    block = f"{AUTO_START}\n{auto_body.strip()}\n{AUTO_END}"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = path.read_text(encoding="utf-8")
        pattern = re.compile(
            re.escape(AUTO_START) + r".*?" + re.escape(AUTO_END), re.DOTALL)
        if pattern.search(old):
            path.write_text(pattern.sub(lambda _: block, old, count=1), encoding="utf-8")
            return "updated"
        path.write_text(old.rstrip() + "\n\n" + block + "\n", encoding="utf-8")
        return "updated"
    path.write_text(fresh_template.replace("{{AUTO}}", block), encoding="utf-8")
    return "created"


def build_company(code, rev, val, news, positions) -> str:
    name, segment = COMPANIES[code]
    up, down = neighbours(code)
    r = rev.get(code, {})
    v = val.get(code, {})
    pos = positions.get(code)

    lines = [f"## 定位\n",
             f"**環節**：[[{segment}]]　{SEGMENT_DESC[segment]}\n"]
    flow = []
    if up:
        flow.append(f"上游 [[{up}]]")
    flow.append(f"**本身 {segment}**")
    if down:
        flow.append(f"下游 [[{down}]]")
    lines.append("**傳導位置**：" + " → ".join(flow) + "\n")
    peer_links = "、".join(f"[[{c} {name_of(c)}]]" for c in sorted(peers(code)))
    lines.append(f"**同環節同業**：{peer_links or '（此環節目前只有這一家）'}\n")

    status = pos["status"] if pos else "觀察"
    if pos and pos.get("quantity"):
        status += f"（{pos['quantity']:,} 股，均價 {pos['avg_price']:.2f}，未實現 {pos['unrealized']:+,.0f}）"
    lines.append(f"**持倉狀態**：{status}\n")

    lines.append("## 數據\n")
    lines.append("| 指標 | 數值 |")
    lines.append("|---|---|")
    lines.append(f"| 月營收（{fmt_period(r.get('period'))}）| {fmt_yi(r.get('revenue'))} |")
    lines.append(f"| 月增 MoM | {fmt_pct(r.get('mom_pct'))} |")
    lines.append(f"| 年增 YoY | {fmt_pct(r.get('yoy_pct'))} |")
    lines.append(f"| 累計營收年增 | {fmt_pct(r.get('cum_yoy_pct'))} |")
    lines.append(f"| 本益比 PER | {fmt_x(v.get('per'))} |")
    lines.append(f"| 股價淨值比 PBR | {fmt_x(v.get('pbr'))} |")
    yield_pct = v.get("yield_pct")
    lines.append(f"| 殖利率 | {'—' if yield_pct is None else f'{yield_pct:.2f}%'} |")
    if r.get("note") and r["note"] != "-":
        lines.append(f"\n**公司對營收變化的說法**：{r['note']}\n")

    items = news.get(code, [])
    lines.append("\n## 近期新聞\n")
    if items:
        for it in items:
            lines.append(f"- [{it['title']}]({it['link']})　<sub>{it['publisher']}</sub>")
    else:
        lines.append("（近期無相關新聞）")
    return "\n".join(lines)


TEMPLATE_COMPANY = """---
tags: [investing, company]
code: {code}
name: {name}
segment: {segment}
updated: {today}
---

# {code} {name}

{{{{AUTO}}}}

## 我的論點

（為什麼追蹤這家？看多還看空？依據是什麼？）

## 觀察指標

（該盯什麼數字才知道論點對不對？例如月營收 YoY 連續三個月、銅價、稼動率）

## 事件時間軸

（消化新資料時，把重要事件按日期加在這裡）

## 還缺什麼

（要做出判斷，還需要哪些資訊？）
"""


def build_segment(segment, rev, val, positions) -> str:
    members = sorted(companies_in(segment), key=lambda c: -(rev.get(c, {}).get("yoy_pct") or -999))
    i = SEGMENT_ORDER.index(segment)
    up = SEGMENT_ORDER[i - 1] if i > 0 else None
    down = SEGMENT_ORDER[i + 1] if i < len(SEGMENT_ORDER) - 1 else None

    lines = [f"**這個環節在做什麼**：{SEGMENT_DESC[segment]}\n"]
    flow = " → ".join(filter(None, [f"[[{up}]]" if up else None,
                                    f"**{segment}**",
                                    f"[[{down}]]" if down else None]))
    lines.append(f"**位置**：{flow}\n")
    lines.append(f"**所屬產業鏈**：[[AI伺服器PCB鏈]]\n")
    lines.append("## 成員\n")
    lines.append("| 公司 | 月營收 YoY | 本益比 | 持倉 |")
    lines.append("|---|---|---|---|")
    for code in members:
        pos = positions.get(code, {}).get("status", "觀察")
        lines.append(f"| [[{code} {name_of(code)}]] | {fmt_pct(rev.get(code, {}).get('yoy_pct'))} "
                     f"| {fmt_x(val.get(code, {}).get('per'))} | {pos} |")
    return "\n".join(lines)


TEMPLATE_SEGMENT = """---
tags: [investing, segment]
segment: {segment}
updated: {today}
---

# {segment}

{{{{AUTO}}}}

## 這個環節現在的狀況

（供需鬆緊？報價漲跌？誰吃到最多？）

## 相關驅動因素

（例如 [[銅價]]、[[HBM4]]）
"""


def build_chain(rev, val, positions, rev_period, val_date) -> str:
    lines = [f"**資料**：{rev_period} 月營收｜{val_date} 估值\n",
             "## 全鏈總覽（由上游到下游）\n"]
    for segment in SEGMENT_ORDER:
        members = companies_in(segment)
        yoys = [rev.get(c, {}).get("yoy_pct") for c in members]
        yoys = [y for y in yoys if y is not None]
        avg = f"{sum(yoys)/len(yoys):+.1f}%" if yoys else "—"
        names = "、".join(f"[[{c} {name_of(c)}]]" for c in sorted(members))
        lines.append(f"### [[{segment}]]　平均營收 YoY {avg}")
        lines.append(f"{names}\n")

    lines.append("## 定價檢驗（成長 vs 估值）\n")
    lines.append("同樣的成長，市場給的價錢差很多——差距就是機會或風險所在。\n")
    lines.append("| 公司 | 環節 | 營收 YoY | 本益比 | 每 1x 本益比買到的成長 |")
    lines.append("|---|---|---|---|---|")
    rows = []
    for code in COMPANIES:
        yoy = rev.get(code, {}).get("yoy_pct")
        per = val.get(code, {}).get("per")
        ratio = (yoy / per) if (yoy and per and per > 0) else None
        rows.append((code, yoy, per, ratio))
    for code, yoy, per, ratio in sorted(rows, key=lambda x: -(x[3] or -999)):
        lines.append(f"| [[{code} {name_of(code)}]] | {COMPANIES[code][1]} | {fmt_pct(yoy)} "
                     f"| {fmt_x(per)} | {'—' if ratio is None else f'{ratio:.2f}'} |")
    lines.append("\n> 最後一欄愈高，代表用同樣的本益比買到愈多成長。這是相對指標，"
                 "不代表便宜就該買——要搭配下面的手寫判斷一起看。")
    return "\n".join(lines)


TEMPLATE_CHAIN = """---
tags: [investing, chain]
updated: {today}
---

# AI伺服器PCB鏈

{{{{AUTO}}}}

## 這條鏈現在走到哪

（上游漲價了嗎？中游轉嫁得動嗎？下游接單如何？）

## 傳導路徑與時間差

（銅價漲 → 金居先反應 → 台燿約一季後轉嫁 → 金像電看接單）

## ⚠️ 目前的矛盾訊號

（同鏈公司說法相反時記在這裡，這是最有價值的訊號）
"""


def build_monthly(rev, rev_period, val) -> str:
    rows = [(c, rev[c]) for c in rev if c in COMPANIES]
    rows.sort(key=lambda x: -(x[1].get("yoy_pct") or -999))
    lines = [f"**期別**：{rev_period}　**涵蓋**：{len(rows)} 家\n",
             "| 公司 | 環節 | 月營收 | MoM | YoY | 累計 YoY |", "|---|---|---|---|---|---|"]
    for code, r in rows:
        lines.append(f"| [[{code} {name_of(code)}]] | {COMPANIES[code][1]} | {fmt_yi(r.get('revenue'))} "
                     f"| {fmt_pct(r.get('mom_pct'))} | {fmt_pct(r.get('yoy_pct'))} "
                     f"| {fmt_pct(r.get('cum_yoy_pct'))} |")
    notes = [(c, r["note"]) for c, r in rows if r.get("note") and r["note"] != "-"]
    if notes:
        lines.append("\n## 公司自己的說法\n")
        for code, note in notes:
            lines.append(f"- **[[{code} {name_of(code)}]]**：{note}")
    return "\n".join(lines)


TEMPLATE_MONTHLY = """---
tags: [investing, monthly]
period: {period}
updated: {today}
---

# {period} 月營收

{{{{AUTO}}}}

## 我看到什麼

（這個月全鏈的重點變化）
"""


def main() -> int:
    val_data, val_date = latest("valuation")
    rev_data, rev_period = latest("revenue")
    news_data, _ = latest("news")
    if not val_data or not rev_data:
        print("❌ data/ 沒有資料，請先跑 tools/fetch_market.py")
        return 1

    val = val_data["companies"]
    rev = rev_data["companies"]
    news = (news_data or {}).get("companies", {})
    positions = load_positions()
    today = date.today().isoformat()
    stats = {"created": 0, "updated": 0}

    for code, (name, segment) in COMPANIES.items():
        path = INV / "companies" / f"{code} {name}.md"
        result = write_auto(
            path,
            build_company(code, rev, val, news, positions),
            TEMPLATE_COMPANY.format(code=code, name=name, segment=segment, today=today))
        stats[result] += 1

    for segment in SEGMENT_ORDER:
        path = INV / "segments" / f"{segment}.md"
        result = write_auto(path, build_segment(segment, rev, val, positions),
                            TEMPLATE_SEGMENT.format(segment=segment, today=today))
        stats[result] += 1

    result = write_auto(INV / "chains" / "AI伺服器PCB鏈.md",
                        build_chain(rev, val, positions, rev_period, val_date),
                        TEMPLATE_CHAIN.format(today=today))
    stats[result] += 1

    result = write_auto(INV / "monthly" / f"{rev_period}月營收.md",
                        build_monthly(rev, rev_period, val),
                        TEMPLATE_MONTHLY.format(period=rev_period, today=today))
    stats[result] += 1

    print(f"✅ 頁面：新建 {stats['created']}、更新 {stats['updated']}"
          f"（營收 {rev_period}、估值 {val_date}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
