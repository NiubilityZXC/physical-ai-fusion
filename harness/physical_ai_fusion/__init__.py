"""Physical-AI-Fusion evaluation harness.

SWE-bench-style: one command install, one command evaluate, deterministic
grading for numeric/concept tasks, versioned JSONL datasets.

    pip install -e harness/
    physical-ai-fusion stats
    physical-ai-fusion evaluate --predictions preds.jsonl
"""
__version__ = "0.1.0"

PACKAGE_ROOT = __file__.rsplit("/", 1)[0]
