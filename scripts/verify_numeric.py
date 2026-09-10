#!/usr/bin/env python3
"""verify_numeric.py — independent-recompute verification for numeric tasks.

Every numeric task carries `verification.evidence.recompute_expr`: a Python
expression that recomputes the answer **from first principles and explicit
constants**, written by the problem constructor to be an independent path
(different algebra/order than the one used to produce answer.value).

This script evaluates each recompute_expr in a restricted namespace
(math module + nothing else) and checks

    |recomputed - answer.value| / |answer.value|  <=  tolerance_rel / 2

(design.md §5 step 2: independent recompute must agree within half the
grading tolerance before a task may enter data/verified/.)

Usage:
    python3 scripts/verify_numeric.py data/staging/plasma-basic.jsonl
    python3 scripts/verify_numeric.py data/staging/*.jsonl --write-log docs/verification-log.md

Exit code 0 = every numeric task with a recompute_expr passed; 1 otherwise.
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import sys
from pathlib import Path

SAFE_NS = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
SAFE_NS.update({"abs": abs, "min": min, "max": max, "round": round})


def recompute(expr: str) -> float:
    """Evaluate a recompute expression in a math-only namespace."""
    code = compile(expr, "<recompute_expr>", "eval")
    if code.co_names:
        bad = [n for n in code.co_names if n not in SAFE_NS]
        if bad:
            raise ValueError(f"recompute_expr uses disallowed names: {bad}")
    val = eval(code, {"__builtins__": {}}, dict(SAFE_NS))  # noqa: S307 - sandboxed namespace
    if not isinstance(val, (int, float)) or not math.isfinite(val):
        raise ValueError(f"recompute_expr did not return a finite number: {val!r}")
    return float(val)


def verify_file(path: Path) -> list[dict]:
    results = []
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            t = json.loads(line)
            if t.get("answer", {}).get("kind") != "numeric":
                continue
            tid = t.get("task_id", f"{path.name}:{ln}")
            ans = t["answer"]
            expr = (t.get("verification") or {}).get("evidence", {}).get("recompute_expr")
            rec = {"task_id": tid, "file": str(path), "status": None, "detail": ""}
            if not expr:
                rec["status"] = "SKIP"
                rec["detail"] = "no recompute_expr"
                results.append(rec)
                continue
            try:
                v = recompute(expr)
            except Exception as e:  # noqa: BLE001
                rec["status"] = "FAIL"
                rec["detail"] = f"recompute error: {e}"
                results.append(rec)
                continue
            gold = float(ans["value"])
            tol = float(ans.get("tolerance_rel", 0.02))
            rel = abs(v - gold) / abs(gold) if gold != 0 else abs(v - gold)
            ok = rel <= tol / 2
            rec["status"] = "PASS" if ok else "FAIL"
            rec["detail"] = f"recomputed={v:.6g} gold={gold:.6g} rel_dev={rel:.2e} (limit {tol/2:.1e})"
            rec["recomputed"] = v
            rec["rel_dev"] = rel
            results.append(rec)
    return results


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--write-log", default=None, help="append results to this markdown log")
    args = ap.parse_args()

    all_results: list[dict] = []
    for pat in args.files:
        paths = sorted(Path().glob(pat)) if any(c in pat for c in "*?") else [Path(pat)]
        for path in paths:
            all_results.extend(verify_file(path))

    n_pass = sum(1 for r in all_results if r["status"] == "PASS")
    n_fail = sum(1 for r in all_results if r["status"] == "FAIL")
    n_skip = sum(1 for r in all_results if r["status"] == "SKIP")
    for r in all_results:
        mark = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️"}[r["status"]]
        print(f"{mark} {r['task_id']:36s} {r['detail']}")
    print(f"\n{n_pass} PASS / {n_fail} FAIL / {n_skip} SKIP (no recompute_expr)")

    if args.write_log:
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [f"\n## 独立复算批次 {ts}\n",
                 "| task_id | 结果 | 复算值 | 相对偏差 |", "|---|---|---|---|"]
        for r in all_results:
            if r["status"] == "SKIP":
                continue
            lines.append(f"| {r['task_id']} | {r['status']} | {r.get('recomputed', ''):.6g} "
                         f"| {r.get('rel_dev', float('nan')):.2e} |")
        with open(args.write_log, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
