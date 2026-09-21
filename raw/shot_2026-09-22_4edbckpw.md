---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-22
image: assets/threads_2026-09-21_4edbckpw_01.jpg
original_url: "https://www.threads.com/share/BAQNRhuZtN"
image_count: 1
expected_min: 1
captured_by: fetch_media
source_note: "threads_2026-09-21_4edbckpw.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-22 — threads_2026-09-21_4edbckpw

> 原始出處：https://www.threads.com/share/BAQNRhuZtN
> 對應筆記：[[threads_2026-09-21_4edbckpw]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-21_4edbckpw_01.jpg]]

## 內容

共 1 張圖。

### 圖 1｜SemiAnalysis：Rubin Ultra 兩種記憶體配置的 TCO 拆解表

深色底表格，右下角浮水印 `semianalysis`。標題：
**Rubin Ultra HBM4E 12-Hi NVL72 vs Rubin Ultra HBM4 8-Hi NVL572**

單位 `$/GPU/hr`，% 為佔 All-in Capital Cost of Ownership 的比重。

| Layer（成本層） | HBM4E 12-Hi NVL72 $/GPU/hr | % | HBM4 8-Hi NVL572 $/GPU/hr | % |
|---|---:|---:|---:|---:|
| HBM Costs | $0.99 | 29% | $0.43 | 14% |
| DRAM Costs | $0.26 | 7% | $0.26 | 9% |
| NAND Costs | $0.16 | 5% | $0.16 | 5% |
| **Memory Costs¹**（紅框標示） | **$1.41** | **41%** | **$0.84** | **28%** |
| GPU Costs (excl HBM) | $0.62 | 18% | $0.46 | 15% |
| Non-GPU Compute Tray Costs | $0.38 | 11% | $0.36 | 12% |
| OEM/ODM + Reseller Margin | $0.19 | 5% | $0.16 | 5% |
| **Scale-Up Networking Cost**（紅框標示） | **$0.13** | **4%** | **$0.37** | **12%** |
| Scale-Out Networking Cost | $0.49 | 14% | $0.49 | 16% |
| Storage Cost | $0.08 | 2% | $0.08 | 3% |
| All Other Costs | $0.18 | 5% | $0.25 | 8% |
| **All-in Capital Cost of Ownership** | **$3.48** | **100%** | **$3.01** | **100%** |

表格下方註腳 1（原文照抄）：
> *We assume a 70% GPU provider markup on HBM costs and 60% GPU provider markup on DRAM costs.*

**圖上直接讀得出來的幾件事**

- 記憶體減配後，**整機 TCO 從 $3.48 降到 $3.01/GPU/hr**，少 $0.47（-13.5%）。
- HBM 單項從 $0.99 → $0.43，**砍掉 57%**（貼文說「砍一半以上」與此相符）。
- 省下來的錢有一大塊回流到 **Scale-Up Networking：$0.13 → $0.37，佔比 4% → 12%**。
- DRAM（$0.26）、NAND（$0.16）、Scale-Out Networking（$0.49）、Storage（$0.08）**兩案完全相同**，變動全集中在 HBM、GPU、Scale-Up 三項。
- 兩個紅框只框了 Memory Costs 與 Scale-Up Networking Cost 兩列——這是製圖者要人看的重點。

**⚠️ 圖與說明文字不一致之處**

1. ⚠️ **NVL572 還是 NVL576**：圖上表頭明寫 **NVL572**，但原貼文與 n8n 摘要寫「NVL576 NPO 從 4% 升到 12%」。兩者差 4。以圖為準是 **NVL572**。
2. ⚠️ **4% → 12% 是哪一列**：貼文說是「NVL576 **NPO**」的佔比。圖上 4% → 12% 這一列的名稱是 **Scale-Up Networking Cost**，表格裡**完全沒有出現 NPO 這個字**。所以「NPO 從 4% 升到 12%」是貼文作者的解讀，不是圖上的原始標籤。
3. ⚠️ **記憶體佔比 40% 還是 41%**：貼文寫「漲價後記憶體佔資本持有成本約 40%」，圖上 Memory Costs 那格是 **41%**。（減配後的 28% 兩邊一致。）
4. ⚠️ **第二欄 Memory Costs 加總差 1 分**：HBM $0.43 + DRAM $0.26 + NAND $0.16 = **$0.85**，但圖上 Memory Costs 寫 **$0.84**。第一欄則吻合（0.99+0.26+0.16=1.41）。應是四捨五入造成，但數字對不起來要記一筆。

**圖上沒有的東西（不要從這張圖推論）**

- 沒有 384GB / 192GB 的容量標示——那是貼文文字補的。
- 沒有時間軸、沒有出貨量、沒有 NVIDIA 官方確認字樣。貼文自己也寫「NVIDIA 未公開確認」。
- 沒有任何台廠名稱，這張表全部是 NVIDIA 自家 BOM 層級的成本結構。

### 為什麼這幾張圖重要

這是**第一份把「HBM 減配」換算成實際金額**的一手資料，而不只是「聽說要減配」。三條可以往下接：

1. **Scale-Up Networking 佔比 4% → 12%**：同一台機器裡，網路互連的錢變成三倍。這直接對到 [[CPO共同封裝光學]]、[[交換器與網通互聯]]、[[NvidiaCPX與Scale-out架構]]——注意圖上 **Scale-Out 完全沒變**（$0.49 兩案相同），漲的只有 **Scale-Up**，兩者不要混為一談。
2. **HBM 佔比 29% → 14%**：若成真，對 [[HBM4與先進封裝]] 與 [[記憶體]] 是負面訊號，但對 [[2330 台積電]] 的 GPU 本體（$0.62 → $0.46）也是降的。可與 [[半導體結構性失衡]] 對照。
3. **NVL72 → NVL572 的機櫃規模放大**：機櫃變大、背板與互連層數變多，是 [[AI伺服器PCB鏈]] 與 [[CCL]]／[[PTFE與材料世代轉換]] 的需求來源。但**這張圖沒有講任何板材規格**，影響路徑待確認，不要直接寫進公司頁的「我的論點」。

原始貼文與留言見 [[threads_2026-09-21_4edbckpw]]。同批讀圖的還有 [[shot_2026-09-22_b8m20uwi]]（封測四檔）與 [[shot_2026-09-22_斗山擴CCL產能大摩點名台廠]]（CCL 擴產）。
