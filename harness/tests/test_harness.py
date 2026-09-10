"""Harness unit tests (deterministic grading)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from physical_ai_fusion.grader import extract_number, grade, grade_choice, grade_numeric
from physical_ai_fusion.loader import load_tasks


def test_extract_number_marker_and_last():
    assert abs(extract_number("先做一堆推导。Final answer: 3.15e6 J") - 3.15e6) < 1e-6
    assert abs(extract_number("推导过程 1.5 与 2.5,答案: 1.54") - 1.54) < 1e-9
    assert abs(extract_number("结果约 0.3 g/cm2,综上") - 0.3) < 1e-9
    assert extract_number("没有任何数字") is None


def test_grade_numeric():
    ans = {"value": 1.5366, "tolerance_rel": 0.02}
    assert grade_numeric("gain G = 1.54", ans)[0] == 1.0
    assert grade_numeric("G is about 3", ans)[0] == 0.0
    ans0 = {"value": 0.0, "tolerance_rel": 0.02}
    assert grade_numeric("value: 0", ans0)[0] == 1.0


def test_grade_choice_multiselect():
    ans = {"correct": ["A", "B", "C"], "options": {"A": 1, "B": 1, "C": 1, "D": 1}}
    assert grade_choice("answer: A, B, C", ans)[0] == 1.0
    assert grade_choice("answer: A, B", ans)[0] == 0.0
    assert grade_choice("选 D", ans)[0] == 0.0


def test_grade_dispatch_and_dataset_load():
    t = {"answer": {"kind": "numeric", "value": 2.0, "tolerance_rel": 0.02},
         "grading": {"mode": "numeric_tolerance"}}
    assert grade("final answer: 2.0", t)[0] == 1.0
    root = Path(__file__).resolve().parents[2]
    files = sorted((root / "data" / "verified").glob("*.jsonl"))
    if files:  # dataset present in repo checkout
        tasks = load_tasks(files)
        assert len(tasks) >= 50
        assert all("task_id" in t for t in tasks)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok {name}")
    print("all harness tests passed")
