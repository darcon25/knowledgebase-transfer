---
tags:
  - source
  - screenshot
type: screenshot
date_captured: 2026-10-08
image: assets/threads_2026-10-08_xs25imsz_01.jpg
original_url: "https://www.threads.com/share/BAfmU4_0o-"
original_id: xs25imsz
image_count: 4
expected_min: 4
captured_by: fetch_media
source_note: "threads_2026-10-08_xs25imsz.md"
status: 已讀圖
---

# 📸 原貼文圖片 2026-10-08 — threads_2026-10-08_xs25imsz

> 原始出處：https://www.threads.com/share/BAfmU4_0o-
> 對應筆記：[[threads_2026-10-08_xs25imsz]]

**取得方式**：`tools/fetch_media.py` 從 Jina Reader 回傳的 markdown 取出主文圖片網址並下載。
n8n 管道把這些網址丟掉了，所以由本機補。

## 圖片

![[threads_2026-10-08_xs25imsz_01.jpg]]

![[threads_2026-10-08_xs25imsz_02.jpg]]

![[threads_2026-10-08_xs25imsz_03.jpg]]

![[threads_2026-10-08_xs25imsz_04.jpg]]

## 內容

四張圖是七小服 Seven Small Services 的輪播（頁碼 01～04，簡體字），頁首標「據 AMD、甲骨文新聞稿及 DCD、ServeTheHome 報道・機櫃科普」，頁尾標「行業知識分享，不構成投資建議」。

### 圖 1｜AMD 也有自己的 72 卡機櫃了

副標：它叫 Helios。一個櫃子裝 72 顆 AMD 的 AI 晶片，對著英偉達的 Vera Rubin 整機櫃。（配圖：AMD 官方圖，機櫃側面印 AMD HELIOS）

| 項目 | 數值 |
|---|---|
| GPU | 72 顆 Instinct MI455X GPU |
| 整櫃 HBM4 顯存 | 31TB |
| 整櫃重量 | 約 2.3 噸，約 5,000 磅 |

### 圖 2｜櫃子裡有什麼：18 個計算托盤，中間夾 6 個交換托盤

由上到下的機櫃配置：

| 位置 | 內容 | 說明 |
|---|---|---|
| 最上 | 電源 | 兩端各一組 |
| 上段 | 9 個計算托盤 | 每個 4 顆 MI455X GPU 加 1 顆 EPYC「Venice」CPU |
| 中段 | 6 個交換托盤 | 櫃內 GPU 互聯，用 UALink |
| 下段 | 9 個計算托盤 | 一共 18 個，72 顆 GPU |
| 最下 | 電源 | 50V 直流母排，全液冷 |

圖註：圖源 AMD 官方圖。**兩端為電源是看圖判斷**。托盤數量據 ServeTheHome（AMD 在 Hot Chips 2026 的介紹）、DCD。

### 圖 3｜和英偉達的放一起看：兩家的機櫃，越做越像

| 項目 | 英偉達 Vera Rubin | AMD Helios |
|---|---|---|
| GPU 數量 | 72 顆 | 72 顆 |
| 計算托盤 | 18 個，每個 4 GPU + 2 CPU | 18 個，每個 4 GPU + 1 CPU |
| 交換托盤 | 9 個 | 6 個 |
| 櫃內互聯 | NVLink，自家的 | UALink，開放標準 |
| 機櫃 | 約 1.8 噸 | 雙倍寬，約 2.3 噸 |
| 冷卻 | 全液冷 | 全液冷 |

進度：蘇姿丰 10 月 6 日說，Helios 三季度已按計劃開始出貨。英偉達的數字據英偉達開發者部落格和超微官方實拍；AMD 的據 DCD、ServeTheHome。

### 圖 4｜我們的判斷：這樣的機櫃還遠，在用的設備照樣要保

| 小標 | 內容 |
|---|---|
| 兩家越做越像 | 都是一櫃 72 顆、全液冷，差別在晶片和互聯 |
| 對機房是新要求 | 雙倍寬、約 2.3 噸、全液冷，承重、供電都要重算 |
| 多數機房的主力沒變 | 還是伺服器、存儲、網絡，維保和備件要跟上 |

結語：能修的修，該換的換。（判斷是作者的；事實來源：AMD、DCD、ServeTheHome、英偉達）

### 核對

- 72 顆 = 18 托盤 × 4 GPU，圖 1／2／3 一致；2.3 噸 ≈ 5,000 磅換算一致。
- ⚠️ 圖 2「兩端為電源」作者自己註明是**看圖判斷**，不是官方規格。
- ⚠️ 原筆記純文字只說兩家「同樣 18 個運算托盤」，沒寫出圖 3 的差異：**Vera Rubin 每托盤 2 顆 CPU、AMD 只有 1 顆**；機櫃重量 1.8 噸 vs 2.3 噸，AMD 還是**雙倍寬**。
- ⚠️ 圖 4 的結論（維保、備件）圖上自己標明「判斷是我們的」，是作者觀點，不是產業數據。
- 31TB HBM4 只給整櫃總量，圖上沒有每顆 GPU 的容量，無法交叉驗算。

## 為什麼這幾張圖重要

- [[CPU市佔與ARM競爭]]：每個計算托盤 CPU 數量 2 顆（NVIDIA）vs 1 顆（AMD EPYC Venice），直接影響 CPU 用量估算，可對照 [[shot_2026-09-21_台廠CPU供應鏈對照表]]
- [[交換器與網通互聯]]：交換托盤 9 vs 6、NVLink vs UALink，是互聯環節內容量差異的具體數字
- [[液冷散熱滲透率]]、[[資料中心電力]]：兩家都全液冷；「雙倍寬、2.3 噸、50V 直流母排，承重與供電要重算」是機房改造需求的證據
- [[HBM4與先進封裝]]：整櫃 31TB HBM4，可對照 [[shot_2026-09-14_CPX轉HBM4與CoWoS受惠]]
- [[輝達法說會與AI資本支出]]、[[AI伺服器PCB鏈]]：Helios Q3 已開始出貨，代表除了 NVIDIA 之外多一個 72 卡整櫃需求來源；可對照 [[shot_2026-09-14_輝達FY2Q27法說會重點]]
- 對應原筆記：[[threads_2026-10-08_xs25imsz]]
