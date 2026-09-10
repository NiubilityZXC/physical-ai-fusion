"""Score aggregation and reporting (results.json + markdown)."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


def aggregate(per_task: list[dict]) -> dict:
    by = lambda key: _agg(per_task, key)
    out = {
        "overall": _agg(per_task, None),
        "by_topic": by("topic"),
        "by_type": by("type"),
        "by_difficulty": by("difficulty"),
    }
    out["counts"] = {
        "total": len(per_task),
        "graded": sum(1 for r in per_task if r["status"] == "graded"),
        "ungraded": sum(1 for r in per_task if r["status"] != "graded"),
    }
    return out


def _agg(rows: list[dict], key: str | None) -> dict:
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        groups[r[key] if key else "all"].append(r)
    if key is None:
        rows = rows
        groups = {"all": rows}
    stats = {}
    for g, rs in groups.items():
        scores = [r["score"] for r in rs]
        stats[g] = {
            "n": len(rs),
            "mean": sum(scores) / len(scores) if scores else 0.0,
        }
    return stats


def write_results(per_task: list[dict], out_json: Path, out_md: Path | None = None) -> dict:
    agg = aggregate(per_task)
    payload = {"summary": agg, "per_task": per_task}
    out_json = Path(out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    if out_md:
        lines = ["# Physical-AI-Fusion evaluation results", "",
                 f"**Overall**: {agg['overall']['all']['mean']*100:.1f}% "
                 f"({agg['counts']['graded']}/{agg['counts']['total']} graded)", "",
                 "| topic | n | mean |", "|---|---|---|"]
        for g, s in sorted(agg["by_topic"].items()):
            lines.append(f"| {g} | {s['n']} | {s['mean']*100:.1f}% |")
        lines += ["", "| type | n | mean |", "|---|---|---|"]
        for g, s in sorted(agg["by_type"].items()):
            lines.append(f"| {g} | {s['n']} | {s['mean']*100:.1f}% |")
        lines += ["", "| difficulty | n | mean |", "|---|---|---|"]
        for g, s in sorted(agg["by_difficulty"].items()):
            lines.append(f"| {g} | {s['n']} | {s['mean']*100:.1f}% |")
        out_md = Path(out_md)
        out_md.parent.mkdir(parents=True, exist_ok=True)
        out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return agg
