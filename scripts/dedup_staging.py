#!/usr/bin/env python3
"""dedup_staging.py — staging 去重与 task_id 冲突修复
规则:
  1. 完全相同的 question 只保留首次出现
  2. task_id 冲突时,后者在同前缀下重新编号(追加到该前缀最大空闲序号)
用法: python3 scripts/dedup_staging.py  (原地修改,先自动备份到 .aris/dedup-backup/)
"""
import glob
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKUP = ROOT / ".aris" / "dedup-backup"
BACKUP.mkdir(parents=True, exist_ok=True)

files = sorted(glob.glob(str(ROOT / "data/staging/*.jsonl")))
seen_q: dict[str, str] = {}
used_ids: set[str] = set()
max_seq: dict[str, int] = {}

removed = 0
renumbered = 0

for f in files:
    p = Path(f)
    shutil.copy2(p, BACKUP / p.name)
    out_lines = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        t = json.loads(line)
        q = t["question"]
        if q in seen_q:
            removed += 1
            continue
        tid = t["task_id"]
        if tid in used_ids:
            m = re.match(r"^(.*?)(\d+)$", tid)
            prefix = m.group(1)
            n = max(max_seq.get(prefix, 0), int(m.group(2)))
            while f"{prefix}{n:04d}" in used_ids or f"{prefix}{n}" in used_ids:
                n += 1
            new_id = f"{prefix}{n:04d}"
            t["task_id"] = new_id
            max_seq[prefix] = n
            renumbered += 1
            tid = new_id
        else:
            m = re.match(r"^(.*?)(\d+)$", tid)
            if m:
                max_seq[m.group(1)] = max(max_seq.get(m.group(1), 0), int(m.group(2)))
        seen_q[q] = tid
        used_ids.add(tid)
        out_lines.append(json.dumps(t, ensure_ascii=False))
    p.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

print(f"removed {removed} duplicate questions; renumbered {renumbered} task_id collisions")
print(f"backup at {BACKUP}")
