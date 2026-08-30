#!/usr/bin/env python3
"""Telegram 推播（含 3 次重試）。

⚠️ **只讀知識庫自己的 .env**。刻意不去借 Maxtrading Review 的設定——
知識庫的通知不應該混進交易報告的管道。沒設定就不送，只記在 log 與
wiki/health.md，不會靜默失敗。
"""
import os
import time
from pathlib import Path

import requests

KB = Path(__file__).resolve().parent.parent
ENV_FILE = KB / ".env"
RETRIES = 3
BACKOFF = 5


def _load_env() -> dict:
    env = {}
    if not ENV_FILE.exists():
        return env
    for line in ENV_FILE.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env.setdefault(key.strip(), value.strip().strip('"').strip("'"))
    return env


def send(text: str) -> bool:
    env = _load_env()
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or env.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID") or env.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("ℹ️  尚未設定知識庫專用的通知管道（Max KnowledgeBase/.env），"
              "本次不推播。報告仍寫在 wiki/health.md。")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text[:4000], "parse_mode": "HTML",
               "disable_web_page_preview": True}
    for attempt in range(1, RETRIES + 1):
        try:
            resp = requests.post(url, json=payload, timeout=20)
            resp.raise_for_status()
            return True
        except Exception as exc:  # noqa: BLE001
            print(f"⚠️  推播第 {attempt}/{RETRIES} 次失敗：{exc}")
            if attempt < RETRIES:
                time.sleep(BACKOFF)
    return False


if __name__ == "__main__":
    import sys
    ok = send(sys.argv[1] if len(sys.argv) > 1 else "知識庫測試訊息")
    print("✅ 已送出" if ok else "❌ 送出失敗")
