#!/bin/bash
# 補讀機制：一天多次回來檢查有沒有漏掉的圖還沒抓、沒讀。
#
# 為什麼需要：18:30 那一次是「當天唯一機會」，任何一次失敗（網路抖、Jina 限流、
# 貼文還沒同步下來、claude 認證問題）都要等隔天。這支腳本每兩小時回來補一次。
#
# 設計原則：
#   - **冪等**：已經抓過／讀過的一律跳過，重複執行不會做白工也不會重複扣費
#   - **安靜**：沒事不推播，只有連續失敗到門檻才叫人
#   - **輕量**：只做 git pull + 補圖 + 讀圖，不跑建頁／統整／消化（那些留給 18:30）
cd "/Users/mmfamily/Max KnowledgeBase" || exit 1

# ⚠️ 地雷：claude CLI 的憑證在 macOS Keychain，沒有 USER 就讀不到（2026-09-14 實測）
export USER="${USER:-$(id -un)}"
export LOGNAME="${LOGNAME:-$USER}"

ALERT_THRESHOLD="${ALERT_THRESHOLD:-3}"   # 同一篇連續失敗幾次才叫人

PY=""
for c in /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 \
         /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3; do
    [ -x "$c" ] && "$c" -c "import requests" 2>/dev/null && PY="$c" && break
done
[ -z "$PY" ] && echo "❌ 找不到堪用的 python3" && exit 1

STAMP="$(date '+%F %T')"

# 1) 先拉。Obsidian 沒開時 github-sync 不會同步，n8n 存的新檔本機根本沒有。
git pull --ff-only >/dev/null 2>&1 || echo "[$STAMP] ⚠️ git pull 失敗，用本機現有檔案"

# 2) 有沒有事情可做？沒有就安靜結束，完全不啟動下游
PENDING_MEDIA=$("$PY" - <<'PYEOF'
import json, re
from pathlib import Path
KB = Path("/Users/mmfamily/Max KnowledgeBase")
def load(p):
    try: return json.loads((KB / p).read_text(encoding="utf-8"))
    except Exception: return {}
checked = load("data/known_issues.json").get("media_checked", {})
captured = set()
for f in (KB / "raw").glob("shot_*.md"):
    m = re.search(r'original_url:\s*"([^"]+)"', f.read_text(encoding="utf-8", errors="ignore"))
    if m: captured.add(m.group(1).split("?")[0])
n = 0
for f in (KB / "raw").glob("*.md"):
    if f.name.startswith("shot_"): continue
    t = f.read_text(encoding="utf-8", errors="ignore")
    if not re.search(r"^platform:\s*(threads|instagram)\s*$", t[:800], re.M): continue
    m = re.search(r'^original_url:\s*"?([^"\n]+)"?\s*$', t[:800], re.M)
    url = (m.group(1).strip().lstrip("/") if m else "").split("?")[0]
    url = url if url.startswith("http") else "https://" + url
    if url in captured or f"raw/{f.name}" in checked: continue
    n += 1
print(n)
PYEOF
)
PENDING_READ=$(grep -l "^status: 待讀圖$" raw/shot_*.md 2>/dev/null | wc -l | tr -d ' ')

if [ "$PENDING_MEDIA" -eq 0 ] && [ "$PENDING_READ" -eq 0 ]; then
    echo "[$STAMP] 沒有待補的圖、也沒有待讀的圖，安靜結束"
    exit 0
fi

echo "[$STAMP] 待補圖 $PENDING_MEDIA 篇、待讀圖 $PENDING_READ 篇，開始補"

# 3) 補圖（冪等，已抓過的自動跳過）
[ "$PENDING_MEDIA" -gt 0 ] && "$PY" tools/fetch_media.py

# 4) 讀圖（冪等，已讀過的自動跳過）
REMAIN_READ=$(grep -l "^status: 待讀圖$" raw/shot_*.md 2>/dev/null | wc -l | tr -d ' ')
[ "$REMAIN_READ" -gt 0 ] && bash tools/read_shots.sh

# 5) 只有「連續失敗到門檻」才叫人——避免每兩小時吵一次
"$PY" - "$ALERT_THRESHOLD" <<'PYEOF'
import json, sys
from pathlib import Path
KB = Path("/Users/mmfamily/Max KnowledgeBase")
sys.path.insert(0, str(KB / "tools"))
threshold = int(sys.argv[1])
try:
    retry = json.loads((KB / "data" / "media_retry.json").read_text(encoding="utf-8"))
except Exception:
    retry = {}
stuck = {k: v for k, v in retry.items() if v.get("attempts", 0) >= threshold}
if not stuck:
    raise SystemExit(0)
lines = [f"• {k.split('/')[-1]}：失敗 {v['attempts']} 次（{v.get('last_error','')[:60]}）"
         for k, v in sorted(stuck.items(), key=lambda x: -x[1]["attempts"])]
msg = ("🖼 <b>補圖一直失敗</b>\n\n" + "\n".join(lines[:10])
       + f"\n\n已重試 {threshold} 次以上仍失敗，可能要開對話手動看。")
try:
    import notify
    notify.send(msg)
except Exception as e:
    print("（通知送不出去：%s）" % e)
PYEOF

echo "[$STAMP] 補讀結束"
