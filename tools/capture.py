#!/usr/bin/env python3
"""把外部內容抓進 raw/，供之後 LLM 消化。

用法：
    python3 tools/capture.py --youtube <網址>
    python3 tools/capture.py --shot <圖片路徑> [--note "這是什麼"]
"""
import argparse
import json
import re
import shutil
import subprocess
import time
import sys
from datetime import date
from pathlib import Path

KB = Path(__file__).resolve().parent.parent
RAW = KB / "raw"
ASSETS = RAW / "assets"


def _run(cmd: list, timeout: int = 120) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip()[:500] or "指令執行失敗")
    return result.stdout


def _subs_to_text(subs: str) -> str:
    """把 VTT/SRT 字幕轉成純文字，去掉時間碼與自動字幕的滾動重複行。"""
    skip_prefix = ("WEBVTT", "Kind:", "Language:", "NOTE", "STYLE")
    lines = []
    for raw_line in subs.splitlines():
        line = raw_line.strip()
        if not line or line.isdigit() or "-->" in line or line.startswith(skip_prefix):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        if lines and lines[-1] == line:
            continue
        lines.append(line)
    # 自動字幕常見「前一句尾 + 新一句」的滾動重複，濾掉被完整包含的短行
    cleaned = []
    for line in lines:
        if cleaned and line in cleaned[-1]:
            continue
        if cleaned and cleaned[-1] in line:
            cleaned[-1] = line
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def _pick_subtitle(files: list, vid: str):
    """依 繁中 → 中文 → 英文 的順序挑一份字幕。"""
    for pref in ("zh-TW", "zh-Hant", "zh", "en"):
        for f in files:
            lang = f.name[len(vid) + 1:].rsplit(".", 1)[0]
            if lang.startswith(pref):
                return f
    return files[0] if files else None


def capture_youtube(url: str) -> Path:
    fields = "%(id)s\t%(title)s\t%(channel)s\t%(upload_date)s\t%(duration_string)s"
    meta = _run(["yt-dlp", "--no-warnings", "--print", fields, url]).strip().split("\t")
    if len(meta) < 5:
        raise RuntimeError(f"取得影片資訊失敗：{meta}")
    vid, title, channel, upload, duration = meta[:5]

    tmp = KB / ".capture_tmp"
    tmp.mkdir(exist_ok=True)
    transcript = ""
    try:
        # 一次只抓一種語言，抓到就停。同時抓多種會被 YouTube 擋（HTTP 429）。
        for lang in ("zh-TW.*", "zh-Hant.*", "zh.*", "en.*"):
            try:
                _run([
                    "yt-dlp", "--no-warnings", "--skip-download",
                    "--write-auto-subs", "--write-subs",
                    "--sub-langs", lang,
                    "--sleep-requests", "1",
                    "-o", str(tmp / "%(id)s"), url,
                ], timeout=300)
            except RuntimeError as exc:
                if "429" in str(exc):
                    time.sleep(20)
                continue
            subs = sorted(tmp.glob(f"{vid}*.vtt")) + sorted(tmp.glob(f"{vid}*.srt"))
            if subs:
                transcript = _subs_to_text(_pick_subtitle(subs, vid).read_text(encoding="utf-8"))
                break
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if not transcript:
        transcript = "（這支影片沒有字幕，需要你補充重點或改用截圖方式）"

    today = date.today().isoformat()
    path = RAW / f"youtube_{today}_{vid}.md"
    path.write_text(
        "---\n"
        "tags:\n  - source\n  - video\n  - youtube\n"
        "type: video\nplatform: youtube\n"
        f"date_captured: {today}\n"
        f'original_url: "{url}"\n'
        f'channel: "{channel}"\n'
        f"duration: {duration}\n"
        "---\n\n"
        f"# 🎬 {title}\n\n"
        f"> 頻道：{channel}｜長度：{duration}｜上傳：{upload}\n"
        f"> 原片：[{url}]({url})\n\n"
        "## 逐字稿\n\n"
        f"{transcript}\n",
        encoding="utf-8",
    )
    return path


def capture_shot(image: str, note: str = "") -> Path:
    src = Path(image).expanduser()
    if not src.exists():
        raise RuntimeError(f"找不到圖片：{src}")
    ASSETS.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    seq = 1
    while (RAW / f"shot_{today}_{seq:02d}.md").exists():
        seq += 1
    stem = f"shot_{today}_{seq:02d}"
    dest = ASSETS / f"{stem}{src.suffix.lower()}"
    shutil.copy2(src, dest)

    path = RAW / f"{stem}.md"
    path.write_text(
        "---\n"
        "tags:\n  - source\n  - screenshot\n"
        "type: screenshot\n"
        f"date_captured: {today}\n"
        f"image: assets/{dest.name}\n"
        "status: 待讀圖\n"
        "---\n\n"
        f"# 📸 截圖存檔 {today} #{seq:02d}\n\n"
        f"![[{dest.name}]]\n\n"
        f"**我的備註**：{note or '（無）'}\n\n"
        "## 內容\n\n"
        "（尚未讀圖。下次對話跟 Claude 說「消化這張截圖」，它會看圖並把內容寫在這裡。）\n",
        encoding="utf-8",
    )
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="把外部內容抓進知識庫 raw/")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--youtube", metavar="URL", help="YouTube 網址，抓逐字稿")
    group.add_argument("--shot", metavar="IMAGE", help="截圖檔案路徑")
    parser.add_argument("--note", default="", help="截圖的備註")
    args = parser.parse_args()

    try:
        path = capture_youtube(args.youtube) if args.youtube else capture_shot(args.shot, args.note)
    except Exception as exc:  # noqa: BLE001
        print(f"❌ 擷取失敗：{exc}", file=sys.stderr)
        return 1

    size = path.stat().st_size
    print(f"✅ 已存入 {path.relative_to(KB)}（{size:,} bytes）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
