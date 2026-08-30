# 操作紀錄

> 這份文件記錄所有對知識庫的操作，只增不減。  
> 格式：`## [YYYY-MM-DD] 操作類型 | 標題`

---

## [2026-04-27] update | 知識庫初始化
建立知識庫架構，包含 CLAUDE.md（操作規則）、index.md（目錄）、log.md（本文件）、wiki/overview.md（概覽），以及 raw/、wiki/entities/、wiki/concepts/、wiki/sources/ 等目錄結構。

## [2026-04-27] ingest | 重複的例行工作，讓 Claude 幫你打包成一個 Skill｜EP.26
消化 AgentCrew Academy EP.26 影片逐字稿。建立來源摘要頁面、3 個概念頁面（Skill技能手冊、MCP工具協議、個人知識庫與第二大腦）、1 個實體頁面（AgentCrew Academy），並更新 index.md 與 overview.md。

## [2026-05-05] ingest | 批次消化 16 個 raw 檔案
處理 raw/ 目錄中的 16 個待消化檔案。

**跳過（無實質內容）**：6 個 Threads 404 錯誤頁面（threads_2026-04-29 系列共 6 個）、EP.26 已消化。

**新建來源頁面（9）**：Claude-Code-Obsidian知識庫節省Token、AI製作PPT工具與Claude-Design、Cloudflare轉型與75分雜學家、Google-2026數位人才探索計畫、ChatGPT財經分析師應用、Claude-Code-AI員工定位、Claude-Code六大核心技能、LINE-Bot自動備份、AI-Agent團隊實戰架構。

**新建概念頁面（2）**：Claude-Design、AI-Agent工作流。

**更新概念頁面（2）**：Skill技能手冊（新增六大核心技能表格）、個人知識庫與第二大腦（新增 Karpathy 方法說明）。

**更新**：index.md（頁面總數 6 → 17）、overview.md。

## [2026-08-28] update | 知識庫改造：多平台進料 × 投資關聯圖 × 每日健檢

把知識庫從「一篇來源一頁摘要」改成投資分析層，連結數 38 → 500+。

**新增工具**（`tools/`）：`capture.py`（YouTube 逐字稿、截圖歸檔）、`fetch_market.py`（月營收／估值／新聞，四個免費 API，含 3 次重試）、`watchlist.py`（36 檔 PCB/CCL 供應鏈名單）、`build_pages.py`（只覆寫 AUTO 區塊，手寫內容永不動）、`health_check.py`（七類問題巡檢）、`notify.py`（Telegram，含重試）、`daily.sh`。

**新增頁面**：36 家公司頁、11 個環節頁、1 條產業鏈頁、3 個驅動因素頁、1 份分析（2026-08-28 PCB 鏈定價檢驗）、1 個月營收頁、4 個非投資主題頁、DATAROMA、知識庫進料管道。

**消化積壓 10 檔**：投資相關 2 檔（半導體 HBM4 筆記、DATAROMA）深度處理；其餘 8 檔按主題歸入 `wiki/topics/`。

**修正**：`check-new-files.py` 現在同時掃 `Clippings/`，並改用 `data/ingested.json` 明確清單比對（原本比對 log.md 文字，會把已消化的 16 檔全部誤報）。

**自動化**：launchd `com.max.knowledgebase.daily` 每天 18:30 跑「抓取 → 建頁 → 健檢 → 推 Telegram」。

**新增 agent**：`.claude/agents/kb-auditor.md`，唯讀稽核員，查需要判讀的問題（訊號矛盾、摘要失真、論點過期）。

**首次健檢結果**：3 項真實問題——Clippings 有一篇重複存檔（cool3c 245188 存兩次）、2 個 raw 檔內容截斷。

## [2026-08-28] lint | 首次稽核（kb-auditor）並修正三項實質錯誤

跑 kb-auditor 稽核當日產出，抓到三個 LLM 判讀層的錯誤，全部已修：

1. **幻覺**：`themes/HBM4與先進封裝.md` 對已知截斷的原文，加了原文沒說的技術解釋（「不用凸塊」「供電穩定性」）→ 改為逐字引用，並註明未知部分。
2. **漏接矛盾訊號**：8/27「PTFE 取代 CCL 傳言使台光電急殺跌停」已在抓回來的新聞裡，卻沒被任何分析引用 → 補進 `chains/AI伺服器PCB鏈.md` 矛盾訊號區、`themes/銅箔報價與銅價.md` 警語、分析頁待查清單。
3. **答案就在資料裡卻寫「未查明」**：宏和 1446 營收 -87.7% 的原因，公司備註早就寫了「本月營建無認列收入」→ 三處「未查明」全部更正。

另確認：抽查 5 家公司頁數字與原始 JSON 完全一致，連結對象無誤連，`build_pages.py` 本身可靠。

**稽核總評**：數字層可信，判斷層尚未啟動——36 家公司頁的「我的論點」全空白，含 7 檔實際持倉。

## [2026-08-28] update | 清除重複存檔、補上 6 檔持倉論點建議稿

**刪除**：`Clippings/別再只會手帳風...你也會用AI.md`（7/8 存的舊版，14,974 bytes），保留 7/21 較完整的 `...GEMINI (245188).md`（19,080 bytes）。舊檔仍在 git 歷史（commit 17e124f）可還原。同步更新 `data/ingested.json` 與 `wiki/topics/設計靈感.md`。

**新增**：6 檔鏈上持倉（台燿、金像電、金居、臻鼎、日月光、台達電）的「我的論點／觀察指標／還缺什麼」建議稿，每頁開頭明確標示為 Claude 建議稿而非使用者判斷。

健檢從 3 項降到 2 項，剩下的兩項都是原始檔內容截斷，屬進料管道問題。

## [2026-08-30] update | 九項問題逐項修正

**已修（7 項）**
1. **截圖管道支援多圖**：`capture.py --shot 圖1 圖2 …` 或直接給資料夾，IG 輪播可一次存成一則筆記，並可附 `--source` 原貼文網址。
2. **截斷檔處理**：逐篇嘗試 WebFetch 重抓。桃機 P4 停車完整補齊寫入 `topics/旅遊與生活`；Claude Design 那篇確認無資訊損失；其餘 7 篇重抓內容比原摘要更少（WebFetch 拿不到串文與留言），決定不補。十大封裝技術那篇內容在圖片裡，只能靠截圖，已列入 `wiki/待補資料清單`。
3. **刪除 6 篇 404 空頁**（threads_2026-04-29 系列），原始網址保留在待補清單。
4. **健檢加入「已確認」機制**（`data/known_issues.json`），處理過的問題不再每天重複提醒。截斷項從 10 降到 1。
5. **PTFE 傳言查證**：不是取代 CCL 環節，是材料世代轉換（Dk 3.0→2.1、Df 0.007→0.0005）。**真正受威脅的是玻纖布**——無布化 PTFE 捨棄玻纖布改用純樹脂加二氧化矽。中國生益領先且據稱已通過輝達認可，台廠三雄仍在送認證。新增 `themes/PTFE與材料世代轉換`，並回頭修正鏈頁、玻纖布、銅箔、台燿四頁的判讀。
6. **楠梓電低本益比查明**：獲利有很大部分來自轉投資中國滬電，本益比與 PCB 本業成長不對應，已排除在鏈內比較之外。金像電因此成為 PCB 環節定價最合理的一檔。
7. **接入毛利率**（證交所／櫃買季度營益分析，37 檔）與**回補 12 個月歷史月營收**（MOPS Big5 HTML 解析）。公司頁新增「營收趨勢」六期走勢與加速／減速判定。

**順帶修掉的意外**：櫃買中心 SSL 憑證（TWCA 缺 Subject Key Identifier）在新版 OpenSSL 下被 Python 拒絕，2026-08-30 首次發生。已加 curl 備援，憑證仍有驗證。

**未解（2 項）**
- 手機管道的輸出長度上限（根因）——需要找出設定位置
- 30 家觀察股的論點空白——低優先，非缺陷

## [2026-08-30] update | 查明 Telegram → n8n 進料管道，兩個缺陷歸因完成

管道位置終於找到：n8n 自架於 Zeabur（`https://maxyyy.zeabur.app`，workflow `gMt3TVBIagJGA6PG`）。
流程：Telegram Trigger → Extract URL → Jina Reader → Prepare Gemini Prompt → Call Gemini API（gemini-2.5-flash）→ Build Markdown → Commit to GitHub → Check Result → Send Telegram Reply。

**缺陷 A｜Jina Reader 讀不動 Threads/IG**：抓到的常是錯誤頁而非貼文 → 那 6 篇「404 空頁」很可能**不是貼文失效**，管道修好後重傳即可。且 Jina 只回文字不回圖片 → 四個月來 `raw/assets/` 一張圖都沒有。此項無解，有圖貼文改走截圖管道。

**缺陷 B｜Gemini 輸出長度上限**：15 篇裡 10 篇斷在句中。gemini-2.5-flash 的「思考」也吃輸出額度，額度不足時筆記會被切斷。待確認 `maxOutputTokens` 與 `thinkingConfig` 實際設定值。

建議修法（三選一或全做）：拉高 maxOutputTokens 並關掉 thinking／把 Jina 原文一併寫進檔案／檢查 finishReason 為 MAX_TOKENS 時在 Telegram 告警。

已更新 `wiki/entities/知識庫進料管道.md`（含查證過程與排除順序）、`wiki/待補資料清單.md`、`wiki/entities/資料源與限制.md`。

## [2026-08-30] ingest | 十大封裝技術補齊，驗證電腦 Chrome 補救路徑

用電腦版 Chrome（已登入 Threads）開啟 `@solution_provider_/post/DavPf5mAcgp`，點開圖片放大後自動截圖，存為 `raw/shot_2026-08-30_01.md` + `raw/assets/shot_2026-08-30_01.jpg`。**這是 raw/assets/ 四個月來的第一張圖。**

四個月前被 Jina Reader 漏掉的內容完整補回：十種封裝技術（打線、覆晶、WLCSP、Fan-In/Fan-Out WLP、SiP、Chiplet、2.5D、3D IC、Hybrid Bonding）的定義、特性與應用。[[HBM4與先進封裝]] 已改寫，補上 2.5D／3D IC／Hybrid Bonding 三者與 HBM4 的關係與技術演進脈絡。

**新增補救路徑並寫入 [[知識庫進料管道]]**：Claude 驅動使用者電腦上已登入的 Chrome 抓貼文與圖片，不需手機手動截圖。限制是需要電腦開機、有網路、且在對話中——**不是背景自動化**，所以與 n8n 雲端管道並存：n8n 負責 24 小時不漏接，電腦端負責補齊。

**健檢首次歸零**（0 項問題）。

## [2026-08-30] update | 截斷根因確認：Gemini maxOutputTokens = 1500

查看 n8n `Call Gemini API` 節點的 Body/JSON，確認原設定為
`generationConfig: { temperature: 0.3, maxOutputTokens: 1500 }`，且**沒有 thinkingConfig**。

gemini-2.5-flash 預設開啟思考，思考 token 也計入這 1500 的額度。1500 token 中文約 1000–1500 字（UTF-8 約 2000–4500 bytes），與被截斷檔案的實際大小 2000–3400 bytes 完全吻合。

建議修法已寫入 [[知識庫進料管道]]：把 maxOutputTokens 改為 8192 並加入 `thinkingConfig: { thinkingBudget: 0 }`；另建議把 Jina 原文一併存檔、以及在 Check Result 檢查 finishReason 為 MAX_TOKENS 時告警。

## [2026-08-31] update | 加入漏圖偵測，並記錄關鍵字法的失敗

**問題**：截斷偵測已有，但「這篇有圖沒抓到」完全沒有偵測能力。

**失敗的嘗試**：關鍵字掃描（「一張圖」「如下圖」等）。實測發現它**漏掉了十大封裝技術那篇**——線索句在貼文開頭，而開頭連同整段被截斷，文字被切、線索也跟著被切。噪音也大（「1/」誤中日期、「影片」誤中純文字貼文）。

**改用的規則**：Threads/IG 是以圖為主的平台且 Jina 拿不到圖，因此凡此兩平台來源、沒有對應 `shot_*.md` 的檔案，一律列為「圖片未確認」。噪音換不漏接，目前列出 13 筆。逐篇確認後記進 `data/known_issues.json` 的 `media_checked` 即不再提醒。

**截斷偵測的盲點也記錄下來**：若 Gemini 剛好在句號處用完額度就抓不到，唯一可靠解是 n8n 端檢查 `finishReason == MAX_TOKENS`。

**更精準的作法**：Jina 回傳的 markdown 含 `![](網址)`，在 Build Markdown 節點數量寫進 frontmatter `media_count`，健檢即可精準比對。屬修法二的附加好處。

## [2026-08-31] ingest | 13 篇圖片逐一確認，兩篇實質補齊

用電腦 Chrome 逐篇開啟檢查（以 JavaScript 讀取圖片數量與 alt，不逐篇截圖，成本低）。結果：

| 類型 | 篇數 | 處理 |
|---|---|---|
| 圖是內容本身 | 2 | **已補齊** |
| 圖與文字重複 | 6 | 記錄後結案 |
| 只有連結預覽縮圖 | 2 | 非內容圖，結案 |
| 純文字沒有圖 | 1 | 結案 |
| 無法檢查 | 1 | instagram.com 瀏覽器權限不允許；該則為 Reel（影片） |
| 已於 08-30 補齊 | 1 | 十大封裝技術 |

**實質補齊的兩篇**

1. `threads_2026-05-06_ofcr2zbd`（AI 生圖字體）——32 種字體控制指令全在兩張圖裡，已抓下並整理成兩份可直接複製的清單（16 種字體名稱 + 16 種風格描述），寫入 `raw/shot_2026-08-31_01.md` 與 [[設計靈感]]。
2. `threads_2026-05-04_2oh8tf9q`（Claude Code 8 件事）——原檔只有標題沒有內文，補齊完整 8 點寫入 [[AI工具與工作流]]。

13 篇的確認結果全部記進 `data/known_issues.json` 的 `media_checked`，健檢回到 0 項。

**副產品**：確認 JavaScript 讀 `img` 的 alt 與尺寸就能判斷有無圖片，不必逐篇截圖——之後批次檢查都用這個方法。

## [2026-08-31] update | 開機自動檢查；並修掉讓每日排程失敗三天的地雷

**新增開機檢查**：`tools/boot_check.py` + launchd `com.max.knowledgebase.boot`（RunAtLoad）。
流程：等網路（最多 5 分鐘）→ `git pull --ff-only` 拉 n8n 存進 GitHub 的新檔 → 跑健檢 → **有待處理項目才推 Telegram**，沒事就安靜。通知會分成「需要在電腦前處理」（截斷、圖片未確認、尚未消化）與「其他」。

**發現並修掉一個嚴重問題**：每日排程 2026-08-28、08-29、08-30 連續三天失敗。
原因是 launchd 的 PATH 只有 `/usr/bin:/bin:...`，`python3` 指到 Apple 內建版本，**該版本沒有 requests**。抓取與健檢兩階段都掛掉，只有 build_pages 成功（它不 import requests）。更糟的是負責回報失敗的健檢本身也是 Python，**連錯誤都送不出來**。

修法：
1. `daily.sh` 逐一測試候選 python 路徑，挑出真的能 `import requests` 的那個
2. 任何階段失敗時，用 **curl** 直接送 Telegram 告警——不依賴 Python 套件，不會跟主程式一起死（已實測 http=200）
3. boot plist 改用絕對路徑

已在 launchd 的乾淨環境（`env -i`）實測 daily.sh 全綠。地雷紀錄寫進 CLAUDE.md。

**教訓**：在終端機手動測試通過 ≠ 排程能跑。要用 `env -i HOME=$HOME PATH=/usr/bin:/bin bash script.sh` 模擬排程環境驗證。

## [2026-08-31] update | 通知管道與 Maxtrading Review 切開；補上 .gitignore

依使用者要求，知識庫的訊息不再發給 `MaxInvestmentreview_bot`。

- `tools/notify.py` 現在**只讀 `Max KnowledgeBase/.env`**，移除對 `Maxtrading Review/.env` 的借用
- `tools/daily.sh` 的 curl 告警同樣只讀知識庫自己的設定
- 沒設定時**明確印出訊息並跳過推播**，報告仍寫入 `wiki/health.md`，不會靜默失敗

**同時補上 `.gitignore`**：這個 vault 原本沒有 `.gitignore`，而 github-sync 外掛每 10 分鐘自動 commit＋push。若把含 token 的 `.env` 放進來會直接外洩。已忽略 `.env`、`data/*.log`、`__pycache__` 等，並附 `.env.example` 範本。

待使用者提供「obsidian notify helper」的 chat_id 或 token 後即可接上。

## [2026-08-31] update | 健檢通知改接 @Obsidiannote_helperbot

知識庫的通知不再走 `MaxInvestmentreview_bot`，改接 **@Obsidiannote_helperbot（Obsidian notify helper）**。
這支正好也是 n8n 進料的 Telegram Trigger，所以「傳連結進來」與「健檢通知出去」在同一個對話，與交易報告完全分離。

**過程中的一個發現**：這支 bot 設有 n8n 的 webhook，而 Telegram 的 webhook 與 `getUpdates` 互斥——所以查不到對話清單。**沒有去呼叫 deleteWebhook**（那會弄壞進料管道），改用「個人對話的 chat_id 等於使用者 Telegram ID、跨 bot 相同」這個特性直接寫入 `413748114`，實測送達。

兩條通知路徑都已驗證：`notify.py`（Python）與 `daily.sh` 的 curl 緊急告警。相關注意事項寫進 CLAUDE.md。

## [2026-08-31] 🔴 發現進料管道停擺一個半月：Gemini API 金鑰失效

使用者連續傳了截圖與多種格式的資料源，GitHub 上完全沒有出現 `📥 Archive:` commit。查 git 歷史發現**最後一次成功存檔是 2026-07-14**，距今一個半月。

n8n Executions 顯示 `Call Gemini API` 節點錯誤：
`Bad request - API key not valid. Please pass a valid API key.`

**兩個獨立問題要分清楚**
1. `maxOutputTokens: 1500` → 5～7 月有進來但斷尾（使用者已修）
2. **Gemini 金鑰失效** → 7/14 之後完全沒進來（待修）

**待辦**：到 aistudio.google.com/apikey 申請新金鑰，更新 n8n 的 `Query Auth account 2` 憑證。

**教訓**：若當初有做「Jina 原文一併存檔」，這一個半月的內容不會全數消失——AI 掛掉最多是「有原文沒摘要」。摘要可以補，原文丟了就沒了。

**健檢盲點**：現行檢查只看「已進來的東西」，偵測不到「該進來卻沒進來」，所以斷了一個半月仍天天顯示 0 項問題。待加「raw/ 超過 N 天沒新檔就提醒」。
