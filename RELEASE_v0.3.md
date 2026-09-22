# Physical-AI-Fusion v0.3.0 — Release Notes

## 亮点

- **699 道 verified 题目**(ICF 356 = 50.9%),13 个 topic,全部公开物理来源 + 本地验证资产
- **100% 确定性判分**:rubric_judge 清零;五条确定性判分路径——
  - `numeric_tolerance`(532):容差带,×10ⁿ/科学计数法/上标形式全覆盖提取
  - `exact_match`(135):单选/多选,中文粘连提取修复
  - `symbolic_equiv`(23):**代数型推导**,固定符号字母表,SymPy 符号等价(PHYSICS 做法:化简为零/常数比例/采样等价)
  - `unit_test`(8):容器内单元测试
  - `swe_patch`(1):**SWE-bench 形式**,真实 FreeGS issue #128,补丁应用 + FAIL_TO_PASS 判别(bug/fix 两态验证)
- **冒烟 699/699 = 100%**:参考答案驱动全部判分路径端到端验证
- **验证流水线**:staging→verified 晋级门,独立复算 532/532,拦截 3 个真实构造错误(Saha/Debye/aT⁴)+ 1 个数据集整体拒绝,日志公开
- **英文平行轨**:data/en/ 数字保真检查 0 失配(物理硬数字逐字符保持)
- **Baseline(进行中)**:doubao-seed-2-1-turbo 当前 87.8%(expert 79.6%,推导 16.7%——headroom 真实存在)

## 数据组成

| type | n | grading |
|---|---|---|
| numeric | 531 | numeric_tolerance |
| concept | 135 | exact_match |
| derivation | 23 | symbolic_equiv |
| code | 9 | unit_test (8) + swe_patch (1) |
| figure | 1 | numeric_tolerance |

难度:undergrad 113 / grad 373 / expert 213

## 使用

```bash
pip install -e harness/
physical-ai-fusion stats
physical-ai-fusion evaluate --predictions preds.jsonl --output results/model.json
```

## 已知限制

- 任务为中文题干(英文轨在 data/en/,v1.0 合并为双轨)
- baseline 扫描受 API 限流影响仍在补齐,完整 4 模型表在后续 patch release 更新
- code 题容器为单一 Dockerfile,per-topic 镜像在 v1.1
