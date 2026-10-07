---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-10-07
image: assets/threads_2026-10-07_qjckxs8b_01.jpg
original_url: "https://www.threads.com/share/BASmfTaScL"
image_count: 4
expected_min: 4
captured_by: fetch_media
source_note: "threads_2026-10-07_qjckxs8b.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-10-07 — threads_2026-10-07_qjckxs8b

> 原始出處：https://www.threads.com/share/BASmfTaScL
> 對應筆記：[[threads_2026-10-07_qjckxs8b]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-10-07_qjckxs8b_01.jpg]]

![[threads_2026-10-07_qjckxs8b_02.jpg]]

![[threads_2026-10-07_qjckxs8b_03.jpg]]

![[threads_2026-10-07_qjckxs8b_04.jpg]]

## 內容

四張圖是「七小服 Seven Small Services」的一組簡體字知識卡（01–04），主題是**英偉達原廠 400G 光模組**。來源標示為 ServeTheHome 與英偉達規格文件。卡片自註「行業知識分享，不構成投資建議」。**全組沒有任何財報、價格或市場數字**。

### 圖 1｜英偉達原廠的 400G 光模組長什麼樣

- 型號：MMS1X00-NS400（圖源 ServeTheHome）
- 用途：AI 集群裡，伺服器和交換機之間靠它把電訊號變成光
- 外形規格 QSFP112；黃色拉環 = 單模模組的標記

| 規格 | 數值 |
|---|---|
| 速率 | 400Gb/s |
| 最遠距離 | 500 米 |
| 400G 時最大功耗 | 7–9.5 瓦 |

### 圖 2｜QSFP112、DR4 各是什麼意思

| 名詞 | 意思 |
|---|---|
| QSFP112 | 外形規格，插在網卡的口上 |
| DR4 | 4 路光並行，每路 100G |
| 1310nm | 光的波長，走單模光纖 |
| MPO-12 | 光纖接頭，綠色外殼是斜面研磨 |

用在哪：插在 ConnectX-7 網卡或 BlueField-3 上，另一頭對接交換機上的雙口 800G 模組。InfiniBand 和乙太網都支援。

### 圖 3｜八成鏈路故障，是光接口髒了

| 原則 | 說明 |
|---|---|
| 先清潔 | 插光纖之前，模組插口和光纖接頭都要清潔 |
| 不用液體 | 用標準清潔工具，不能上液體 |
| 留防塵帽 | 模組和光纖的防塵帽都留著，運輸時蓋上 |

實測溫度：ServeTheHome 插在 ConnectX-8 網卡上，運行在 40 多度；官方外殼工作溫度上限 70 度。
原話：80% of transceiver link problems are related to dirty optical connectors.

### 圖 4｜鏈路不通，先別急著換模組

1. 先查接口乾不乾淨——英偉達說八成問題出在這裡，先清潔再考慮換
2. 光模組是常備件——插拔件，壞了可單換，關鍵鏈路要備幾隻
3. 換之前核對標籤——型號、接頭、波長要對得上，單模和多模不能混插

結語：「能修的修，該換的換。」（標明判斷是作者的）

⚠️ 圖 2 寫的是插在 ConnectX-7／BlueField-3，圖 3 的實測卻是插在 ConnectX-8 上，兩者不是同一張網卡（不一定矛盾，但要注意實測環境不同）。
⚠️ 原筆記討論串裡的 AI Server 產業鏈八層、汎銓、美光 512GB RDIMM、CoWoS-L 等內容**都不在這四張圖上**，圖只講 400G 光模組。

### 為什麼這幾張圖重要

- 投資數據價值低，屬**技術名詞對照**：DR4／QSFP112／1310nm 單模、400G 對接 800G 的架構，可作為 [[光收發模組與矽光子]] 的入門註解
- 「光模組是插拔耗材、關鍵鏈路要備品」對光模組需求量的推估有參考意義，可連到 [[交換器與網通互聯]]、[[光通訊CPO]]
- 同日矽光子測試相關圖：[[shot_2026-10-07_8shke8da]]
- 原始筆記：[[threads_2026-10-07_qjckxs8b]]
