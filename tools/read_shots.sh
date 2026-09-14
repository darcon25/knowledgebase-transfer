#!/bin/bash
# 讀圖層：把 shot_*.md 的「## 內容」從佔位符變成真的內容。
#
# 為什麼需要這一步：
#   fetch_media.py 只負責「下載」，下載不等於「讀懂」。
#   很多 Threads/IG 貼文的重點整個在圖裡（法說圖卡、投行表格、產業鏈圖），
#   純文字摘要完全看不到那些數字。圖抓回來了但沒人讀，等於沒補。
#
# 刻意的限制（與 auto_ingest.sh 一致）：
#   - 只處理 status: 待讀圖 的 shot_ 檔，沒有就不啟動（不燒 token）
#   - 只准填 shot_ 檔的「## 內容」段落，不准碰 raw/ 的其他檔案
#   - 一次最多處理 MAX_BATCH 篇，避免單次跑太久或爆量
cd "/Users/mmfamily/Max KnowledgeBase" || exit 1

# ⚠️ 地雷：claude CLI 的憑證存在 macOS Keychain，**沒有 USER 環境變數就讀不到**，
# 會回「OAuth session expired and could not be refreshed」而整個消化階段靜默失敗。
# launchd 的環境很乾淨，不能假設有這個變數。2026-09-14 實測確認。
export USER="${USER:-$(id -un)}"
export LOGNAME="${LOGNAME:-$USER}"


MAX_BATCH="${1:-8}"

PY=""
for c in /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 \
         /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3; do
    [ -x "$c" ] && "$c" -c "import requests" 2>/dev/null && PY="$c" && break
done
[ -z "$PY" ] && echo "❌ 找不到堪用的 python3" && exit 1

CLAUDE="/Users/mmfamily/.nvm/versions/node/v22.22.2/bin/claude"
[ -x "$CLAUDE" ] || { echo "❌ 找不到 claude CLI"; exit 1; }

PENDING=$(grep -l "^status: 待讀圖$" raw/shot_*.md 2>/dev/null | head -n "$MAX_BATCH")

if [ -z "$PENDING" ]; then
    echo "[$(date '+%F %T')] 沒有待讀圖的檔案，不啟動 Claude"
    exit 0
fi

COUNT=$(echo "$PENDING" | wc -l | tr -d ' ')
echo "[$(date '+%F %T')] 發現 $COUNT 個待讀圖檔案"
echo "$PENDING"

PROMPT="你在 /Users/mmfamily/Max KnowledgeBase 這個 Obsidian 知識庫裡工作。

以下 shot_ 檔案剛用 tools/fetch_media.py 從原貼文補回圖片，但「## 內容」還是佔位符
「（待讀圖後填寫）」。請**用 Read 工具逐一打開每個檔案裡 ![[...]] 指向的
raw/assets/ 圖片，實際看圖**，然後把內容寫進該檔的「## 內容」段落。

待處理檔案：
$PENDING

寫作要求：
1. **每一張圖都要讀、都要寫**。有四張就寫四張，不要只寫第一張。
   多張時用「### 圖 1｜<小標>」分段。
2. **把圖裡的數字與表格照抄成 Markdown 表格**。這是整件事的重點——
   這些數字原本的純文字摘要一個都沒有，不要只寫「圖中顯示財報數據」這種空話。
3. 只寫圖上真的有的東西。看不清楚就寫「圖片模糊無法辨識」，**不要推測、不要補充背景知識**。
4. 如果是影片封面或純封面圖（沒有實質內容），就直說「這是影片，只抓得到封面縮圖」，
   並說明從標題能推得什麼、不能推得什麼。
5. 發現圖裡的數字自相矛盾或與說明文字不符時，**明確標出來**（用 ⚠️），
   例如說明寫 GPU 233% 但表格裡 233% 那列其實是 PCB。
6. 最後加一段「**為什麼這幾張圖重要**」，說明可以餵給哪些 wiki 頁面，
   並用 [[雙括號]] 連到相關頁面或其他 shot_ 檔。
7. 寫完把該檔的 \`status: 待讀圖\` 改成 \`status: 已讀圖\`。

嚴格禁止：
- 不要修改 raw/ 裡的**其他**檔案。這次唯一的例外是上列 shot_ 檔的
  「## 內容」段落與 status 那一行——那兩處本來就是留白待填的。
- 不要碰原始的 threads_*.md / instagram_*.md 筆記（那些是 n8n 存的原始資料，永遠唯讀）。
- 不要寫 wiki/（消化進 wiki 是 auto_ingest.sh 的工作，不是這一步）。

最後用三到五行中文說明你讀了幾篇、幾張圖、哪幾篇最有價值。"

OUTPUT=$("$CLAUDE" -p "$PROMPT" \
    --add-dir "/Users/mmfamily/Max KnowledgeBase" \
    --allowed-tools "Read,Edit,Glob,Grep" \
    --permission-mode acceptEdits 2>&1)
STATUS=$?

echo "$OUTPUT"

LEFT=$(grep -l "^status: 待讀圖$" raw/shot_*.md 2>/dev/null | wc -l | tr -d ' ')
SUMMARY=$(echo "$OUTPUT" | tail -10)

if [ $STATUS -ne 0 ]; then
    "$PY" tools/notify.py "🤖 <b>自動讀圖失敗</b>
$COUNT 篇待讀，但 Claude 執行出錯。請開對話手動處理。"
else
    "$PY" tools/notify.py "🖼 <b>自動讀圖完成</b>（$COUNT 篇）

$SUMMARY

還有 $LEFT 篇待讀。⚠️ AI 讀圖可能看錯數字，重要數據請抽查原圖。"
fi
