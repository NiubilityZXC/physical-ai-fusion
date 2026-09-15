#!/usr/bin/env python3
"""gen_figures.py — 论文数据图生成(F1 topic 分布;F3 baseline 若有数据)"""
import json
import glob
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 9, "figure.dpi": 200, "savefig.bbox": "tight"})

TASKS = [json.loads(l) for f in sorted(glob.glob("data/verified/*.jsonl"))
         for l in open(f, encoding="utf-8") if l.strip()]

# ---- F1: topic x type stacked bars, ICF highlighted ----
topics = sorted({t["topic"] for t in TASKS})
types = ["numeric", "concept", "derivation", "figure"]
cnt = defaultdict(Counter)
for t in TASKS:
    cnt[t["topic"]][t["type"]] += 1

fig, ax = plt.subplots(figsize=(5.2, 3.2))
colors = {"numeric": "#4C72B0", "concept": "#55A868", "derivation": "#C44E52", "figure": "#8172B3"}
left = [0] * len(topics)
for ty in types:
    vals = [cnt[tp][ty] for tp in topics]
    ax.barh(range(len(topics)), vals, left=left, color=colors[ty], label=ty, height=0.72)
    left = [l + v for l, v in zip(left, vals)]
ax.set_yticks(range(len(topics)))
labels = []
for tp in topics:
    n = sum(cnt[tp].values())
    mark = "*" if tp.startswith("icf/") else ""
    labels.append(f"{tp} ({n}){mark}")
ax.set_yticklabels(labels, fontsize=7.5)
ax.invert_yaxis()
for i, tp in enumerate(topics):
    if tp.startswith("icf/"):
        ax.get_yticklabels()[i].set_color("#1f4e9c")
        ax.get_yticklabels()[i].set_fontweight("bold")
ax.set_xlabel("verified tasks")
ax.legend(fontsize=7, ncol=4, frameon=False, loc="lower right")
icf_n = sum(v for tp in topics if tp.startswith("icf/") for v in cnt[tp].values())
ax.set_title(f"ICF subdomains: {icf_n}/{len(TASKS)} = {100*icf_n/len(TASKS):.0f}% (* bold)", fontsize=9)
fig.tight_layout()
fig.savefig("figures/fig_topic_dist.pdf")
print("figures/fig_topic_dist.pdf written")

# ---- F3: baseline per-difficulty bars (only if baseline files exist) ----
bfiles = sorted(glob.glob("results/baseline-*.jsonl"))
if bfiles:
    series = {}
    for bf in bfiles:
        model = bf.split("baseline-")[-1].rsplit(".", 1)[0]
        preds = {json.loads(l)["task_id"]: json.loads(l)["response"]
                 for l in open(bf, encoding="utf-8") if l.strip()}
        import sys
        sys.path.insert(0, "harness")
        from physical_ai_fusion.grader import grade
        by_diff = defaultdict(list)
        for t in TASKS:
            if t["task_id"] in preds and t["grading"]["mode"] in ("numeric_tolerance", "exact_match"):
                s, _ = grade(preds[t["task_id"]], t)
                by_diff[t["difficulty"]].append(s)
        series[model] = {d: (sum(v) / len(v) if v else 0) for d, v in by_diff.items()}
    diffs = ["undergrad", "grad", "expert"]
    fig, ax = plt.subplots(figsize=(4.6, 2.6))
    import numpy as np
    x = np.arange(len(diffs))
    w = 0.8 / max(len(series), 1)
    for i, (m, s) in enumerate(sorted(series.items())):
        ax.bar(x + i * w, [s.get(d, 0) for d in diffs], w, label=m)
    ax.set_xticks(x + w * (len(series) - 1) / 2)
    ax.set_xticklabels(diffs)
    ax.set_ylim(0, 1)
    ax.set_ylabel("accuracy")
    ax.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    fig.savefig("figures/fig_baseline.pdf")
    print("figures/fig_baseline.pdf written")
else:
    print("no baseline files yet; F3 skipped")
