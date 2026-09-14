#!/usr/bin/env python3
"""把 Threads / IG 貼文的圖片補進 raw/assets/。

背景：n8n 管道只把 Jina Reader 的文字餵給 Gemini，Jina 回傳 markdown 裡的
`![](圖片網址)` 整段被丟掉，所以四個月來一張圖都沒進來。
（舊診斷寫「Jina 拿不到 Threads 圖」是錯的，2026-09-14 實測 Jina 拿得到。）

這支工具不必等 n8n 改好：自己重讀原貼文、抓出主文的圖、下載存檔。

CLAUDE.md 規定 `raw/` 的既有筆記不可修改，所以圖片另存成 `raw/shot_*.md`
（沿用 2026-08-30 就有的截圖慣例），health_check 本來就認得這種檔，不必改健檢。

⚠️ cdninstagram 的網址帶簽章有效期（約一週），所以一定要下載成檔案，
   只存網址過幾天就變 403。

用法：
    python3 tools/fetch_media.py                 # 掃 raw/ 全部沒補過的貼文
    python3 tools/fetch_media.py --dry-run       # 只看會抓到什麼，不寫檔
    python3 tools/fetch_media.py --limit 5       # 只處理前 5 篇
    python3 tools/fetch_media.py --file raw/x.md # 只處理指定檔
"""
import argparse
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

import requests

KB = Path(__file__).resolve().parent.parent
RAW = KB / "raw"
ASSETS = RAW / "assets"
DATA = KB / "data"

JINA = "https://r.jina.ai/"
TIMEOUT = 90
PAUSE = 3  # r.jina.ai 免費額度有速率限制，篇與篇之間停一下

# Jina 轉出來的 markdown 圖片：![Image 3: 某某's profile picture](網址)
IMG_RE = re.compile(r"!\[Image \d+(?::\s*(?P<alt>[^\]]*))?\]\((?P<url>https?://[^)\s]+)\)")
VIDEO_HINT = "having trouble playing this video"

EXT_BY_TYPE = {
    "image/jpeg": ".jpg", "image/jpg": ".jpg", "image/png": ".png",
    "image/webp": ".webp", "image/gif": ".gif", "image/heic": ".heic",
}


def log(msg: str) -> None:
    print(msg, flush=True)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def normalize_url(url: str) -> str:
    """有些筆記的 original_url 存成 //www.threads.com/... 少了 scheme。"""
    url = url.strip()
    if url.startswith("//"):
        return "https:" + url
    return url


def is_profile_pic(alt: str, url: str) -> bool:
    """IG CDN 慣例：路徑含 `-19` 的是大頭貼，`-15` 才是貼文本體的圖／影片縮圖。"""
    if alt and "profile picture" in alt:
        return True
    return bool(re.search(r"/t51\.[\d.]+-19/", url))


def extract_main_media(markdown: str) -> list:
    """只取「主文」的圖，不要留言與 Related threads 的圖。

    兩個平台版面不同，但都有同一個界線——第二個大頭貼就是留言區的開始：
      Threads：作者大頭貼 → 內文 → 主文的圖 → 留言者大頭貼
      IG：主文的圖 → 作者大頭貼（會重複出現兩次）→ 留言者大頭貼
    所以主文區間 = 文件開頭到「第二個大頭貼」為止，兩種版面都涵蓋得到。
    """
    hits = [(m.start(), m.end(), m.group("alt") or "", m.group("url"))
            for m in IMG_RE.finditer(markdown)]
    profiles = [pos for pos, _, alt, url in hits if is_profile_pic(alt, url)]
    end = profiles[1] if len(profiles) > 1 else len(markdown)

    out, seen = [], set()
    for pos, stop, alt, url in hits:
        if pos >= end or is_profile_pic(alt, url):
            continue
        key = url.split("?")[0]
        if key in seen:
            continue
        seen.add(key)
        # 影片只抓得到縮圖，標記出來免得日後誤以為圖抓壞了。
        # ⚠️ 要從比對結束的位置往後看——圖片網址本身就可能長達七百字元。
        tail = markdown[stop:stop + 300]
        out.append({"url": url, "alt": alt, "is_video": VIDEO_HINT in tail})
    return out


def fetch_markdown(url: str) -> str:
    r = requests.get(JINA + url, timeout=TIMEOUT)
    r.raise_for_status()
    return r.text


def download(url: str, dest_stem: Path) -> Path:
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    ctype = (r.headers.get("content-type") or "").split(";")[0].strip().lower()
    ext = EXT_BY_TYPE.get(ctype)
    if not ext:
        ext = Path(url.split("?")[0]).suffix or ".jpg"
    dest = dest_stem.with_suffix(ext)
    dest.write_bytes(r.content)
    return dest


def note_candidates(only: str | None) -> list:
    if only:
        p = (KB / only) if not Path(only).is_absolute() else Path(only)
        return [p]
    return sorted(RAW.glob("*.md"))


def parse_note(path: Path):
    """回傳 (text, platform, original_url)；不是 threads/IG 貼文就回 None。"""
    text = path.read_text(encoding="utf-8", errors="ignore")
    head = text[:800]
    m_plat = re.search(r"^platform:\s*(threads|instagram)\s*$", head, re.M)
    m_url = re.search(r'^original_url:\s*"?([^"\n]+)"?\s*$', head, re.M)
    if not m_plat or not m_url:
        return None
    return text, m_plat.group(1), normalize_url(m_url.group(1))


def captured_urls() -> set:
    """已經有截圖檔（手動或本工具）的貼文網址。"""
    out = set()
    for f in RAW.glob("shot_*.md"):
        m = re.search(r'original_url:\s*"([^"]+)"', f.read_text(encoding="utf-8", errors="ignore"))
        if m:
            out.add(m.group(1).split("?")[0])
    return out


def companion_path(src: Path, day: str) -> Path:
    """配套的 shot_ 檔名，沿用 raw/shot_<日期>_<主題>.md 慣例。"""
    topic = src.stem.split("_", 2)[-1] if "_" in src.stem else src.stem
    base = RAW / f"shot_{day}_{topic}.md"
    n = 2
    while base.exists():
        base = RAW / f"shot_{day}_{topic}_{n}.md"
        n += 1
    return base


def write_companion(src: Path, url: str, files: list, day: str) -> Path:
    """把圖片寫成獨立的 shot_ 檔，原筆記一個字都不動。"""
    out = companion_path(src, day)
    embeds = []
    for f, is_video in files:
        embeds.append(f"![[{f.name}]]")
        if is_video:
            embeds.append("> ⬆️ 這則是影片，只抓得到封面縮圖。")
        embeds.append("")

    body = f"""---
tags:
  - source
  - screenshot
type: screenshot
date_captured: {day}
image: assets/{files[0][0].name}
original_url: "{url}"
image_count: {len(files)}
captured_by: fetch_media
source_note: "{src.name}"
status: 待讀圖
---

# 📸 原貼文圖片 {day} — {src.stem}

> 原始出處：{url}
> 對應筆記：[[{src.stem}]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

""" + "\n".join(embeds) + """
## 內容

（待讀圖後填寫）
"""
    out.write_text(body, encoding="utf-8")
    return out


def record_checked(results: dict) -> None:
    p = DATA / "known_issues.json"
    d = load_json(p) or {}
    checked = d.setdefault("media_checked", {})
    checked.update(results)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--file")
    args = ap.parse_args()

    ASSETS.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    already = captured_urls()
    checked = (load_json(DATA / "known_issues.json") or {}).get("media_checked", {})
    done = 0
    got_images = 0
    no_images = 0
    failed = []
    results = {}

    for path in note_candidates(args.file):
        if path.name.startswith("shot_"):
            continue
        parsed = parse_note(path)
        if not parsed:
            continue
        text, platform, url = parsed
        if not args.file and (url.split("?")[0] in already or f"raw/{path.name}" in checked):
            continue
        if args.limit and done >= args.limit:
            break
        done += 1

        log(f"\n[{done}] {path.name}\n    {url}")
        try:
            md = fetch_markdown(url)
        except Exception as e:
            log(f"    ❌ 讀不到原貼文：{e}")
            failed.append((path.name, str(e)[:120]))
            time.sleep(PAUSE)
            continue

        media = extract_main_media(md)
        if not media:
            log("    · 主文沒有圖")
            no_images += 1
            if not args.dry_run:
                results[f"raw/{path.name}"] = f"{today} fetch_media 自動確認：主文沒有圖"
            time.sleep(PAUSE)
            continue

        log(f"    · 主文有 {len(media)} 張")
        if args.dry_run:
            for m in media:
                log(f"      {'🎬' if m['is_video'] else '🖼'} {m['url'][:100]}")
            time.sleep(PAUSE)
            continue

        saved = []
        for i, m in enumerate(media, 1):
            stem = ASSETS / f"{path.stem}_{i:02d}"
            try:
                f = download(m["url"], stem)
                saved.append((f, m["is_video"]))
                log(f"      ✅ {f.name} ({f.stat().st_size // 1024} KB)")
            except Exception as e:
                log(f"      ❌ 第 {i} 張下載失敗：{e}")
        if saved:
            got_images += 1
            comp = write_companion(path, url, saved, today)
            log(f"      📝 {comp.name}")
            kinds = "、".join("影片封面" if v else "圖" for _, v in saved)
            results[f"raw/{path.name}"] = (
                f"{today} fetch_media 自動補齊 {len(saved)} 張（{kinds}），見 raw/{comp.name}")
        else:
            failed.append((path.name, "圖片全部下載失敗"))
        time.sleep(PAUSE)

    if results:
        record_checked(results)

    log("\n===== 完成 =====")
    log(f"處理 {done} 篇：補到圖 {got_images} 篇、確認沒圖 {no_images} 篇、失敗 {len(failed)} 篇")
    for name, why in failed:
        log(f"  ❌ {name}：{why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
