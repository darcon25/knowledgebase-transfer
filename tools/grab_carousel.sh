#!/bin/bash
# 用已登入的 Chrome 抓 IG 輪播的完整圖片。
#
# 為什麼需要：登出狀態的 Instagram 只吐得出輪播的前一兩張（Threads 沒這問題），
# 連 IG 自己的公開 API 也擋。只有已登入的瀏覽器看得到全部。
#
# 前置條件（兩道鎖，缺一不可）：
#   1. 系統設定 → 隱私權與安全性 → 自動化 → 終端機 → 勾選 Google Chrome
#   2. Chrome 選單列 → 檢視 → 開發人員 → 允許 Apple 事件的 JavaScript
#      ⚠️ 這道鎖用完建議關掉：開著時任何有權限的程式都能在你的分頁執行 JS
#
# 用法：
#   bash tools/grab_carousel.sh <IG貼文網址> <存檔前綴>
# 例：
#   bash tools/grab_carousel.sh https://www.instagram.com/p/Dc75npUE6uq/ instagram_2026-09-08_台股散熱題材投資筆記
set -u
KB="/Users/mmfamily/Max KnowledgeBase"
URL="${1:?請給 IG 貼文網址}"
PREFIX="${2:?請給存檔前綴（不含編號與副檔名）}"
MAX_SLIDES="${3:-20}"

js() {
  osascript -e "with timeout of 40 seconds
tell application \"Google Chrome\"
  return execute front window's active tab javascript \"$1\"
end tell
end timeout" 2>&1 | head -5
}

echo "▶ 開新視窗載入：$URL"
osascript -e "with timeout of 30 seconds
tell application \"Google Chrome\"
  set w to make new window
  set URL of active tab of w to \"$URL\"
end tell
end timeout" >/dev/null 2>&1
sleep 8

if js "document.title" | grep -qi "error\|未獲授權\|已關閉"; then
    echo "❌ 無法執行 JavaScript，請確認上面兩道鎖都開了"; exit 1
fi

# 先倒回第一張（貼文網址可能帶 img_index 直接跳到中間）
# ⚠️ 這裡的等待不能短。2026-09-14 實測 sleep 1/2 只抓到 5/11 張——
#    IG 是點了才載入，圖還沒載完就 grab 會整格漏掉，而且不會有任何錯誤。
for _ in $(seq 1 "$MAX_SLIDES"); do
  R=$(js "(function(){var b=[...document.querySelectorAll('button')].find(function(x){return (x.getAttribute('aria-label')||'')==='上一步';});if(!b)return 'AT_START';b.click();return 'back';})()")
  [ "$R" = "AT_START" ] && break
  sleep 1.5
done

# 累積器：只收「輪播 ul 容器」裡的大圖，避開推薦貼文與大頭貼的雜訊
js "(function(){
  window.__grab=function(){
    var ul=null;
    for(var n=0;n<document.images.length;n++){
      var im=document.images[n];
      if(im.naturalWidth>=600){
        var p=im,d=0;
        while(p&&d<12){ if(p.tagName==='UL'){ul=p;break;} p=p.parentElement; d++; }
        if(ul)break;
      }
    }
    if(!ul)return 0;
    [].forEach.call(ul.querySelectorAll('img'),function(x){
      if(x.naturalWidth>=600&&window.__kb.indexOf(x.src)<0)window.__kb.push(x.src);
    });
    return window.__kb.length;
  };
  window.__kb=[];
  return window.__grab();
})()" >/dev/null

echo "▶ 逐格翻頁"
for i in $(seq 1 "$MAX_SLIDES"); do
  sleep 3                       # 先等圖載完再收，順序不能顛倒
  N=$(js "window.__grab()")
  R=$(js "(function(){var b=[...document.querySelectorAll('button')].find(function(x){return (x.getAttribute('aria-label')||'')==='下一步';});if(!b)return 'END';b.click();return 'ok';})()")
  echo "   第 $i 格：累積 $N 張"
  [ "$R" = "END" ] && break
done
sleep 3
TOTAL=$(js "window.__grab()")

# 用頁碼圓點交叉驗證有沒有抓齊——這是唯一能自動察覺漏抓的線索
DOTS=$(js "(function(){var d=[...document.querySelectorAll('div')].filter(function(x){return x.children.length>2&&x.children.length<25&&[].every.call(x.children,function(c){return c.tagName==='DIV'&&c.offsetWidth<=10&&c.offsetWidth>=4;});});return d.length?d[0].children.length:0;})()")
echo "▶ 共 $TOTAL 張（頁碼圓點顯示 $DOTS 格）"
if [ "$DOTS" -gt 0 ] 2>/dev/null && [ "$TOTAL" -lt "$DOTS" ] 2>/dev/null; then
  echo "   ⚠️ 抓到的張數少於圓點數，可能漏抓，請重跑一次"
fi

TMP=$(mktemp)
osascript -e "with timeout of 40 seconds
tell application \"Google Chrome\"
  return execute front window's active tab javascript \"window.__kb.join(String.fromCharCode(10))\"
end tell
end timeout" > "$TMP" 2>&1

n=1
while read -r u; do
  [ -z "$u" ] && continue
  f=$(printf "%s/raw/assets/%s_%02d.jpg" "$KB" "$PREFIX" "$n")
  code=$(curl -s -m 60 -o "$f" -w "%{http_code}" "$u")
  echo "   $(basename "$f") http=$code $(du -h "$f" 2>/dev/null | cut -f1)"
  n=$((n+1))
done < "$TMP"
rm -f "$TMP"

# 抓完就關掉這個視窗，不留在使用者的分頁堆裡
osascript -e 'tell application "Google Chrome" to close front window' >/dev/null 2>&1
echo "✅ 完成，共 $((n-1)) 張"
