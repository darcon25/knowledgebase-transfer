---
tags:
  - source
  - social_media
  - threads
type: social_media
platform: threads
date_captured: 2026-09-21
original_url: "https://www.threads.com/share/__HyenIPt"
media_count: 0
---

# 🧵 2026-09-21 存檔

> 原文：[查看貼文](https://www.threads.com/share/__HyenIPt)

## 摘要
這篇貼文深入探討了CPO（共同封裝光學）技術的實際應用與市場誤解。作者指出CPO旨在解決高速SerDes在PCB上傳輸的損耗問題，將光學引擎移至ASIC旁以縮短電氣介面。然而，CPO並非全面取代銅線，NVIDIA的策略是短距離仍用銅線，長距離或高頻寬才逐步導入光學。市場對CPO對CCL（銅箔基板）的影響存在過度簡化的預期，特別是關於高階CCL需求將大幅下降的說法，作者認為這忽略了時間軸、不同應用場景以及材料技術的複雜性。

## 重點整理
*   **CPO核心目的與NVIDIA策略：** CPO是為了解決高速SerDes在PCB長距離傳輸造成的訊號損耗與功耗問題，透過將光學引擎整合至ASIC旁，縮短高速電氣介面。NVIDIA的實踐是將CPO首先導入Scale-out網路交換器，並強調在機架內仍優先使用銅線，僅在長距離、高頻寬需求下才逐步採用光學。
*   **市場對CPO影響的誤解：** 市場普遍認為CPO會導致CCL全面降規至M4等級，且高階CCL需求將大幅下降。作者認為這是過度簡化，忽略了PCIe技術的持續升級（Gen5→Gen6→Gen7）以及不同板卡、通道、距離對材料需求的差異。
*   **CPO對材料需求的轉變而非消失：** CPO確實可能減少PCB上超高速SerDes長距離走線對「大面積超低損耗CCL」的需求，但材料問題並未消失，而是轉移到封裝基板、interposer、光引擎基板、熱管理、CTE、電源完整性等更高價值密度的領域，對材料的要求也從單純的Dk/Df轉向Dk/Df + Low CTE + thermal + dimensional stability + power integrity等多重性能指標。
*   **高階CCL技術持續演進：** 高階CCL的性能由樹脂、玻纖布、銅箔共同決定，M4到M8/M9等級的差異巨大，涉及Low-Dk/Q-glass、碳氫樹脂、PPO、HVLP銅箔等先進技術。HVLP銅箔廠商也指出AI伺服器與高速交換器已進入112G/224G PAM4，HVLP3已大量出貨，HVLP4正往更高階驗證。
*   **CPO大規模滲透的時間軸：** CPO的大規模滲透是一個長期過程。TrendForce預估2026年CPO在AI資料中心光學收發器的滲透率僅約0.5%，到2030年才可能提高到35%。NVIDIA的roadmap也顯示，CPO Switch量產始於2026年，逐步擴張至Scale-up約在2027-2028年，真正影響大型高階CCL需求的時間點可能落在2028-2030年之後。

## 關鍵概念
*   **CPO (Co-Packaged Optics, 共同封裝光學)：** 將光學引擎與ASIC（如交換器晶片）共同封裝，以縮短高速電氣訊號傳輸距離，降低損耗和功耗。
*   **SerDes (Serializer/Deserializer)：** 高速串列/並列轉換器，用於高速數據傳輸。
*   **Insertion Loss (插入損耗)：** 訊號在傳輸路徑中因介質、連接器等造成的能量損失。
*   **CCL (Copper Clad Laminate, 銅箔基板)：** PCB（印刷電路板）的基礎材料，由銅箔和絕緣材料（如樹脂、玻纖布）組成。
*   **Dk (Dielectric Constant, 介電常數)：** 影響訊號傳輸速度和阻抗的材料特性。
*   **Df (Dissipation Factor, 損耗因子)：** 衡量材料對電磁波能量損耗的程度，Df越低，訊號損耗越小。
*   **HVLP (Hyper Very Low Profile) 銅箔：** 表面粗糙度極低的銅箔，用於減少高速訊號傳輸中的Skin Effect（集膚效應）和插入損耗。
*   **PCIe (Peripheral Component Interconnect Express)：** 高速串列擴展匯流排標準，用於連接CPU與周邊設備。
*   **NVLink：** NVIDIA開發的高速互連技術，用於GPU之間或GPU與CPU之間的高速通訊。
*   **Scale-out Network Switch：** 擴展型網路交換器，主要用於資料中心內部橫向擴展的網路架構。
*   **Scale-up Optical/CPO：** 垂直擴展型光學/CPO，可能指用於GPU-to-GPU、跨機架等更大型、更高速的互連應用。
*   **M4/M6/M7/M8/M9：** 指不同等級的CCL材料，數字越大通常代表性能越好，損耗越低。

## 可行動洞察
*   **重新評估CPO對CCL產業的影響：** 市場對CPO的影響存在過度樂觀或悲觀的誤解。應避免將CPO視為CCL的「終結者」，而應理解其對材料需求的轉變，即從大面積低損耗材料轉向高價值密度、多功能整合的先進材料。這意味著CCL廠商需專注於高階材料的研發，如低CTE、散熱、厚銅、高頻特性（Dk/Df）與尺寸穩定性兼具的產品。
*   **關注時間軸與NVIDIA的實際策略：** CPO的大規模滲透是一個長期過程，短期內（2026年前）對高階CCL的需求影響有限。應密切關注NVIDIA等領導廠商的實際產品導入進度與技術路線圖，而非僅憑新聞稿或市場傳言。特別是NVIDIA強調銅線在短距離的優勢，意味著「煉銅」的需求仍將持續。
*   **深入研究不同應用場景的材料需求：** 不能將所有PCB應用混為一談。AI伺服器平台升級（PCIe Gen5→Gen6→Gen7）、224G電訊號升級、PCB層數增加、800G/1.6T光模組、NVLink銅線互連等，都對高階CCL（如M8/M9、HVLP、Low-Dk/Q-glass）有持續需求。應區分CPO影響的特定領域（如超高速SerDes長距離走線）與其他仍需高階材料的領域。
*   **關注先進封裝與熱管理材料機會：** CPO將問題集中到封裝基板、interposer、光引擎基板、熱管理等領域。這為提供低CTE、高散熱效率、高尺寸穩定性、優異電源完整性材料的廠商帶來新的成長機會。
*   **投資策略應基於長期趨勢與數據：** 避免因短期市場情緒而做出過度反應。參考TrendForce等專業機構對CPO滲透率和時間軸的預估，並結合產業領導者的實際發言，制定更穩健的投資或業務發展策略。

## 原文（Jina Reader）

```
Title: @4arcues93_ on Threads

URL Source: https://www.threads.com/share/__HyenIPt

Markdown Content:
[](https://www.threads.com/)

[](https://www.threads.com/)

[](https://www.threads.com/search)

# [Thread 8.3K views](https://www.threads.com/@4arcues93_/post/DdfwOuKoEjB?xmt=AQG0JvELOo7leMBKjyBXlG-xXmfH4RkHL-bcTo8l1h_zSFrzCGBpawT57_5gb4yaxH8_UMw&slof=1)

[![Image 1: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwOuKoEjB)

談談CPO CCL CPO 本來就是為了解決高速 SerDes 在 PCB 上傳太遠造成 insertion loss、功耗與訊號完整性惡化。

Synopsys 對 CPO 的定義很直接，傳統架構裡，高速訊號要從 switch ASIC 經過 PCB 跑到前面板光模組；CPO 把 optical engine 移到 ASIC 附近，使高速電氣介面縮短到幾毫米。

NVIDIA 自己也說CPO 把 optical engine 直接整合在 switch ASIC 旁，目的就是消除 electrical SerDes loss。

「CPO 會減少部分 PCB 上超高速 SerDes 長距離走線」是真的。

135

10

5

31

[![Image 2: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwOtWoNhu)

·Author

現在 NVIDIA 正式量產的 CPO，首先導入的是 Scale-out network switch，也就是 Spectrum-X Ethernet Photonics、Quantum-X InfiniBand Photonics 這些交換器，不是GPU Server 全部 PCB 訊號都直接變成光。 NVIDIA 今年 5 月已宣布 Spectrum-X Ethernet Photonics 進入量產，CPO 是放在 switch ASIC 周圍。

今年 GTC Taipei，NVIDIA Networking SVP Gilad Shainer 談架構時直接說，能用 copper 的地方，就會用 copper。原因是成本、可靠度、功耗都很好，他甚至直接說：rack 內可以用 copper，NVLink 就是 copper；距離拉長、跨 rack 之後才需要 optical。 NVIDIA 現在真正走的方向比較像： 短距離 → 繼續用銅。 距離變長、頻寬太高 → 光逐步滲透。 而不是銅全部死掉全部變光。

11

1

[![Image 3: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwOunIAVI)

·Author

然後新聞稿上「只剩 PCIe Gen5」這句話本身就很有問題，PCIe 5.0 是 32 GT/s，但現在 PCI-SIG 的 PCIe 6.0 已經是 64 GT/s，而且 PCIe 7.0 世代進一步往 128 GT/s 發展。所以把整個 Server motherboard 都講成：「以後只剩 PCIe Gen5 32G 的低速控制訊號。」我認為這是過度簡化， 而且 PCIe 本身不是單純「控制訊號」，它是高速 I/O interconnect，現在一般型伺服器反而正在發生，PCIe Gen5 → Gen6 M6 → M7聯茂今年法說談的核心成長邏輯就是這個。 很矛盾的點就是一邊市場說 CPO 之後 CCL 全部退回 M4，但另一邊真正正在發生的 CPU Server 平台升級卻是 M6 → M7。原因就是不同 board、不同 channel、不同距離，根本不能全部混在一起談。

8

1

[![Image 4: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwOuDoJHx)

·Author

那真正被 CPO 打到的是「為了讓超高速訊號在一大片 PCB 上跑很遠，所以必須整張板大量使用超低損耗 CCL」這個邏輯，這個邏輯未來確實可能弱化，但是高階材料需求 ≠ 消失。比較準確的講法是大面積、高階低損耗材料的用量可能下降，但材料的價值密度會往 ASIC package、optical engine substrate、advanced substrate、低 CTE、散熱、厚銅等方向轉移。

而且 CPO 本身其實沒有把「材料問題」消滅 這一點很多人忽略。CPO 把 optical engine 搬到 ASIC 旁邊之後，確實讓 board-level 高速走線縮短，但它同時把問題集中到封裝基板、interposer、光引擎基板、熱管理、CTE、電源完整性。所以未來材料要求會從單純，Dk、Df 越低越好，變成Dk/Df + Low CTE + thermal + dimensional stability + power integrity。

8

1

[![Image 5: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwOvpIIsY)

·Author

再來現在一張高階 CCL 的性能，是樹脂、玻纖布、銅箔共同決定的。MEGTRON4 屬於 Low Transmission Loss，Df 約 0.005； 到 MEGTRON6、7、8 已經進入 Ultra-low Transmission Loss，部分 M7/M8 產品 Df 可以降到約 0.001～0.002 的區間，所以所謂 M4、M8、M9，不是單純名字換一下而已。背後牽涉Low-Dk / Q-glass、碳氫樹脂、PPO、HVLP 銅箔、低 CTE、熱穩定性，而且傳輸速率越高，skin effect 越嚴重，銅箔表面 roughness 對 insertion loss 的影響越大。

HVLP 銅箔廠商今年也明確指出，AI Server 與高速 switch 已進入 112G/224G PAM4，HVLP3 已大量出貨，HVLP4 正在往更高階 CCL/PCB 驗證。 因此如果 CPO 把原本長距離 224G SerDes 從 PCB 移到 ASIC 附近，這部分對超低損耗 CCL 與 HVLP 的 content 確實存在下降風險。

8

1

[![Image 6: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwOtRoPf7)

·Author

但剩下的 electrical channel，以及先進封裝裡面更高密度的 electrical interconnect，並沒有因此變簡單。

時間軸才是這次事件最重要的地方，這次市場最大問題，我認為不是方向看錯，而是把 2030 年附近的故事一次 price-in 到 2026 年，TrendForce 今年 3 月的估計是2026 年 CPO 在 AI 資料中心 optical transceiver 的滲透率大約只有 0.5%；到 2030 年左右，有機會提高到約 35%，而且 TrendForce 引述產業看法指出，ultra-short-reach 的 rack 內 copper 至少到 2028 年左右仍會是主流方案。

Scale-up optical/CPO 真正開始大量影響 GPU-to-GPU、跨 rack 架構，比較可能落在 2027～2029 之後。TrendForce 6 月的研究也把 meaningful ramp 放在 2028～2029 左右。 這其實跟 NVIDIA 自己的 roadmap 很吻合。

5

1

[![Image 7: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)](https://www.threads.com/@4arcues93_)

[4arcues93_](https://www.threads.com/@4arcues93_)

[1d](https://www.threads.com/@4arcues93_/post/DdfwO_6IHkK)

·Author

NVIDIA 今年 7 月公布 NVLink 6 時，仍然是 rack-scale electrical fabric；但未來 NVLink scale-up domain 可以延伸到 1,152 GPU，屆時才會導入 CPO。

簡單濃縮就是 2026：CPO Switch 開始量產。 2027～2028：逐步往 Scale-up 擴張。 2028～2030：才是真正要重新估算大型高階 CCL 面積需求的時間。

現階段 AI 架構仍處在 224G 電訊號升級 + PCB 層數增加 + PCIe Gen6 + 800G/1.6T + NVLink copper + CPO Scale-out 同時並存。

所以短中期 M8/M9、HVLP、Low-Dk/Q-glass 的需求邏輯並沒有突然被推翻。

[![Image 8](https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/817961606_17909010852513769_8726523112977323754_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzk5MDExOTkzMTc5OTY5NzY3NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQueHBpZHMuMTQ2OS5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=GLMfoZZSb9QQ7kNvwG82bda&_nc_oc=AdpyTw8ju9LsIl0Cee4bBCyifiarw_E1aZ3Og-e7UYsVf8HTlh8FDLkRKvZVTvgNgec&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJaCnT-ssPlVDmsrj5HVPnLl5qc6mHIMBXM9L5q_q-BSg&oe=6AB695CD)](https://www.threads.com/@4arcues93_/post/DdfwO_6IHkK/media)

9

1

4

[![Image 9: eric_ouo5678's profile picture](https://scontent-sea1-1.cdninstagram.com/v/t51.82787-19/735897782_18056997524592208_1378253151373501605_n.jpg?_nc_cat=101&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=n_EhVfcgy9IQ7kNvwGoVwRZ&_nc_oc=Adoy-hxfAxRVWY8l9iGgbUtvAdmkunHvTPczXc84D_Q3bKRSDgXRdTwHue-S76BYt7c&_nc_zt=24&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQLpp6bCNnHEk-8ZmqMOtDEra4V82I4QcQWKVX3yPNlbDQ&oe=6AB67CF6)](https://www.threads.com/@eric_ouo5678)

[eric_ouo5678](https://www.threads.com/@eric_ouo5678)

[20h](https://www.threads.com/@eric_ouo5678/post/DdgHauknSCB)

![Image 10: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)

蠻正確的 而且現在除了CPO之外 CSP也同步朝CPC發展 都是為了減少高速訊號在PCB中的走線距離的應用

2

[![Image 11: yjchenzn99's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.89012-19/573323465_1219825463302212_7278921664109726296_n.jpg?stp=dst-jpg_tt6&_nc_cat=1&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=r_LELBptIrYQ7kNvwF6aWa5&_nc_oc=AdrfRE8zFVL03ubUuQgWboI3vxm5HzfnSdqfUjOL6v6N81nAQcWrDYXa6jmjC-7kPRw&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQLMwoXBapPcrCDe_gI291r2pBKLBIAJ4b-_LnGDhadZtQ&oe=6AB67122)](https://www.threads.com/@yjchenzn99)

[yjchenzn99](https://www.threads.com/@yjchenzn99)

[17h](https://www.threads.com/@yjchenzn99/post/DdgbWjhkkR6)

ㄗㄢ

1

[![Image 12: forstercheng's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/579684582_17842173249618055_8179312757152811600_n.jpg?_nc_cat=110&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=CISXmjSD7aAQ7kNvwEArDHG&_nc_oc=AdqMHfSlh_BeguQFF_Pqt6h36yWm_IvUCc_DdahN1b0YxBLVyQUPfuLd_IY-y3slSik&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQI3TazqtkRkHjuak4UyCj3JROWq2i7HR2NXnCJjor64mA&oe=6AB67C71)](https://www.threads.com/@forstercheng)

[forstercheng](https://www.threads.com/@forstercheng)

[2h](https://www.threads.com/@forstercheng/post/DdiHcfemZy6)

![Image 13: A Threads user's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.75761-19/510961051_17842574745523444_8844616329824512881_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=dUhAGCsoipMQ7kNvwGFgLm1&_nc_oc=Adrmbk6Ff-xJB-9C_Ba0MwKAfE1NpoWVUIyQIWg21Ffj8MW9XZ65-pflqYLLBfDau04&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7b289&oh=00_AQJ_-tLXGXLULdJhbBYS7otXqxLJoFOWi7LyLJoMIe-xLw&oe=6AB67E13)

用量還是會成長，可能比想像中的少，因為CPO

1

Related threads

[![Image 14: shenkuei_'s profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.2885-19/357829015_1008179500549748_6419774226957305972_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEtIcH_rh1WhdJT1lSHHYwVl261LQT1NVjFwVz3zYn0qs9ymSFLd54Ok_G5-N-iVc8&_nc_ohc=sb8qcVSL200Q7kNvwHOg9vy&_nc_gid=0X1phrUzjgmO5aKH2TMElw&edm=APs17CUBAAAA&ccb=7-5&oh=00_AQK-l18HkD-o9PA-B_PkknuazK19xiaZqpb-yQQTBscDoA&oe=6AB67822&_nc_sid=10d13b)](https://www.threads.com/@shenkuei_)

[shenkuei_](https://www.threads.com/@shenkuei_)

[台股](https://www.threads.com/search?q=%E5%8F%B0%E8%82%A1&serp_type=tags&tag_id=18280855960087606)

[08/29/26](https://www.threads.com/@shenkuei_/post/Dcnte3kEZ1u)

CPO（光學共封裝）全球完整供應鏈概念股總整理 一、 EDA / IP 與 IC 設計（核心架構與通訊晶片） 美股： Broadcom (AVGO)：全球網路交換晶片（Switch ASIC）與 CPO 架構龍頭。 NVIDIA (NVDA)：主導 NVSwitch 與 AI GPU 整合 CPO 光學傳輸。 Marvell (MRVL)：高速光通訊 DSP、Driver IC 與交換晶片巨頭。 Cisco (CSCO)：矽光子架構與高階網路交換器領導廠商。 Synopsys (SNPS) / Cadence (CDNS)：提供矽光子光電集成電路（PIC）EDA 設計工具。 Credo (CRDO) / Macom (MTSI)：超高速 SERDES、Driver IC 與 TIA 晶片。 POET Technologies (POET)：專注光學引擎（Optical Engine）整合平台開發。 台股： 聯發科 (2454)：佈局客製化晶片（ASIC）與高階 CPO 傳輸架構。

Translate

[![Image 15: Art Glow GIF by dualvoidanima](https://media3.giphy.com/media/v1.Y2lkPTA1NzQyMTNjdjRtM2wxMHFzcmxsM2sxMWhzeXcxZjJ5ajJsNG03c3JkcTFhcHB3cSZlcD12MV9naWZzX2dpZklkJmN0PWc/hTP2q3u3FeSTkaRhaK/200.gif)](https://www.threads.com/@shenkuei_/post/Dcnte3kEZ1u/media)

87

5

19

[![Image 16: ccl.9999's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/793090527_17897140692599491_3283198340104825045_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEtIcH_rh1WhdJT1lSHHYwVl261LQT1NVjFwVz3zYn0qs9ymSFLd54Ok_G5-N-iVc8&_nc_ohc=IkqFRJXsEz0Q7kNvwFQINiW&_nc_gid=0X1phrUzjgmO5aKH2TMElw&edm=APs17CUBAAAA&ccb=7-5&oh=00_AQIGev-HMFUdus_Ia9h7adP6Kc38Y7zxGrRBWhljtYlAtw&oe=6AB6A0AA&_nc_sid=10d13b)](https://www.threads.com/@ccl.9999)

[ccl.9999](https://www.threads.com/@ccl.9999)

[CCL](https://www.threads.com/search?q=CCL&serp_type=tags&tag_id=18411709768032604)

[3d](https://www.threads.com/@ccl.9999/post/DdY_Vklk4IQ)

剛證實PTFE少的可憐

又來一個搞笑前外資 來看看CPO能取代的有多麼小一塊蛋糕

CPO一來，CCL全降 M4？先把分母算清楚。

Yole 的 2029 年資料顯示，Scale-out CPO 約 180 萬 ports，相較傳統 Pluggable Ethernet／InfiniBand 約 6,690 萬 ports，換算滲透率只有約 2.6%。

再看 AI 機櫃本身：中金估 VR200 NVL72 的 Switch PCB 約占整櫃 PCB value 22.3%；國信對 Rubin NVL144 CPX 的拆解則約 16–19%。

所以就算把這些 CPO Switch 整塊都算成「受材料降規影響」：

2.6% × 16–22% ≈ 0.4–0.6%。

而且這 0.4–0.6% 還不是 CCL 被取代。NVIDIA 官方定義很清楚：CPO 主要取代的是 可插拔光模組，以及 Switch ASIC 到光模組之間的高速電氣路徑；PCB 並沒有消失。

更諷刺的是，廣達那張被拿來喊「M9→M4」的圖裡，CPO Switch 自己還是 50 層、6.8mm PCB。

Translate

65

1

4

20

[![Image 17: orion__06666's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/731219811_17887096506582779_4448532474143600634_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gEtIcH_rh1WhdJT1lSHHYwVl261LQT1NVjFwVz3zYn0qs9ymSFLd54Ok_G5-N-iVc8&_nc_ohc=mq2cbtXaR8gQ7kNvwFOgqUG&_nc_gid=0X1phrUzjgmO5aKH2TMElw&edm=APs17CUBAAAA&ccb=7-5&oh=00_AQKT6PSgC0Z9xHGl38864KFzYjg-_8rq6U245JfmU8Yz2Q&oe=6AB68603&_nc_sid=10d13b)](https://www.threads.com/@orion__06666)

[orion__06666](https://www.threads.com/@orion__06666)

[2d](https://www.threads.com/@orion__06666/post/DddCTJmE7Gi)

NPO/CPO pitch變小、精度要求跳級之後，first-pass yield必然下降,良率沒過的模組需要重新對位、重新耦合,這代表耦光操作次數會超過原本的理論值,另外TSM講的CPO on Substrate vs CPO on Interposer是兩條漸進路徑,如果客戶往Interposer/CoWoS這條路線走（效能更好、10倍功耗效益）,代表耦光可能要在wafer級或CoWoS中介層級再做一次 coupler,不是模組封裝完才耦光,這等於在既有的模組級耦光之外,多出一個晶圓／中介層級耦光的新站別。

Translate

72

3

4

[![Image 18: inbloom.tech's profile picture](https://scontent-sea1-1.cdninstagram.com/v/t51.82787-19/770700834_18088530083179302_1937746750348539253_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEtIcH_rh1WhdJT1lSHHYwVl261LQT1NVjFwVz3zYn0qs9ymSFLd54Ok_G5-N-iVc8&_nc_ohc=HOLZ2GIbEUQQ7kNvwHHDya3&_nc_gid=0X1phrUzjgmO5aKH2TMElw&edm=APs17CUBAAAA&ccb=7-5&oh=00_AQL96_jqw8_p4KyJ_93WIRLw0RDBAX1rsEmCefGTdC0F4w&oe=6AB67DCC&_nc_sid=10d13b)](https://www.threads.com/@inbloom.tech)

[inbloom.tech](https://www.threads.com/@inbloom.tech)

[5d](https://www.threads.com/@inbloom.tech/post/DdTn68xj8gk)

【拆解系列：CPO（共同封裝光學）】

資料中心兩顆晶片要傳資料，銅線速度一高就衰減，訊號跑幾十公分就糊，電都燒在補訊號上。光纖不會：一根玻璃絲，光跑一公里還剩九成能量。

但電腦不會講光，所以兩端要有光模組做電光互換。模組過去插在面板上，電訊號還得在板子上爬幾十公分。就是把它搬到運算晶片旁邊，路徑縮到幾毫米。省下的電，就是省下那段路。CPO（共同封裝光學）就是把它搬到運算晶片旁邊。

Translate

5

3

2

[![Image 19: im_jasmine77777's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/759411157_18072732233475430_6816029389336346267_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zNjQuYzIifQ&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gEtIcH_rh1WhdJT1lSHHYwVl261LQT1NVjFwVz3zYn0qs9ymSFLd54Ok_G5-N-iVc8&_nc_ohc=QHV4Wxd3V8wQ7kNvwEDlHiR&_nc_gid=0X1phrUzjgmO5aKH2TMElw&edm=APs17CUBAAAA&ccb=7-5&oh=00_AQLl2d3Aelaqn8MW9fyq1CUO7WC3bmFNBLjh5HFMONb-5Q&oe=6AB685EF&_nc_sid=10d13b)](https://www.threads.com/@im_jasmine77777)

[im_jasmine77777](https://www.threads.com/@im_jasmine77777)

[4d](https://www.threads.com/@im_jasmine77777/post/DdYApr0gaoL)

CPO還沒那麼快，LightCounting甚至預估到2029年銅在1.6T還有50%share。 而且在CPO大規模替代銅前，像NVIDIA Rubin的Midplane PCB也還在44層、M9的材料。 雖然高速傳輸訊號從PCB電路轉移到封裝的光互聯，但PCB還是需要供電和低速訊號走線，所以CCL會降規，但不會降那麼多，而且是之後的事，時間點的問題，看你trade什麼時候 看起來是安餒，小弟淺淺觀點

Translate

![Image 20](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/813372209_18086266166475430_546406477230709479_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=109&ig_cache_key=Mzk4Nzk0MDA3OTY0MDUxOTAyMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTA5OC5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=9CiLVqUZ7JgQ7kNvwFZ4PM0&_nc_oc=AdpI6_z_is1Dw1uH9TeEnj2hPLwRf-VQOpsdE098RMkQk4h6nXFZXEdONjiD0hADwhY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7a22e&oh=00_AQK7MivnUEh-icIV4D6_N1iT1s6adCDKh5RwwwPRUKqiDQ&oe=6AB67E98)

![Image 21](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/813421294_18086266175475430_4564995198126581285_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzk4Nzk0MDA3ODU2Njc3MTgyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTA5OS5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=ZfyfDeupPo4Q7kNvwF-O61M&_nc_oc=AdpSP9npFEFcQioTH73wbCXMRGqDcEahtaNKT_xXeqxt0NlTo0dR85iXSjdpP8DftQM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7a22e&oh=00_AQIO8rbBSqirF_yGrtf56ENB8HC2xkYtAvp8IsjLpoBsPQ&oe=6AB6817D)

![Image 22](https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/813282401_18086266163475430_4964713557779306648_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzk4Nzk0MDA3ODYzMDQwMDA3MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6IkNBUk9VU0VMX0lURU0ueHBpZHMuMTE0Ny5zZHIucmVndWxhcl9waG90by5DMyJ9&_nc_ohc=EmOOBpqBSycQ7kNvwEE8-Fu&_nc_oc=AdpCyUY6lZnpIdOuokCDnWoi83WsMjlnEvzgYQtbyfG6WB3VzYmbiT4KO4UfmAbf4Eg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=0X1phrUzjgmO5aKH2TMElw&_nc_ss=7a22e&oh=00_AQIn7ZWFaMcUWX4aPVrjR3FherKk4ONBzMzuqdCXYwJ6Ow&oe=6AB69DD9)

[![Image 23: _77luka77_'s profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.2885-19/490477170_1019692796260855_7454712952469433247_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDUwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEtIcH_rh1WhdJT1lSHHYwVl261LQT1NVjFwVz3zYn0qs9ymSFLd54Ok_G5-N-iVc8&_nc_ohc=JCczgZX84HkQ7kNvwGoniSU&_nc_gid=0X1phrUzjgmO5aKH2TMElw&edm=APs17CUBAAAA&ccb=7-5&oh=00_AQJDjSQ4z2gmasl01bp3zcR4DN7RTNGFJjuzrIlxfTIQtQ&oe=6AB68A33&_nc_sid=10d13
```

## 相關頁面

<!-- [[]] -->