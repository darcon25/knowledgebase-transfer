---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-21
image: assets/threads_2026-09-21_aormonoj_01.jpg
original_url: "https://www.threads.com/share/_wHgwVlUD"
image_count: 4
expected_min: 4
captured_by: fetch_media
source_note: "threads_2026-09-21_aormonoj.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-21 — threads_2026-09-21_aormonoj

> 原始出處：https://www.threads.com/share/_wHgwVlUD
> 對應筆記：[[threads_2026-09-21_aormonoj]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-21_aormonoj_01.jpg]]

![[threads_2026-09-21_aormonoj_02.jpg]]

![[threads_2026-09-21_aormonoj_03.jpg]]

![[threads_2026-09-21_aormonoj_04.jpg]]

## 內容

共 4 張圖，是「超視角 VUEXON｜產業情報站」把 TrendForce 2026/09/18 研究整理成的懶人包。
圖 1～3 是同一系列的「重點 1／2／3」，圖 4 是獨立的規格比較表。四張圖都在頁尾標註「資料整理：TrendForce 2026/09/18」（圖 4 標 2026/09）。

### 圖 1｜重點 1：為什麼 CoWoS-L 仍是主流？

主標：**TrendForce｜CoWoS-L 至 2028 年仍是 AI 晶片主流封裝**

| # | 小標 | 圖上文字 |
|---|---|---|
| 1 | AI 晶片持續升級，推動 2.5D 封裝往更大面積發展 | TrendForce 指出，隨著 AI 晶片效能提升、晶片尺寸變大、HBM 數量增加，2.5D 先進封裝正往更大封裝面積發展。（配圖三階段：效能提升 → 晶片尺寸變大 → HBM 數量增加） |
| 2 | CoWoS-S 逐漸接近物理極限 | 過去主流是 CoWoS-S，但當運算晶粒與 HBM 數量持續增加，傳統大型矽中介層逐漸接近物理極限。（示意圖：HBM＋運算晶粒＋HBM 坐在「大型矽中介層」上） |
| 3 | CoWoS-L 以局部矽橋設計滿足新一代大型 AI 需求 | CoWoS-L 透過局部矽橋設計，在更大封裝面積下仍可維持高速互連，更適合新一代大型 AI 加速器。（示意圖標「局部矽橋設計」） |
| 4 | 至少到 2028 年仍是主流 | TrendForce 預估，至少到 2028 年，CoWoS-L 仍會是 AI 晶片主流封裝方案。 |

**小比較（圖右下角）**

| 方案 | 圖上說明 |
|---|---|
| CoWoS-S | 適合較早期配置 |
| CoWoS-L | 支援更大晶片、更複雜封裝 |

頁尾標語：「AI 晶片越做越大，封裝也跟著升級！」

### 圖 2｜重點 2：誰在推動 CoWoS-L 需求？

| # | 小標 | 圖上文字與數字 |
|---|---|---|
| 1 | AI GPU 率先採用 | NVIDIA 與 AMD 新一代 AI 加速器已開始採用 CoWoS-L。 |
| 2 | GPU 出貨成長 | TrendForce 預估 **NVIDIA 2026 年高階 GPU 出貨量年增約 30%**；AMD 自 **2026 年下半年**推動 **MI400、MI450**，也將拉動先進封裝需求。（長條圖標 2025 → 2026，箭頭標 +30%） |
| 3 | 自研 ASIC 成為新動能 | **Google TPU v7、AWS Trainium v3** 是主要需求來源；**Meta 的 MTIA 400** 已採用 CoWoS-L。 |
| 4 | 需求逐步擴散 | **AWS 與 Microsoft 預期在 2027 年開始導入 CoWoS-L**，需求將從 GPU 擴散到大型雲端業者自研 AI 晶片。 |

頁尾標語：「不只 GPU，雲端業者自研 ASIC 也開始帶動封裝升級！」

### 圖 3｜重點 3：競爭格局與後續觀察

| # | 小標 | 圖上文字 |
|---|---|---|
| 1 | 主要競爭者 | **Intel EMIB-T 是 CoWoS-L 的主要競爭方案**；優點是不需要大型完整矽中介層，有機會降低封裝成本。（左右對照圖：CoWoS-L「需要大型完整矽中介層」／Intel EMIB-T「不需要大型矽中介層，有機會降低封裝成本」） |
| 2 | 誰可能採用 EMIB-T | TrendForce 預期 **Google 可能在 2027 年採用 EMIB-T**，**AWS 也正在測試 EMIB 技術**。 |
| 3 | CoWoS-L 為何仍能守住主流 | 關鍵在**技術成熟度**（生態系完整、技術更穩定）、**量產經驗**（已有大量量產實績）與**良率控制**（製程良率持續優化），因此至少到 2028 年仍具優勢。 |
| 4 | 後續觀察（三項） | ① 追蹤 CoWoS-L 占比提高速度　② 單顆晶片使用 HBM 數量　③ Google／AWS／Microsoft 自研 ASIC 量產進度 |

**產業影響，受惠鏈（圖右下角燈泡框，逐字照抄）**：HBM、先進封裝、矽橋／中介層、基板、封裝設備。

頁尾標語：「AI 晶片不只比算力，也比封裝能力！」

### 圖 4｜TSMC CoWoS vs Intel EMIB 技術比較（本組最有價值的一張）

標題：**TSMC CoWoS vs Intel EMIB 技術比較**｜封裝技術比較｜TrendForce 2026/09

| 廠商 | 封裝技術與規格 | 2024 | 2025 | 2026 | 2027 | 2028 |
|---|---|:--:|:--:|:--:|:--:|:--:|
| TSMC | CoWoS 方案 | CoWoS-S | CoWoS-S | CoWoS-L | CoWoS-L | CoWoS-L |
| TSMC | 光罩曝光倍數 | 3.3X | 5.5X | 5.5X | 9.5X | 14X |
| TSMC | SoC/Chiplet 數量 | 2 | 4 | 4 | 8 | 20 |
| TSMC | HBM 模組數量 | 8 | 12 | 12 | 12 | 20 |
| Intel | EMIB 方案 | EMIB | EMIB | EMIB-T | EMIB-T | EMIB-T |
| Intel | 光罩曝光倍數 | 4X | 4X | >8X | >8X | >12X |
| Intel | HBM 模組數量 | - | - | 12 | 12 | >24 |

> 原圖用合併儲存格：TSMC 的 CoWoS-S 橫跨 2024–2025、CoWoS-L 橫跨 2026–2028；光罩 5.5X 與 Chiplet 4、HBM 12 橫跨 2025–2026；Intel 的 EMIB 橫跨 2024–2025、EMIB-T 橫跨 2026–2028，4X 橫跨 2024–2025、>8X 橫跨 2026–2027，HBM「-」橫跨 2024–2025、12 橫跨 2026–2027。上表已把合併格展開成逐年，**數值本身一字未改**。

**觀察重點（圖下方三格）**

1. 台積電 CoWoS-S 正往 CoWoS-L 升級
2. Intel EMIB 正朝 EMIB-T 演進
3. AI 晶片競爭也在比封裝延展能力

### ⚠️ 需要標記的地方

- ⚠️ **原筆記的摘要混進了「相關貼文」的內容，不是這四張圖講的事。** n8n 產的摘要提到「探針卡、測試設備」「PCB 高階鑽針」「尖點高階鍍膜鑽針占比 56%、毛利率 36.59% → 41.77%」。**這四張圖裡完全沒有這些字**——它們來自 Jina Reader 抓到的 Threads「Related threads」區塊（@pocketsecurities 與 @ricch.jjourneey 的另外兩則貼文）。引用時千萬不要把尖點的毛利率數字掛在 TrendForce 頭上。
- ⚠️ **圖 4 的規格對比，結論與圖 1／圖 3 的文字方向相反。** 圖 3 說 CoWoS-L 能守住主流；但圖 4 的表格顯示 **2028 年 Intel EMIB-T 的 HBM 模組數量 >24，反而高於 TSMC CoWoS-L 的 20**。也就是說「純規格上 Intel 更激進，CoWoS-L 的優勢來自良率／量產經驗而非規格上限」——圖 3 第 3 點其實已經承認了這點，但圖 1、圖 2 的標語（「至 2028 年仍是主流」）容易讓人誤讀成規格領先。**這是這組圖最該記住的一句話。**
- ⚠️ **光罩曝光倍數的口徑不同，不能直接相減比較。** TSMC 欄是確定值（3.3X／5.5X／9.5X／14X），Intel 欄全是下限值（4X／>8X／>12X）。2024 年 Intel 的 4X 高於 TSMC 的 3.3X，但那是 EMIB 與 CoWoS-S 兩種不同架構，**這個「Intel 贏」沒有意義**。
- ⚠️ **HBM 模組數量在 2025→2027 三年連續停在 12，然後 2028 一次跳到 20**，而同期 SoC/Chiplet 從 4 → 8 → 20。圖上沒有解釋為什麼 HBM 卡住三年，也沒有標註這是「單一封裝上限」還是「主流配置」。**這個欄位的定義不明，引用時要註明。**
- ⚠️ **圖 2 的「NVIDIA 2026 年高階 GPU 出貨量年增約 30%」沒有絕對數字**，長條圖只有 2025／2026 兩根柱子、無刻度。只能當成成長率引用，**不能反推出貨量**。
- ⚠️ **圖 2 與圖 3 對 Google 的說法看似打架**：圖 2 說 Google TPU v7 是 CoWoS-L「主要需求來源」，圖 3 說 TrendForce 預期 Google 可能在 2027 年採用 Intel EMIB-T。兩者不必然矛盾（可能是不同世代／雙供應商），但**圖上沒有說明兩者關係**，追蹤 Google TPU 供應鏈時要把這組並列的訊號記下來。
- ⚠️ 圖 2 寫「Meta 的 MTIA 400 已採用 CoWoS-L」——用的是**完成式「已」**，與 Google／AWS 的「是主要需求來源」時態不同，圖上未說明 MTIA 400 是否已量產。

### 為什麼這幾張圖重要

這組圖把「先進封裝」這一環從模糊的概念變成**有年份、有數字的路線圖**，而且是第一手研究機構（TrendForce）的口徑。知識庫裡原本的先進封裝討論沒有這種逐年規格表。

**可以餵給的驅動因素頁（themes）**

- [[HBM4與先進封裝]]——**這是最直接的收件人**。圖 4 的 HBM 模組數量逐年表（8 → 12 → 12 → 12 → 20）與 SoC/Chiplet 數量（2 → 4 → 4 → 8 → 20）可以整張搬過去，補上目前這頁缺的量化骨架。
- [[AI-ASIC與GoogleTPU供應鏈]]——圖 2 的「Google TPU v7／AWS Trainium v3／Meta MTIA 400」與圖 3 的「Google 2027 可能改用 EMIB-T」，是這頁該記的兩組並列訊號。
- 建議**新開一頁「CoWoS-L 與 EMIB-T 的封裝路線之爭」**（目前 themes/ 沒有對應頁），把圖 3、圖 4 的競爭格局放進去，並從 [[3711 日月光投控]]、[[2330 台積電]] 連過來，避免變成孤島頁。

**可以餵給的環節頁（segments）**

- [[wiki/investing/segments/封測]]——圖 3 的「受惠鏈」五項（HBM、先進封裝、矽橋／中介層、基板、封裝設備）正好對應數個現有環節頁。
- [[wiki/investing/segments/載板]]——受惠鏈中的「基板」。
- [[wiki/investing/segments/設備]]——受惠鏈中的「封裝設備」。
- [[wiki/investing/segments/記憶體]]——HBM 模組數量的逐年變化直接影響這一環的需求量。

**與其他 shot 檔的關係**

- [[shot_2026-09-21_7kptbv00]]——同一天的台廠 CPU 供應鏈圖，其中 ASEH（$3711）與 PTI（$6239）的 EFB 封裝、三家 ABF 載板廠，正是本組圖「受惠鏈」裡的「先進封裝」與「基板」。兩張圖一個講技術路線、一個講台廠對應，**合起來才是完整的一條鏈**。
- [[shot_2026-09-21_uqfxqh5s]]——講封測廠欣銓的 ASIC CP 測試訂單；本組圖 2、圖 3 說明的正是「雲端自研 ASIC 起量」這個上游動能，兩者是同一個故事的上下游。

**原始貼文**：[[threads_2026-09-21_aormonoj]]（@vuexon0829，2026-09-21）
