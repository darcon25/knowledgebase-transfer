#!/usr/bin/env python3
"""每日統整：只講「變化」，不講意見。

程式做得到的統整——誰的估值跳動、誰的成長轉折、持倉在環節內的相對位置
有沒有變。這些是事實，不是判斷。判斷留給你或 LLM 那一層。

產出 wiki/今日值得注意.md，並回傳值得推播的重點清單。
"""
import json
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watchlist import COMPANIES, SEGMENT_ORDER, companies_in, name_of  # noqa: E402

KB = Path(__file__).resolve().parent.parent
DATA = KB / "data"
WIKI = KB / "wiki"

PER_JUMP_PCT = 5.0        # 本益比單次變動超過這個百分比就值得看一眼
YOY_SWING_PCT = 15.0      # 月營收 YoY 相對上期變動這麼多，代表動能轉折
HELD = {"6274", "2368", "8358", "4958", "3711", "2308"}


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def snapshots(folder: str, n: int = 2) -> list:
    files = sorted((DATA / folder).glob("*.json"))[-n:]
    return [(f.stem, load(f)) for f in files]


def valuation_moves() -> list:
    """比較最近兩次估值快照，找出跳動明顯的個股。"""
    snaps = snapshots("valuation", 2)
    if len(snaps) < 2:
        return []
    (prev_date, prev), (cur_date, cur) = snaps
    out = []
    for code in COMPANIES:
        a = (prev or {}).get("companies", {}).get(code, {}).get("per")
        b = (cur or {}).get("companies", {}).get(code, {}).get("per")
        if not a or not b:
            continue
        pct = (b / a - 1) * 100
        if abs(pct) >= PER_JUMP_PCT:
            out.append({
                "code": code, "pct": pct, "from": a, "to": b,
                "held": code in HELD,
                "text": (f"[[{code} {name_of(code)}]] 本益比 {a:.1f}x → {b:.1f}x"
                         f"（{pct:+.1f}%）"),
            })
    out.sort(key=lambda x: (not x["held"], -abs(x["pct"])))
    return out


def revenue_turns() -> tuple:
    """月營收有新期別時，比較全鏈動能：誰加速、誰減速。"""
    snaps = snapshots("revenue", 2)
    if len(snaps) < 2:
        return None, []
    (prev_p, prev), (cur_p, cur) = snaps
    rows = []
    for code in COMPANIES:
        a = (prev or {}).get("companies", {}).get(code, {}).get("yoy_pct")
        b = (cur or {}).get("companies", {}).get(code, {}).get("yoy_pct")
        if a is None or b is None:
            continue
        rows.append({"code": code, "prev": a, "cur": b, "delta": b - a,
                     "held": code in HELD})
    turns = [r for r in rows if abs(r["delta"]) >= YOY_SWING_PCT]
    turns.sort(key=lambda x: (not x["held"], -abs(x["delta"])))
    return (prev_p, cur_p, rows), turns


def segment_ranking() -> list:
    """持倉股在自己環節裡的「成長÷本益比」排名。"""
    val = snapshots("valuation", 1)
    rev = snapshots("revenue", 1)
    if not val or not rev:
        return []
    v = (val[0][1] or {}).get("companies", {})
    r = (rev[0][1] or {}).get("companies", {})
    out = []
    for seg in SEGMENT_ORDER:
        members = []
        for code in companies_in(seg):
            yoy = r.get(code, {}).get("yoy_pct")
            per = v.get(code, {}).get("per")
            if yoy is None or not per:
                continue
            members.append((code, yoy / per))
        if len(members) < 2:
            continue
        members.sort(key=lambda x: -x[1])
        for i, (code, ratio) in enumerate(members, 1):
            if code in HELD:
                out.append({"code": code, "seg": seg, "rank": i,
                            "total": len(members), "ratio": ratio})
    return out


def main() -> int:
    moves = valuation_moves()
    rev_ctx, turns = revenue_turns()
    ranks = segment_ranking()
    today = date.today().isoformat()

    lines = ["---", "tags: [digest]", f"updated: {today}", "---", "",
             "# 今日值得注意", "",
             f"**產生時間**：{datetime.now():%Y-%m-%d %H:%M}", "",
             "> 這頁每天自動覆寫，**只陳述變化，不下判斷**。",
             "> 判斷請看各公司頁的「我的論點」與 [[2026-08-28-PCB鏈定價檢驗]]。", ""]

    lines.append(f"## 估值跳動（單次變動 ≥ {PER_JUMP_PCT}%）\n")
    if moves:
        lines.append("| 公司 | 變化 | 持倉 |")
        lines.append("|---|---|---|")
        for m in moves:
            lines.append(f"| [[{m['code']} {name_of(m['code'])}]] | "
                         f"{m['from']:.1f}x → {m['to']:.1f}x（{m['pct']:+.1f}%）| "
                         f"{'★' if m['held'] else ''} |")
    else:
        lines.append("（沒有明顯跳動）")

    lines.append(f"\n## 營收動能轉折（YoY 相對上期變動 ≥ {YOY_SWING_PCT} 個百分點）\n")
    if rev_ctx and turns:
        prev_p, cur_p, _ = rev_ctx
        lines.append(f"比較期別：{prev_p} → {cur_p}\n")
        lines.append("| 公司 | YoY 變化 | 方向 | 持倉 |")
        lines.append("|---|---|---|---|")
        for t in turns:
            arrow = "加速 📈" if t["delta"] > 0 else "減速 📉"
            lines.append(f"| [[{t['code']} {name_of(t['code'])}]] | "
                         f"{t['prev']:+.1f}% → {t['cur']:+.1f}% | {arrow} | "
                         f"{'★' if t['held'] else ''} |")
    else:
        lines.append("（沒有新期別，或沒有明顯轉折）")

    lines.append("\n## 持倉在環節內的相對位置\n")
    if ranks:
        lines.append("「成長÷本益比」在同環節的排名。掉到後段代表同業裡有更划算的選擇，"
                     "不等於該換股，但值得回答「為什麼是這一檔」。\n")
        lines.append("| 持倉 | 環節 | 排名 | 比值 |")
        lines.append("|---|---|---|---|")
        for r in ranks:
            warn = " ⚠️" if r["rank"] == r["total"] and r["total"] >= 3 else ""
            lines.append(f"| [[{r['code']} {name_of(r['code'])}]] | {r['seg']} | "
                         f"{r['rank']}/{r['total']}{warn} | {r['ratio']:.2f} |")
    else:
        lines.append("（資料不足）")

    (WIKI / "今日值得注意.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 回傳值得推播的重點（只挑持倉相關與最極端的，避免每天洗版）
    notable = []
    for m in moves[:3]:
        if m["held"] or abs(m["pct"]) >= PER_JUMP_PCT * 2:
            notable.append(("估值", m["text"]))
    for t in turns[:3]:
        if t["held"]:
            arrow = "加速" if t["delta"] > 0 else "減速"
            notable.append(("營收", f"[[{t['code']} {name_of(t['code'])}]] YoY "
                                    f"{t['prev']:+.0f}% → {t['cur']:+.0f}%（{arrow}）"))
    for r in ranks:
        if r["rank"] == r["total"] and r["total"] >= 3:
            notable.append(("排名", f"{name_of(r['code'])} 在 {r['seg']} 環節"
                                    f"排最後（{r['rank']}/{r['total']}）"))

    # 交給 health_check 一起推，避免一天收到兩則通知
    (DATA / "notable.json").write_text(
        json.dumps({"date": today,
                    "items": [{"kind": k, "text": t} for k, t in notable]},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"✅ 今日值得注意：估值跳動 {len(moves)}、動能轉折 {len(turns)}、"
          f"值得推播 {len(notable)} 項")
    return 0


if __name__ == "__main__":
    sys.exit(main())
