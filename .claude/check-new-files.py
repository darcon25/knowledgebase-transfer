#!/usr/bin/env python3
"""SessionStart hook：掃出還沒消化的來源檔案（raw/ 與 Clippings/）。"""
import json
import os

KB = "/Users/mmfamily/Max KnowledgeBase"
SOURCE_DIRS = ["raw", "Clippings"]

# 已消化清單。log.md 只有敘述、沒有檔名，靠它比對會大量誤報，所以另存明確清單。
try:
    with open(os.path.join(KB, "data", "ingested.json"), encoding="utf-8") as fh:
        done = set(json.load(fh)["files"])
except Exception:
    done = set()

new = []
for folder in SOURCE_DIRS:
    path = os.path.join(KB, folder)
    try:
        entries = os.listdir(path)
    except Exception:
        continue
    for name in sorted(entries):
        if name.startswith(".") or not os.path.isfile(os.path.join(path, name)):
            continue
        rel = f"{folder}/{name}"
        if rel in done:
            continue
        new.append(rel)

if new:
    lst = "\n".join("- " + f for f in new)
    print(json.dumps({
        "systemMessage": f"📂 知識庫：發現 {len(new)} 個未消化的新檔案\n{lst}",
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                f"以下來源檔案尚未消化：\n{lst}\n"
                "請主動詢問使用者是否要開始消化這些檔案。"
            ),
        },
    }, ensure_ascii=False))
