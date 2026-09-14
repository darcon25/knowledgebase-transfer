---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/threads_2026-08-31_GoogleTPU轉COT模式_01.jpg
original_url: "https://www.threads.com/share/BAQIz5N5rC"
image_count: 1
captured_by: fetch_media
source_note: "threads_2026-08-31_GoogleTPU轉COT模式.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — threads_2026-08-31_GoogleTPU轉COT模式

> 原始出處：https://www.threads.com/share/BAQIz5N5rC
> 對應筆記：[[threads_2026-08-31_GoogleTPU轉COT模式]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-08-31_GoogleTPU轉COT模式_01.jpg]]

## 內容

**工商時報製表（張珈睿）：谷歌 TPU ASIC 競逐版圖**，資料來源：採訪整理。

| 業者 | 關係／定位 | 核心優勢 |
|---|---|---|
| **博通（Broadcom）** | TPU 既有主要 ASIC 合作夥伴 | 完整 ASIC 統包、高速 SerDes、網通 IP 及量產經驗 |
| **聯發科** | 列 TPU 第八代、第九代合作夥伴 | 前端設計、自有 IP、I/O 整合及大型晶片量產能力 |
| **超微（AMD）** | 市場傳可能參與新一代 TPU／Chiplet 生態系 | CPU、GPU、Chiplet、先進封裝及高速互連技術 |
| **邁威爾（Marvell）** | 已與谷歌達成客製化晶片協議；市場關注 **Tiberius 專案** | 高速 SerDes、客製晶片、網路互連、NPO 及先進封裝能力 |
| **世芯-KY** | **潛在 TPU 挑戰者** | 台積電最先進製程、實體設計、2.5D、Chiplet、CoWoS 量產經驗 |

---

**為什麼重要**：這張表把 Google TPU 的供應商競爭格局一次講清楚，原純文字摘要沒有。

**與其他篇的交叉點**
- [[高階CCL三雄成長階段比較]] 圖 5 有 Marvell 向 SEC 揭露的原文：2026-07-29 與 Google 的協議
  涵蓋 AI 推論加速器、儲存控制器、網路介面控制器、記憶體介面控制器與近記憶體運算——
  正好佐證這張表裡「已與谷歌達成客製化晶片協議」那一列
- [[GoogleTPU受惠族群檢驗]]（萬寶）說「世芯有贏，但這次不是靠 TPU」，
  且 **TPU v10 仍由聯發科整合**、TPU 營收占聯發科比重 2028 年達 65%

**三篇合起來的結論**：博通仍是主力、聯發科吃 v8/v9（並可能延續到 v10）、
Marvell 切入周邊系統晶片、世芯目前仍是「潛在挑戰者」而非既有供應商。
可餵給 [[2454 聯發科]]、[[3661 世芯-KY]] 兩頁，並在 [[themes]] 的 CSP 自研 ASIC 頁建立供應商版圖。
