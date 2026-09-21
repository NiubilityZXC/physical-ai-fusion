"""symbolic_equiv grader — SymPy symbolic-equivalence grading (PHYSICS benchmark style).

answer.kind = "expression":
  {"kind": "expression", "expression": "sqrt(A*k*g)", "symbols": ["A","k","g"],
   "proportional": false}   # proportional=true allows a pure numeric constant factor

Deterministic pipeline:
  1. extract final expression from the response (marker first, then last "x = expr" line);
     strip common LaTeX (\\gamma, \\sqrt, \\cdot, \\frac, ^{}).
  2. parse within the task's declared symbol alphabet (^ -> **, sqrt/log/exp/pi allowed).
  3. PASS iff: simplify(model - gold) == 0; or (proportional) simplify(model/gold)
     is a nonzero free-symbol-free constant; or numerically equal on 5 positive samples (rel<1e-6).
Returns (score, detail). If sympy is unavailable returns (0, "sympy-unavailable").
"""
from __future__ import annotations

import random
import re

try:
    import sympy
    from sympy.parsing.sympy_parser import (
        parse_expr,
        standard_transformations,
        implicit_multiplication_application,
        convert_xor,
    )
    _TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
    _HAVE_SYMPY = True
except Exception:  # pragma: no cover
    _HAVE_SYMPY = False

GREEK = {
    "gamma": "gamma", "alpha": "alpha", "beta": "beta", "omega": "omega",
    "rho": "rho", "tau": "tau", "lambda": "lam", "Lambda": "Lam",
    "epsilon": "eps", "varepsilon": "eps", "kappa": "kappa", "mu": "mu",
    "nu": "nu", "sigma": "sigma", "chi": "chi", "pi": "pi",
}
MARKER = re.compile(r"(?:final answer|answer|答案|答|结果|结论)\s*[:：=是为]?\s*", re.I)
ASSIGN = re.compile(r"[A-Za-z][A-Za-z0-9_{}\\]*\s*=\s*(.+)$")


def _latex_to_plain(s: str) -> str:
    s = s.strip().strip("$").strip()
    s = re.sub(r"\\left|\\right", "", s)
    s = re.sub(r"\\mathrm\{([^}]*)\}|\\text\{([^}]*)\}", r"\1\2", s)
    s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt\[(\d+)\]\{([^{}]*)\}", r"(\2)**(1/\1)", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", s)
    s = re.sub(r"\\sqrt\s*\(([^()]*)\)", r"sqrt(\1)", s)
    s = re.sub(r"\\sqrt\s+([A-Za-z0-9_]+)", r"sqrt(\1)", s)
    s = re.sub(r"\\cdot|\\times", "*", s)
    s = re.sub(r"\\ln\b", "log", s)
    s = re.sub(r"\\exp\b", "exp", s)
    s = re.sub(r"\\log\b", "log", s)
    for k, v in GREEK.items():
        s = re.sub(r"\\" + k + r"\b", v, s)
    s = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", s)
    s = re.sub(r"\^(\w)", r"**\1", s)
    s = s.replace("{", "(").replace("}", ")")
    s = re.sub(r"\s+", "", s)
    return s


def extract_expression(response: str) -> str | None:
    if not response:
        return None
    cands = []
    ms = list(MARKER.finditer(response))
    if ms:
        cands.append(response[ms[-1].end():].split("\n")[0])
    for line in reversed(response.strip().split("\n")):
        m = ASSIGN.search(line.strip())
        if m and re.search(r"[A-Za-z0-9]", m.group(1)):
            cands.append(m.group(1))
            break
    for line in reversed(response.strip().split("\n")):
        ls = line.strip().strip("$").strip()
        if len(ls) > 1 and re.search(r"[+\-*/^=]|sqrt|log|exp", ls):
            cands.append(ls)
            break
    for c in cands:
        c = c.strip().rstrip("。.;,;")
        if c:
            return c
    return None


def _parse(expr: str, symbols: list[str]):
    plain = _latex_to_plain(expr)
    local = {s: sympy.Symbol(s, positive=True) for s in symbols}
    local.update({"sqrt": sympy.sqrt, "log": sympy.log, "exp": sympy.exp,
                  "pi": sympy.pi, "Abs": sympy.Abs, "abs": sympy.Abs})
    return parse_expr(plain, local_dict=local, transformations=_TRANS, evaluate=True)


def grade_expression(response: str, answer: dict) -> tuple[float, str]:
    if not _HAVE_SYMPY:
        return 0.0, "sympy-unavailable"
    gold_str = answer.get("expression", "").strip()
    symbols = answer.get("symbols") or sorted(set(re.findall(r"[A-Za-z](?:_[A-Za-z0-9]+)?", gold_str)))
    proportional = bool(answer.get("proportional", False))
    got_str = extract_expression(response)
    if not got_str:
        return 0.0, "no expression found in response"
    try:
        gold = _parse(gold_str, symbols)
        got = _parse(got_str, symbols)
    except Exception as e:
        return 0.0, f"parse error: {type(e).__name__}: {str(e)[:80]} (got={got_str[:60]!r})"
    try:
        if sympy.simplify(got - gold) == 0:
            return 1.0, f"symbolically equal (gold={gold_str})"
        if proportional:
            ratio = sympy.simplify(got / gold)
            if ratio.is_number and ratio.free_symbols == set() and ratio != 0:
                return 1.0, f"proportional with constant factor {ratio} (gold={gold_str})"
        rng = random.Random(2026)
        free = sorted(gold.free_symbols | got.free_symbols, key=lambda s: s.name)
        ok = True
        for _ in range(5):
            subs = {s: rng.uniform(0.5, 3.0) for s in free}
            try:
                gv = float(gold.subs(subs))
                xv = float(got.subs(subs))
            except Exception:
                ok = False
                break
            if gv == 0 or abs(xv - gv) / max(abs(gv), 1e-300) > 1e-6:
                ok = False
                break
        if ok:
            return 1.0, f"numerically equal on 5 samples (gold={gold_str})"
    except Exception as e:
        return 0.0, f"eval error: {type(e).__name__}: {str(e)[:80]}"
    return 0.0, f"not equivalent: got={got_str[:60]!r} gold={gold_str!r}"
