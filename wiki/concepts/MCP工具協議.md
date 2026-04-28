---
tags: [concept]
sources: 1
updated: 2026-04-27
---

# MCP（Model Context Protocol，模型情境協議）

MCP 是一組封裝好的工具包，讓 Claude Code 能與特定的外部服務或網站互換資訊。透過 MCP，Claude 可以上網搜尋、讀取第三方平台資料（如 Reddit 貼文），或執行其他超出對話框能力的操作。

> **白話說明**：MCP 就像是幫 Claude 裝上各種「插件」，讓它能做更多事，例如幫你去 Reddit 上抓最新文章。

## 重點

- MCP 讓 Claude Code 突破對話框限制，直接與外部平台溝通
- 可透過 Claude Code 搜尋並安裝所需的 MCP
- 安裝後可在 Claude Code 介面確認已載入的 MCP 清單
- 不同 MCP 對應不同服務（如 Reddit MCP、網頁搜尋 MCP 等）

## 與 Skill 的關係

MCP 提供工具能力，[[concepts/Skill技能手冊]] 負責定義使用這些工具的步驟流程。兩者搭配可實現複雜的自動化工作流。

## 相關連結

- [[concepts/Skill技能手冊]]
- [[concepts/個人知識庫與第二大腦]]

## 來源

- [[sources/重複的例行工作讓Claude幫你打包成一個Skill-EP26]]
