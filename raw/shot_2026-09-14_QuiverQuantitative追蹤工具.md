---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/threads_2026-09-13_QuiverQuantitative追蹤工具_01.jpg
original_url: "https://www.threads.com/share/BAUbJ8a-ga"
image_count: 3
captured_by: fetch_media
source_note: "threads_2026-09-13_QuiverQuantitative追蹤工具.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — threads_2026-09-13_QuiverQuantitative追蹤工具

> 原始出處：https://www.threads.com/share/BAUbJ8a-ga
> 對應筆記：[[threads_2026-09-13_QuiverQuantitative追蹤工具]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-13_QuiverQuantitative追蹤工具_01.jpg]]

![[threads_2026-09-13_QuiverQuantitative追蹤工具_02.jpg]]

![[threads_2026-09-13_QuiverQuantitative追蹤工具_03.jpg]]

## 內容

**Quiver Quantitative 追蹤工具介面截圖**，3 張（其中圖 2 與圖 3 內容完全相同，為同一畫面的重複張）。
非投資標的內容，屬**工具／資料源**類。

### 圖 1｜Congress Trading — 個別政治人物頁（範例：J. D. Vance）
頁面分頁：Trades／Live Stock Portfolio／Net Worth／Revolving Door／Supporters／Opponents／Corporate Donors／Proposed Legislation。
- 左欄基本資料：Republican / Ohio；Trade Volume **$3.25M**；Total Trades 3；Last Traded Oct 3, 2023；Current Member: No；Years Active 2023–2025
- Net Worth 區：淨值估計曲線（2022→2023 約 6M–9M 區間）＋ Top Holdings 圓餅
  - Mutual Funds $5.00M／Bank Deposit $873K／Business Entity $750K／Real Estate $750K／Mutual Funds $216K
- Disclosed Holdings 表欄位：Ticker／Asset Type／Asset Name／Amount／Owner／Report Year／Filed
  - QQQ（Invesco QQQ Trust Series 1）$1,000,001–$5,000,000，Joint，2023，Filed Aug 13, 2024
  - DIA（SPDR Dow Jones Industrial Average ETF）$500,001–$1,000,000，Joint，2023
  - Narya Capital Fund I（Business Entity, Limited Partnership）$500,001–…，Self，2023

### 圖 2／圖 3｜Donald Trump Stock Trade Tracker
左欄：President of the United States／Republican／Years Active 2017–2021, 2025–Present／Age 80。
「Track Trump's Stock Trades」區塊示範用 **Quiver API** 取資料（JSON 範例含 Ticker／Company／Transaction／Amount／Filed／Traded／ExcessReturn 欄位）。

Recent Trades 表（欄位：Stock／Transaction／Filed／Traded／估計超額報酬）：
| Stock | 交易 | 金額 | Filed | Traded | 超額報酬 |
|---|---|---|---|---|---|
| TEAM Atlassian | Purchase | $1,001–$15,000 | Aug 22, 2026 | Jun 23, 2026 | **114.07%** |
| ELF e.l.f. Beauty | Purchase | $1,001–$15,000 | Aug 22, 2026 | Jun 3, 2026 | 83.99% |
| LFST LifeStance Health | Purchase | $15,001–$50,000 | Aug 22, 2026 | Jun 4, 2026 | 69.81% |
| INSP Inspire Medical | Sale | $15,001–$50,000 | Aug 22, 2026 | Jun 4, 2026 | 68.42% |
| CRM Salesforce | Purchase | $50,001–$100,000 | Aug 22, 2026 | Jun 18, 2026 | 61.49% |
| VEEV Veeva Systems | Sale | $50,001–$100,000 | Aug 22, 2026 | Jun 12, 2026 | 61.43% |
| VLO Valero Energy | Sale | $1,001–$15,000 | Aug 22, 2026 | Jun 16, 2026 | 60.68% |
| VEEV Veeva Sys Class… | Sale | $1,001–$15,000 | Aug 22, 2026 | Jun 23, 2026 | 60.15% |

> 「Estimated excess return of the underlying stock since the transaction」是網站自算的超額報酬，
> 注意 **Filed 與 Traded 相差約兩個月**——申報有延遲，不是即時訊號。

---

**這篇的性質**：工具介紹，不是個股分析。歸類到非投資線的 [[topics]]／工具頁，
或 [[entities/資料源與限制]] 作為「美國國會與政治人物持股申報」的資料源登記。
可用性重點：有免費網頁介面與 Quiver API；限制是**申報延遲**與金額只給區間不給精確值。

⚠️ 圖 2 與圖 3 為完全相同的畫面（貼文輪播重複張），非漏抓。
