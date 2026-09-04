---
tags: [topic]
updated: 2026-09-04
---

# AI 工具與工作流

非投資類的收藏清單。只做分類與一句話說明，要細節請開原始檔。

| 資料 | 一句話 | 原始檔 |
|---|---|---|
| Claude Code + Codex CLI 整合 | 在同一個終端機完成程式、生圖與自動化，減少視窗切換造成的注意力中斷 | `raw/threads_2026-05-06_ClaudeCode整合CodexCLI.md` |
| 多 Agent 組織架構 | 效率差距不在提示詞技巧，而在能否設計出讓多個 Agent 自動協作的迴圈 | `raw/threads_2026-05-07_多Agent組織架構.md` |
| AI 生圖字體控制 | 用精準提示詞控制 32 種字體風格，解決 AI 生圖文字亂碼。**完整 32 條指令見 [[設計靈感]]** | `raw/threads_2026-05-06_AI生圖字體控制.md` + `raw/shot_2026-08-31_AI生圖32種字體指令.md` |
| 🤖 2026-09-04 AI 網站評分服務 | IG 創作者 jarrenpoh 推的服務：用 AI 評估自己的網站分數，留言「檢查」索取連結。**服務名稱、評分項目與實際連結原文未說明**，這是一則互動式行銷貼文 | `raw/instagram_2026-09-04_AI網站評分服務.md` |
| Perplexity 混合運算（Hybrid Compute）| 公開資料丟雲端、敏感檔案留在 Mac 本機跑，中間有 Privacy Gate 遮罩姓名／Email／電話。**門檻：Apple silicon、macOS 15+、統一記憶體至少 24GB（建議 32GB）**。⚠️ 不是完全離線，雲端仍參與部分任務，敏感資訊偵測也可能漏判 | `raw/threads_2026-09-02_Perplexity混合運算隱私.md` |

## Claude Code 使用前該知道的 8 件事

來源 `raw/threads_2026-05-04_ClaudeCode使用前8件事.md` 原本只存到標題沒有內文，2026-08-31 用電腦 Chrome 開原貼文補齊。

> Claude Code 不是比較會寫程式的聊天機器人，而是**能讀檔、改檔、跑指令的 AI 開發助理**。

1. 新手先從 VS Code、Desktop 或 Web 開始
2. **先設定權限邊界**，刪檔、部署、推送要人工確認
3. 日常任務用 Sonnet，困難重構再用 Opus
4. 寫好 `CLAUDE.md`，讓它看懂專案規則
5. 重複流程可以整理成 Skills
6. Subagents 和 MCP 不要一開始全開
7. 提示詞要像任務規格書：先分析、再計畫、後修改
8. 先懂 Git、Branch、Commit、Diff、PR、MCP 等基本術語

> 核心不是把專案丟給 AI 放生，而是建立**可控、可檢查、可重複**的協作流程——先讓它懂規則，再讓它動手。

出處：`https://www.threads.com/@journal_of_digital_narrative/post/DX6uTKbknWz`
（原貼文另有 6 張圖卡，內容與上述 8 點相同，未另存）

## 相關連結

- [[AI-Agent工作流]]、[[Skill技能手冊]]、[[個人知識庫與第二大腦]]
