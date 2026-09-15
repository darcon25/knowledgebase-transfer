---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-15
image: assets/threads_2026-09-15_gmnbxuie_01.jpg
original_url: "https://www.threads.com/share/BCKUwYT3Cb"
image_count: 6
expected_min: 6
captured_by: fetch_media
source_note: "threads_2026-09-15_gmnbxuie.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-15 — threads_2026-09-15_gmnbxuie

> 原始出處：https://www.threads.com/share/BCKUwYT3Cb
> 對應筆記：[[threads_2026-09-15_gmnbxuie]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-15_gmnbxuie_01.jpg]]

![[threads_2026-09-15_gmnbxuie_02.jpg]]

![[threads_2026-09-15_gmnbxuie_03.jpg]]

![[threads_2026-09-15_gmnbxuie_04.jpg]]

![[threads_2026-09-15_gmnbxuie_05.jpg]]

![[threads_2026-09-15_gmnbxuie_06.jpg]]

## 內容

**TrendForce：2H26 NOR Flash 價格走勢分化，高容量產品漲幅上看 90%~110%**
（TechNews 2026/09/14 報導，6 張圖）

### 核心數據
- **上半年 NOR Flash 合約價平均累積漲幅達 100%～120%**
- **下半年 256Mb 以上高容量產品仍有 90%～110% 上漲空間**
- 128Mb 以下中低容量：中系供應商產能逐步釋出，**2026 第四季漲幅落在 10%～20%**

### 2H26 各類 NOR Flash 供需與價格趨勢
| 產品類別 | 2H26 供給狀況 | 核心需求驅動力 | 2H26 價格趨勢 |
|---|---|---|---|
| **高容量（≥256Mb）** | **嚴重供不應求** | AI Server、ADAS、Edge-AI | **持續上漲，漲幅 90–110%** |
| **Octal/xSPI 高階規格** | 供應偏緊 | AI 晶片、高速數據傳播 | 持續上漲 |
| **車規／航太高可靠度** | 供給緊張 | 車用智慧化、低軌衛星 | 持續上漲 |
| 通用型／中低容量（≤128Mb） | 供需相對平衡 | 消費電子、小家電、TWS | 高檔震盪／盤整 |

### AI 伺服器為什麼吃這麼多 NOR Flash
- **單台 AI 伺服器對 NOR 的需求量為傳統伺服器的 3～5 倍**
- **AI 伺服器內部配備大量 Retimer 晶片，每顆 Retimer 均需要獨立 NOR Flash 載入微碼**
  → 推升高容量及 **Octal SPI NOR** 需求
- 邊緣 AI、AI PC 與機器人等本地推論設備帶動**模型韌體規模數倍增長**

### 另一條需求線：低軌衛星與航太
衛星本體核心晶片組需要可靠度高的 NOR Flash 執行快速開機與韌體備份；
地面接收天線亦內建 NOR 以維持即時運算與 OTA 韌體更新。
**航太用 NOR 要求抗輻射與耐極端溫差，為台系、美系廠商建立技術壁壘。**

---

**為什麼重要**：[[記憶體]] 環節先前只有 DRAM／NAND 的資料，**NOR Flash 這條線是空白的**。

**關鍵機制是 Retimer**：AI 伺服器內每顆 Retimer 都要一顆獨立 NOR 載入微碼 ——
這是**結構性的用量倍增**，不是單純的漲價。與 [[HBM4與先進封裝]] 記的
「AGI 階段記憶體需求 ~16×」屬於同一個現象的不同層面。

⚠️ **這篇沒有點名任何台廠**。NOR Flash 的台系供應商（旺宏 2337、華邦電 2344）中，
**只有 [[2344 華邦電]] 在觀察名單內**，且它主要被記錄為 DRAM 廠。
旺宏目前不在名單上——若要追 NOR 這條線，這是明顯的覆蓋缺口。

⚠️ 低軌衛星那段與 [[6213 聯茂]] 的「低軌衛星地面接收設備 2027 上半年開始貢獻、從泰國廠出貨」
指向同一個終端市場，但**兩者是不同零件**（NOR 是晶片、聯茂做的是 CCL 板材），不要混為一談。
