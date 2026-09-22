#!/usr/bin/env python3
"""gen_baseline_table.py — 从 results/baseline-*.jsonl 生成论文 baseline 表与摘要
用法: python3 scripts/gen_baseline_table.py  (仓库根目录)
输出: paper/sections/baseline_table.tex + results/baseline_summary.json
"""
import glob
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "harness"))
from physical_ai_fusion.grader import grade  # noqa: E402

TASKS = [json.loads(l) for f in sorted(glob.glob(str(ROOT / "data/verified/*.jsonl")))
         for l in open(f, encoding="utf-8") if l.strip()]
DET = {"numeric_tolerance", "exact_match", "symbolic_equiv", "unit_test", "swe_patch"}

rows = {}
for bf in sorted(glob.glob(str(ROOT / "results/baseline-*.jsonl"))):
    model = Path(bf).stem.replace("baseline-", "")
    if model == "glm-5.3":
        continue
    preds = {}
    for line in open(bf, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            preds[r["task_id"]] = r.get("response", "")
    per = defaultdict(list)
    fails = defaultdict(list)
    for t in TASKS:
        if t["grading"]["mode"] not in DET:
            continue
        resp = preds.get(t["task_id"])
        if resp is None:
            continue
        s, detail = grade(resp, t)
        per["overall"].append(s)
        per[f"diff:{t['difficulty']}"].append(s)
        per[f"type:{t['type']}"].append(s)
        per[f"topic:{t['topic']}"].append(s)
        if s == 0 and len(fails[t["type"]]) < 4:
            fails[t["type"]].append((t["task_id"], detail))
    n = len(per["overall"])
    if not n:
        continue
    rows[model] = {
        "n": n,
        "overall": sum(per["overall"]) / n,
        "by_diff": {d: sum(per[f"diff:{d}"]) / len(per[f"diff:{d}"]) for d in ("undergrad", "grad", "expert") if per[f"diff:{d}"]},
        "by_type": {ty: sum(per[f"type:{ty}"]) / len(per[f"type:{ty}"]) for ty in ("numeric", "concept", "derivation", "code", "figure") if per[f"type:{ty}"]},
        "by_topic": {tp: sum(per[f"topic:{tp}"]) / len(per[f"topic:{tp}"]) for tp in sorted({t["topic"] for t in TASKS}) if per[f"topic:{tp}"]},
        "fails": {k: v for k, v in fails.items() if v},
    }

(ROOT / "results/baseline_summary.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(f"models: {list(rows)} -> results/baseline_summary.json")

def pct(x): return f"{100*x:.1f}"

lines = [r"\begin{table}[t]", r"\centering",
         r"\caption{Deterministic-task accuracy on the verified split (single attempt, temperature 0.2). $n$ = tasks answered (sweep status noted in text; read non-complete rows as preliminary).}",
         r"\label{tab:baseline}", r"\small",
         r"\begin{tabular}{@{}lccccc@{}}", r"\toprule",
         r"Model & $n$ & Overall & undergrad & grad & expert \\\\", r"\midrule"]
for m, r in sorted(rows.items(), key=lambda kv: -kv[1]["overall"]):
    lines.append(f"{m} & {r['n']} & {pct(r['overall'])}\% & "
                 f"{pct(r['by_diff'].get('undergrad',0))}\% & {pct(r['by_diff'].get('grad',0))}\% & {pct(r['by_diff'].get('expert',0))}\% \\\\")
lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
(ROOT / "paper/sections/baseline_table.tex").write_text("\n".join(lines))
print("paper/sections/baseline_table.tex written")
