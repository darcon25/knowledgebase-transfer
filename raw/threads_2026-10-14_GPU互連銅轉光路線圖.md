---
tags:
  - source
  - social_media
  - threads
type: social_media
platform: threads
date_captured: 2026-10-14
original_url: "https://www.threads.com/share/BBKX42RFhR"
original_id: 2d99wa6q
media_count: 0
---

# 🧵 2026-10-14 存檔

> 原文：[查看貼文](https://www.threads.com/share/BBKX42RFhR)

## 摘要
這篇貼文深入探討了在高速運算環境中，GPU互連技術從銅線轉向光纖的趨勢，特別是在Scale-up（機櫃內）和Scale-out（跨機櫃）兩種情境下的應用。貼文指出隨著傳輸速度的提升，銅線面臨距離限制和訊號衰減的挑戰，促使CPO/NPO等光學技術的導入，並預測了NVIDIA未來幾代產品在光纖應用上的演進。

## 重點整理
*   **Scale-up與Scale-out的互連差異：** Scale-up（機櫃內）追求極高頻寬、極低延遲，目前仍以銅線NVLink為主；Scale-out（跨機櫃）因距離長，已率先導入光纖技術（如CPO/NPO）。
*   **銅線的物理限制：** 隨著傳輸速度（如200G/通道到400G/通道）的提升，銅線的有效傳輸距離急劇縮短，且在高頻下訊號衰減嚴重，使其在未來高速互連中面臨瓶頸。
*   **CPO/NPO的導入時機：** CPO/NPO（共同封裝光學/近引擎光學）技術最先應用於跨機櫃的Scale-out情境，例如NVIDIA的Quantum-X和Spectrum-X交換器。
*   **NVIDIA未來產品的光纖演進：** 預計NVIDIA的Rubin Ultra NVL576（2027）將開始在機櫃內導入光纖，而Feynman NVL1152（2028）則會實現NVSwitch的CPO共封裝。
*   **光纖連接的複雜性：** 即使光纖解決了距離和速度問題，但大規模叢集（如Tomahawk 7串聯1,024顆晶片需131,072根光纖）的連接複雜度仍是一大挑戰。

## 關鍵概念
*   **CPO (Co-Packaged Optics)：** 共同封裝光學，將光學元件與電子晶片（如交換器ASIC）封裝在同一模組中，以縮短電氣傳輸距離，降低功耗和延遲。
*   **NPO (Near-Packaged Optics)：** 近引擎光學，光學元件與電子晶片緊密排列在同一基板上，但未完全共封裝。
*   **Scale-up：** 指在單一系統或機櫃內，透過高速互連（如NVLink）擴展運算能力，通常追求極致的頻寬和低延遲。
*   **Scale-out：** 指透過網路將多個獨立系統或機櫃連接起來，形成更大的運算叢集，通常涉及較長的傳輸距離。
*   **NVLink：** NVIDIA開發的高速互連技術，用於GPU之間以及GPU與CPU之間的直接連接，提供高頻寬和低延遲。
*   **Rubin NVL72/144, Rubin Ultra NVL576, Feynman NVL1152：** NVIDIA未來幾代GPU架構和相關互連技術的代號，反映了其在高速運算領域的技術路線圖。
*   **Tomahawk 7：** Broadcom的高速乙太網路交換器晶片系列，常用於資料中心和AI叢集。

## 可行動洞察
*   **關注光學技術發展：** CPO/NPO是未來高速互連的關鍵趨勢，應持續關注其技術成熟度、成本效益及標準化進程，這對資料中心、AI基礎設施的規劃至關重要。
*   **評估現有基礎設施的銅線瓶頸：** 對於需要高速互連的應用，應評估現有銅線基礎設施在未來升級時可能遇到的頻寬和距離限制，提前規劃光纖導入方案。
*   **理解NVIDIA的技術路線圖：** NVIDIA在AI硬體領域的領導地位使其技術路線圖具有指標意義。了解其在光纖互連上的規劃，有助於預測未來AI伺服器和資料中心的發展方向。
*   **考慮部署和維護的複雜性：** 儘管光纖解決了速度和距離問題，但大規模光纖部署的複雜性（如連接、管理、故障排除）仍需仔細規劃，這可能需要新的工具和專業知識。
*   **探索不同互連方案的平衡：** 在設計高性能運算系統時，需要權衡Scale-up和Scale-out的需求，並在銅線和光纖之間找到最佳的成本、性能和部署複雜度平衡點。

## 原文（Jina Reader）

```
Title: 股溜股溜 (@guliuguliu__888) on Threads

URL Source: https://www.threads.com/share/BBKX42RFhR

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

# [Thread](https://www.threads.com/@guliuguliu__888/post/DeeafC6k9ck?xmt=AQG0YUj1miv606Z0ns-EqzsvOklEuP4WMLiUfdAe_dlbOMEK9Gy9qc4zqOpFyUICaVxNk6El&slof=1)

849 views

[![Image 1: guliuguliu__888's profile picture](https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/722447623_18067845926419033_7265718511565988568_n.jpg?_nc_cat=109&ccb=7-5&_nc_sid=30ff31&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=YcV0B81WgP0Q7kNvwGU9Kmq&_nc_oc=AdoZcpbkR0gYAPPud7RJE3Uk3x4v_nseEz69ExPta5tfUtU-poQWrnOK_lzytnQ0o8A&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=13pefKpDxfOLQEyf7aWzNg&_nc_ss=7b289&oh=00_AQMWKfTJ0AnP7BN2klKdRNsrsmYAlDopHxYCYeEChHeLyg&oe=6AD57530)](https://www.threads.com/@guliuguliu__888)

[guliuguliu__888](https://www.threads.com/@guliuguliu__888)

[CPO](https://www.threads.com/search?q=CPO&serp_type=tags&tag_id=18359774869109170)

[2h](https://www.threads.com/@guliuguliu__888/post/DeeafC6k9ck)

Scale-up（機櫃內）：同一櫃 GPU 高速互連，像一台超級電腦，要極高頻寬、極低延遲。目前 Rubin NVL72 櫃內 NVLink 仍然是全銅 Scale-out（跨機櫃）：多個機櫃串成更大叢集，距離長，本來就用光纖。CPO／NPO 最先導入的就是這裡，例如 NVIDIA Quantum-X、Spectrum-X 交換器 1. 銅線撞牆：速度越快，傳得越短 200G／通道約 2.5 公尺，到 400G／通道再減半 在 112GHz 下，銅線每英吋插損逼近 -10dB，448G 銅線被視為不可另外，Tomahawk 7 如果要串 1,024 顆晶片，需要 131,072 根光纖 光是想到要接這麼多條線，頭就痛了😨 2. 機櫃跳級：NVL72 → NVL576 → NVL1152 Rubin NVL72／144（2026）：機櫃內全銅 Rubin Ultra NVL576（2027）：8 座機櫃，櫃內開始走光 Feynman NVL1152（2028）：NVSwitch 共封裝 CPO

2

1

1

3

Log in or sign up for Threads See what people are talking about and join the conversation.[Log in with username instead](https://www.threads.com/login?show_choice_screen=false)

*   © 2026
*   [Threads Terms](https://help.instagram.com/769983657850450)
*   [Privacy Policy](https://help.instagram.com/515230437301944)
*   [Cookies Policy](https://help.instagram.com/1896641480634370/)
*   Report a problem

```

## 相關頁面

<!-- [[]] -->