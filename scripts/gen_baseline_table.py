#!/usr/bin/env python3
"""gen_baseline_table.py — 从 results/baseline-*.jsonl 生成论文 baseline 表(T3)与图(F3 数据)
用法: python3 scripts/gen_baseline_table.py  (在仓库根目录运行)
输出: paper/sections/baseline_table.tex + results/baseline_summary.md
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
DETERMINISTIC = {"numeric_tolerance", "exact_match"}

rows = {}
for bf in sorted(glob.glob(str(ROOT / "results/baseline-*.jsonl"))):
    model = Path(bf).stem.replace("baseline-", "")
    preds = {}
    for line in open(bf, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            preds[r["task_id"]] = r.get("response", "")
    per = defaultdict(list)
    fails = defaultdict(list)
    for t in TASKS:
        if t["grading"]["mode"] not in DETERMINISTIC:
            continue
        resp = preds.get(t["task_id"])
        if resp is None:
            continue
        s, detail = grade(resp, t)
        per["overall"].append(s)
        per[f"topic:{t['topic']}"].append(s)
        per[f"diff:{t['difficulty']}"].append(s)
        per[f"type:{t['type']}"].append(s)
        if s == 0:
            fails[t["type"]].append((t["task_id"], detail))
    rows[model] = {
        "overall": sum(per["overall"]) / len(per["overall"]) if per["overall"] else 0.0,
        "n": len(per["overall"]),
        "by_diff": {d: sum(per[f"diff:{d}"]) / len(per[f"diff:{d}"]) for d in ("undergrad", "grad", "expert") if per[f"diff:{d}"]},
        "by_type": {ty: sum(per[f"type:{ty}"]) / len(per[f"type:{ty}"]) for ty in ("numeric", "concept", "figure") if per[f"type:{ty}"]},
        "by_topic": {tp: sum(per[f"topic:{tp}"]) / len(per[f"topic:{tp}"]) for tp in sorted({t["topic"] for t in TASKS}) if per[f"topic:{tp}"]},
        "fail_examples": dict(fails),
    }

out = ROOT / "results/baseline_summary.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(f"models: {list(rows)} -> {out}")

# LaTeX 主表(T3)
lines = [r"\begin{table}[t]", r"\centering",
         r"\caption{Deterministic-task accuracy on the verified split (93 numeric+concept+figure tasks; derivation tasks judged separately).}",
         r"\label{tab:baseline}", r"\small",
         r"\begin{tabular}{@{}lccccc@{}}", r"\toprule",
         r"Model & Overall & undergrad & grad & expert & numeric/concept \\", r"\midrule"]
for m, r in sorted(rows.items(), key=lambda kv: -kv[1]["overall"]):
    def pct(x): return f"{100*x:.1f}"
    lines.append(f"{m} & {pct(r['overall'])} & "
                 f"{pct(r['by_diff'].get('undergrad',0))} & {pct(r['by_diff'].get('grad',0))} & {pct(r['by_diff'].get('expert',0))} & "
                 f"{pct(r['by_type'].get('numeric',0))}/{pct(r['by_type'].get('concept',0))} \\")
lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
(ROOT / "paper/sections/baseline_table.tex").write_text("\n".join(lines))
print("paper/sections/baseline_table.tex written")
