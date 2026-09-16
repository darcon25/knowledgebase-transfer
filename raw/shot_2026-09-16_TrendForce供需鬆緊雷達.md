---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-09-16
image: assets/threads_2026-09-16_TrendForce供需鬆緊雷達_01.jpg
original_url: "https://www.threads.com/share/_qkD99vOO"
image_count: 1
expected_min: 1
captured_by: fetch_media
source_note: "threads_2026-09-16_TrendForce供需鬆緊雷達.md"
status: 已讀圖
original_id: wpy4125a
---

# 📸 原貼文圖片 2026-09-16 — threads_2026-09-16_TrendForce供需鬆緊雷達

> 原始出處：https://www.threads.com/share/_qkD99vOO
> 對應筆記：[[threads_2026-09-16_TrendForce供需鬆緊雷達]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-09-16_TrendForce供需鬆緊雷達_01.jpg]]

## 內容

共 1 張圖。TrendForce 官方製表（右下角有 TrendForce logo，中央有浮水印），全英文。

### 圖 1｜TrendForce AI 伺服器零組件供需雷達（2026/09/14）

欄位原文：Item ／ Status ／ Current Lead Time ／ Balanced Lead Time ／ Quick Take。
交期欄位的單位在圖上只寫 `W`，圖卡未展開這個縮寫。

| Item | Status | Current Lead Time | Balanced Lead Time | Quick Take（原文照抄） |
|---|---|---|---|---|
| GPU | Balanced | 20–30W | 20–30W | NVIDIA Blackwell (B300/GB300) has been shipping on schedule since 2Q26. |
| DRAM | Very Tight | 20W | 8W | Supplier inventories are depleted, but high margins may support occasional additional supply, particularly for 96GB/128GB RDIMMs. |
| NAND (eSSD) | Tight | 16W | 8W | Due to recent surging demand, eSSD is expected to face tight supply in 2027. |
| HDD | Very Tight | 50W | 16W | As NAND price increases widen the gap versus HDDs, CSPs are prioritizing HDDs to lower TCO, then using QLC eSSDs to fill remaining gaps. |
| ABF | Very Tight | 48–56W | 12W | AI-related chips are rapidly increasing in die size and layer count. Tight upstream T-glass supply and lower yields for high-layer-count ABF are slowing capacity expansion, resulting in persistent shortages. |
| MLCC | Tight | 30W | 12W | MLCC leader Murata is accelerating cuts in standard consumer and low-end automotive lines. Yageo and CCTC are poised to capture the order shifts. |

#### 狀態定義（圖下方 Status key，共五級）

| 標示 | 定義（原文） |
|---|---|
| Very Tight | severe shortage |
| Tight | constrained supply |
| Tightening | conditions worsening |
| Balanced | supply-demand balance |
| Easing | conditions improving |

註：`Tightening` 與 `Easing` 兩級只出現在圖例，這張表的六個項目都沒有用到。

**資料來源（圖上標註）**：Source: TrendForce, Sep 14, 2026

#### 交期偏離倍數（用表上兩欄相除算出，非圖上原有）

| Item | 現行／均衡 |
|---|---|
| ABF | 約 4.0–4.7 倍 |
| HDD | 約 3.1 倍 |
| DRAM | 2.5 倍 |
| MLCC | 2.5 倍 |
| NAND (eSSD) | 2.0 倍 |
| GPU | 1.0 倍 |

#### ⚠️ 圖文對照差異

貼文文字寫「**缺的已經不是晶片，是其餘零件跟不上**」，但表上六項裡有三項本身就是晶片，而且全都缺：**DRAM（Very Tight）、NAND/eSSD（Tight）**，ABF 是載板、HDD 是成品硬碟、MLCC 是被動元件。表上唯一 Balanced 的只有 **GPU** 一項。

正確的讀法應該是「**缺的不再是 GPU，而是 GPU 以外的所有東西（含記憶體晶片）**」——貼文把「晶片」等同於「GPU」了。這個差異會直接影響後續判斷，不要沿用貼文原句。

### 為什麼這張圖重要

這是一張把「AI 伺服器到底卡在哪裡」量化成交期數字的表，而且是帶日期（2026/09/14）的官方製表，可以當基準點，之後拿新版對照看鬆緊變化。

可餵的頁面：

- **ABF 48–56W vs 均衡 12W，是全表最嚴重的一項**，且 Quick Take 直接點名「上游 T-glass 供給緊、高層數 ABF 良率低」→ [[ABF載板隱性減產]]、[[載板]]、[[玻纖布缺料]]、[[8046 南電]]、[[3189 景碩]]、[[3037 欣興]]
- **DRAM / NAND** → [[記憶體]]、[[2408 南亞科]]、[[2344 華邦電]]、[[8299 群聯]]
- **MLCC**：Quick Take 明講 Murata 砍標準品線、Yageo（國巨）與 CCTC 可望接單移轉 → [[3026 禾伸堂]]
- **GPU 是唯一 Balanced**，且註明 B300/GB300 自 2Q26 起如期出貨 → [[輝達法說會與AI資本支出]]、[[終端需求]]
- 整體「瓶頸從晶片轉到週邊」的結構 → [[半導體結構性失衡]]、[[AI伺服器PCB鏈]]

同批次另兩則貼文見 [[shot_2026-09-16_大摩AI機櫃PCB含量]]（大摩 AI 機櫃 PCB content）與 [[shot_2026-09-16_Intel18A良率追到80]]（先進製程良率）。
