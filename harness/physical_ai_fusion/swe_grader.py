"""swe_patch grader — SWE-bench form: apply the model's patch, run FAIL_TO_PASS tests.

task["swe"] = {
  "repo_path": "/tmp/freegs",
  "base_commit": "9fbec20",
  "bug_intro_patch": "harness/tests/swe/freegs-128-bugintro.patch",  # optional
  "fail_to_pass": ["harness/tests/swe/test_freegs_triangularity_lower.py"],
  "pass_to_pass": [],
  "venv": "/tmp/venv-freegs/bin/python",
  "timeout_s": 600
}
Model response must contain a unified diff (```diff fence or bare diff).
Pipeline: clean clone -> checkout base_commit -> [apply bug_intro] -> apply model
patch (git apply --check first) -> run FAIL_TO_PASS (all must pass) -> PASS_TO_PASS.
"""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

DIFF_FENCE = re.compile(r"```(?:diff|patch)\s*\n(.*?)```", re.S)
HUNK_RE = re.compile(r"^@@ -\d+", re.M)


def extract_patch(response: str) -> str | None:
    if not response:
        return None
    m = DIFF_FENCE.search(response)
    if m:
        return m.group(1)
    for marker in ("diff --git", "--- a/"):
        i = response.find(marker)
        if i >= 0 and HUNK_RE.search(response):
            return response[i:]
    return None


def _run(cmd: list[str], cwd: str | None, timeout: int) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr)[-3000:]
    except subprocess.TimeoutExpired:
        return 124, f"timeout after {timeout}s"


def grade_swe_patch(response: str, task: dict, timeout: int = 600) -> tuple[float, str]:
    swe = task.get("swe")
    if not swe:
        return 0.0, "task has no swe config"
    patch = extract_patch(response)
    if not patch:
        return 0.0, "no unified-diff patch found in response"
    venv_py = swe.get("venv", "python3")
    timeout = int(swe.get("timeout_s", timeout))
    bench_root = Path(__file__).resolve().parents[2]

    with tempfile.TemporaryDirectory(prefix="swe-") as tmp:
        rc, out = _run(["git", "clone", "-q", swe["repo_path"], tmp + "/repo"], None, 300)
        if rc != 0:
            return 0.0, f"repo clone failed: {out[:200]}"
        repo = tmp + "/repo"
        rc, out = _run(["git", "checkout", "-q", swe["base_commit"]], repo, 120)
        if rc != 0:
            return 0.0, f"base checkout failed: {out[:200]}"
        bip = swe.get("bug_intro_patch")
        if bip:
            src = bench_root / bip
            if src.exists():
                rc, out = _run(["git", "apply", str(src)], repo, 60)
                if rc != 0:
                    return 0.0, f"bug-intro patch failed: {out[:200]}"
        (Path(repo) / "model.patch").write_text(patch, encoding="utf-8")
        rc, out = _run(["git", "apply", "--check", "model.patch"], repo, 60)
        if rc == 0:
            rc, out = _run(["git", "apply", "model.patch"], repo, 60)
        if rc != 0:
            # git apply 对行数计数错误零容忍;退回更宽容的 patch(模糊匹配上下文)
            rc2, out2 = _run(["patch", "-p1", "--fuzz=3", "-s", "-i", "model.patch"], repo, 60)
            if rc2 != 0:
                return 0.0, f"patch does not apply: git-apply: {out[:120]} | patch: {out2[:120]}"
        # 不检查"是否有改动":bug-intro 存在时,空/无效补丁自然会被 FAIL_TO_PASS 拦下;
        # 正确修复会让树回到上游状态,反而是干净的。测试是唯一裁决。
        ftp = swe.get("fail_to_pass", [])
        if not ftp:
            return 0.0, "no fail_to_pass tests configured"
        results = []
        for rel in ftp:
            test_path = bench_root / rel
            if not test_path.exists():
                test_path = Path(repo) / rel
            rc, out = _run([venv_py, "-m", "pytest", str(test_path), "-x", "-q"], repo, timeout)
            results.append((rel, rc, out[-400:]))
        failed = [r for r in results if r[1] != 0]
        if failed:
            detail = "; ".join(f"{r[0]} FAIL: {r[2][-150:]}" for r in failed)
            return 0.0, f"FAIL_TO_PASS failed: {detail}"
        for rel in swe.get("pass_to_pass", []):
            test_path = bench_root / rel
            rc, out = _run([venv_py, "-m", "pytest", str(test_path), "-q"], repo, timeout)
            if rc != 0:
                return 0.0, f"PASS_TO_PASS regression: {out[-300:]}"
        return 1.0, f"all {len(ftp)} FAIL_TO_PASS tests pass after patch"
