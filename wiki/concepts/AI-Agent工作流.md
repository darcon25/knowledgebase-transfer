---
tags: [concept]
sources: 2
updated: 2026-05-05
---

# AI Agent 工作流（Agentic Workflow）

AI Agent 工作流是讓 AI 從「問答工具」升級為「可自主執行任務的代理人」的架構。多個 Agent 可以分工協作，完成需要多步驟規劃、執行與監控的複雜任務。

> **白話說明**：不只是問 AI 問題，而是讓 AI 像員工一樣接受任務、拆解步驟、自動完成，你只需要在關鍵節點審核結果。

## 重點

- **單一 Agent**：在固定工作流（Skill）中自主執行多個步驟，無需每步人工指揮
- **多 Agent 協作**：多個 AI 代理人分工（如 COO Agent 指揮多個專才 Agent）
- **任務管理介面**：透過 Trello 等看板下達任務，核心 Agent 進行拆解分派，實現「遠端控制公司」的作業感
- **監控**：必須建立即時監控機制（如 Monivy），防止「無聲的故障」導致客戶流失
- **NO_REPLY 機制**：讓 Agent 判斷何時沈默，避免 Agent 之間無意義對話燒 Token

## 關鍵職位：Agent Operator

負責將商業規則轉化為 AI Pipeline、串接系統數據、並持續優化 Agent 執行結果的角色。這比單純學習 Prompt Engineering 更具長期競爭力。

## 相關連結

- [[concepts/Skill技能手冊]]
- [[concepts/MCP工具協議]]

## 來源

- [[sources/AI-Agent團隊實戰架構]]
- [[sources/Claude-Code六大核心技能]]
