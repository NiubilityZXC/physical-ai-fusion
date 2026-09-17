#!/usr/bin/env python3
"""translate_tasks.py — 为 verified 题目生成英文平行文本(question_en 字段)

规则(保真红线):
  - 只翻译 question 文本;数字、公式、单位、选项 A/B/C/D 键不变
  - choice 题同时翻译 options 为 options_en
  - 输出 data/en/<原文件名>(不改动 data/verified,校验由消费方合并或直接用 en 目录)
  - 断点续跑
用法: python3 scripts/translate_tasks.py [--model doubao-seed-2-1-turbo] [--limit N]
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = (
    "把下面的核聚变物理题面忠实翻译为英文。规则:"
    "1) 所有数字、公式、物理量符号、单位保持原样(如 1.602176634e-19、n_c、cm^-3);"
    "2) 专业术语用标准英文(如 Rayleigh-Taylor instability、hot spot、hohlraum、areal density);"
    "3) 只输出翻译后的题面,不要解释,不要解题。\n\n题面:\n{q}"
)


def load_auth():
    env = json.loads((Path.home() / ".claude" / "settings.json").read_text())["env"]
    return env["ANTHROPIC_AUTH_TOKEN"], env["ANTHROPIC_BASE_URL"]


def chat(model: str, prompt: str, key: str, base: str, timeout: float = 90.0) -> str:
    body = json.dumps({"model": model, "max_tokens": 2048,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(base.rstrip("/") + "/v1/messages", data=body,
                                 headers={"Content-Type": "application/json", "x-api-key": key,
                                          "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    txt = "".join(c.get("text", "") for c in d.get("content", []))
    if not txt.strip():
        raise RuntimeError("empty text from model")
    return txt.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="doubao-seed-2-1-turbo")
    ap.add_argument("--limit", type=int, default=10**9)
    args = ap.parse_args()
    key, base = load_auth()
    outdir = ROOT / "data" / "en"
    outdir.mkdir(parents=True, exist_ok=True)
    total_done = 0
    for f in sorted(glob.glob(str(ROOT / "data/verified/*.jsonl"))):
        name = Path(f).name
        outp = outdir / name
        done_ids = set()
        if outp.exists():
            done_ids = {json.loads(l)["task_id"] for l in open(outp, encoding="utf-8") if l.strip()}
        lines = [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
        with open(outp, "a", encoding="utf-8") as fh:
            for t in lines:
                if t["task_id"] in done_ids or total_done >= args.limit:
                    continue
                q_en = None
                for attempt in range(2):
                    try:
                        q_en = chat(args.model, PROMPT.format(q=t["question"]), key, base)
                        break
                    except Exception as e:
                        print(f"  {t['task_id']} attempt {attempt+1}: {type(e).__name__}", flush=True)
                        time.sleep(5 * (attempt + 1))
                if q_en is None:
                    continue
                rec = dict(t)
                rec["question_en"] = q_en
                if t["answer"].get("kind") == "choice":
                    opts_en = {}
                    for k_, v_ in t["answer"]["options"].items():
                        for attempt in range(2):
                            try:
                                opts_en[k_] = chat(args.model, PROMPT.format(q=v_), key, base)
                                break
                            except Exception:
                                time.sleep(5)
                        else:
                            opts_en[k_] = v_
                    rec["options_en"] = opts_en
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()
                total_done += 1
                if total_done % 20 == 0:
                    print(f"  ... {total_done} translated", flush=True)
    print(f"translated total: {total_done} -> {outdir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
