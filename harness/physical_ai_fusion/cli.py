"""CLI: physical-ai-fusion evaluate / inspect / stats

Examples:
    physical-ai-fusion stats
    physical-ai-fusion inspect --task icf-ig-0001
    physical-ai-fusion evaluate --predictions preds.jsonl \
        --output results/results.json --output-md results/results.md
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from .loader import dataset_files, load_tasks
from .grader import grade
from .report import write_results

DEFAULT_ROOT = Path(__file__).resolve().parents[2]


def _load_predictions(path: str) -> dict[str, str]:
    preds = {}
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{ln}: invalid JSON — {e}") from e
            preds[r["task_id"]] = r.get("response", "")
    return preds


def cmd_stats(args) -> int:
    files = dataset_files(args.root, args.split)
    tasks = load_tasks(files)
    c_topic = Counter(t["topic"] for t in tasks)
    c_type = Counter(t["type"] for t in tasks)
    c_diff = Counter(t["difficulty"] for t in tasks)
    print(f"split={args.split}  tasks={len(tasks)}  files={len(files)}")
    print("\ntopic:")
    for k, v in sorted(c_topic.items()):
        print(f"  {k:28s} {v}")
    print("\ntype:", dict(c_type))
    print("difficulty:", dict(c_diff))
    return 0


def _apply_lang(tasks: list[dict], lang: str | None) -> list[dict]:
    """--lang en: 用 question_en/options_en 覆盖展示与 prompt 视图(缺失时回退中文)。"""
    if lang != "en":
        return tasks
    out = []
    for t in tasks:
        t = dict(t)
        if t.get("question_en"):
            t["question"] = t["question_en"]
        if t.get("options_en") and isinstance(t.get("answer"), dict) and t["answer"].get("kind") == "choice":
            t["answer"] = dict(t["answer"], options=t["options_en"])
        out.append(t)
    return out


def cmd_inspect(args) -> int:
    files = dataset_files(args.root, args.split)
    tasks = {t["task_id"]: t for t in _apply_lang(load_tasks(files), args.lang)}
    if args.task:
        t = tasks.get(args.task)
        if not t:
            print(f"task {args.task!r} not found in {args.split}", file=sys.stderr)
            return 2
        print(json.dumps(t, ensure_ascii=False, indent=2))
        return 0
    for tid, t in tasks.items():
        print(f"{tid:36s} {t['type']:10s} {t['difficulty']:9s} {t['question'][:60]}")
    return 0


def cmd_evaluate(args) -> int:
    files = dataset_files(args.root, args.split)
    tasks = _apply_lang(load_tasks(files), args.lang)
    preds = _load_predictions(args.predictions)
    per_task = []
    for t in tasks:
        resp = preds.get(t["task_id"])
        if resp is None:
            per_task.append({"task_id": t["task_id"], "topic": t["topic"], "type": t["type"],
                             "difficulty": t["difficulty"], "score": 0.0, "status": "missing",
                             "detail": "no prediction for task"})
            continue
        score, detail = grade(resp, t)
        per_task.append({"task_id": t["task_id"], "topic": t["topic"], "type": t["type"],
                         "difficulty": t["difficulty"], "score": score, "status": "graded",
                         "detail": detail})
    out_json = Path(args.output)
    out_md = Path(args.output_md) if args.output_md else out_json.with_suffix(".md")
    agg = write_results(per_task, out_json, out_md)
    s = agg["overall"]["all"]
    print(f"split={args.split} graded={agg['counts']['graded']}/{agg['counts']['total']} "
          f"mean={s['mean']*100:.1f}%")
    print(f"results: {out_json}")
    if per_task and any(r["status"] == "missing" for r in per_task):
        print(f"warning: {sum(1 for r in per_task if r['status'] == 'missing')} tasks had no prediction (scored 0)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="physical-ai-fusion",
                                 description="Physical-AI-Fusion benchmark harness")
    ap.add_argument("--root", default=str(DEFAULT_ROOT), help="benchmark repo root")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def _sp(name, help):
        p = sub.add_parser(name, help=help)
        p.add_argument("--split", default="verified", choices=["verified", "staging"])
        p.add_argument("--lang", default=None, choices=[None, "en", "zh"],
                       help="question language view (en uses question_en/options_en when present)")
        return p

    _sp("stats", "dataset statistics")
    p = _sp("inspect", "list tasks or show one")
    p.add_argument("--task", default=None, help="task_id to dump")
    p = _sp("evaluate", help="grade a predictions file")
    p.add_argument("--predictions", required=True, help="JSONL: {task_id, response}")
    p.add_argument("--output", default="results/results.json")
    p.add_argument("--output-md", default=None)

    args = ap.parse_args(argv)
    return {"stats": cmd_stats, "inspect": cmd_inspect, "evaluate": cmd_evaluate}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
