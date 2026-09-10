#!/usr/bin/env python3
"""validate_tasks.py — Physical-AI-Fusion task JSONL schema validator (schema_version 1.0).

Usage:
    python3 scripts/validate_tasks.py data/staging/*.jsonl
    python3 scripts/validate_tasks.py data/verified/*.jsonl --strict-verification

Exit code 0 = all files valid; 1 = any error.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

SCHEMA_VERSION = "1.0"
TOPICS = {
    "icf/ignition-gain", "icf/rt-rm-instability", "icf/lpi", "icf/rad-hydro",
    "icf/eos-opacity", "icf/implosion", "icf/target-design", "icf/diagnostics",
    "mcf", "zpinch", "plasma-basic", "fusion-engineering", "simulation",
}
TYPES = {"numeric", "concept", "derivation", "code", "figure"}
DIFFICULTIES = {"undergrad", "grad", "expert"}
ANSWER_KINDS = {"numeric", "choice", "expression", "rubric", "code"}
GRADING_MODES = {"numeric_tolerance", "exact_match", "rubric_judge", "unit_test"}
SOURCE_TYPES = {"textbook", "paper", "report", "public-data", "local_sim", "local_experiment"}
TASK_ID_RE = re.compile(r"^[a-z][a-z0-9-]*-\d{4}$")

# grading mode <-> answer kind compatibility
KIND_MODE = {
    "numeric": {"numeric_tolerance"},
    "choice": {"exact_match"},
    "expression": {"exact_match", "rubric_judge"},
    "rubric": {"rubric_judge"},
    "code": {"unit_test"},
}
# type <-> answer kind compatibility
TYPE_KIND = {
    "numeric": {"numeric"},
    "concept": {"choice"},
    "derivation": {"expression", "rubric"},
    "code": {"code"},
    "figure": {"numeric", "choice"},
}


def err(errors, tid, msg):
    errors.append(f"[{tid}] {msg}")


def validate_task(t: dict, strict_verification: bool, errors: list[str]):
    tid = t.get("task_id", "<missing-id>")

    # --- identity & enums ---
    if not isinstance(tid, str) or not TASK_ID_RE.match(tid):
        err(errors, tid, "task_id missing or bad format (expected slug-NNNN)")
    if t.get("schema_version") != SCHEMA_VERSION:
        err(errors, tid, f"schema_version must be {SCHEMA_VERSION!r}")
    if t.get("topic") not in TOPICS:
        err(errors, tid, f"topic {t.get('topic')!r} not in taxonomy")
    if t.get("type") not in TYPES:
        err(errors, tid, f"type {t.get('type')!r} invalid")
    if t.get("difficulty") not in DIFFICULTIES:
        err(errors, tid, f"difficulty {t.get('difficulty')!r} invalid")
    if not isinstance(t.get("question"), str) or len(t["question"].strip()) < 20:
        err(errors, tid, "question missing or too short (<20 chars)")

    # --- answer ---
    a = t.get("answer")
    if not isinstance(a, dict):
        err(errors, tid, "answer missing or not an object")
        return
    kind = a.get("kind")
    if kind not in ANSWER_KINDS:
        err(errors, tid, f"answer.kind {kind!r} invalid")
        return
    if t.get("type") in TYPE_KIND and kind not in TYPE_KIND[t["type"]]:
        err(errors, tid, f"answer.kind {kind!r} incompatible with type {t.get('type')!r}")

    if kind == "numeric":
        v = a.get("value")
        if not isinstance(v, (int, float)) or not math.isfinite(v):
            err(errors, tid, "numeric answer.value must be finite number")
        if not isinstance(a.get("unit"), str) or not a["unit"].strip():
            err(errors, tid, "numeric answer requires non-empty unit")
        tol = a.get("tolerance_rel")
        if not isinstance(tol, (int, float)) or not (0 < tol <= 0.2):
            err(errors, tid, "tolerance_rel must be in (0, 0.2]")
    elif kind == "choice":
        opts = a.get("options")
        corr = a.get("correct")
        if not isinstance(opts, dict) or len(opts) < 3:
            err(errors, tid, "choice answer requires >=3 options")
        elif not isinstance(corr, list) or not corr or any(c not in opts for c in corr):
            err(errors, tid, "correct must be non-empty list of keys present in options")
    elif kind == "expression":
        if not isinstance(a.get("expression"), str) or not a["expression"].strip():
            err(errors, tid, "expression answer requires non-empty expression")
    elif kind == "rubric":
        r = a.get("rubric")
        if not isinstance(r, list) or len(r) < 3:
            err(errors, tid, "rubric answer requires >=3 scoring points")
        else:
            w = [p.get("weight") for p in r]
            if any(not isinstance(x, (int, float)) or x <= 0 for x in w):
                err(errors, tid, "every rubric point needs weight > 0")
            elif abs(sum(w) - 1.0) > 1e-6:
                err(errors, tid, f"rubric weights must sum to 1.0 (got {sum(w):.4f})")
            if any(not isinstance(p.get("point"), str) or len(p["point"]) < 10 for p in r):
                err(errors, tid, "every rubric point needs a description (>=10 chars)")
    elif kind == "code":
        c = a.get("code")
        if not isinstance(c, dict):
            err(errors, tid, "code answer requires code object")
        else:
            for f in ("entry_point", "test_file", "timeout_s"):
                if f not in c:
                    err(errors, tid, f"code answer missing {f}")
            if isinstance(c.get("timeout_s"), (int, float)) and not (1 <= c["timeout_s"] <= 3600):
                err(errors, tid, "timeout_s out of range [1, 3600]")

    # --- grading ---
    g = t.get("grading")
    if not isinstance(g, dict) or g.get("mode") not in GRADING_MODES:
        err(errors, tid, f"grading.mode {g.get('mode') if isinstance(g, dict) else None!r} invalid")
    elif g["mode"] not in KIND_MODE[kind]:
        err(errors, tid, f"grading.mode {g['mode']!r} incompatible with answer.kind {kind!r}")

    # --- metadata ---
    m = t.get("metadata")
    if not isinstance(m, dict):
        err(errors, tid, "metadata missing")
    else:
        if not isinstance(m.get("source"), str) or len(m["source"]) < 10:
            err(errors, tid, "metadata.source required (>=10 chars)")
        if m.get("source_type") not in SOURCE_TYPES:
            err(errors, tid, f"metadata.source_type {m.get('source_type')!r} invalid")
        if not isinstance(m.get("license"), str) or not m["license"].strip():
            err(errors, tid, "metadata.license required")

    # --- verification ---
    v = t.get("verification")
    if not isinstance(v, dict):
        err(errors, tid, "verification block missing")
    else:
        methods = v.get("methods", [])
        vb = v.get("verified_by", [])
        if strict_verification:
            if not methods:
                err(errors, tid, "strict: verification.methods empty")
            if not vb:
                err(errors, tid, "strict: verification.verified_by empty")
            if not v.get("verified_at"):
                err(errors, tid, "strict: verification.verified_at empty")
        # numeric tasks should carry an independent recompute expression to be verifiable
        if kind == "numeric" and strict_verification:
            ev = v.get("evidence", {})
            if not isinstance(ev.get("recompute_expr"), str) or not ev["recompute_expr"].strip():
                err(errors, tid, "strict: numeric task lacks evidence.recompute_expr")


def validate_file(path: Path, strict: bool) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                t = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"[{path.name}:{ln}] JSON parse error: {e}")
                continue
            if not isinstance(t, dict):
                errors.append(f"[{path.name}:{ln}] line is not a JSON object")
                continue
            if t.get("task_id") in seen_ids:
                errors.append(f"[{path.name}:{ln}] duplicate task_id {t.get('task_id')}")
            seen_ids.add(t.get("task_id"))
            validate_task(t, strict, errors)
    return errors


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict-verification" in sys.argv
    if not args:
        print(__doc__)
        return 2
    all_errors: list[str] = []
    n_tasks = 0
    for pat in args:
        for path in sorted(Path().glob(pat)) if any(c in pat for c in "*?") else [Path(pat)]:
            errs = validate_file(path, strict)
            n = sum(1 for line in open(path, encoding="utf-8") if line.strip())
            n_tasks += n
            status = "OK " if not errs else "ERR"
            print(f"{status} {path} ({n} tasks, {len(errs)} errors)")
            all_errors.extend(errs)
    if all_errors:
        print("\n".join(all_errors[:80]))
        if len(all_errors) > 80:
            print(f"... and {len(all_errors) - 80} more errors")
    print(f"\n{n_tasks} tasks, {len(all_errors)} errors total")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
