"""Deterministic graders.

numeric_tolerance: extract a number from the model response and compare
against answer.value with relative tolerance.  Number extraction is fully
deterministic and documented:

  1. If the response contains a fenced ``answer:`` / ``答案`` marker, parse the
     first number after the LAST such marker.
  2. Otherwise take the LAST number that appears in the response.

exact_match (choice): collect the set of option letters the response commits
to (``Answer: A, C`` or ``选 A`` patterns), compare exactly with the key.

Both graders return (score: float in {0,1}, detail: str).
"""
from __future__ import annotations

import re
from pathlib import Path

NUM_RE = re.compile(
    r"(?<![A-Za-z0-9_.])"                       # no leading identifier chars
    r"(-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)"       # plain / scientific
    r"(?![A-Za-z0-9_.])"                        # no trailing identifier chars
)
MARKER_RE = re.compile(r"(?:final answer|answer|答案|答)\s*[:：=是]?\s*", re.I)
LETTER_RE = re.compile(r"\b([A-D])\b")
# 中文字符与选项字母紧邻的格式: "答案是A" / "选项AC" / "选A、C" / "A、C 正确"
GLUE_RE = re.compile(r"(?:答案(?:是|为)?|选项(?:是|为)?|选|答|为)\s*([A-D](?:\s*[,，、和与及]+\s*[A-D])*)")
MULTI_GLUE_RE = re.compile(r"(?:^|[\s,，、；;])([A-D]{2,4})(?=[\s,，、；;.]|$)")


def _to_float(s: str) -> float:
    return float(s.replace("×10", "e").replace("E", "e"))


def extract_number(response: str) -> float | None:
    """Deterministic number extraction (marker-first, then last number)."""
    if not response:
        return None
    matches = list(MARKER_RE.finditer(response))
    if matches:
        last = matches[-1]
        rest = response[last.end():]
        m = NUM_RE.search(rest)
        if m:
            return _to_float(m.group(1))
    nums = NUM_RE.findall(response)
    return _to_float(nums[-1]) if nums else None


def grade_numeric(response: str, answer: dict) -> tuple[float, str]:
    gold = float(answer["value"])
    tol = float(answer.get("tolerance_rel", 0.02))
    got = extract_number(response)
    if got is None:
        return 0.0, "no number found in response"
    if gold == 0:
        ok = abs(got - gold) <= tol
    else:
        ok = abs(got - gold) / abs(gold) <= tol
    rel = abs(got - gold) / abs(gold) if gold else abs(got - gold)
    return (1.0 if ok else 0.0), f"gold={gold:.6g} got={got:.6g} rel_dev={rel:.2e} tol={tol:.1e}"


def extract_letters(response: str) -> set[str]:
    """Letters the response commits to. Order: marker-window → glue patterns → all standalone letters."""
    if not response:
        return set()
    # 1. marker 之后 80 字符内(允许字母紧贴中文)
    matches = list(MARKER_RE.finditer(response))
    if matches:
        rest = response[matches[-1].end():][:80]
        letters = set(LETTER_RE.findall(rest))
        letters |= set(re.findall(r"([A-D])(?=[,，、。.\s]|$)", rest))
        if letters:
            return letters
    # 2. "答案是A/选项AC/选A、C" 等紧贴格式
    for m in GLUE_RE.finditer(response):
        letters = set(re.findall(r"[A-D]", m.group(1)))
        if letters:
            return letters
    # 3. 紧缩多选 "AC" "ABC" 形式
    for m in MULTI_GLUE_RE.finditer(response):
        letters = set(m.group(1))
        if len(letters) == len(m.group(1)):
            return letters
    # 4. 全文独立字母
    return set(LETTER_RE.findall(response))


def grade_choice(response: str, answer: dict) -> tuple[float, str]:
    key = set(answer.get("correct", []))
    got = extract_letters(response)
    if not got:
        return 0.0, f"no option letters found (key={sorted(key)})"
    ok = got == key
    return (1.0 if ok else 0.0), f"key={sorted(key)} got={sorted(got)}"


def grade(response: str, task: dict) -> tuple[float, str]:
    mode = task["grading"]["mode"]
    if mode == "numeric_tolerance":
        return grade_numeric(response, task["answer"])
    if mode == "exact_match":
        return grade_choice(response, task["answer"])
    if mode == "unit_test":
        from .code_grader import grade_code
        root = Path(__file__).resolve().parents[2]
        return grade_code(response, task, root)
    if mode == "symbolic_equiv":
        from .sympy_grader import grade_expression
        return grade_expression(response, task["answer"])
    if mode == "swe_patch":
        from .swe_grader import grade_swe_patch
        return grade_swe_patch(response, task)
    return 0.0, f"grading mode {mode!r} requires the optional LLM-judge module (v1.1); skipped"
