#!/usr/bin/env python3
"""輪詢 GitHub 上的指令檔並執行。

雲端的 n8n 連不到這台電腦，所以用 GitHub 當信箱：
n8n 寫指令檔 → 這支程式 git pull 看到 → 執行 → 刪掉指令檔 → 回報 Telegram。

支援的指令（放在 data/commands/ 底下）：
  補齊.json   把待補清單的第一個網址用 Chrome 開起來
  健檢.json   立刻跑一次健檢並回報
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import health_check  # noqa: E402
import notify  # noqa: E402

KB = Path(__file__).resolve().parent.parent
CMD_DIR = KB / "data" / "commands"
NEEDS_ME = {"疑似截斷", "圖片未確認", "尚未消化"}


def log(msg: str) -> None:
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line)
    with open(KB / "data" / "fetch.log", "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def git(*args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=KB, capture_output=True,
                          text=True, timeout=120)


def pending_urls() -> list:
    """從健檢結果抽出待補的網址，附上檔名方便辨識。"""
    out = []
    for title, items in health_check.collect():
        if title not in NEEDS_ME:
            continue
        for item in items:
            lines = item.splitlines()
            url = next((l.strip() for l in lines if l.strip().startswith("http")), "")
            name = lines[0].split("：", 1)[-1].split("（")[0].split(" —")[0].strip()
            out.append({"title": title, "name": name, "url": url})
    return out


def cmd_fill() -> str:
    items = pending_urls()
    if not items:
        return "✅ 沒有待補的項目，什麼都不用做。"

    with_url = [i for i in items if i["url"]]
    if not with_url:
        names = "\n".join(f"• {i['name']}（{i['title']}）" for i in items[:5])
        return f"有 {len(items)} 項待處理，但都沒有可開啟的網址：\n{names}"

    first = with_url[0]
    subprocess.run(["open", "-a", "Google Chrome", first["url"]], timeout=30)
    rest = len(with_url) - 1
    return (f"🌐 已用 Chrome 開啟：\n{first['name']}\n{first['url']}\n\n"
            f"回到電腦後跟 Claude 說「補一下」，它會照清單處理完"
            + (f"（還有 {rest} 項）" if rest else "") + "。")


def cmd_health() -> str:
    checks = health_check.collect()
    total = sum(len(items) for _, items in checks)
    health_check.write_report(checks, total)
    if total == 0:
        return "✅ 健檢完成：沒有任何問題。"
    lines = [f"健檢完成，{total} 項待處理："]
    lines += [f"• {t} {len(i)}" for t, i in checks if i]
    return "\n".join(lines)


HANDLERS = {"補齊": cmd_fill, "健檢": cmd_health}


def main() -> int:
    result = git("pull", "--ff-only", "origin", "main")
    if result.returncode != 0:
        log(f"⚠️ git pull 失敗，仍檢查本機指令：{result.stderr.strip()[:80]}")

    if not CMD_DIR.exists():
        return 0
    # 忽略點開頭的檔案（.gitkeep 之類），不然會被當成指令
    files = sorted(f for f in CMD_DIR.glob("*.json") if not f.name.startswith("."))
    if not files:
        return 0

    for f in files:
        name = f.stem
        handler = HANDLERS.get(name)
        log(f"收到指令：{name}")
        if handler is None:
            notify.send(f"❓ 不認得的指令「{name}」\n目前支援：{'、'.join(HANDLERS)}")
        else:
            try:
                notify.send(handler())
            except Exception as exc:  # noqa: BLE001
                notify.send(f"❌ 指令「{name}」執行失敗：{type(exc).__name__}")
                log(f"指令 {name} 失敗：{exc}")
        f.unlink(missing_ok=True)      # 執行完就刪，避免重複觸發

    git("add", "data/commands")
    git("commit", "-m", "🤖 指令已執行")
    git("push", "origin", "main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
