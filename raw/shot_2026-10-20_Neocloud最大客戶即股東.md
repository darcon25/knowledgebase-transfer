---
original_id: w4cxc3tl
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-10-20
image: assets/threads_2026-10-20_w4cxc3tl_01.jpg
original_url: "https://www.threads.com/share/BASYoPxhVp"
image_count: 1
expected_min: 1
captured_by: fetch_media
source_note: "threads_2026-10-20_w4cxc3tl.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-10-20 — threads_2026-10-20_w4cxc3tl

> 原始出處：https://www.threads.com/share/BASYoPxhVp
> 對應筆記：[[threads_2026-10-20_w4cxc3tl]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-10-20_w4cxc3tl_01.jpg]]

## 內容

### 圖 1｜Neoclouds' Biggest Customers Are Also Their Owners and Guarantors

副標：Contracted Backlog by Counterparty, $B · Nvidia Has Equity or Warrants in 5 of 8; Google Backstops 3。
出處標示 © 2026 Boring Biz，資料截至 9/30/26。

**GPU Clouds（GPU 雲）**

| 公司 | 代號・口徑 | 合約積壓總額 | 依客戶拆分（$B） | 股權關係 | 擔保／兜底／預付 |
|---|---|---|---|---|---|
| CoreWeave | CRWV・backlog, 6/30/26 | **$104.2B** | Meta 35.2・OpenAI 22.4・Nvidia 6.3・other (incl. Microsoft) 40.3 | Nvidia ~10%（added $2B, 1/26） | Nvidia buys any unused capacity: $6.3B through 2032 |
| Nscale | Private・S-1 TCV, 9/26 | **$103.0B** | Microsoft 43.8・Anthropic 44.6・other 14.6 | Nvidia shareholder (+$1B, 9/26) | Nvidia backstops ~$0.9B of leases |
| Lambda | Private・backlog, 9/26 | **$50.0B** | Anthropic 35.0・other (incl. Microsoft) 15.0 | Nvidia investor (Series D) | Nvidia $1.5B GPU leaseback; holds the Beacon Point lease |
| Nebius | NBIS・RPO, 6/30/26 | **$37.5B** | Microsoft 17.4・Meta 15.0 (+ up to 15.0 more)・other 5.1 | Nvidia 9.3%（$2B, 3/26） | — |
| IREN | IREN・signed TCV, 7/26 | **$15.9B** | Microsoft 9.7・Nvidia 3.4・other 2.8 | Nvidia warrant: 30M sh. at $70 (≤$2.1B) | Microsoft prepaid ~20% (~$1.9B) |

**AI Campus Hosts（前比特幣礦商轉型的 AI 園區）**

| 公司 | 代號・口徑 | 合約積壓總額 | 依客戶拆分（$B） | 股權關係 | 擔保／兜底／預付 |
|---|---|---|---|---|---|
| Hut 8 | HUT・lease TCV, 7/26 | **$26.6B** | Nvidia 19.6 (Beacon Point)・Fluidstack 7.0 | — | Google guarantees Fluidstack's $7.0B lease |
| TeraWulf | WULF・lease TCV, 7/26 | **$25.7B** | Anthropic 19.0・Fluidstack 6.7 | Google ~14% (warrants) | Google backs $3.2B of Fluidstack rent |
| Cipher | CIFR・lease backlog, 8/26 | **$11.4B** | Amazon ~7.5・Fluidstack ~3.9 | Google 5.4% (warrants) | Google up to $1.73B; Amazon guarantees its lease |

圖例顏色：黑＝Big Tech（Microsoft, Meta, Amazon）、紅＝AI labs（OpenAI, Anthropic）、藍＝Nvidia、灰＝Other / undisclosed。

圖下附註（原文照抄）：
- Same megawatts, stacked: Hut 8 leases Beacon Point to Nvidia ($19.6B) → Lambda runs the GPUs → Anthropic buys the compute ($35B). **Rows are not additive.**
- Source: CoreWeave, Nebius, IREN, Hut 8, TeraWulf and Cipher filings and releases; Nscale S-1 (via Investing.com); Lambda investor letter (via WSJ); Nvidia stakes per 13G/WSJ; Beacon Point tenant per FT. Values are base-term contract value; some customer deals are "up to" and partly delivered.

**核對**：
- 8 列的分項加總都等於總額（例：CoreWeave 35.2＋22.4＋6.3＋40.3＝104.2；Nscale 43.8＋44.6＋14.6＝103.0），無矛盾。
- 副標「Nvidia 持股或認股權 5/8」＝CoreWeave、Nscale、Lambda、Nebius、IREN；「Google 兜底 3」＝Hut 8、TeraWulf、Cipher，與表格一致。
- ⚠️ **各列不能相加**：Hut 8 的 Nvidia $19.6B、Lambda 的 Anthropic $35B 是同一批電力（Beacon Point）被重複計算，圖上自己標明。
- ⚠️ 各公司口徑不同（backlog／RPO／TCV／lease TCV），基準日也不同（6/26～9/26），橫向比較要小心；部分合約是「up to」，不是確定金額。
- ⚠️ 原筆記 [[threads_2026-10-20_w4cxc3tl]] 的 AI 摘要把 Neocloud 猜成 AWS／Azure／GCP 等主流雲，**與圖不符**——圖上指的是 CoreWeave、Nebius 等 GPU 專業雲與礦商轉型的 AI 園區。

## 為什麼這幾張圖重要

- 直接回答「AI 算力需求有多少是循環融資」：最大客戶同時是股東與擔保人（Nvidia 投資＋買下閒置算力、Google 擔保租約），可餵 [[AI資本支出的融資結構]] 與 [[長期合約LTA與AI營收佔比]]。
- 礦商轉 AI 園區的電力／場地需求，可補 [[資料中心電力]]。
- Nvidia 自己也是買方（CoreWeave 6.3、IREN 3.4、Hut 8 19.6），可對照 [[輝達法說會與AI資本支出]]。
- 鏈頁 [[AI伺服器PCB鏈]] 若有「需求是否被灌水」的討論，這張表是第一手數字來源。
