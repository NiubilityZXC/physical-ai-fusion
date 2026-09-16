# Physical-AI-Fusion

**A quantitative physics-AI benchmark for nuclear fusion, with an inertial-confinement-fusion (ICF) focus.**

- **691 verified problems** across 13 topics — **ICF 50.1%** (ignition & gain, RT/RM instabilities, laser–plasma interactions, radiation hydrodynamics, EOS & opacity, implosion dynamics, target design, diagnostics), plus MCF, Z-pinch, plasma fundamentals, fusion engineering, and computational physics
- **Task types**: 566 numeric (tolerance-banded deterministic grading), 103 concept (exact-match multiple choice), 13 derivation (rubric-judge, reported separately), 8 code (unit-test), 1 figure
- **Every answer is double-verified**: independent recomputation (`recompute_expr`) for all numeric tasks + cross-source / expert-review / second-solver for the rest, with a staged `staging → verified` promotion gate and a public verification log
- **SWE-bench-style usability**: `pip install -e harness/`, then one command to evaluate; deterministic scores; versioned JSONL datasets; verified split is the headline set

## Quick start

```bash
git clone https://github.com/NiubilityZXC/physical-ai-fusion.git
cd physical-ai-fusion
pip install -e harness/

physical-ai-fusion stats                 # dataset statistics
physical-ai-fusion inspect --task icf-ignition-gain-0001

# predictions: one JSON per line: {"task_id": "...", "response": "..."}
physical-ai-fusion evaluate --predictions preds.jsonl \
    --output results/my_model.json --output-md results/my_model.md
```

Deterministic tasks (numeric / concept / figure) are graded locally and instantly.
Derivation tasks use a locked rubric judge (module planned for v1.1) and are reported separately.

## Repository layout

```
data/verified/    the benchmark (JSONL, one task per line, schema v1.0)
data/staging/    pre-promotion tasks (do not cite; may change or be dropped)
harness/         pip package `physical-ai-fusion` (loader, graders, CLI, report)
scripts/         validation / verification / promotion / baseline runner
docs/            design, sources, related-work, verification log
paper/           NeurIPS submission (LaTeX)
```

## Task schema (v1.0)

```json
{
  "task_id": "icf-ignition-gain-0001",
  "schema_version": "1.0",
  "topic": "icf/ignition-gain",
  "type": "numeric | concept | derivation | figure",
  "difficulty": "undergrad | grad | expert",
  "question": "self-contained problem statement (constants included)",
  "answer": {"kind": "numeric", "value": 1.5366, "unit": "1", "tolerance_rel": 0.02},
  "grading": {"mode": "numeric_tolerance"},
  "metadata": {"source": "...", "source_type": "...", "license": "...", "notes": "..."},
  "verification": {"methods": ["independent-recompute", "cross-source"],
                   "evidence": {"recompute_expr": "3.15/2.05"},
                   "verified_by": ["..."], "verified_at": "..."}
}
```

## Verification pipeline (the moat)

1. **Schema validation** — `scripts/validate_tasks.py` (field completeness, taxonomy, answer/grading consistency; `--strict-verification` for the verified split)
2. **Independent recomputation** — `scripts/verify_numeric.py` evaluates each numeric task's `recompute_expr` in a sandboxed math-only namespace and requires agreement within *half* the grading tolerance
3. **Promotion gate** — `scripts/promote_verified.py` moves `staging → verified` only when (1)–(2) pass and non-numeric tasks carry ≥2 independent verification methods; every batch appends to `docs/verification-log.md`
4. **Local-material discipline** — anything sourced from local simulations must show a physics-identity check or a byte-identical baseline rerun before it may enter; a capacitor prognostics dataset was **rejected wholesale** by this gate (see the log)

The pipeline has already caught two constructor arithmetic slips (a Saha prefactor and a Debye-length exponent) — exactly the failure mode it exists to prevent.

## Data sources

Public physics only: NRL Plasma Formulary, standard textbook formulas (Atzeni; Lindl; Drake; Kruer; Zel'dovich & Raizer; Freidberg), LLNL/NIF public ignition data (2022-12-05 2.05→3.15 MJ; 2025-04-07 record 8.6 MJ, gain 4.13), ITER official parameters, and verified local simulation assets (0-D Z-pinch dataset with 10,944 internally consistent rows; a screen-hydrogenic average-atom opacity model with a byte-identical baseline rerun; a FLASH 4.8 15-MA Al-liner Z-pinch setup). No classified or export-controlled content. Each task records `source`, `source_type`, and `license`.

## Results

See `results/` (reference predictions score 93/93 on deterministic tasks — a grader sanity check) and `results/baseline-*.jsonl` / `results/*.md` for model baselines.

## License

Code (harness, scripts): MIT. Dataset: CC BY 4.0. Problem statements derive from public sources under fair use, with per-task attribution in `metadata.source`.

## Citation

```bibtex
@misc{physical-ai-fusion-2026,
  title  = {Physical-AI-Fusion: A Quantitative Fusion-Physics Benchmark with ICF Focus},
  author = {Physical-AI-Fusion Team},
  year   = {2026},
  url    = {https://github.com/NiubilityZXC/physical-ai-fusion}
}
```
