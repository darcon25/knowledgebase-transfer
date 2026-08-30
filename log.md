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
