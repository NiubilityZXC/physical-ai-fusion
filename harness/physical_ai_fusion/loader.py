"""Dataset loader with schema sanity checks (fails fast, SWE-bench style)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


def load_tasks(paths: Iterable[Path | str]) -> list[dict]:
    tasks: list[dict] = []
    for p in paths:
        p = Path(p)
        with open(p, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    t = json.loads(line)
                except json.JSONDecodeError as e:
                    raise ValueError(f"{p}:{ln}: invalid JSON — {e}") from e
                for field in ("task_id", "topic", "type", "question", "answer", "grading"):
                    if field not in t:
                        raise ValueError(f"{p}:{ln}: missing field {field!r}")
                tasks.append(t)
    ids = [t["task_id"] for t in tasks]
    if len(ids) != len(set(ids)):
        dupes = {i for i in ids if ids.count(i) > 1}
        raise ValueError(f"duplicate task_ids: {sorted(dupes)}")
    return tasks


def dataset_files(repo_root: Path | str, split: str = "verified") -> list[Path]:
    root = Path(repo_root)
    d = root / "data" / split
    files = sorted(d.glob("*.jsonl"))
    if not files:
        raise FileNotFoundError(f"no JSONL files under {d}")
    return files
