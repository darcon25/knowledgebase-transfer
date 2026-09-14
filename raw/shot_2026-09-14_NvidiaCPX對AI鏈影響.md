---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/instagram_2026-09-01_NvidiaCPX對AI鏈影響_01.jpg
original_url: "https://www.instagram.com/p/DctzPOGCQBK/?igsi=MWdnZ3J1dWZoNXhheg=="
image_count: 1
captured_by: fetch_media
source_note: "instagram_2026-09-01_NvidiaCPX對AI鏈影響.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — instagram_2026-09-01_NvidiaCPX對AI鏈影響

> 原始出處：https://www.instagram.com/p/DctzPOGCQBK/?igsi=MWdnZ3J1dWZoNXhheg==
> 對應筆記：[[instagram_2026-09-01_NvidiaCPX對AI鏈影響]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[instagram_2026-09-01_NvidiaCPX對AI鏈影響_01.jpg]]

## 內容

**與 [[CPX轉HBM4與CoWoS受惠]] 為同一張截圖**（郭明錤 Ming-Chi Kuo 推文，Nvidia 重啟 Rubin CPX，
兩則不同貼文引用了同一張圖）。完整內容已整理在該篇，這裡不重複，只留重點索引：

- Nvidia 已重啟 Rubin CPX，**預計 1Q27 開始生產**
- CPX 單顆功耗 2,300 W，記憶體 **168 GB HBM4**（舊版為 128 GB GDDR7，Rubin 為 288 GB HBM4）
- 採**獨立 MGX ETL 機櫃**，可配 64／128／192／256 顆；每 64 顆一模組，8 運算托盤 + 1 交換機托盤
- NVLink 只做托盤內 8 顆 scale-up（每顆 1–1.5 TB/s）；托盤間走 **Spectrum-6 Ethernet 全銅 L1**，跨模組走 **OSFP 光纖**
- **CPX : Rubin 建議 1:1**，CPX 做 prefill 與 KV cache，經 Ethernet RDMA 交給 Rubin decode
- 每托盤（8 顆 CPX）約 **1.34 TB HBM4**

→ 詳細條列與投資含意見 [[shot_2026-09-14_CPX轉HBM4與CoWoS受惠]]。

---

⚠️ **重複來源提醒**：同一則郭明錤推文在 2026-09-01 前後被至少兩個帳號轉貼，
n8n 因此存了兩份筆記。消化時擇一為主即可，另一份留作出處佐證。
