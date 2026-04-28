# Knowledge Base Schema

這份文件定義了這個知識庫的結構與操作規則。每次對話開始時，LLM 應先讀取此文件。

## 目錄結構

```
Max KnowledgeBase/
├── CLAUDE.md          ← 本文件：操作規則與結構定義
├── index.md           ← 所有 wiki 頁面的目錄（每次更新後維護）
├── log.md             ← 操作紀錄（只增不減）
├── raw/               ← 原始資料來源（只讀，不可修改）
│   └── assets/        ← 本地圖片檔案
└── wiki/              ← LLM 生成與維護的知識頁面
    ├── overview.md    ← 整體知識庫的綜合摘要
    ├── entities/      ← 人物、地點、組織等實體頁面
    ├── concepts/      ← 觀念、主題、理論等概念頁面
    └── sources/       ← 每份原始資料的摘要頁面
```

## 核心原則

- `raw/` 資料夾的內容**永遠不可修改**，只能讀取
- `wiki/` 資料夾由 LLM 全權負責建立與維護
- 每次操作後必須更新 `index.md` 與 `log.md`
- Wiki 頁面之間應積極建立 `[[內部連結]]`

## 操作流程

### 一、消化新資料（Ingest）

當使用者提供新的資料來源時：

1. **閱讀**資料（可能是文字、PDF、網頁等）
2. **討論**：與使用者確認重點與關注面向
3. **建立摘要頁面**：在 `wiki/sources/` 建立 `來源標題.md`
4. **更新相關頁面**：
   - 若提到已有頁面的實體/概念 → 更新對應頁面
   - 若出現新的重要實體/概念 → 在 `wiki/entities/` 或 `wiki/concepts/` 建立新頁面
   - 若與既有知識有矛盾 → 在相關頁面標註衝突
5. **更新 `index.md`**：加入新頁面條目
6. **更新 `log.md`**：追加一筆 ingest 紀錄
7. **更新 `wiki/overview.md`**：若對整體理解有重大影響

### 二、回答問題（Query）

1. 讀取 `index.md` 找出相關頁面
2. 讀取相關頁面並整合答案
3. 附上出處（引用 wiki 頁面連結）
4. 若答案有獨立價值，可將其儲存為新的 wiki 頁面
5. 在 `log.md` 追加紀錄

### 三、健康檢查（Lint）

當使用者要求 `/lint` 時：

- 找出無連結指向的孤立頁面
- 找出有矛盾的說法
- 找出被多次提及但缺乏專屬頁面的概念
- 建議可以補充的新資料來源
- 更新 `log.md`

## 頁面格式規範

### Wiki 頁面（entities / concepts）

```markdown
---
tags: [entity|concept]
sources: [來源頁面連結數量]
updated: YYYY-MM-DD
---

# 頁面標題

一段核心摘要（2-4 句）。

## 重點

- 重點一
- 重點二

## 相關連結

- [[相關頁面 A]]
- [[相關頁面 B]]

## 來源

- [[sources/來源名稱]]
```

### 來源摘要頁面（sources/）

```markdown
---
tags: [source]
type: article|paper|book|video|podcast|other
date_ingested: YYYY-MM-DD
---

# 來源標題

**類型**：文章 / 論文 / 書籍 / 影片 / 其他  
**原始位置**：`raw/檔案名稱` 或 URL

## 摘要

（3-6 句核心內容）

## 關鍵要點

- 要點一
- 要點二

## 相關 Wiki 頁面

- [[concepts/概念名稱]]
- [[entities/實體名稱]]
```

## Log 格式

每筆紀錄格式：

```
## [YYYY-MM-DD] 操作類型 | 標題
簡短描述發生了什麼事，影響了哪些頁面。
```

操作類型：`ingest`、`query`、`lint`、`update`

---

**說明**：這份知識庫使用「LLM Wiki」架構，由 LLM 負責維護所有 wiki 內容，使用者負責提供資料來源與提問方向。
