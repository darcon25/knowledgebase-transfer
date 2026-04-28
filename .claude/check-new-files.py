#!/usr/bin/env python3
import os, json

raw_dir = "/Users/mmfamily/Max KnowledgeBase/raw"
log_file = "/Users/mmfamily/Max KnowledgeBase/log.md"

try:
    log = open(log_file).read()
except Exception:
    log = ""

try:
    new = [
        f for f in os.listdir(raw_dir)
        if os.path.isfile(os.path.join(raw_dir, f))
        and not f.startswith(".")
        and f not in log
    ]
except Exception:
    new = []

if new:
    lst = "\n".join("- " + f for f in sorted(new))
    print(json.dumps({
        "systemMessage": f"📂 知識庫：發現 {len(new)} 個未消化的新檔案\n{lst}",
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": f"raw/ 目錄中有以下尚未消化的檔案：\n{lst}\n請主動詢問使用者是否要開始消化這些檔案。"
        }
    }))
