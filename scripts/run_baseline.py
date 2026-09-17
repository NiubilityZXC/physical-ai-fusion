#!/usr/bin/env python3
"""run_baseline.py — 在 verified 子集上跑模型 baseline(ark plan 端点)

用法:
    python3 scripts/run_baseline.py --model doubao-seed-2-1-turbo \
        --output results/baseline-doubao-seed-2-1-turbo.jsonl [--limit 106]

    API key 读取顺序: env ARK_API_KEY -> ~/.arkcli/config.yaml(字段含 key/token)
    绝不打印密钥。预测文件可断点续跑(已存在的 task_id 跳过)。
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROMPT = (
    "你是一名核聚变/等离子体物理专家。请解答下面这道题,给出简要推理过程,"
    "并在最后单独一行给出最终答案,格式严格为:\n"
    "Final answer: <数值+单位>  或  Final answer: <选项字母,如 A, C>\n\n"
    "题目:\n{question}"
)


def load_auth() -> tuple[str, str]:
    """返回 (token, base_url)。顺序: ~/.claude/settings.json env -> env -> ~/.arkcli/config.yaml"""
    sp = Path.home() / ".claude" / "settings.json"
    if sp.exists():
        try:
            env = json.loads(sp.read_text()).get("env", {})
            if env.get("ANTHROPIC_AUTH_TOKEN") and env.get("ANTHROPIC_BASE_URL"):
                return env["ANTHROPIC_AUTH_TOKEN"], env["ANTHROPIC_BASE_URL"]
        except Exception:
            pass
    if os.environ.get("ARK_API_KEY"):
        return os.environ["ARK_API_KEY"], os.environ.get("ARK_BASE_URL", "https://ark.cn-beijing.volces.com/api/plan")
    raise SystemExit("no auth found (~/.claude/settings.json env / ARK_API_KEY)")


def chat(model: str, messages: list[dict], key: str, base: str, timeout: float = 90.0) -> str:
    """Anthropic /v1/messages(x-api-key)优先,失败后回退 OpenAI /chat/completions。"""
    flat = "\n\n".join(m["content"] for m in messages if m["role"] == "user")
    body = json.dumps({"model": model, "max_tokens": 1024,
                       "messages": [{"role": "user", "content": flat}]}).encode()
    try:
        req = urllib.request.Request(
            base.rstrip("/") + "/v1/messages", data=body,
            headers={"Content-Type": "application/json", "x-api-key": key,
                     "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read())
        return "".join(c.get("text", "") for c in data.get("content", []))
    except urllib.error.HTTPError as e:
        if e.code not in (401, 404):
            raise
    # fallback: OpenAI style on <base>/v3
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": flat}],
                       "max_tokens": 1024, "temperature": 0.2}).encode()
    req = urllib.request.Request(
        base.rstrip("/") + "/v3/chat/completions", data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.loads(r.read())
    return data["choices"][0]["message"]["content"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--base", default=None, help="override resolved base url (default: from auth source)")
    ap.add_argument("--output", default=None)
    ap.add_argument("--limit", type=int, default=10**9)
    ap.add_argument("--split", default="verified")
    args = ap.parse_args()

    out_path = Path(args.output or f"results/baseline-{args.model}.jsonl")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    done: set[str] = set()
    if out_path.exists():
        for line in out_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["task_id"])
    key, base = load_auth()
    if args.base:
        base = args.base

    tasks = [json.loads(l) for f in sorted(glob.glob(str(ROOT / "data" / args.split / "*.jsonl")))
             for l in open(f, encoding="utf-8") if l.strip()]
    todo = [t for t in tasks if t["task_id"] not in done][: args.limit]
    print(f"model={args.model} tasks={len(todo)} (skip {len(done)} already done)")
    fail = 0
    with open(out_path, "a", encoding="utf-8") as fh:
        for i, t in enumerate(todo):
            qtext = t["question"]
            if t["answer"].get("kind") == "choice":
                opts = "\n".join(f"{k}. {v}" for k, v in t["answer"]["options"].items())
                qtext = qtext + "\n\n选项:\n" + opts
            prompt = PROMPT.format(question=qtext)
            for attempt in range(2):
                try:
                    resp = chat(args.model, [{"role": "user", "content": prompt}], key, base)
                    fh.write(json.dumps({"task_id": t["task_id"], "response": resp}, ensure_ascii=False) + "\n")
                    fh.flush()
                    break
                except Exception as e:
                    wait = 5 * (attempt + 1)
                    print(f"  [{i+1}/{len(todo)}] {t['task_id']} attempt {attempt+1} failed: {type(e).__name__} {e} — retry in {wait}s",
                          flush=True)
                    time.sleep(wait)
            else:
                fail += 1
                print(f"  [{i+1}/{len(todo)}] {t['task_id']} FAILED permanently", flush=True)
            if (i + 1) % 10 == 0:
                print(f"  ... {i+1}/{len(todo)} done", flush=True)
    print(f"written: {out_path} (failures: {fail})")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
