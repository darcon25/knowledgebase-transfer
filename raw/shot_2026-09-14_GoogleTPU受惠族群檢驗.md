---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-14
image: assets/instagram_2026-08-31_GoogleTPU受惠族群檢驗_01.png
original_url: "https://www.instagram.com/p/Dcr9yYOimcX/?img_index=7&igsi=eHZxM2t3aGliZGJm"
image_count: 2
expected_min: 7
captured_by: fetch_media
source_note: "instagram_2026-08-31_GoogleTPU受惠族群檢驗.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-09-14 — instagram_2026-08-31_GoogleTPU受惠族群檢驗

> 原始出處：https://www.instagram.com/p/Dcr9yYOimcX/?img_index=7&igsi=eHZxM2t3aGliZGJm
> 對應筆記：[[instagram_2026-08-31_GoogleTPU受惠族群檢驗]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

⚠️ **這組輪播沒抓齊**：原網址的 `img_index=7` 顯示至少有 7 張，這裡只有 2 張。
登出狀態的 IG 只吐得出前一兩張，其餘要用已登入的 Chrome 開貼文逐張補。

## 圖片

![[instagram_2026-08-31_GoogleTPU受惠族群檢驗_01.png]]

![[instagram_2026-08-31_GoogleTPU受惠族群檢驗_02.png]]

## 內容

**萬寶投顧研究部圖卡**，原輪播共 **7 張**，這裡只抓到 **05/07 與 06/07** 兩張（詳見上方警告）。
主題：Google TPU 題材的受惠族群檢驗。

### 圖 05/07｜世芯有贏，但這次不是靠 TPU
兩條敘事並列：
| 公司表態 | 大摩獲利模型 |
|---|---|
| Google → **COT 機會** → 世芯 | **亞馬遜** → 獲利上修 → 世芯 |

> 結論：**題材 ≠ 獲利來源。公司說法跟法人模型，現在指向不同客戶。**

### 圖 06/07｜位置確認：v10 仍由聯發科整合
**單顆認列均價**：v9 **1.3 萬美元** → v10 **1.8 萬美元**（I/O 裸晶尺寸變大，單顆認列均價提高）

**TPU 營收預估與出貨量**
| 年 | 營收預估 | 出貨量 |
|---|---|---|
| 2027 | **130–150 億美元** | v8t：300 萬顆 |
| 2028 | **430–450 億美元** | v8t：100 萬顆｜v9：300 萬顆 |
| 2029 | **上看 700 億美元** | v9：400 萬顆｜v10：約 100 萬顆 |

**TPU 營收占聯發科總營收比重：2027 38% → 2028 65%**

兩點註記：
- 眼前 2027–2028 主力仍是 v8t 與 v9，**v10 主要影響 2029 年後格局**
- 大摩維持 TPU 營收預估；素材指出現股價約為 **2028 年 EPS 的 12 倍**

---

⚠️ **這篇沒抓齊**：缺 01～04 與 07/07。已抓到的兩張是全篇最關鍵的數字頁
（TPU 營收預估表與 v9→v10 單價），但缺少前段的族群名單與最後的結論頁。
需要用已登入的 Chrome 補。

**可用之處**：TPU 營收占聯發科比重 2028 年達 65% 是很強的結構性數字，
可放進 [[2454 聯發科]] 與 [[3661 世芯-KY]] 兩頁，並連到 [[themes]] 的 CSP 自研 ASIC 驅動因素。
「題材 ≠ 獲利來源」這個提醒也值得記進 [[concepts]]：世芯的獲利上修來自亞馬遜而非 Google TPU。
與 [[GoogleTPU轉COT模式]] 對照閱讀。
