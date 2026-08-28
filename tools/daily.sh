#!/bin/bash
# 每日一條龍：抓資料 → 建頁面 → 健檢推播
# 由 launchd 排程呼叫，也可以手動執行
cd "/Users/mmfamily/Max KnowledgeBase" || exit 1
PY=/usr/bin/python3
command -v python3 >/dev/null && PY=$(command -v python3)

echo "===== $(date '+%Y-%m-%d %H:%M:%S') 每日更新開始 ====="
"$PY" tools/fetch_market.py   || echo "⚠️ 抓取階段有問題，仍繼續後續步驟"
"$PY" tools/build_pages.py    || echo "⚠️ 建頁階段失敗"
"$PY" tools/health_check.py   || echo "⚠️ 健檢階段失敗"
echo "===== $(date '+%Y-%m-%d %H:%M:%S') 每日更新結束 ====="
