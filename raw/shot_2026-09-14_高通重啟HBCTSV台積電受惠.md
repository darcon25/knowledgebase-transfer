---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/threads_2026-09-01_高通重啟HBCTSV台積電受惠_01.jpg
original_url: "https://www.threads.com/share/_mWQDsilX"
image_count: 1
captured_by: fetch_media
source_note: "threads_2026-09-01_高通重啟HBCTSV台積電受惠.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — threads_2026-09-01_高通重啟HBCTSV台積電受惠

> 原始出處：https://www.threads.com/share/_mWQDsilX
> 對應筆記：[[threads_2026-09-01_高通重啟HBCTSV台積電受惠]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-01_高通重啟HBCTSV台積電受惠_01.jpg]]

## 內容

**自製圖卡：HBM vs HBC 對比總覽**（註：資訊截至 2024 年 5 月）

| | **HBM**（High Bandwidth Memory 高頻寬記憶體） | **HBC**（High Bandwidth Cache 高頻寬快取記憶體） |
|---|---|---|
| **目標** | 提供極高頻寬滿足運算需求 | 降低功耗與延遲、提升整體效能 |
| **結構方式** | **2.5D 封裝**：記憶體堆疊在運算晶片旁邊（HBM DRAM Die 多層堆疊 → TSV → Interposer 中介層 → Package Substrate） | **3D 整合**：記憶體更靠近或垂直整合在運算晶片上（DRAM/Cache Die → TSV／混合鍵合 Hybrid Bonding → Compute Die → Package Substrate） |
| **記憶體類型** | DRAM（如 HBM3E、HBM4） | DRAM 或低功耗記憶體（如 LPDDR 類） |
| **TSV 使用** | 大量使用 TSV 垂直貫穿連接 DRAM Die | 使用 TSV（可能搭配 Hybrid Bonding 混合鍵合） |
| **與運算晶片關係** | 並排放置，透過 Interposer 連接 | 更靠近或垂直整合在運算晶片上 |
| **封裝技術** | 2.5D 封裝（CoWoS、EMIB 等） | 3D 整合（更高階的 3D IC 技術） |
| **資料傳輸路徑** | GPU ↔ Interposer ↔ HBM | CPU/GPU ↔ 垂直互連記憶體（更短路徑） |
| **頻寬** | 極高（TB/s 級） | 目標更高（更短距離，更高頻寬） |
| **功耗** | 已大幅降低 | 目標再降低（更短距離、電壓更低） |
| **成熟度** | **已量產，廣泛應用於 AI / HPC** | **尚在發展中，預計 2027 年後逐步導入** |
| **成本** | 高（HBM 堆疊 + 2.5D 封裝成本高） | 預期更高（3D 整合技術更複雜） |
| **散熱挑戰** | 相對可控（HBM 在晶片旁） | **更高**（記憶體更靠近核心，熱密度更高） |

**HBM 優點**：技術成熟已大規模量產／頻寬高適合大資料量運算／擴充性佳（可堆疊更多層數）
**HBM 挑戰**：功耗仍高／2.5D 封裝成本高／資料路徑較長

**HBC 優點**：更低延遲、更低功耗／頻寬潛力更高／記憶體與運算高度整合
**HBC 挑戰**：技術難度高（TSV + 混合鍵合）／散熱挑戰大／良率與成本控制困難

**主要應用**
- HBM：AI 加速器／GPU、高效能運算（HPC）、資料中心
- HBC：AI SoC／邊緣 AI、行動裝置／穿戴裝置、未來高效能運算

**總結**：HBM 是目前主流高頻寬記憶體方案，已廣泛應用於 AI 與 HPC；
HBC 是下一代更進階的整合方案，目標是更低功耗、更高效能，但技術挑戰更高，仍在發展中。

---

**為什麼重要**：這張表把 **2.5D（HBM）與 3D／Hybrid Bonding（HBC）的差異講得最清楚**，
補上了 [[HBM記憶體牆與熱密度]] 那張「突破記憶體高牆的三大封裝方案」的技術細節
（方案三「記憶體內運算」與 HBC 的 3D 整合是同一條路線）。

**投資含意**：HBC 走 **Hybrid Bonding**，這正是台積電 SoIC 的強項——
原檔名的「台積電受惠」應該是指這一點。**HBC 預計 2027 年後逐步導入**，時程與
[[CPX轉HBM4與CoWoS受惠]]（Rubin CPX 1Q27 生產）、[[載板家族變動與ABF預告]]（T-glass 新產能 2027 年中）
都落在同一個時間窗。

⚠️ **注意這張圖的資料截至 2024 年 5 月，已有兩年以上**，
HBM4 的規格請以 [[HBM記憶體牆與熱密度]] 的 Micron 表為準（該表為 2026 年資料）。
⚠️ 原檔名提到「高通重啟」，但圖中**完全沒有高通（Qualcomm）的內容**，該資訊應在貼文文字裡。
