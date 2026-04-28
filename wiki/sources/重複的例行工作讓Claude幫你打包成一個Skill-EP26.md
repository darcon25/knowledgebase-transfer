---
tags: [source]
type: video
date_ingested: 2026-04-27
---

# 重複的例行工作，讓 Claude 幫你打包成一個 Skill｜EP.26

**類型**：YouTube 影片  
**原始位置**：`raw/重複的例行工作，讓 Claude 幫你打包成一個 Skill｜EP.26.md`  
**來源頻道**：AgentCrew Academy  
**發布日期**：2026-04-22  
**影片連結**：https://www.youtube.com/watch?v=qH5urefmSyk

## 摘要

本影片由講師 Dustin 示範如何將已跑通的 Claude Code 工作流打包成一個「Skill（技能手冊）」。Skill 是一份封裝好的 Markdown 提示詞文件（skill.md），讓 Claude 讀懂後可按固定步驟自動執行。示範工作流為：透過 MCP 抓取 Reddit 文章 → 查詢個人知識庫擬草稿 → 去 AI 味 → 置入部落格連結 → 輸出到剪貼簿。完成一次手動流程後，只需告訴 Claude「把這個 session 的工作流包成 Skill」，未來打一個斜線指令即可全程自動執行。

## 關鍵要點

- Skill = 一份給 AI 讀的 Markdown 工作手冊（skill.md），非給人讀
- Skill 可手動觸發（打斜線指令）或由模型判斷自動觸發
- 主檔可建立索引連到副檔，實現「按需載入」
- 不需要寫任何程式碼：先手把手帶 Claude 跑一遍，再請它打包成 Skill
- MCP（Model Context Protocol）是讓 Claude 與外部服務互通的封裝工具包
- 個人知識庫（第二大腦）可作為 Claude 的查詢來源，產出符合個人風格的內容
- 發文最後一步保留人工操作，以避免被平台視為垃圾訊息

## 示範工作流步驟

1. 透過 Reddit MCP 批次抓取近期貼文（30-50 篇）
2. 讓 Claude 篩選值得回覆的 3 篇
3. 查詢個人知識庫，擬定符合教學風格的英文草稿
4. 使用「去 AI 味」Skill 重寫，使文字更自然
5. 查詢部落格文章索引，置入相關連結
6. 輸出最終草稿並複製至剪貼簿，人工貼上回覆

## 相關 Wiki 頁面

- [[concepts/Skill技能手冊]]
- [[concepts/MCP工具協議]]
- [[concepts/個人知識庫與第二大腦]]
- [[entities/AgentCrew Academy]]
