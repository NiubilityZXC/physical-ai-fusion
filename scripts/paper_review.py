#!/usr/bin/env python3
"""paper_review.py — 用 ark 端点跨族模型对论文做 NeurIPS D&B 评审(Phase 5)"""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env = json.loads((Path.home() / ".claude" / "settings.json").read_text())["env"]
KEY, BASE = env["ANTHROPIC_AUTH_TOKEN"], env["ANTHROPIC_BASE_URL"]


def review(round_no: int, prev_feedback: str = "") -> str:
    secs = []
    for f in sorted((ROOT / "paper" / "sections").glob("*.tex")):
        secs.append(f"% ==== {f.name} ====\n" + f.read_text(encoding="utf-8"))
    paper = "\n".join(secs)
    prompt = f"""You are an expert NeurIPS Datasets & Benchmarks reviewer reviewing a paper about a fusion-physics LLM benchmark (688 verified tasks, ICF 50.9%, mechanical verification pipeline, SWE-bench-style harness).

PAPER (all sections):
{paper[:60000]}

{("Previous review round feedback (already addressed):" + prev_feedback) if prev_feedback else ""}

Give a structured review:
1. Score (1-10) with one-line justification
2. Strengths (3-5 bullets)
3. Weaknesses ordered by severity, each with a concrete actionable fix (be specific: section, what to change)
4. Overclaim check: any statement not supported by the evidence described (numbers, verification, baselines)? List each with severity CRITICAL/MAJOR/MINOR
5. Missing content a D&B reviewer would demand (dataset documentation, maintenance, ethics, contamination, licensing, checklist)
End with exactly one line:
VERDICT: accept | weak accept | borderline | weak reject | reject"""
    body = json.dumps({"model": "deepseek-v4-pro", "max_tokens": 6000,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(
        BASE.rstrip("/") + "/v1/messages", data=body,
        headers={"Content-Type": "application/json", "x-api-key": KEY,
                 "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
    txt = "".join(c.get("text", "") for c in d.get("content", []))
    if not txt.strip():
        txt = "[thinking only]\n" + "\n".join(
            c.get("thinking", "") for c in d.get("content", []) if c.get("type") == "thinking")
    trace = ROOT / ".aris" / "traces"
    trace.mkdir(parents=True, exist_ok=True)
    (trace / f"paper-review-round{round_no}.json").write_text(
        json.dumps({"model": d.get("model"), "id": d.get("id"), "text": txt}, ensure_ascii=False, indent=2))
    return txt


if __name__ == "__main__":
    prev = Path(sys.argv[2]).read_text(encoding="utf-8")[:3000] if len(sys.argv) > 2 else ""
    print(review(int(sys.argv[1]), prev))
