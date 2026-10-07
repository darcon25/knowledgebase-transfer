---
tags:
  - source
  - social_media
  - threads
type: social_media
platform: threads
date_captured: 2026-10-07
original_url: "https://www.threads.com/share/BBQk6PPO6X"
media_count: 1
media_urls:
  - "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/836834417_17990512764111621_557744551730229430_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=108&ig_cache_key=NDAwMTYwMTYwODE3Nzg2Mjk3Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQueHBpZHMuMTUwNC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=tuX0ruqmBzEQ7kNvwEdugxd&_nc_oc=AdoMbqzudy40HwC-MaI9D6Za9pwe1iBanSPzFOgVfS8PNl3UFDMYFlbLKfu6XLJjeqE&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=n0mFYQNkoNRor34o5NMzWw&_nc_ss=7b289&oh=00_AQMPb6kEmyJyJ3qcZ0g0n8AIuXaGp_7D6P6UctIhuRfCtg&oe=6ACB688E"
---

# 🧵 2026-10-07 存檔

> 原文：[查看貼文](https://www.threads.com/share/BBQk6PPO6X)

## 摘要
這篇貼文是關於Google TPU v8網通架構的分析，作者Klu分享了其在互連技術上的顯著提升，並將其與Nvidia的Scale up/out/across策略進行比較。貼文特別強調了互連晶片速度的翻倍、Jupiter和Virgo兩種架構的應用，以及相關硬體規格的升級，並推薦了幾家潛在的供應商。

## 重點整理
*   **TPU v8互連架構全面升級：** Google TPU v8在機櫃內、機櫃間及叢集間的互連能力均有顯著提升，旨在對標Nvidia的Scale up/out/across策略。
*   **互連晶片速度翻倍與雙架構應用：** 互連晶片速度升級至每秒19.2Tb，並引入Jupiter（處理南北向流量）和Virgo（處理東西向流量）兩種架構以提升整體互連效率。
*   **硬體規格提升：** TPU v8每個節點需使用3個收發器（transceiver），Serdes速度提升至200Gbps，且每個TPU的銅纜（copper cables）使用量增加至1.9條。
*   **潛在供應商推薦：** 報告中主要推薦了LITE、CLS、光聖、聯鈞等公司，作者額外提及聯鈞可能是因雷射封裝需求增加。
*   **作者對內容被刪除的不滿：** 作者提到前兩篇關於TPU的貼文被強制刪除，表達了不屈服的態度。

## 關鍵概念
*   **Google TPU (Tensor Processing Unit)：** Google專為機器學習工作負載設計的客製化ASIC晶片。
*   **TPU v8網通架構：** 指Google最新一代TPU在網路通訊方面的設計與技術。
*   **Scale up / out / across：** 描述系統擴展能力的三種策略，通常用於高效能運算和資料中心。
    *   **Scale up (垂直擴展)：** 增加單一節點的資源（如CPU、記憶體）。
    *   **Scale out (水平擴展)：** 增加更多節點來分散負載。
    *   **Scale across：** 通常指跨多個叢集或資料中心的擴展。
*   **互連晶片 (Interconnect Chip)：** 用於連接多個處理器、記憶體或其他硬體組件，實現高速資料傳輸的晶片。
*   **Jupiter (North-South traffic)：** 指資料中心內，伺服器與外部網路或核心網路之間的流量。
*   **Virgo (East-West traffic)：** 指資料中心內，伺服器之間或應用程式之間的流量。
*   **Transceiver (收發器)：** 結合發射器和接收器的電子設備，用於光纖通訊等。
*   **Serdes (Serializer/Deserializer)：** 序列器/解序列器，用於高速資料傳輸，將平行資料轉換為序列資料進行傳輸，再轉換回來。
*   **Copper Cables (銅纜)：** 傳統的電纜，用於短距離、高速的資料傳輸。
*   **雷射封裝：** 一種先進的半導體封裝技術，可能與光通訊模組或高速互連有關。

## 可行動洞察
*   **追蹤AI硬體發展趨勢：** Google TPU v8的互連技術升級，顯示AI基礎設施對高速、高效能網路通訊的需求持續增長。這對於投資者、硬體供應商和資料中心營運商來說是重要的趨勢。
*   **研究相關供應鏈機會：** 貼文提及LITE、CLS、光聖、聯鈞等公司，可進一步研究這些公司在光通訊、高速連接器、雷射封裝等領域的技術實力與市場地位，評估其是否能從TPU v8的升級中受益。
*   **關注資料中心網路架構演進：** Jupiter和Virgo兩種流量處理架構的應用，反映了資料中心在優化不同方向流量傳輸效率上的策略。這對於網路設備供應商和資料中心架構師具有參考價值。
*   **深入理解Serdes和Transceiver技術：** Serdes速度提升至200Gbps，以及每個節點對Transceiver的需求增加，表明這些關鍵零組件的技術門檻和市場需求都在提高。可關注相關技術的最新進展和供應商。
*   **分析Nvidia與Google的競爭策略：** 將TPU v8的升級與Nvidia的Scale up/out/across策略進行比較，有助於理解兩大AI晶片巨頭在基礎設施層面的競爭態勢和技術路線。

## 主文圖片

原貼文主文有 1 張圖。本機 `tools/fetch_media.py` 會下載成 `raw/shot_*.md`。
（下列網址帶簽章，約一週後失效，僅作線索。）

1. https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/836834417_17990512764111621_557744551730229430_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=108&ig_cache_key=NDAwMTYwMTYwODE3Nzg2Mjk3Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQueHBpZHMuMTUwNC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=tuX0ruqmBzEQ7kNvwEdugxd&_nc_oc=AdoMbqzudy40HwC-MaI9D6Za9pwe1iBanSPzFOgVfS8PNl3UFDMYFlbLKfu6XLJjeqE&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=n0mFYQNkoNRor34o5NMzWw&_nc_ss=7b289&oh=00_AQMPb6kEmyJyJ3qcZ0g0n8AIuXaGp_7D6P6UctIhuRfCtg&oe=6ACB688E

## 原文（Jina Reader）

```
Title: Klu (@klu_jfk) on Threads

URL Source: https://www.threads.com/share/BBQk6PPO6X

Markdown Content:
[](https://www.threads.com/)

[Home](https://www.threads.com/)

New thread

[Search](https://www.threads.com/search)

Messages

Activity

Profile

Insights

[Log in](https://www.threads.com/login?show_choice_screen=false)

More

[](https://www.threads.com/)

[](https://www.threads.com/)

[](https://www.threads.com/search)

# [Thread](https://www.threads.com/@klu_jfk/post/DeIi3YUEsk8?xmt=AQG02Kj4UVo3OuOj5lwzEbFc15c0OU56rEQHRMxWclOqhzoi1jc0rLbfbrD_eb9IwWx1JPXw&slof=1)

13.5K views

[![Image 1: klu_jfk's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/722204573_17971540836111621_6439737941885017060_n.jpg?stp=dst-jpg_s206x206_tt6&_nc_cat=110&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=BPuMm5FdyhcQ7kNvwGMQA6Q&_nc_oc=AdoIb7xbyc2n1dDYjlSRmF8gzrflae6nV3dYUIXWoadhXgi-uQUhKnC0RVf47pnwsAw&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=n0mFYQNkoNRor34o5NMzWw&_nc_ss=7b289&oh=00_AQPSyID6vLp0m5sLUkM2fyJzyegjXbo9k-6F4-WFRGGucA&oe=6ACB60D8)](https://www.threads.com/@klu_jfk)

[klu_jfk](https://www.threads.com/@klu_jfk)

[23h](https://www.threads.com/@klu_jfk/post/DeIi3YUEsk8)

一些關於Google TPU的小事 VI

上兩篇寫的TPU被強制刪文！沒游泳的，我不會屈服的！

今天來蹭一下Aletheia早上發的v8網通架構。

1. TPU v8這次在機櫃內 / 機櫃間 / cluster 間的互連都有所提升，基本上就是對應Nvidia的Scale up / out / across。

2. 互連晶片互聯直接翻倍升級到每秒19.2Tb，並且會使用Jupiter（North-South traffic)以及Virgo (East-West traffic)兩種架構來提升整體的互連效率。

3. 其他重點還包含v8 per node會需要用到3個transceiver，Serdes提升到200Gbps，copper cables提升到1.9 per TPU。

4. 整篇報告主推LITE / CLS / 光聖 / 聯鈞。最後一個我自己偷渡的，雷射封裝這樣一定要更多啊！

[![Image 2](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/836834417_17990512764111621_557744551730229430_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=108&ig_cache_key=NDAwMTYwMTYwODE3Nzg2Mjk3Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQueHBpZHMuMTUwNC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=tuX0ruqmBzEQ7kNvwEdugxd&_nc_oc=AdoMbqzudy40HwC-MaI9D6Za9pwe1iBanSPzFOgVfS8PNl3UFDMYFlbLKfu6XLJjeqE&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=n0mFYQNkoNRor34o5NMzWw&_nc_ss=7b289&oh=00_AQMPb6kEmyJyJ3qcZ0g0n8AIuXaGp_7D6P6UctIhuRfCtg&oe=6ACB688E)](https://www.threads.com/@klu_jfk/post/DeIi3YUEsk8/media)

342

13

4

66

Log in or sign up for Threads See what people are talking about and join the conversation.[Log in with username instead](https://www.threads.com/login?show_choice_screen=false)

*   © 2026
*   [Threads Terms](https://help.instagram.com/769983657850450)
*   [Privacy Policy](https://help.instagram.com/515230437301944)
*   [Cookies Policy](https://help.instagram.com/1896641480634370/)
*   Report a problem

```

## 相關頁面

<!-- [[]] -->