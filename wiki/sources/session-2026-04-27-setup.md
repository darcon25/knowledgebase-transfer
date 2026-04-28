---
tags: [source]
type: session-log
date_ingested: 2026-04-27
---

# 知識庫建置 Session — 2026-04-27

**類型**：對話紀錄  
**目的**：建立個人 LLM Wiki 知識庫架構並自動化操作流程

---

## 背景

使用者提供了「LLM Wiki」設計模式文件，描述一種以 LLM 持續維護 Markdown 知識庫的架構概念。目標是在 Obsidian 中建立一個由 Claude 自動維護的個人知識庫。

---

## 本次完成的事項

### 1. 建立知識庫架構

在 `/Users/mmfamily/Max KnowledgeBase/` 建立以下結構：

```
Max KnowledgeBase/
├── CLAUDE.md                        ← LLM 操作規則（schema）
├── index.md                         ← 所有 wiki 頁面的目錄
├── log.md                           ← 操作紀錄（只增不減）
├── raw/                             ← 原始資料來源（只讀）
│   └── assets/                      ← 本地圖片
└── wiki/                            ← LLM 生成的知識頁面
    ├── overview.md                  ← 整體綜合摘要
    ├── entities/                    ← 人物、地點、組織
    ├── concepts/                    ← 觀念、主題、理論
    └── sources/                     ← 每份資料的摘要頁面
```

### 2. 釐清兩個常見誤解

- **CLAUDE.md 不需要手動載入**：Claude Code 在專案目錄中會自動讀取 `CLAUDE.md`，無需每次說「請先讀取 CLAUDE.md」。
- **`/ingest` 指令可以簡化**：使用者原本需要手動輸入完整路徑，可以透過 hook 或 skill 自動化。

### 3. 設定 SessionStart Hook（自動掃描新檔案）

建立以下兩個檔案：

**`.claude/check-new-files.py`**
- 掃描 `raw/` 目錄中所有檔案（排除隱藏檔與 `assets/` 子目錄）
- 與 `log.md` 比對，找出尚未被消化的新檔案
- 若有新檔案，輸出 JSON 通知使用者，並注入 `additionalContext` 讓 Claude 主動詢問

**`.claude/settings.json`**
- 設定 `SessionStart` hook，每次開啟 Claude Code 時自動執行掃描腳本

---

## 核心概念摘要（LLM Wiki 架構）

| 層次 | 內容 | 誰負責 |
|------|------|--------|
| Raw Sources | 原始文章、PDF、筆記 | 使用者提供 |
| Wiki | Markdown 知識頁面，互相連結 | LLM 建立與維護 |
| Schema (CLAUDE.md) | 操作規則與格式定義 | 使用者與 LLM 共同演化 |

**三種操作：**
- **Ingest**：消化新資料 → 建立摘要、更新相關頁面、更新 index 與 log
- **Query**：回答問題 → 讀取 wiki 頁面、整合答案、好答案可存回 wiki
- **Lint**：健康檢查 → 找孤立頁面、矛盾、缺失概念

---

## 下一步建議

1. 重新啟動 Claude Code 讓 hook 生效
2. 把第一份資料放進 `raw/` 測試完整消化流程
3. 安裝 Obsidian Web Clipper 瀏覽器擴充套件，方便快速收集網路文章
