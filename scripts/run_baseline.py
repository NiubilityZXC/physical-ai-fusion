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


def load_api_key() -> str:
    if os.environ.get("ARK_API_KEY"):
        return os.environ["ARK_API_KEY"]
    cfgp = Path.home() / ".arkcli" / "config.yaml"
    if cfgp.exists():
        try:
            import yaml
            cfg = yaml.safe_load(cfgp.read_text())
        except Exception:
            cfg = None
        if cfg:
            for k, v in cfg.items():
                if isinstance(v, str) and len(v) > 30 and ("key" in k.lower() or "token" in k.lower()):
                    return v
                if isinstance(v, dict):
                    for k2, v2 in v.items():
                        if isinstance(v2, str) and len(v2) > 30 and ("key" in k2.lower() or "token" in k2.lower()):
                            return v2
    raise SystemExit("no API key found (set ARK_API_KEY or configure ~/.arkcli/config.yaml)")


def chat(model: str, messages: list[dict], key: str, base: str, timeout: float = 120.0) -> str:
    body = json.dumps({"model": model, "messages": messages, "max_tokens": 2048,
                       "temperature": 0.2}).encode()
    req = urllib.request.Request(
        base.rstrip("/") + "/chat/completions", data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.loads(r.read())
    return data["choices"][0]["message"]["content"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--base", default="https://ark.cn-beijing.volces.com/api/plan/v3")
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
    key = load_api_key()

    tasks = [json.loads(l) for f in sorted(glob.glob(str(ROOT / "data" / args.split / "*.jsonl")))
             for l in open(f, encoding="utf-8") if l.strip()]
    todo = [t for t in tasks if t["task_id"] not in done][: args.limit]
    print(f"model={args.model} tasks={len(todo)} (skip {len(done)} already done)")
    fail = 0
    with open(out_path, "a", encoding="utf-8") as fh:
        for i, t in enumerate(todo):
            prompt = PROMPT.format(question=t["question"])
            for attempt in range(3):
                try:
                    resp = chat(args.model, [{"role": "user", "content": prompt}], key, args.base)
                    fh.write(json.dumps({"task_id": t["task_id"], "response": resp}, ensure_ascii=False) + "\n")
                    fh.flush()
                    break
                except (urllib.error.URLError, urllib.error.HTTPError, KeyError, TimeoutError) as e:
                    wait = 10 * (attempt + 1)
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
