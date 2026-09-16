#!/usr/bin/env python3
"""gen_opacity_problems.py — 从 SNOP Rosseland 自由程黄金表生成 eos-opacity 数据题

数据源(用户确认的黄金表,见 element_free_path_reference_manifest.json):
  ~/Rosseland_opa_new_hetero/equally/data_{Be,Al,Au2}.txt,各 125000 行
  列: log10(ρ[g/cm³]), log10(T[eV]), log10(hν[eV]), lnu(平均自由程,cm)
  50 点对数网格: coord = 10**(log10(low)+(log10(high)-log10(low))*idx/50), idx=1..50
    rod(密度) 0.01-30000 g/cm³; tep(温度) 50-200000 eV; tgama(光子能量) 50-30000 eV
验证: 网格公式独立重建坐标 + 表中 lnu 原值 → recompute 与答案一致(容差 2%,
  黄金表自身精度 5e-6,见 manifest)。

题型:
  F1 不透明度: 给 (元素,ρ,T,hν,lnu) 求 κ=1/(ρ·lnu) [cm²/g]
  F2 网格坐标: 给轴与索引,求对数网格坐标值
  F3 自由程判读: 给 (ρ,T,hν) 与该行 lnu,问该工况辐射输运处于什么状态(薄/厚判定,给光学深度)
  F4 双点比较: 同材料两个温度点的 lnu 比值 → κ 比值
用法: python3 scripts/gen_opacity_problems.py > data/staging/eos-opacity-gen.jsonl
"""
import json
import math
import random

BASE = "/home/user/Rosseland_opa_new_hetero/equally"
FILES = {"Be": "data_Be.txt", "Al": "data_Al.txt", "Au": "data_Au2.txt"}
ZOF = {"Be": 4, "Al": 13, "Au": 79}
GRID = {"rod": (0.01, 30000.0), "tep": (50.0, 200000.0), "tgama": (50.0, 30000.0)}
SEED = 20260915


def gridval(axis, idx):
    low, high = GRID[axis]
    return 10 ** (math.log10(low) + (math.log10(high) - math.log10(low)) * idx / 50)


def read_table(sym):
    rows = []
    for line in open(f"{BASE}/{FILES[sym]}", encoding="utf-8", errors="ignore"):
        p = line.split()
        if len(p) >= 4:
            try:
                rows.append((float(p[0]), float(p[1]), float(p[2]), float(p[3])))
            except ValueError:
                continue
    return rows


def rec(tid, diff, q, value, unit, tol, expr, notes, srctype="local_sim", methods=None):
    return {"task_id": tid, "schema_version": "1.0", "topic": "icf/eos-opacity",
            "type": "numeric", "difficulty": diff, "question": q,
            "answer": {"kind": "numeric", "value": value, "unit": unit, "tolerance_rel": tol},
            "grading": {"mode": "numeric_tolerance"},
            "metadata": {"source": "本地 SNOP Rosseland 自由程黄金表(用户确认;~/Rosseland_opa_new_hetero/equally,可复现性门禁 ELEMENT_FREE_PATH_REPRODUCIBILITY.md)",
                         "source_type": srctype, "license": "local-verified", "notes": notes},
            "verification": {"methods": methods or ["independent-recompute", "local-sim-baseline"],
                             "evidence": {"recompute_expr": expr},
                             "verified_by": ["gen_opacity_problems.py+verify_numeric.py"], "verified_at": "2026-09-15"}}


def main():
    rng = random.Random(SEED)
    tables = {s: read_table(s) for s in FILES}
    problems = []
    n = 3000

    # F1: κ = 1/(ρ·lnu) — 每元素 6 题
    for sym in ("Be", "Al", "Au"):
        cand = [r for r in tables[sym] if r[3] > 1e-6]
        for r in rng.sample(cand, 6):
            lr, lt, lg, lnu = r
            rho, T, hv = 10 ** lr, 10 ** lt, 10 ** lg
            kappa = 1 / (rho * lnu)
            if not (1e-3 < kappa < 1e9):
                continue
            n += 1
            problems.append(rec(
                f"icf-eos-opacity-{n}", "grad",
                f"SNOP 模型给出 {sym}(Z={ZOF[sym]})在 ρ={rho:.4g} g/cm³、T={T:.4g} eV、光子能量 hν={hv:.4g} eV 处的 Rosseland 自由程 l={lnu:.6g} cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。",
                float(f"{kappa:.5g}"), "cm^2/g", 0.02,
                f"1/({rho:.6g}*{lnu})",
                f"黄金表行(logρ={lr},logT={lt},loghν={lg},lnu={lnu})"))

    # F2: 网格坐标 — 6 题
    axes = [("rod", "密度 ρ", "g/cm³"), ("tep", "温度 T", "eV"), ("tgama", "光子能量 hν", "eV")]
    for ax, name, unit in axes:
        for _ in range(2):
            idx = rng.randint(5, 45)
            v = gridval(ax, idx)
            low, high = GRID[ax]
            n += 1
            problems.append(rec(
                f"icf-eos-opacity-{n}", "undergrad",
                f"某不透明度表在 {name} 轴上取 50 点对数网格:coord=10^(log10({low})+(log10({high})-log10({low}))·i/50),i=1..50。求 i={idx} 处的坐标值({unit})。",
                float(f"{v:.5g}"), unit, 0.02,
                f"10**(log10({low})+(log10({high})-log10({low}))*{idx}/50)",
                "网格公式(见 manifest)", srctype="textbook",
                methods=["independent-recompute"]))

    # F3: 光学深度判定 — 6 题
    for sym in ("Al", "Au"):
        cand = [r for r in tables[sym] if r[3] > 1e-6]
        for r in rng.sample(cand, 3):
            lr, lt, lg, lnu = r
            rho, T, hv = 10 ** lr, 10 ** lt, 10 ** lg
            L = rng.choice([0.001, 0.01, 0.1])
            tau = L / lnu
            n += 1
            problems.append(rec(
                f"icf-eos-opacity-{n}", "grad",
                f"{sym} 等离子体 ρ={rho:.4g} g/cm³、T={T:.4g} eV,对 hν={hv:.4g} eV 光子的自由程 l={lnu:.6g} cm。求厚度 L={L} cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。",
                float(f"{tau:.5g}"), "1", 0.02,
                f"{L}/{lnu}",
                "光学深度定义;判定写进 notes(τ>1 为厚)" if tau > 1 else "光学深度定义;判定写进 notes(τ<1 为薄)"))

    # F4: 双点 κ 比 — 6 题(同元素同 ρ 不同 T 的两行)
    for sym in ("Al", "Au"):
        rows = [r for r in tables[sym] if r[3] > 1e-6]
        for _ in range(3):
            r1 = rng.choice(rows)
            same_rho = [r for r in rows if abs(r[0] - r1[0]) < 1e-9 and r[2] == r1[2] and r[1] != r1[1]]
            if not same_rho:
                continue
            r2 = rng.choice(same_rho)
            rho = 10 ** r1[0]
            k1 = 1 / (rho * r1[3])
            k2 = 1 / (rho * r2[3])
            ratio = k2 / k1
            if not (0.02 < ratio < 50):
                continue
            n += 1
            problems.append(rec(
                f"icf-eos-opacity-{n}", "expert",
                f"{sym} 在 ρ={rho:.4g} g/cm³、hν={10**r1[2]:.4g} eV 下:T₁={10**r1[1]:.4g} eV 时自由程 l₁={r1[3]:.6g} cm,T₂={10**r2[1]:.4g} eV 时 l₂={r2[3]:.6g} cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。",
                float(f"{ratio:.5g}"), "1", 0.02,
                f"({r1[3]})/({r2[3]})",
                "同 ρ 下 κ∝1/l,密度约掉;考查比值法"))

    for p in problems:
        print(json.dumps(p, ensure_ascii=False))


if __name__ == "__main__":
    main()
