#!/usr/bin/env python3
"""每日資料健檢：巡出規則能判定的問題，寫 wiki/health.md 並推 Telegram。

只查「機械可判定」的問題。需要理解才能判斷的（訊號矛盾、摘要失真、
論點過期）交給 .claude/agents/kb-auditor.md 那個稽核 agent。
"""
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notify  # noqa: E402

KB = Path(__file__).resolve().parent.parent
DATA = KB / "data"
WIKI = KB / "wiki"
SOURCE_DIRS = ["raw", "Clippings"]

STALE_DAYS = 3
LINK_RE = re.compile(r"\[\[([^\]|#]+)")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def check_duplicates() -> list:
    """同一個來源網址存了多份。"""
    by_url = defaultdict(list)
    for folder in SOURCE_DIRS:
        for f in (KB / folder).glob("*.md"):
            head = f.read_text(encoding="utf-8", errors="ignore")[:1200]
            m = re.search(r'^(?:source|original_url):\s*"?([^"\n]+)"?', head, re.M)
            if m:
                by_url[m.group(1).strip()].append(f"{folder}/{f.name}")
    return [f"重複存檔：{url}\n    → " + "\n    → ".join(files)
            for url, files in by_url.items() if len(files) > 1]


def check_uningested() -> list:
    done = set((load_json(DATA / "ingested.json") or {}).get("files", []))
    out = []
    for folder in SOURCE_DIRS:
        for f in sorted((KB / folder).glob("*.md")):
            rel = f"{folder}/{f.name}"
            if rel not in done:
                out.append(f"尚未消化：{rel}")
    return out


def check_truncated() -> list:
    """抓被截斷的來源檔。

    手機管道存進來的檔案有輸出長度上限，常常存到一半就斷在句子中間。
    判斷方式：正文最後一行沒有以句尾標點結束 → 幾乎確定被截斷。
    """
    out = []
    for folder in SOURCE_DIRS:
        for f in sorted((KB / folder).glob("*.md")):
            text = f.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---"):
                continue
            if "404" in text[:600]:          # Threads 失效頁，不是截斷
                continue
            # 只檢查手機管道（Threads/IG）的檔案：它們格式固定、句子完整。
            # YouTube 逐字稿沒有標點、網頁剪存結尾是 HTML，套同一條規則會誤報。
            if not re.search(r"^platform:\s*(threads|instagram)\s*$", text[:600], re.M):
                continue
            body = text.split("## 相關頁面")[0]
            body = body.split("---", 2)[-1]
            lines = [l.strip() for l in body.splitlines() if l.strip()]
            if not lines:
                continue
            last = lines[-1]
            if last.startswith("#"):          # 只有標題沒內容
                out.append(f"內容截斷：{folder}/{f.name}（只有標題，沒有內文）")
                continue
            if not re.search(r"[。！？!?）)」』\]:：]$", last):
                out.append(f"內容截斷：{folder}/{f.name} — 結尾斷在「…{last[-20:]}」")
    return out


def check_links() -> tuple:
    # health.md 可以被連結，但不掃它的內容——報告裡的問題文字會自我汙染
    pages = {p.stem: p for p in WIKI.rglob("*.md")}
    dead, incoming = [], defaultdict(int)
    for path in (p for p in pages.values() if p.name != "health.md"):
        for target in LINK_RE.findall(path.read_text(encoding="utf-8", errors="ignore")):
            target = target.strip().split("/")[-1]
            if target in pages:
                incoming[target] += 1
            elif target:
                dead.append(f"斷連結：{path.relative_to(KB)} → [[{target}]]")
    orphans = [f"孤島頁（沒有任何頁連過來）：{p.relative_to(KB)}"
               for stem, p in pages.items()
               if incoming.get(stem, 0) == 0 and p.name not in ("overview.md", "health.md")]
    return dead, orphans


def check_stale() -> list:
    files = sorted((DATA / "valuation").glob("*.json"))
    if not files:
        return ["估值資料：從未抓取過"]
    latest = files[-1].stem
    try:
        age = (date.today() - date.fromisoformat(latest)).days
    except ValueError:
        return [f"估值資料日期異常：{latest}"]
    if age > STALE_DAYS:
        return [f"估值資料已 {age} 天沒更新（最新 {latest}）→ 排程可能掛了"]
    return []


def check_numbers() -> list:
    """公司頁 AUTO 區塊的數字，必須與 data/ 的原始值一致。"""
    val_files = sorted((DATA / "valuation").glob("*.json"))
    rev_files = sorted((DATA / "revenue").glob("*.json"))
    if not val_files or not rev_files:
        return []
    val = load_json(val_files[-1])["companies"]
    rev = load_json(rev_files[-1])["companies"]

    out = []
    for page in (WIKI / "investing" / "companies").glob("*.md"):
        code = page.stem.split(" ", 1)[0]
        text = page.read_text(encoding="utf-8", errors="ignore")
        for label, expected in (("年增 YoY", rev.get(code, {}).get("yoy_pct")),
                                ("本益比 PER", val.get(code, {}).get("per"))):
            if expected is None:
                continue
            m = re.search(rf"\|\s*{re.escape(label)}\s*\|\s*([+-]?[\d.]+)", text)
            if not m:
                continue
            shown = float(m.group(1))
            if abs(shown - expected) > 0.15:
                out.append(f"數字不符：{page.name} 的「{label}」寫 {shown}，"
                           f"原始資料是 {expected}")
    return out


def main() -> int:
    checks = []
    dead, orphans = check_links()
    for title, items in (
        ("重複存檔", check_duplicates()),
        ("尚未消化", check_uningested()),
        ("疑似截斷", check_truncated()),
        ("斷連結", dead),
        ("孤島頁", orphans),
        ("數字不符", check_numbers()),
        ("資料過期", check_stale()),
    ):
        checks.append((title, items))

    total = sum(len(items) for _, items in checks)
    now = datetime.now()
    lines = [
        "---", "tags: [health]", f"updated: {now:%Y-%m-%d}", "---", "",
        "# 知識庫健檢",
        "",
        f"**檢查時間**：{now:%Y-%m-%d %H:%M}　**發現問題**：{total} 項",
        "",
        "> 這頁由 `tools/health_check.py` 每天自動覆寫，只查規則能判定的問題。",
        "> 需要判讀的（訊號矛盾、摘要失真、論點過期）請叫 kb-auditor 稽核。",
        "",
    ]
    for title, items in checks:
        lines.append(f"## {title}（{len(items)}）\n")
        lines.extend([f"- {item}" for item in items] if items else ["- ✅ 沒有問題"])
        lines.append("")

    (WIKI / "health.md").write_text("\n".join(lines), encoding="utf-8")

    summary_items = [f"• {title} {len(items)}" for title, items in checks if items]
    if total:
        worst = [items[0] for _, items in checks if items][:3]
        text = (f"📚 <b>知識庫健檢</b>　{now:%m/%d %H:%M}\n"
                f"發現 {total} 項問題\n" + "\n".join(summary_items) +
                "\n\n最需要看的：\n" + "\n".join(f"– {w.splitlines()[0]}" for w in worst))
    else:
        text = f"📚 <b>知識庫健檢</b>　{now:%m/%d %H:%M}\n✅ 全部正常"
    notify.send(text)

    print(f"✅ 健檢完成：{total} 項問題，已寫入 wiki/health.md")
    for title, items in checks:
        print(f"   {title}: {len(items)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
