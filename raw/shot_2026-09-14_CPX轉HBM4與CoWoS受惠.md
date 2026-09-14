---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/threads_2026-09-01_CPX轉HBM4與CoWoS受惠_01.jpg
original_url: "https://www.threads.com/share/_jBHsTqf6"
image_count: 1
captured_by: fetch_media
source_note: "threads_2026-09-01_CPX轉HBM4與CoWoS受惠.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — threads_2026-09-01_CPX轉HBM4與CoWoS受惠

> 原始出處：https://www.threads.com/share/_jBHsTqf6
> 對應筆記：[[threads_2026-09-01_CPX轉HBM4與CoWoS受惠]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-01_CPX轉HBM4與CoWoS受惠_01.jpg]]

## 內容

**郭明錤（Ming-Chi Kuo, @mingchikuo）推文截圖：Nvidia 重啟 Rubin CPX**

> 正當市場認為 Rubin CPX 已被 Nvidia 從產品藍圖中移除之際，我最新的產業調查顯示，
> **Nvidia 已重啟 Rubin CPX，預計於 1Q27 開始生產**。相較舊版，重啟後的 Rubin CPX 擁有更強的
> 預填充（prefill）效能，GPU 規格與機櫃架構也都有明顯改變，足以證明 Nvidia 對 prefill 方案的高度重視。

### 1. Rubin CPX GPU 規格
- CPX 算力接近 Rubin，單顆 GPU 最高功耗也同為 **2,300 W**
- **CPX 記憶體改為 168 GB HBM4**，低於 Rubin 的 288 GB HBM4，但**高於舊版 CPX 的 128 GB GDDR7**

### 2. 機櫃設計
- 新版 CPX 採用**獨立的 MGX ETL 機櫃**，不再像舊版與 Rubin 共櫃
- 客戶可依需求配置 **64、128、192 或 256 顆 CPX**
- 每 64 顆 CPX 組成一個機櫃模組，每個機櫃模組配置 **8 個運算托盤**（每托盤 8 顆 CPX）與 **1 個交換機托盤**

### 3. Scale-up 與 scale-out
- NVLink 僅用於同一托盤內 8 顆 CPX GPU 的 scale-up，每顆 CPX 的 **NVLink 頻寬為 1–1.5 TB/s**（vs. 每顆 Rubin 的 3.6 TB/s）
- 同一機櫃模組內的托盤間，透過 **Spectrum-6 Ethernet（全銅 L1）** 進行 scale-out
- 跨機櫃模組時，由各模組的 Spectrum-6 透過 **OSFP 光纖** scale-out

### 4. 運作方式
- CPX 需與 **Vera Rubin NVL72** 搭配，Nvidia 建議 **CPX 與 Rubin 的比例為 1:1**
- CPX 負責預填充（prefill）並建立 KV cache，再透過 **Ethernet RDMA** 傳給 Rubin 執行解碼生成（decode）

### 5. 產品定位：長上下文 prefill 的最高性價比方案
- 目前 AI 推論工作量中，**超過一半來自處理輸入內容（context）並建立對應的 KV cache**
- CPX 以更彈性的部署方式與更低成本承接 prefill
- 每個運算托盤（8 顆 CPX）約有 **1.34 TB HBM4**，足以支援大多數長上下文 prefill 與 KV cache 建立需求

互動數：3 則回覆／21 轉推／135 讚／30K 瀏覽。

---

**為什麼重要**：這是一手產業調查，資訊密度很高，原純文字摘要抓不到規格細節。
投資含意有三層：
1. **CPX 記憶體從 GDDR7 改為 HBM4** → HBM 需求再往上（呼應 [[AGI硬體需求與載板記憶體]] 的 ~16×）
2. **CPX:Rubin = 1:1 且獨立機櫃** → 機櫃數量、PCB／CCL、電源、散熱用量同步倍增
3. **托盤間走 Spectrum-6 全銅 L1、跨模組走 OSFP 光纖** → 銅纜與光模組兩邊都吃得到，
   可連 [[CPO共封裝光學供應鏈]]

⚠️ 同一張截圖也出現在 [[NvidiaCPX對AI鏈影響]]（不同貼文、相同來源圖），兩篇可合併理解。
