---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/threads_2026-09-02_AI供應鏈CCL散熱ASIC展望_01.jpg
original_url: "https://www.threads.com/share/_mevdCh1l"
image_count: 1
captured_by: fetch_media
source_note: "threads_2026-09-02_AI供應鏈CCL散熱ASIC展望.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — threads_2026-09-02_AI供應鏈CCL散熱ASIC展望

> 原始出處：https://www.threads.com/share/_mevdCh1l
> 對應筆記：[[threads_2026-09-02_AI供應鏈CCL散熱ASIC展望]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-02_AI供應鏈CCL散熱ASIC展望_01.jpg]]

## 內容

**聯茂（ITEQ）法說會簡報第 10 頁：「完整的產品線規劃」**——CCL 材料等級金字塔。

### 材料等級對照表（損耗等級 × Df 值 × 產品型號）
| 損耗等級 | 材料等級 | **Df 值** | 對應產品型號 |
|---|---|---|---|
| **Extreme Low Loss** | **M9** | **0.0010～0.0005** | IT-999GSE2/3 |
| **Super Ultra Low Loss** | **M8** | 0.0015～0.0010 | IT-998GSE2、IT-998GSE |
| **Ultra Low Loss** | **M7** | 0.005～0.0015 | IT988G/SE、IT988GL/SE、IT968GSE |
| **Very Low Loss** | **M6** | 0.006～0.005 | IT968G |
| **Low Loss** | **M4** | 0.009～0.006 | IT958G、IT170GRA2、IT170GL、IT150DA |
| **Mid Loss** | **M2** | 0.015～0.009 | IT170GRA1、IT170GT |
| **Standard Loss** | **M** | > 0.015 | IT158、IT180A |

**RF Application（射頻應用）另列**：IT-88GMW、IT-8300GA、IT-8350G、IT-8615G

### 簡報自述的兩點
- 隨著高速運算資料中心、AI 伺服器升級等需求，帶動**高頻高速材料需求高度成長**
- **ITEQ 在高頻高速材料市場的市占率將顯著提升**

---

**為什麼這張圖重要**：這是整個知識庫裡**第一張把 M 等級與 Df 數值對應清楚的官方資料**。
先前 [[高階CCL三雄成長階段比較]]、[[載板家族變動與ABF預告]] 等篇一直在講「M6 升 M7」「M8 切入 CSP」，
但沒有定義。有了這張表就能量化：**每升一級，Df 大約砍半**。

可直接放進 [[segments/CCL]] 當作術語對照表，並回頭校正各公司頁對「高階占比」的定義：
- 台光電說的「M7 等級以上」＝ Df ≤ 0.005
- 聯茂說的「M6 以上占比 40%」＝ Df ≤ 0.006
- 聯茂「M8 已切入美系 CSP 自研 ASIC 與 800G 交換器」＝ Df 0.0015～0.0010 那一階
