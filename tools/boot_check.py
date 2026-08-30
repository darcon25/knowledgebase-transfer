#!/usr/bin/env python3
"""開機時自動檢查知識庫，有待處理項目就推 Telegram。

流程：等網路 → 拉 GitHub 上的新檔 → 跑健檢 → 有問題才通知。
沒問題就安靜，不打擾。
"""
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import health_check  # noqa: E402
import notify  # noqa: E402

KB = Path(__file__).resolve().parent.parent
WAIT_MINUTES = 5
CHECK_INTERVAL = 20


def log(msg: str) -> None:
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line)
    with open(KB / "data" / "fetch.log", "a", encoding="utf-8") as fh:
        fh.write(f"{line}\n")


def wait_for_network() -> bool:
    """開機當下通常還沒連上網，最多等 5 分鐘。"""
    deadline = time.time() + WAIT_MINUTES * 60
    while time.time() < deadline:
        result = subprocess.run(
            ["curl", "-sS", "--max-time", "8", "-o", "/dev/null",
             "https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL"],
            capture_output=True)
        if result.returncode == 0:
            return True
        time.sleep(CHECK_INTERVAL)
    return False


def pull_latest() -> str:
    """把 n8n 存進 GitHub 的新檔案拉下來。有本機修改就跳過，不強推。"""
    result = subprocess.run(["git", "pull", "--ff-only"], cwd=KB,
                            capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        return f"⚠️ git pull 跳過（{result.stderr.strip()[:80]}）"
    return "已是最新" if "Already up to date" in result.stdout else "已拉取新檔案"


def main() -> int:
    log("=== 開機檢查開始 ===")
    if not wait_for_network():
        log(f"❌ 等待 {WAIT_MINUTES} 分鐘仍無網路，放棄")
        return 1
    log(f"✅ 網路正常｜{pull_latest()}")

    checks = health_check.collect()
    total = sum(len(items) for _, items in checks)
    health_check.write_report(checks, total)

    if total == 0:
        log("✅ 沒有待處理項目，不打擾")
        return 0

    needs_me = {"疑似截斷", "圖片未確認", "尚未消化"}
    mine = [(t, items) for t, items in checks if items and t in needs_me]
    others = [(t, items) for t, items in checks if items and t not in needs_me]

    lines = [f"💻 <b>知識庫開機檢查</b>　{datetime.now():%m/%d %H:%M}", ""]
    if mine:
        lines.append("<b>需要在電腦前處理</b>（跟 Claude 說「補一下」）：")
        lines += [f"• {t} {len(items)} 篇" for t, items in mine]
    if others:
        lines.append("")
        lines.append("<b>其他</b>：")
        lines += [f"• {t} {len(items)}" for t, items in others]
    notify.send("\n".join(lines))
    log(f"✅ 已通知：{total} 項待處理")
    return 0


if __name__ == "__main__":
    sys.exit(main())
