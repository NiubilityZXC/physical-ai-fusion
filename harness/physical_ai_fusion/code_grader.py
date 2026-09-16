"""code_grader.py — 代码题判定:把模型回复中的 Python 代码抽取到 solution.py,
在子进程中运行该题的测试文件,按通过比例计分(全过=1.0)。

提取规则(确定性):
  1. 优先取最后一个 ```python ...``` 围栏块;
  2. 否则取最后一个 ``` ...``` 围栏块;
  3. 否则把整段回复当作代码。
运行方式:把 <test_file> 与 solution.py 放在同一临时目录,用当前解释器执行
`python <test_file>`(测试文件内部 import solution 并做断言,退出码 0 = 全过)。
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

FENCE_PY = re.compile(r"```python\s*\n(.*?)```", re.S)
FENCE_ANY = re.compile(r"```\s*\n(.*?)```", re.S)


def extract_code(response: str) -> str:
    m = FENCE_PY.findall(response)
    if m:
        return m[-1]
    m = FENCE_ANY.findall(response)
    if m:
        return m[-1]
    return response


def grade_code(response: str, task: dict, repo_root: Path, timeout: int | None = None) -> tuple[float, str]:
    code = task.get("answer", {}).get("code") or task.get("code") or {}
    test_file = code.get("test_file")
    if not test_file:
        return 0.0, "task has no answer.code.test_file"
    tpath = repo_root / test_file
    if not tpath.exists():
        return 0.0, f"test file missing: {test_file}"
    timeout = timeout or int(code.get("timeout_s", 60))
    src = extract_code(response)
    if "def " not in src:
        return 0.0, "no function definition found in response"
    with tempfile.TemporaryDirectory(prefix="paif_code_") as td:
        td = Path(td)
        (td / "solution.py").write_text(src, encoding="utf-8")
        target = td / tpath.name
        target.write_text(tpath.read_text(encoding="utf-8"), encoding="utf-8")
        try:
            p = subprocess.run([sys.executable, target.name], cwd=td,
                               capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return 0.0, f"timeout ({timeout}s)"
        out = (p.stdout + p.stderr).strip().replace("\n", " | ")[-300:]
        return (1.0 if p.returncode == 0 else 0.0), f"exit={p.returncode} {out}"
