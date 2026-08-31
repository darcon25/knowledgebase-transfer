#!/bin/bash
# 判斷層自動化：有新資料才叫 Claude 消化，沒事就不花錢。
#
# 刻意的限制：
#   - 只在有未消化檔案時啟動（沒事不燒 token）
#   - 只能寫 wiki/，不准碰 raw/ 與 Clippings/（原始資料不可修改）
#   - 不准動 <!-- AUTO --> 區塊（那是 build_pages.py 的地盤）
#   - 寫入的內容一律標 🤖 與日期，方便事後辨識與稽核
cd "/Users/mmfamily/Max KnowledgeBase" || exit 1

PY=""
for c in /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 \
         /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3; do
    [ -x "$c" ] && "$c" -c "import requests" 2>/dev/null && PY="$c" && break
done
[ -z "$PY" ] && echo "❌ 找不到堪用的 python3" && exit 1

CLAUDE="/Users/mmfamily/.nvm/versions/node/v22.22.2/bin/claude"
[ -x "$CLAUDE" ] || { echo "❌ 找不到 claude CLI"; exit 1; }

# 有未消化的檔案嗎？沒有就直接結束
PENDING=$("$PY" - <<'PYEOF'
import json
from pathlib import Path
kb = Path("/Users/mmfamily/Max KnowledgeBase")
try:
    done = set(json.loads((kb / "data" / "ingested.json").read_text(encoding="utf-8"))["files"])
except Exception:
    done = set()
pending = []
for folder in ("raw", "Clippings"):
    for f in sorted((kb / folder).glob("*.md")):
        rel = f"{folder}/{f.name}"
        if rel not in done:
            pending.append(rel)
print("\n".join(pending))
PYEOF
)

if [ -z "$PENDING" ]; then
    echo "[$(date '+%F %T')] 沒有未消化的檔案，不啟動 Claude"
    exit 0
fi

COUNT=$(echo "$PENDING" | wc -l | tr -d ' ')
echo "[$(date '+%F %T')] 發現 $COUNT 個未消化檔案，啟動自動消化"
echo "$PENDING"

PROMPT="你在 /Users/mmfamily/Max KnowledgeBase 這個 Obsidian 知識庫裡工作。

先讀 CLAUDE.md 了解規則，然後消化以下未消化的來源檔案：
$PENDING

嚴格遵守：
1. 絕對不要修改 raw/ 與 Clippings/ 裡的任何檔案（原始資料不可變）
2. 絕對不要碰任何 <!-- AUTO:START --> 到 <!-- AUTO:END --> 之間的內容
3. 每一個你寫下的事實都必須來自來源檔，不確定就寫「原文未說明」，不要自行補充推論
4. 你新增的段落開頭標上「🤖 $(date '+%Y-%m-%d') 自動消化」
5. 消化完務必把檔案路徑加進 data/ingested.json 的 files 陣列
6. 分流規則見 CLAUDE.md「分流判斷」那一段（2026-08-31 已放寬）：
   - 提到名單公司 → 更新該公司頁的「事件時間軸」
   - 只有主題相關（AI 伺服器、資料中心、電力、散熱、半導體、輝達／台積電供應鏈、
     總經等）→ 更新或新建 wiki/investing/themes/ 的驅動因素頁，
     並從受影響的公司頁連過去
   - 都不是 → 才歸進 wiki/topics/
7. 新建任何頁面後，務必在 wiki/overview.md 加一行連結，否則會變孤島頁
8. 不要建立新的 insights 頁，也不要改公司頁的「我的論點」——那需要人的判斷

最後用三到五行中文說明你做了什麼、動到哪些檔案。"

OUTPUT=$("$CLAUDE" -p "$PROMPT" \
    --add-dir "/Users/mmfamily/Max KnowledgeBase" \
    --allowed-tools "Read,Write,Edit,Glob,Grep" \
    --permission-mode acceptEdits 2>&1)
STATUS=$?

echo "$OUTPUT"

SUMMARY=$(echo "$OUTPUT" | tail -12)
if [ $STATUS -ne 0 ]; then
    "$PY" tools/notify.py "🤖 <b>自動消化失敗</b>
$COUNT 個檔案待處理，但 Claude 執行出錯。
請開對話手動處理。"
else
    "$PY" tools/notify.py "🤖 <b>自動消化完成</b>（$COUNT 個檔案）

$SUMMARY

⚠️ AI 寫的內容已標記 🤖，建議抽查。"
fi
