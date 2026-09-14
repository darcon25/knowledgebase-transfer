#!/bin/bash
# 每日一條龍：抓資料 → 建頁面 → 健檢推播
# 由 launchd 排程呼叫，也可以手動執行
cd "/Users/mmfamily/Max KnowledgeBase" || exit 1

# ⚠️ 地雷：claude CLI 的憑證存在 macOS Keychain，**沒有 USER 環境變數就讀不到**，
# 會回「OAuth session expired and could not be refreshed」而整個消化階段靜默失敗。
# launchd 的環境很乾淨，不能假設有這個變數。2026-09-14 實測確認。
export USER="${USER:-$(id -un)}"
export LOGNAME="${LOGNAME:-$USER}"


# ⚠️ 一定要用絕對路徑。launchd 的 PATH 很乾淨，python3 會指到 Apple 內建版本，
# 那個版本沒有 requests，2026-08-28～30 的排程就是這樣連續失敗三天沒人知道。
PY=""
for candidate in \
    /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 \
    /opt/homebrew/bin/python3 \
    /usr/local/bin/python3 \
    /usr/bin/python3
do
    if [ -x "$candidate" ] && "$candidate" -c "import requests" 2>/dev/null; then
        PY="$candidate"
        break
    fi
done

# 找不到堪用的 Python 時，用 curl 直接告警——這條路不依賴任何 Python 套件
alert() {
    local msg="$1"
    # 只用知識庫自己的設定，不借用 Maxtrading Review 的管道
    local env_file="/Users/mmfamily/Max KnowledgeBase/.env"
    [ -f "$env_file" ] || return
    local token chat
    token=$(grep -m1 '^TELEGRAM_BOT_TOKEN=' "$env_file" 2>/dev/null | cut -d= -f2- | tr -d '"'"'"' ')
    chat=$(grep -m1 '^TELEGRAM_CHAT_ID=' "$env_file" 2>/dev/null | cut -d= -f2- | tr -d '"'"'"' ')
    [ -z "$token" ] && return
    curl -sS --max-time 20 -o /dev/null \
        "https://api.telegram.org/bot${token}/sendMessage" \
        --data-urlencode "chat_id=${chat}" \
        --data-urlencode "text=${msg}"
}

if [ -z "$PY" ]; then
    echo "❌ 找不到裝有 requests 的 python3"
    alert "🚨 知識庫排程失敗：找不到裝有 requests 的 python3，今天沒有更新。"
    exit 1
fi

# ⚠️ 一定要先拉。github-sync 是 Obsidian 外掛，**Obsidian 沒開就不會同步**，
# n8n 存進 GitHub 的新檔在本機根本不存在，後面的補圖與消化全都會漏掉。
echo "----- git pull -----"
if git -C "/Users/mmfamily/Max KnowledgeBase" pull --ff-only 2>&1; then
    echo "✅ 已同步遠端"
else
    echo "⚠️ git pull 失敗，繼續用本機現有檔案（可能漏掉 n8n 新存的）"
    alert "⚠️ 知識庫 git pull 失敗，今天的補圖／消化可能漏掉 n8n 新存的檔案。"
fi

echo "===== $(date '+%Y-%m-%d %H:%M:%S') 每日更新開始（$PY）====="
failed=""
"$PY" tools/fetch_market.py  || failed="${failed}抓取 "
"$PY" tools/fetch_media.py   || failed="${failed}補圖 "
bash tools/read_shots.sh     || failed="${failed}讀圖 "
"$PY" tools/build_pages.py   || failed="${failed}建頁 "
"$PY" tools/digest.py        || failed="${failed}統整 "

# 判斷層：有未消化檔案才會真的呼叫 Claude，沒事不花錢
bash tools/auto_ingest.sh    || failed="${failed}自動消化 "
"$PY" tools/health_check.py  || failed="${failed}健檢 "

if [ -n "$failed" ]; then
    echo "⚠️ 失敗階段：$failed"
    alert "🚨 知識庫每日更新有階段失敗：${failed}
請看 data/launchd_error.log"
fi
echo "===== $(date '+%Y-%m-%d %H:%M:%S') 每日更新結束 ====="
