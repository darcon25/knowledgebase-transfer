# Knowledge Base Schema

這份文件定義了這個知識庫的結構與操作規則。每次對話開始時，LLM 應先讀取此文件。

## 目錄結構

```
Max KnowledgeBase/
├── CLAUDE.md          ← 本文件：操作規則與結構定義
├── Clippings/         ← 網頁剪存（Obsidian Web Clipper）
├── index.md           ← 所有 wiki 頁面的目錄
├── log.md             ← 操作紀錄（只增不減）
├── raw/               ← 原始資料來源（Threads/IG/YouTube/截圖）
│   └── assets/        ← 本地圖片檔案
├── data/              ← 程式抓回來的數據（不要手動編輯）
│   ├── ingested.json  ← 已消化的來源檔清單
│   ├── revenue/       ← 月營收（含回補的 12 個月歷史）
│   ├── margin/        ← 季度毛利率與利潤率
│   ├── known_issues.json ← 已確認處理／決定不處理的問題，健檢會略過
│   ├── valuation/     ← 本益比、股價淨值比、殖利率
│   └── news/          ← 個股新聞標題
├── tools/             ← 自動化程式（見下方「工具」段）
└── wiki/              ← LLM 生成與維護的知識頁面
    ├── overview.md    ← 入口頁，連到所有主要頁面
    ├── health.md      ← 每日健檢報告（程式自動覆寫）
    ├── investing/     ← 投資分析（深度）
    │   ├── companies/ ← 一家公司一頁
    │   ├── segments/  ← 產業鏈環節
    │   ├── themes/    ← 驅動因素（跨公司的樞紐節點）
    │   ├── chains/    ← 產業鏈總圖
    │   ├── monthly/   ← 每月營收彙整
    │   └── insights/  ← 分析結論存檔（帶日期，可回頭驗證）
    ├── topics/        ← 非投資主題（只分類，不深入）
    ├── entities/      ← 人物、組織等實體頁面
    ├── concepts/      ← 觀念、方法論
    └── sources/       ← 來源摘要頁面
```

## 工具

| 指令 | 做什麼 |
|---|---|
| `python3 tools/capture.py --youtube <網址>` | 抓 YouTube 逐字稿進 raw/ |
| `python3 tools/capture.py --shot <圖片…> --note "說明" [--source 網址]` | 截圖進 raw/，**可一次多張**（IG 輪播、X、限動、付費內容走這條） |
| `python3 tools/fetch_market.py` | 抓月營收、估值、毛利率、新聞（每天 18:30 自動跑） |
| `python3 tools/backfill_revenue.py --months 12` | 從 MOPS 回補歷史月營收（一次性，已補 12 個月） |
| `python3 tools/build_pages.py` | 用資料更新公司頁與環節頁 |
| `python3 tools/health_check.py` | 資料健檢，寫 health.md 並推 Telegram |
| `tools/daily.sh` | 以上三件一次做完（launchd 每天 18:30 呼叫） |
| `python3 tools/boot_check.py` | 開機時自動跑：等網路 → git pull → 健檢 → 有待處理才推 Telegram |

### ⚠️ 排程的地雷（踩過一次）

**launchd 的 PATH 很乾淨，`python3` 會指到 Apple 內建版本，那個版本沒有 `requests`。**
2026-08-28～30 的每日排程因此連續失敗三天，而且「回報失敗」的健檢本身也是用 Python 寫的，所以連錯誤都送不出來。

修法（已套用）：
1. `daily.sh` 逐一測試候選路徑，挑出**真的能 `import requests`** 的那個 python
2. 失敗時用 **curl** 直接送 Telegram 告警——這條路不依賴任何 Python 套件，不會跟主程式一起死
3. launchd plist 一律寫**絕對路徑**，不要依賴 PATH

**重要**：`build_pages.py` 只會覆寫 `<!-- AUTO:START -->` 到 `<!-- AUTO:END -->` 之間的內容。
手寫的論點、觀察指標、事件時間軸**永遠不會被蓋掉**。

## 核心原則

- `raw/` 資料夾的內容**永遠不可修改**，只能讀取
- `wiki/` 資料夾由 LLM 全權負責建立與維護
- 每次操作後必須更新 `index.md` 與 `log.md`
- Wiki 頁面之間應積極建立 `[[內部連結]]`

## 操作流程

### 一、消化新資料（Ingest）

新資料來自 `raw/` 或 `Clippings/`。**第一步永遠是判斷它是不是投資相關**，兩條路的深度不同。

1. **閱讀**資料
2. **分流判斷**：內容有沒有提到 `tools/watchlist.py` 名單上的公司、或 PCB/CCL/半導體/總經？

**A. 投資相關 → 深度處理**

3. 抽出提到的公司代號
4. 更新對應的 `wiki/investing/companies/<代號 名稱>.md`：
   - 把事件寫進「事件時間軸」（**寫在 AUTO 區塊外面**）
   - 若影響原本判斷，更新「我的論點」與「還缺什麼」
5. 若牽動兩家以上 → 更新 `wiki/investing/segments/` 或 `chains/AI伺服器PCB鏈.md` 的傳導路徑
6. 若出現新的跨公司驅動因素（漲價循環、技術轉換、缺料）→ 在 `wiki/investing/themes/` 建頁，並從相關公司頁連過去
7. **若同鏈公司說法互相矛盾 → 在鏈頁的「⚠️ 目前的矛盾訊號」明確標記**。這是最有價值的訊號，不要略過

**B. 非投資 → 只分類**

3. 歸進 `wiki/topics/` 對應主題頁的表格（一句話說明 + 原始檔路徑）
4. 沒有對應主題就開一頁新的。**不要寫深度摘要**

**兩條路都要做的收尾**

8. 把檔案路徑加進 `data/ingested.json` 的 `files`（否則每次開新對話都會被當成未消化）
9. 更新 `index.md` 與 `log.md`
10. 若對整體理解有重大影響 → 更新 `wiki/overview.md`

### 二、回答問題（Query）

1. 讀取 `index.md` 找出相關頁面
2. 讀取相關頁面並整合答案
3. 附上出處（引用 wiki 頁面連結）
4. 若答案有獨立價值，可將其儲存為新的 wiki 頁面
5. 在 `log.md` 追加紀錄

### 三、健康檢查

分兩層，不要搞混：

**機械層**（每天 18:30 自動跑，零成本）
`tools/health_check.py` 查重複存檔、未消化、內容截斷、斷連結、孤島頁、數字不符、資料過期。
結果寫 `wiki/health.md` 並推 Telegram。使用者問「知識庫有什麼問題」時，先讀這頁。

**判讀層**（使用者要求時才跑，有 token 成本）
呼叫 `kb-auditor` agent（定義在 `.claude/agents/kb-auditor.md`）。
它查需要理解才能判斷的：訊號矛盾、摘要失真、論點過期、連錯對象、覆蓋缺口。
**它沒有寫入權限**——只提報告，改不改由使用者決定。

## 頁面格式規範

### Wiki 頁面（entities / concepts）

```markdown
---
tags: [entity|concept]
sources: [來源頁面連結數量]
updated: YYYY-MM-DD
---

# 頁面標題

一段核心摘要（2-4 句）。

## 重點

- 重點一
- 重點二

## 相關連結

- [[相關頁面 A]]
- [[相關頁面 B]]

## 來源

- [[sources/來源名稱]]
```

### 來源摘要頁面（sources/）

```markdown
---
tags: [source]
type: article|paper|book|video|podcast|other
date_ingested: YYYY-MM-DD
---

# 來源標題

**類型**：文章 / 論文 / 書籍 / 影片 / 其他  
**原始位置**：`raw/檔案名稱` 或 URL

## 摘要

（3-6 句核心內容）

## 關鍵要點

- 要點一
- 要點二

## 相關 Wiki 頁面

- [[concepts/概念名稱]]
- [[entities/實體名稱]]
```

## Log 格式

每筆紀錄格式：

```
## [YYYY-MM-DD] 操作類型 | 標題
簡短描述發生了什麼事，影響了哪些頁面。
```

操作類型：`ingest`、`query`、`lint`、`update`

---

**說明**：這份知識庫使用「LLM Wiki」架構，由 LLM 負責維護所有 wiki 內容，使用者負責提供資料來源與提問方向。
