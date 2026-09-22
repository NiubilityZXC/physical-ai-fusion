#!/usr/bin/env python3
"""fix_translations.py — 用严格 prompt 重译数字保真检查不合格的翻译题

不合格定义(与抽检脚本一致): 物理硬数字(含小数点/科学计数法/≥4位整数)
集合在 zh 与 en 中不一致(数值归一化后)。
"""
import glob
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env = json.loads((Path.home() / ".claude" / "settings.json").read_text())["env"]
KEY, BASE = env["ANTHROPIC_AUTH_TOKEN"], env["ANTHROPIC_BASE_URL"]

PROMPT = (
    "把下面的核聚变物理题面忠实翻译为英文。绝对规则(违反即错误):"
    "1) 所有数字必须逐字符保持原样,包括科学计数法写法(如 1e15、1.435e+05、8.3236e-10、2.485e6),"
    "不得改写为 '1×10^15' 或 'about 1.435' 或丢失指数;"
    "2) 公式与物理量符号保持原样(如 n_c、κ、ρR、E=½mv²);"
    "3) 只输出翻译后的题面,不要解释。\n\n题面:\n{q}"
)


def phys_nums(s):
    out = []
    for m in re.findall(r"\d+\.\d+(?:[eE][+-]?\d+)?|\d+[eE][+-]?\d+|\d{4,}", s):
        try:
            out.append(round(float(m), 6))
        except ValueError:
            pass
    return sorted(out)


def chat(model, prompt, timeout=90):
    body = json.dumps({"model": model, "max_tokens": 2048,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(BASE.rstrip("/") + "/v1/messages", data=body,
                                 headers={"Content-Type": "application/json", "x-api-key": KEY,
                                          "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    return "".join(c.get("text", "") for c in d.get("content", [])).strip()


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "doubao-seed-2-1-turbo"
    fixed = failed = 0
    for f in sorted(glob.glob(str(ROOT / "data/en/*.jsonl"))):
        lines = [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
        changed = False
        for t in lines:
            if "question_en" not in t:
                continue
            if phys_nums(t["question"]) == phys_nums(t["question_en"]):
                continue
            for attempt in range(3):
                try:
                    t["question_en"] = chat(model, PROMPT.format(q=t["question"]))
                    if phys_nums(t["question"]) == phys_nums(t["question_en"]):
                        fixed += 1
                        changed = True
                        break
                except Exception as e:
                    print(f"  {t['task_id']} attempt {attempt+1}: {type(e).__name__}", flush=True)
                    time.sleep(5 * (attempt + 1))
            else:
                failed += 1
                print(f"  STILL BAD: {t['task_id']}", flush=True)
        if changed:
            open(f, "w", encoding="utf-8").write(
                "\n".join(json.dumps(t, ensure_ascii=False) for t in lines) + "\n")
    print(f"re-translated OK: {fixed}, still failing: {failed}")


if __name__ == "__main__":
    main()
