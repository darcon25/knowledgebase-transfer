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
    accepted = (load_json(DATA / "known_issues.json") or {}).get("truncation_accepted", {})
    out = []
    for folder in SOURCE_DIRS:
        for f in sorted((KB / folder).glob("*.md")):
            if f"{folder}/{f.name}" in accepted:      # 已確認處理過，不再重複提醒
                continue
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


# 貼文自己提到有圖的線索。只能當優先度參考——文字被截斷時線索也會一起消失，
# 十大封裝技術那篇就是這樣漏掉的。
MEDIA_HINTS = ("一張圖", "如下圖", "這張圖", "這張表", "附圖", "見圖", "下圖",
               "整理了一張", "如圖", "圖表", "輪播", "第一張", "如下表")


def check_missing_media() -> list:
    """Threads/IG 是以圖為主的平台，但 Jina Reader 拿不到圖。

    與其猜哪篇有圖，不如反過來：這兩個平台來的貼文只要沒有對應截圖，
    一律列為「圖片未確認」，由人逐篇看過後記進 known_issues。
    """
    checked = (load_json(DATA / "known_issues.json") or {}).get("media_checked", {})

    # 已經用截圖補過的貼文網址
    captured = set()
    for f in (KB / "raw").glob("shot_*.md"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r'original_url:\s*"([^"]+)"', text)
        if m:
            captured.add(m.group(1).split("?")[0])

    out = []
    for f in sorted((KB / "raw").glob("*.md")):
        rel = f"raw/{f.name}"
        if rel in checked or f.name.startswith("shot_"):
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        if not re.search(r"^platform:\s*(threads|instagram)\s*$", text[:600], re.M):
            continue
        m = re.search(r'original_url:\s*"([^"]+)"', text)
        url = m.group(1).split("?")[0] if m else ""
        if url and url in captured:
            continue
        hints = [h for h in MEDIA_HINTS if h in text]
        mark = f"（文中提到圖：{'、'.join(hints)}）" if hints else ""
        out.append(f"圖片未確認：{rel}{mark}\n    {url}")
    # 文中有線索的排前面
    return sorted(out, key=lambda x: "文中提到圖" not in x)


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


def collect() -> list:
    """跑完所有檢查，回傳 [(名稱, 問題清單), ...]。boot_check.py 也會用。"""
    checks = []
    dead, orphans = check_links()
    for title, items in (
        ("重複存檔", check_duplicates()),
        ("尚未消化", check_uningested()),
        ("疑似截斷", check_truncated()),
        ("圖片未確認", check_missing_media()),
        ("斷連結", dead),
        ("孤島頁", orphans),
        ("數字不符", check_numbers()),
        ("資料過期", check_stale()),
    ):
        checks.append((title, items))
    return checks


def write_report(checks: list, total: int) -> None:
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


def main() -> int:
    checks = collect()
    total = sum(len(items) for _, items in checks)
    now = datetime.now()
    write_report(checks, total)

    # 帶上 digest 產生的「今日值得注意」，兩者合成同一則通知
    notable = (load_json(DATA / "notable.json") or {})
    fresh = notable.get("date") == date.today().isoformat()
    notable_items = notable.get("items", []) if fresh else []

    summary_items = [f"• {title} {len(items)}" for title, items in checks if items]
    if total or notable_items:
        parts = [f"📚 <b>知識庫每日更新</b>　{now:%m/%d %H:%M}"]
        if notable_items:
            parts.append("\n<b>今日值得注意</b>")
            parts += [f"• {i['text']}" for i in notable_items[:5]]
        if total:
            worst = [items[0] for _, items in checks if items][:2]
            parts.append(f"\n<b>待處理 {total} 項</b>")
            parts += summary_items
            parts += [f"– {w.splitlines()[0]}" for w in worst]
        text = "\n".join(parts)
    else:
        # 沒問題也沒變化就完全不推，不打擾
        text = ""
    if text:
        notify.send(text)
    else:
        print("ℹ️  今天沒有問題也沒有值得注意的變化，不推播")

    print(f"✅ 健檢完成：{total} 項問題，已寫入 wiki/health.md")
    for title, items in checks:
        print(f"   {title}: {len(items)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
