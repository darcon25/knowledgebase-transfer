---
original_id: 4xdkdqfr
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-10-27
image: assets/threads_2026-10-27_4xdkdqfr_01.jpg
original_url: "https://www.threads.com/share/BApHRFIGbC"
image_count: 1
expected_min: 1
captured_by: fetch_media
source_note: "threads_2026-10-27_4xdkdqfr.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-10-27 — threads_2026-10-27_4xdkdqfr

> 原始出處：https://www.threads.com/share/BApHRFIGbC
> 對應筆記：[[threads_2026-10-27_4xdkdqfr]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-10-27_4xdkdqfr_01.jpg]]

## 內容

### 圖 1｜TrendForce 伺服器關鍵零組件供需與交期表

來源：TrendForce, Oct 26, 2026。交期單位 W＝週（weeks）。
「Current Lead Time」＝目前交期，「Balanced Lead Time」＝供需平衡時的正常交期。

| 品項 | 狀態 | 目前交期 | 平衡時交期 |
|---|---|---|---|
| CPU | Tight | 25–30W | 16–20W |
| GPU | Balanced | 30-40W | 30-40W |
| DRAM | Very Tight | 20W | 8W |
| NAND (eSSD) | Tight | 16W | 8W |
| HDD | Very Tight | 50W | 16W |
| ABF | Very Tight | 48–56W | 12W |
| MLCC | Tight | 35W | 12W |

**圖例**

| 狀態 | 意思 |
|---|---|
| Very Tight | severe shortage（嚴重短缺） |
| Tight | constrained supply（供給受限） |
| Tightening | conditions worsening（惡化中） |
| Balanced | supply-demand balance（供需平衡） |
| Easing | conditions improving（改善中） |

圖例列了 Tightening 與 Easing，但表中**沒有任何品項**落在這兩類。

**目前交期是平衡交期的幾倍**（直接用圖上數字相除，區間取兩端）

| 品項 | 倍數 |
|---|---|
| ABF | 4.0–4.7 倍 |
| HDD | 約 3.1 倍 |
| MLCC | 約 2.9 倍 |
| DRAM | 2.5 倍 |
| NAND (eSSD) | 2.0 倍 |
| CPU | 約 1.25–1.9 倍 |
| GPU | 1.0 倍 |

**與說明文字核對**：貼文說「DRAM、HDD 及 ABF 條街都好缺」，正好是表中三個 Very Tight，一致。

⚠️ 原筆記的 AI 摘要寫了「PC DRAM 合約價上漲 13-18%、NAND 季增 15-20%、Enterprise SSD 位元需求年增 80%」
以及 Dell PowerEdge R770 的規格，**這些都不在這張圖裡，也不是本貼文作者寫的**——
是 Jina 抓到頁面下方「Related threads」其他人（riccinov、gansotaku、mayagpu）的貼文，被 AI 混進摘要。
消化時要把這些數字跟本篇來源分開。

⚠️ GPU 是表中唯一「Balanced」，但它的交期 30–40 週絕對值並不短，只是本來就這麼長；
「Balanced」不等於「交期短」。

## 為什麼這幾張圖重要

- 原筆記只有一句「DRAM、HDD、ABF 都缺」，這張表補上了**七種零組件的實際交期與正常交期**，
  能量化缺的程度：ABF 是最緊的（交期為正常的 4 倍以上），比記憶體還緊。
- 可餵給：[[ABF載板隱性減產]] 與 [[載板]] 環節（[[3037 欣興]]、[[8046 南電]]、[[3189 景碩]]：ABF 交期 48–56 週）、
  [[記憶體]] 環節（[[2408 南亞科]]、[[2344 華邦電]]、[[8299 群聯]]：DRAM Very Tight、eSSD Tight）、
  [[MLCC缺貨漲價]]（MLCC 35 週 vs 正常 12 週）、[[CPU市佔與ARM競爭]]（CPU Tight）。
- 與 [[shot_2026-10-25_qht2qrjb]]（AWS 說記憶體、電力短缺過 2027 年仍不會結束）互相印證：需求端與供給端說法一致。
- 與 [[shot_2026-10-24_8vlx7dxe]]（臻鼎 ABF 長期毛利目標 50–60%）可放在一起看 ABF 的供需。
