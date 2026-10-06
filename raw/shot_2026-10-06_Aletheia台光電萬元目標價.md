---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-10-06
image: assets/instagram_2026-10-05_8c03mxaq_01.jpg
original_url: "https://www.instagram.com/p/DeGdjOmjNbR/?stkn=Z2Q5eHJobGV6MzE1"
image_count: 1
expected_min: 1
captured_by: fetch_media
source_note: "instagram_2026-10-05_8c03mxaq.md"
status: 已讀圖
original_id: 8c03mxaq
---

# 📸 原貼文圖片 2026-10-06 — instagram_2026-10-05_8c03mxaq

> 原始出處：https://www.instagram.com/p/DeGdjOmjNbR/?stkn=Z2Q5eHJobGV6MzE1
> 對應筆記：[[instagram_2026-10-05_8c03mxaq]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[instagram_2026-10-05_8c03mxaq_01.jpg]]

## 內容

### 圖 1｜封面：外資給予台光電萬元目標價

這是**單張封面圖**，沒有數字表格。

| 欄位 | 圖上內容 |
|---|---|
| 來源標示 | 口袋證券 |
| 分類標籤 | 台股 |
| 標題 | 外資給予台光電萬元目標價／聚焦TPU擴張與材料升級 |
| 副標 | 從每櫃CCL價值提升到產能擴充，解析Aletheia對未來成長的預期 |
| 畫面 | 電路板特寫照片（說明文字註明「圖片來源：台光電」），無文字標註 |

**能推得的**：主角是 [[2383 台光電]]、出處是 Aletheia、目標價量級為「萬元」。
**不能推得的**：所有具體數字都不在圖上。

所有數字（TPU 顆數、每櫃 PCB/CCL 價值、板層數、產能、EPS、毛利率）**只在貼文說明文字**，
原筆記 [[instagram_2026-10-05_8c03mxaq]] 的「原文」段已完整保存，不需靠圖。

以說明文字自身數字交叉驗算（非圖上內容，僅檢查內部一致性）：

| 檢查項 | 說明文字 | 驗算 | 結果 |
|---|---|---|---|
| 目標價 | 10,000 元＝2027–28 平均 EPS × 30 | (262.85 + 403.76) ÷ 2 × 30 ≈ 9,999 | 一致 |
| 產能倍數 | 2028 約為 2025 的 1.9 倍 | 1,110 ÷ 585 ≈ 1.90 | 一致 |

## 為什麼這幾張圖重要

圖本身沒有新資訊，價值在說明文字。消化時應以原筆記為準，餵給：

- [[2383 台光電]]：外資目標價、EPS／毛利率預估、產能規畫（注意是 Aletheia 觀點，非公司財測）
- [[AI-ASIC與GoogleTPU供應鏈]]：TPU 2026→2028 顆數、v7→v8 每櫃價值與層數
- [[CCL]]、[[交換器與網通互聯]]：800G／1.6T 交換器層數與 M8／M9 材料
- [[長期合約LTA與AI營收佔比]]、[[PTFE與材料世代轉換]]、[[CPO共同封裝光學]]：報告列出的三項變數
- 同一份 Aletheia 報告的供應鏈圖卡：[[shot_2026-10-06_lsspfuqy]]
