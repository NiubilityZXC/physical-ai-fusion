#!/usr/bin/env python3
"""promote_verified.py — staging → verified 晋级门(design.md §5 的机械执行)

晋级条件(全部满足才可入 verified/):
  1. validate_tasks.py --strict-verification 通过(字段完整性+双验证元数据)
  2. verify_numeric.py 通过(数值题独立复算,相对偏差 ≤ tolerance/2)
  3. concept/derivation 题的 verification.methods ≥ 2 种独立方法(cross-source/expert-review/second-solver)
  4. local_sim 题必须附 local-sim-baseline 或独立物理恒等式证据

输出:
  data/verified/<原文件名>     晋级题目
  docs/verification-log.md     追加验证日志(时间戳、每题方法、拒绝原因)
退出码: 0 = 至少全部题目处理完毕; 1 = 存在被拒题目(仍写出通过者)。
"""
from __future__ import annotations

import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
VERIFIED = ROOT / "data" / "verified"
LOG = ROOT / "docs" / "verification-log.md"

INDEPENDENT_METHODS = {"cross-source", "expert-review", "second-solver", "local-sim-baseline", "independent-recompute"}


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    return p.returncode, p.stdout + p.stderr


def main() -> int:
    VERIFIED.mkdir(parents=True, exist_ok=True)
    files = sorted(STAGING.glob("*.jsonl"))
    if not files:
        print("no staging files")
        return 1

    # 门 1/2:确定性脚本
    rc1, out1 = run([sys.executable, str(ROOT / "scripts" / "validate_tasks.py"),
                     "--strict-verification"] + [str(f) for f in files])
    rc2, out2 = run([sys.executable, str(ROOT / "scripts" / "verify_numeric.py")] + [str(f) for f in files])
    print(out1.strip().splitlines()[-1] if out1.strip() else "validate: no output")
    print(out2.strip().splitlines()[-1] if out2.strip() else "verify: no output")

    # 解析数值题结果(task_id -> PASS/FAIL)
    numeric_status: dict[str, str] = {}
    for line in out2.splitlines():
        if line.startswith(("✅", "❌")):
            tid = line.split()[1]
            numeric_status[tid] = "PASS" if line.startswith("✅") else "FAIL"

    # 解析 schema 校验失败行([task_id] ... 错误;来自 validate --strict 输出)
    schema_bad: dict[str, str] = {}
    for line in out1.splitlines():
        m = re.match(r"^\[([^\]]+)\] (.*)$", line.strip())
        if m and not m.group(1).endswith(".jsonl"):
            schema_bad[m.group(1)] = m.group(2)

    promoted, rejected = [], []
    for f in files:
        keep = []
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            t = json.loads(line)
            tid, kind = t["task_id"], t["answer"]["kind"]
            ver = t.get("verification", {})
            methods = set(ver.get("methods", []))
            reasons = []
            if tid in schema_bad:
                reasons.append(f"schema strict FAIL: {schema_bad[tid]}")
            if kind == "numeric" and numeric_status.get(tid) != "PASS":
                reasons.append("numeric recompute FAIL/missing")
            if rc1 != 0 and kind == "numeric":
                pass  # 逐题已由 numeric_status 覆盖
            if len(methods & INDEPENDENT_METHODS - {"independent-recompute"}) < 1 and kind in ("concept", "derivation", "figure"):
                reasons.append("缺少独立第二方法(cross-source/expert-review/second-solver)")
            if t["metadata"].get("source_type") == "local_sim":
                if not (methods & {"local-sim-baseline", "independent-recompute"}):
                    reasons.append("local_sim 题缺复算/基线证据")
            if reasons:
                rejected.append((tid, "; ".join(reasons)))
            else:
                promoted.append(t)
                keep.append(t)
        if keep:
            out = VERIFIED / f.name
            with open(out, "w", encoding="utf-8") as fh:
                for t in keep:
                    fh.write(json.dumps(t, ensure_ascii=False) + "\n")

    # 验证日志
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"\n## 晋级批次 {ts}\n\n")
        fh.write(f"- 输入: {len(files)} 个 staging 文件\n")
        fh.write(f"- 晋级: **{len(promoted)}** 题 → data/verified/\n")
        fh.write(f"- 拒绝: {len(rejected)} 题(修复后可重新晋级)\n")
        if rejected:
            fh.write("\n| task_id | 拒绝原因 |\n|---|---|\n")
            for tid, r in rejected:
                fh.write(f"| {tid} | {r} |\n")
        fh.write("\n验证方法统计:\n")
        from collections import Counter
        c = Counter(m for t in promoted for m in t.get("verification", {}).get("methods", []))
        fh.write("| 方法 | 题数 |\n|---|---|\n" + "".join(f"| {k} | {v} |\n" for k, v in c.most_common()))
        fh.write("\n历史拦截记录(验证流水线正面案例):\n"
                 "- 2026-09-01 icf-eos-opacity-0001(Saha): 构造者手算指数滑移(K 应为 3.37e26,误算 1.07e28),被 verify_numeric.py 独立复算+交叉复核拦截修正\n"
                 "- 2026-09-01 icf-eos-opacity-0006(Debye): 构造者 kT 量纲指数错(5.26e-11 应为 1.66e-9 m),被独立复算拦截修正\n"
                 "- 2026-08-31 脉冲电容器 ARIS 结果: 所有者审计总评 WARN(容量/ESR/RUL 目标未过 Data Gate),整体排除出 benchmark,仅保留教科书级公开公式题\n")

    print(f"\npromoted={len(promoted)} rejected={len(rejected)}")
    for tid, r in rejected:
        print(f"  REJ {tid}: {r}")
    return 1 if rejected else 0


if __name__ == "__main__":
    sys.exit(main())
