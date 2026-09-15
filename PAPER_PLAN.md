# PAPER_PLAN — Physical-AI-Fusion (NeurIPS 2026, Datasets & Benchmarks)

## Title(候选)

**Physical-AI-Fusion: A Quantitatively-Verified Physics Benchmark for Nuclear Fusion with an Inertial-Confinement Focus**

## 一句话定位

> 第一个聚焦核聚变——尤其惯性约束聚变(ICF)——的定量计算 benchmark;每题答案经独立复算+交叉来源双验证;评测易用性对标 SWE-bench(pip install + 一条命令评测 + verified 子集 + 确定性评分)。

## Claims–Evidence Matrix

| # | Claim | Evidence(文件/表) |
|---|---|---|
| C1 | 现有物理/科学 benchmark 中聚变(尤其 ICF)定量内容≈0 | related-work.md §1-2;IDEA_REPORT §A;PKU FusionBench 精读:10,605 题中含带单位数值题仅 80(0.75%),ICF 纵深题 <5%(docs/survey 快照分析) |
| C2 | Physical-AI-Fusion 提供 106 道双验证定量题,ICF 占 52% | data/verified/(13 文件,106 题);统计见 results/stats;topic 分布图 F1 |
| C3 | 答案正确性由机械化流水线保证:schema 校验 + 独立复算 + 晋级门 + 日志 | scripts/validate_tasks.py、verify_numeric.py(63 numeric PASS/0 FAIL)、promote_verified.py、docs/verification-log.md |
| C4 | 流水线真实拦截错误(不是装饰) | verification-log:2 个构造者算术滑移被拦截修正(Saha、Debye);电容器数据集整体被拒 |
| C5 | 本地模拟资产可转化为 benchmark 题(护城河) | docs/survey/local-materials.md:zpinch 10,944 行 E=½mv² 一致性 10,942/10,944;SNOP Z̄ 独立加权=程序输出(0 偏差);FLASH 算例参数 |
| C6 | SWE-bench 式易用性 | harness/:pip install -e + `physical-ai-fusion evaluate --predictions`;烟囱测试 93/93 deterministic PASS;Dockerfile |
| C7 | baseline 显示当前模型在 expert 题上有显著不足(headroom) | results/baseline-*.jsonl + results/*.md(待补:ark 端点 2-3 模型) |

## Section 结构(8 sections + appendix)

1. **Introduction**(1 页):AI4Science 评测缺口;GPQA 饱和(GPT-5.2 92%)需要新难 benchmark;聚变是物理 AI 的高价值试验场;四点贡献(benchmark、验证流水线、harness、baseline)。
2. **Related Work**(0.75 页):通用科学 benchmark(SciBench/PHYSICS/GPQA/OlympiadBench/FEABench/FrontierScience);聚变专属(PKU FusionBench 精读、TokaMark、Fusion Equilibrium Challenge、XiHeFusion、LPI-LLM);空白定位。
3. **The Physical-AI-Fusion Benchmark**(1.5 页):topic 体系(ICF 8 子域+5 领域);题型(numeric/concept/derivation/figure);schema v1.0;题目统计表 T1 + 分布图 F1;两道示例题(Box 1)。
4. **Verification Pipeline**(1.25 页):staging→verified 晋级门四步;recompute_expr 独立复算机制;本地数据治理(物理恒等式、字节级基线复跑);拦截案例(Box 2 三个真实案例);与"出题人自查"惯例对比。
5. **Evaluation Harness**(0.75 页):SWE-bench 映射表 T2;CLI;确定性评分(数字/选项抽取规则);rubric judge(锁定模型+prompt,单独报告);Docker。
6. **Experiments**(0.75 页):设置(模型、prompt、温度);主表 T3(分 topic/难度/题型);rubric 题单独行;失败模式分析(单位错、公式错选、数值精度、热电子类概念混淆)。
7. **Discussion & Limitations**(0.5 页):规模(106 题 v0.1 vs 目标千题)、推导题 judge 依赖、本地题源的不可复算部分只用于参数题、无双语对照;扩展路线(code 题、数据题接入 TokaMark/ConStellaration)。
8. **Conclusion**(0.25 页)。
- **Appendix**:A. 完整 topic 定义与示例;B. 数据来源与许可清单;C. 验证日志摘录;D. harness 使用手册;E. 额外 baseline 明细。
- **Checklist**:NeurIPS D&B checklist(必须)。

## 图/表计划

| ID | 内容 | 数据源 | 生成方式 |
|---|---|---|---|
| F1 | topic×type 堆叠条形图(ICF 52% 高亮) | data/verified/ 统计 | matplotlib(scripts/gen_fig_topic_dist.py) |
| F2 | 验证流水线流程图(staging→4 门→verified,含拦截支路) | design.md §5 | matplotlib/figure-spec |
| F3 | baseline 主结果条形图(分难度) | results/baseline-*.jsonl | matplotlib(待 baseline) |
| T1 | 题目统计(topic×type×difficulty) | data/verified/ | LaTeX 表格(脚本生成) |
| T2 | SWE-bench 特性映射表 | design.md §1 | 手写 |
| T3 | baseline 主结果表 | results/ | 脚本生成 |
| Box1 | 两道示例题(1 numeric 经复算 + 1 derivation rubric) | data/verified/ | 摘录 |
| Box2 | 拦截案例三则(Saha/Debye/电容器) | verification-log.md | 摘录 |

## 引用骨架(references.bib,~25 条)

benchmark 类:SWE-bench(2310.06770)、SciBench(2307.10635)、GPQA(2311.12022)、PHYSICS(2503.21821)、OlympiadBench(2402.14008)、FEABench(2504.06260)、LLM-SRBench(2504.10415)、FrontierScience(OpenAI 2025)
聚变×AI:PKU FusionBench(GitHub)、TokaMark(2602.10132;2607.11915)、Fusion Equilibrium Challenge(官网)、LPI-LLM(2407.11098)、XiHeFusion(2502.05615)、Offline RL Plasma Control(2606.07550)、AI for fusion energy(2603.25777)、FusionMAE(doi:10.1038/s42005-026-02626-3)
物理:Atzeni、Lindl、Drake、Kruer、Zel'dovich、Freidberg、NRL Plasma Formulary、Takabe 1985、Sedov/Taylor、NIF 点火(LLNL 2022/2025 新闻稿)、ITER 官网

## 页面预算

正文 ≤ 9 页(NeurIPS 2026 D&B:正文 9 页 + 参考文献不限)+ appendix。当前规划正文约 7.5 页,留改进余量。

## 风险与备选

- baseline 若因 API 配额缺失:正文先写 harness 烟囱结果 + 留出 baseline 表占位,API 恢复后补(reviewer 会要求 baseline,优先补齐)。
- NeurIPS 模板:使用官方 neurips_2026.sty(若本机无,则用 neurips_2024/2025 兼容版并在投稿前替换)。
