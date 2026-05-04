# 知識庫概覽

> 這份頁面由 LLM 維護，綜合整個知識庫目前的核心內容與主要脈絡。

**建立日期**：2026-04-27  
**最後更新**：2026-05-05  
**資料來源數量**：10  
**Wiki 頁面數量**：17

---

## 主要主題

知識庫目前涵蓋三個核心主題群：

1. **Claude Code 工作流自動化**：Skill、MCP、個人知識庫的應用方法
2. **AI 工具生態**：Claude Design、ChatGPT 應用、AI Agent 團隊架構
3. **學習與知識管理**：75分雜學家策略、以產出促進學習

## 核心洞見

- **Skill 是工作流自動化的核心單元**：將已跑通的工作流封裝成 skill.md，未來只需一個斜線指令即可重現
- **不需要寫程式**：先手動帶 Claude 跑一遍，再讓 Claude 自己打包成 Skill
- **個人知識庫 × AI = 個人化輸出**：Karpathy 方法——本地資料夾 + Claude Code，不需 RAG，可節省最高 95% token
- **AI Agent 是下一階段**：從「問答」→「Skill 自動化」→「多 Agent 協作團隊」，Agent Operator 成為新型關鍵職位
- **大廠整合吃掉小工具**：Claude 正在從文字擴展到設計（Claude Design），單功能套殼工具生存空間縮小

## 知識地圖

```
Claude Code 工作流自動化
    ├─ Skill（技能手冊）
    │    ├─ Skill Creator / Superpowers / GSD / Ultrareview / Claude Mem
    │    └─ 手動示範後讓 Claude 自動打包
    ├─ MCP（工具協議）
    │    └─ 對接外部服務（Reddit、Google Drive 等）
    └─ 個人知識庫（第二大腦）
         └─ Karpathy 方法：本地資料夾 + Claude Code

AI 工具生態
    ├─ Claude Design（AI 設計 + PPTX 匯出）
    ├─ AI Agent 工作流
    │    ├─ 任務看板（Trello）指揮
    │    ├─ Agent Operator 職位
    │    └─ NO_REPLY 機制
    └─ ChatGPT 財經分析師應用

平台與資源
    ├─ AgentCrew Academy（Dustin 講師）
    └─ Google 2026 數位人才探索計畫（免費，截止 2026/8/10）
```

## 知識缺口

- MCP 的安裝步驟尚無詳細頁面
- Claude Cowork（桌面代理）的具體使用方法未收錄
- Cloudflare AI 邊緣運算（Workers、R2）尚無專屬頁面
- AgentCrew 其他集數尚未 ingest
