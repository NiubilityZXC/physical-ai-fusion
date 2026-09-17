#!/usr/bin/env python3
"""contract_review.py — 用 ark 端点跨族模型评审论文验收契约(Phase 1.5)"""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env = json.loads((Path.home() / ".claude" / "settings.json").read_text())["env"]
KEY, BASE = env["ANTHROPIC_AUTH_TOKEN"], env["ANTHROPIC_BASE_URL"]

def review(round_no: int, extra: str = "") -> str:
    contract = (ROOT / "PAPER_ACCEPTANCE_CONTRACT.md").read_text(encoding="utf-8")
    plan = (ROOT / "PAPER_PLAN.md").read_text(encoding="utf-8")
    prompt = f"""You are negotiating the acceptance contract for a NeurIPS datasets-and-benchmarks paper BEFORE it is written.

PAPER PLAN (context):
{plan[:5000]}

PROPOSED ACCEPTANCE CONTRACT:
{contract}

{extra}

Push back on the contract, not the plan: (a) untestable or vibes assertions — demand checkable rewrites; (b) missing assertions — claims in the plan with no coverage, foreseeable overclaim risks; (c) assertions the evidence inventory cannot satisfy.
Be specific and brief (≤12 demands). End with exactly one line:
CONTRACT_ACCEPTED: yes    or    CONTRACT_ACCEPTED: no
followed by numbered revision demands if no."""
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
        txt = "[no text block; thinking only]\n" + "\n".join(
            c.get("thinking", "") for c in d.get("content", []) if c.get("type") == "thinking")
    trace = ROOT / ".aris" / "traces"
    trace.mkdir(parents=True, exist_ok=True)
    (trace / f"contract-review-round{round_no}.json").write_text(
        json.dumps({"model": d.get("model"), "id": d.get("id"), "text": txt}, ensure_ascii=False, indent=2))
    return txt


if __name__ == "__main__":
    extra = sys.argv[2] if len(sys.argv) > 2 else ""
    print(review(int(sys.argv[1]), extra))
