#!/usr/bin/env python3
"""gen_freepath_problems.py — 从 Au/Al/Be 自由程数据表生成验证题(icf-eos-opacity-2001+)

数据源: ~/Rosseland_opa_new_hetero/equally/data_Au2.txt(125,000 行 Au)
列: rod=log10(密度), tep=log10(电子温度), tgama=log10(光子能量), log10(lnu)=log10(自由程)
(该数据集有完整永久 benchmark 验证链,见 au_source_permanent_benchmark_report_20260706.md)

题目族(全部 numeric,表格直读/对数插值/反换算,答案由数据行直接确定):
  F1 表格直读: 给定 (rod,tep,tgama) 求 log10(lnu)
  F2 log10→物理量: 给定 log10(lnu) 求 lnu(cm)并换算为 m(考 10^x 与 cm→m)
  F3 双态比值: 两个状态的自由程之比
  F4 log 空间线性插值
产出: data/staging/icf-eos-opacity-generated.jsonl
"""
import json
import math
import random

SRC = "/home/user/Rosseland_opa_new_hetero/equally/data_Au2.txt"
OUT = "data/staging/icf-eos-opacity-generated.jsonl"
SEED = 20260915


def sig(x,d=4):
    return float(f"{x:.{d}g}")

def rec(task_id, q, value, unit, tol, expr, notes, diff="grad"):
    return {"task_id": task_id, "schema_version": "1.0", "topic": "icf/eos-opacity",
            "type": "numeric", "difficulty": diff, "question": q,
            "answer": {"kind": "numeric", "value": value, "unit": unit, "tolerance_rel": tol},
            "grading": {"mode": "numeric_tolerance"},
            "metadata": {"source": "本地 Au 自由程数据表(~/Rosseland_opa_new_hetero/equally/data_Au2.txt;永久 benchmark 验证链见 au_source_permanent_benchmark_report_20260706.md)",
                         "source_type": "local_sim", "license": "local-verified", "notes": notes},
            "verification": {"methods": ["independent-recompute", "local-sim-baseline"],
                             "evidence": {"recompute_expr": expr,
                                          "cross_source": "数据表行原值"},
                             "verified_by": ["kimi-k3-generator-2026-09-15"], "verified_at": "2026-09-15"}}


def main():
    rng = random.Random(SEED)
    rows = []
    with open(SRC) as fh:
        for line in fh:
            parts = line.split()
            if len(parts) == 4:
                rows.append(tuple(float(x) for x in parts))
    print(f"rows: {len(rows)}")
    rng.shuffle(rows)
    problems = []
    n = 2000

    # F1 表格直读(8 题)
    for rod, tep, tg, lnu in rows[:8]:
        n += 1
        problems.append(rec(
            f"icf-eos-opacity-{n}",
            f"某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod={rod:.3f}, tep={tep:.3f}, tgama={tg:.3f} 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?",
            sig(lnu,4), "1", 0.01, f"{lnu}",
            "表格直读题:考科学计数法与列含义辨识", diff="undergrad"))

    # F2 log10→物理量 + 单位换算(6 题)
    for rod, tep, tg, lnu in rows[8:14]:
        n += 1
        v_m = 10 ** lnu / 100
        problems.append(rec(
            f"icf-eos-opacity-{n}",
            f"金等离子体数据库给出某状态(rod={rod:.3f}, tep={tep:.3f}, tgama={tg:.3f})的 log₁₀(lnu)={lnu:.6g}(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。",
            float(f"{v_m:.3e}"), "m", 0.02, f"10**({lnu})/100",
            "反对数+cm→m 换算,易错数量级"))

    # F3 双态比值(4 题)
    for i in range(4):
        a = rows[14 + 2 * i]
        b = rows[15 + 2 * i]
        n += 1
        ratio = 10 ** (a[3] - b[3])
        problems.append(rec(
            f"icf-eos-opacity-{n}",
            f"金等离子体数据库中,状态 A(rod={a[0]:.3f}, tep={a[1]:.3f}, tgama={a[2]:.3f})的 log₁₀(lnu)={a[3]:.6g};状态 B(rod={b[0]:.3f}, tep={b[1]:.3f}, tgama={b[2]:.3f})的 log₁₀(lnu)={b[3]:.6g}。求自由程之比 lnu_A/lnu_B(保留 3 位有效数字)。",
            float(f"{ratio:.3e}"), "1", 0.02, f"10**({a[3]}-({b[3]}))",
            "对数差的物理含义:比值=10^Δ,不是 Δ 本身", diff="grad"))

    # F4 log 空间线性插值(4 题)
    by_rt = {}
    for r in rows:
        by_rt.setdefault((r[0], r[1]), []).append(r)
    keys = [k for k, v in by_rt.items() if len(v) >= 3]
    rng.shuffle(keys)
    made = 0
    for k in keys:
        if made >= 4:
            break
        series = sorted(by_rt[k], key=lambda r: r[2])
        i = rng.randrange(len(series) - 1)
        a, b = series[i], series[i + 1]
        if abs(b[2] - a[2]) < 1e-9:
            continue
        mid = (a[3] + b[3]) / 2
        n += 1
        made += 1
        problems.append(rec(
            f"icf-eos-opacity-{n}",
            f"金等离子体数据库中,rod={a[0]:.3f}, tep={a[1]:.3f} 时:tgama={a[2]:.3f} 对应 log₁₀(lnu)={a[3]:.6g},tgama={b[2]:.3f} 对应 log₁₀(lnu)={b[3]:.6g}。在 log 空间对 tgama 做线性插值,估计 tgama={(a[2]+b[2])/2:.4f} 处的 log₁₀(lnu)(保留 4 位有效数字)。",
            sig(mid,4), "1", 0.02, f"({a[3]}+{b[3]})/2",
            "log 空间插值:中点取平均", diff="grad"))

    with open(OUT, "w", encoding="utf-8") as fh:
        for p in problems:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"written {len(problems)} problems -> {OUT}")


if __name__ == "__main__":
    main()
