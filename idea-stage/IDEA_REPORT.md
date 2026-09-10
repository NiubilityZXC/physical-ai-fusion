# Idea Discovery Report — Physical-AI-Fusion

**Direction**: 物理 AI × 核聚变定量 benchmark(侧重惯性约束聚变 ICF)+ NeurIPS 论文
**Date**: 2026-08-31
**Pipeline**: research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline
**Run ID**: physical-ai-fusion-20260831
**状态**: Phase 1(文献调研)完成,方向已由 RESEARCH_BRIEF.md 锁定(不推翻,只细化)

## Executive Summary

在既定方向(核聚变定量 benchmark,ICF 占比 ≥50%,SWE-bench 式易用性,双验证流水线)内,第二轮文献调研确认了四个空白依然成立,并用硬数据加固:(1) 唯一直接竞品 PKU-XLab FusionBench(10,605 题,纯知识问答)ICF 物理题占比仅 ~14%(宽口径)且其中绝大多数是"约束方式概念"级题目,定量计算题占比 <1%(全库仅 80 题含带单位数值);(2) 聚变×AI 的 NeurIPS 社区需求已被 Fusion Equilibrium Challenge(9,121 shots,CC BY 4.0)证实,但它是 MCF 诊断 ML 竞赛,与物理知识/计算 benchmark 互补;(3) 通用物理 benchmark(SciBench/PHYSICS/GPQA/OlympiadBench/FEABench/PhysReason)聚变题 ≈ 0,且 GPQA 已被头部模型饱和(GPT-5.2 92%),社区需要新的难 benchmark;(4)  FrontierScience(OpenAI, 2025-12)的 rubric 评分架构与 SWE-bench 的 harness 范式提供了可直接借鉴的两块拼图,但均无聚变内容。**结论:按既定方向推进,差异化定位"ICF 纵深 × 定量/推导/代码题 × 双验证流水线 × SWE-bench 式 harness"。**

## Literature Landscape

### A. 通用科学/物理 benchmark(格式借鉴,聚变题≈0)

| 论文 | arXiv | 任务类型 | 评分机制 | 规模 | 与本项目关系 |
|---|---|---|---|---|---|
| SciBench (Wang et al., 2023) ✅ | 2307.10635 | 大学理科计算题(含物理 217 题) | 数值答案+容差,CoT prompt 研究 | ~700 | 数值题容差评分格式直接借鉴 |
| PHYSICS (Feng et al., 2025) ✅ | 2503.21821 | 物理 PhD 资格考试题 | SymPy 自动等价判定 | ~1.3k | 开放计算题自动评分管线借鉴 |
| OlympiadBench (He et al., 2024) ✅ | 2402.14008 | 奥赛级双语多模态 | 人工+rubric | 8.4k | 难度分层与标注规范借鉴 |
| GPQA (Rein et al., 2023) ✅ | 2311.12022 | PhD 级选择题 448 | 准确率 | 448 | 已饱和(GPT-5.2 92%)→ 新难 benchmark 的论据 |
| LLM-SRBench (2025) ✅ | 2504.10415 | 科学方程发现 | 符号等价 | ~240 | 推导题题型参照 |
| FEABench (2025) ✅ | 2504.06260 | 多物理 FEA 推理 | 代码执行+结果比对 | ~200 | 计算物理代码题评分借鉴 |
| Towards a Large Physics Benchmark (2025) ✅ | 2507.21695 | 大规模物理题 | 混合 | >10k | 规模参照;仍无聚变纵深 |
| PhysReason(2025)⚠️pending | — | 物理推理 | 过程评分 | — | 过程评分借鉴 |
| SWE-bench (Jimenez et al., 2023) ✅ | 2310.06770 | 真实 GitHub issue 修复 | FAIL_TO_PASS 单测 | 2.3k | **整体范式对标**(harness、verified 子集、一条命令评测) |
| FrontierScience (OpenAI, 2025-12) ⚠️web-only | cdn.openai.com | 奥赛+PhD 研究双轨 | **rubric 评分架构** | 700+ | 推导题 rubric judge 设计直接借鉴;GPT-5.2 Olympiad 77%/Research 25% |

### B. 聚变/等离子体专属 benchmark 与数据集(直接竞品+互补)

| 工作 | 出处 | 类型 | 与本项目关系 |
|---|---|---|---|
| **PKU-XLab FusionBench** ⚠️GitHub-only | github.com/PKU-XLab/FusionBench (MIT) | 聚变知识问答 10,605 题(单选 4,081/多选 6,021/判断 503) | **直接竞品,已精读**(见下方精读框):无定量/代码题、无验证流水线、ICF 物理纵深不足 |
| TOKAMARK (IBM×UKAEA×STFC, 2026) ✅ | 2602.10132 | MAST 托卡马克 AI 模型 benchmark,14 任务 | MCF 诊断 ML 侧;互补,mcf/ 子域可引用 |
| TokaMark robustness (2026) ✅ | 2607.11915 | MAST 11,573 放电诊断鲁棒性 | 同上 |
| Fusion Equilibrium Challenge (NeurIPS 2026 Competition) ⚠️web-only | fusion-equilibrium-challenge.sophelio.io | 磁平衡重建竞赛;9,121 shots(DIII-D 7,915 + MAST 1,206),CC BY 4.0,HuggingFace ~98-133GB | NeurIPS 社区对聚变 AI 需求的直接证据;竞赛≠知识 benchmark,互补 |
| Offline RL for Plasma Control (2026) ✅ | 2606.07550 | 等离子体控制 RL codebase+benchmark | 控制侧;互补 |
| ConStellaration ⚠️pending | — | 类 QI 仿星器边界数据集+优化 benchmark | MCF 数据集,可改造出题 |
| NuclearQAv2 (2026) ✅ | 2606.27047 | 核领域结构化 QA | 核工程 QA;无 ICF 定量 |
| NRC Reactor Operator Licensing Exam (2026) ✅ | 2607.22067 | 裂变堆执照考试多模态 benchmark | 裂变侧;证明"核领域考试题"路线可行 |
| FusionMAE (Nat. Comms. Phys. 2026) ✅ doi:10.1038/s42005-026-02626-3 | — | 聚变诊断控制自监督预训练大模型 | 应用侧 |
| AI foundation models for experimental fusion tasks ✅ doi:10.3389/fphy.2024.1531334 | — | 聚变实验任务基础模型 | 应用侧 |

**PKU FusionBench 精读(2026-08-31,数据集快照存 `docs/survey/pku-fusionbench-dataset-snapshot.json`,8.8MB,不入 git)**:
- 总量 10,605 题;题型:multiple_choice 6,021 / single_choice 4,081 / true_false 503(README 提到填空题,快照中无)。
- 领域分布:Plasma Instabilities 2,319 / Transport 2,187 / Waves 2,152 / Fusion Device Concepts 880 / Heating & Current Drive 636 / PFC & Divertor 524 / Nonlinear 495 / Neutronics & Blanket 351 / Diagnostics & Control 289 / 其余 <300 —— **分类体系无 ICF 独立类目**。
- ICF 相关题:宽口径关键词(inertial/ignition/hohlraum/implosion/ablation/hot spot/NIF/OMEGA/Lawson 等,含选项文本)命中 1,473(13.9%),抽样核查其中大量为"约束方式辨析"级概念题(如"哪些方法可实现压缩加热"),**真正 ICF 物理纵深题(点火条件定量、RT/LPI 计算、内爆动力学)占比估计 <5%**。
- 含带单位数值的题仅 80/10,605(0.75%)→ **定量计算题基本为零**。
- 无人工/独立复算验证流程;答案随题库发布,正确性靠出题方自查。
- 结论:本项目与其错位竞争成立 —— 题型(定量/推导/代码)× 纵深(ICF)× 验证流水线三个维度均不重叠。

### C. 聚变×AI 模型与应用(论文引言/related work 引用素材)

| 工作 | arXiv/出处 | 要点 |
|---|---|---|
| LPI-LLM (Chen et al., 2024) ✅ | 2407.11098 | LLM+储备池预测 ICF 激光-等离子体不稳定性热电子;ICF×LLM 先例 |
| XiHeFusion (2025) ✅ | 2502.05615 | 聚变科学传播 LLM + 180+ 题聚变评估集(知识型) |
| Challenges & opportunities for AI in fusion energy (2026) ✅ | 2603.25777 | 综述:AI 在聚变的机会清单,可作引言宏观论据 |
| CFETR/HFRC MHD 设计分析 ✅ | 2107.11742 | mcf/ 题源素材 |
| Fusion GPT 1.5B(SC24 workshop) | tpc.dev | 聚变领域小模型先例 |

### D. 可出题物理文献(problem mining 源)

| 论文 | arXiv | 可出题点 |
|---|---|---|
| Rayleigh–Taylor instability in multiple finite-thickness fluid layers ✅ | 2403.12271 | RT 增长率变体推导题 |
| Fuel target implosion in ion-beam ICF ✅ | 1504.01831 | 重离子 ICF 内爆概念/数值题 |
| Magnetized plasma target for PJMIF ✅ | 1803.03323 | 磁惯性约束概念题 |
| ViDA: Vlasov-Darwin solver ✅ | 1905.02953 | 动理论模拟 code 题素材 |
| Deep Learning and Computational Physics (Lecture Notes) ✅ | 2301.00942 | simulation/ 教学算例 |

### E. 出题素材的公开数据源(第二轮确认)

- **NIF 点火公开序列**(LLNL 官网,可引用):2022-12-05 首次点火 2.05MJ→3.15MJ(gain≈1.5);2025 年序列:02-23 5.0MJ(gain 2.44)、**04-07 8.6±0.45MJ / 2.08MJ / gain 4.13(历史纪录,连续梯度掺杂 W:HDC 靶丸)**、06-22 2.4MJ(LANL burning plasma)、10-01 3.5MJ(gain 1.74,第 10 次点火+钚生存能力实验)。来源:lasers.llnl.gov 新闻稿 + LLNL FY2025 年报。→ `icf/ignition-gain` 真实数据题。
- **NRL Plasma Formulary**(公开 PDF,US Naval Research Lab):标准公式库(plasma frequency、Larmor radius、Debye length、Coulomb logarithm、braking/thermalization 尺度)→ `plasma-basic/` 出题基准。
- **教科书标准公式**:Atzeni(ignition/gain 曲线、间接驱动能量学)、Lindl(hot spot 判据)、Drake(HEDP 标度)、Kruer(LPI 阈值)、Zel'dovich(冲击波/自相似)、Freidberg(β 极限、Greenwald、IPB98(y,2) 定标)。
- **FLASH 自带验证算例**(Sedov/Sod/RT/KH)+ Su-Olson/Marshak 辐射输运半解析解 → `simulation/` 代码题基准。
- **不透明度/EOS 公开数据**:NIST ASD(电离能)、OPEN-ADAS、TOPS/OPAL 公开表 → `eos-opacity` 数据源。
- **ITER 官方参数**(iter.org Facts & Figures):R=6.2m、a=2.0m、B=5.3T、I=15MA、Q=10、500MW → `mcf/`、`fusion-engineering/` 真实数据题。

## Ranked Ideas → 设计决策(Phase 2,2026-09-01)

> 方向已由 RESEARCH_BRIEF 锁定("不要推翻已定方向")。本阶段在既定方向内完成关键设计决策。
> 过程说明:idea-creator 标准流程的 GPT-5.6-Sol xhigh 头脑风暴环节因本机无 Codex MCP 而不可达;
> 按 ARIS 跨族评审原则,设计决策由 executor(kimi-k3)分析提出,将在 Phase 4 由跨族模型(ark 端点,非 kimi 族)做对抗性评审。

### D1. v1 规模与 topic 配比(staging 100 题,verified ≥50)

| topic | 题数 | 占比 | 说明 |
|---|---|---|---|
| icf/ignition-gain | 8 | | Lawson、triple product、NIF 真实序列能量学 |
| icf/rt-rm-instability | 7 | | RT/RM 增长率、Takabe 修正、Atwood 数 |
| icf/lpi | 6 | | SBS/SRS/TPD 阈值、四分之一临界密度 |
| icf/rad-hydro | 7 | | Marshak 波、热波、冲击波关系 |
| icf/eos-opacity | 7 | | Saha、Rosseland/Planck 平均、本地平均原子模型 |
| icf/implosion | 7 | | 收敛比、hot spot、面密度、Kidder 模型 |
| icf/target-design | 5 | | 靶丸结构、间接驱动能量学 |
| icf/diagnostics | 5 | | 中子产额/谱、X 射线、背光 |
| **icf/ 小计** | **52** | **52%** | ✓ ≥50% 红线 |
| zpinch/ | 12 | 12% | 本地零维数据集(已验证)+ 脉冲功率 + MRT |
| mcf/ | 12 | 12% | ITER 参数、β 极限、Greenwald、IPB98(y,2) |
| plasma-basic/ | 12 | 12% | NRL Formulary 标准公式 |
| fusion-engineering/ | 6 | 6% | 氚增殖、包层、第一壁 |
| simulation/ | 6 | 6% | Sedov/Sod/RT 解析解 + FLASH 设置解读 |
| **合计** | **100** | | |

### D2. 题型与评分方式(确定性优先)

| 题型 | 占比 | grading |
|---|---|---|
| numeric | ~55% | `numeric_tolerance`(相对容差带,默认 2%;题目注明) |
| concept | ~20% | `exact_match`(多选/判断,选项固定) |
| derivation | ~15% | `rubric_judge`(借鉴 FrontierScience granular rubric:每题 5-8 个评分点,judge 模型+prompt 版本锁定,通过阈值 ≥80% 得分点) |
| code | ~7% | `unit_test`(容器内 pytest,数值断言) |
| figure | ~3% | v1 少量(图表读数,按 numeric_tolerance) |

主表只报 numeric+concept+code(全确定性);rubric_judge 题单独成行报告。

### D3. 难度分布

undergrad 30% / grad 45% / expert 25%。expert 题特征:多步链式定量(如 NIF 能量学:激光→x 光转换→烧蚀压力→内爆速度→产额)、需重跑本地代码(Rosseland Fortran)、或需综合 ≥3 个公式。

### D4. 本地数据行题构造规则(zpinch/)

1. 从 10,944 行按 (I, tr, m) 分层抽样;
2. 答案取数据行原值,默认容差 ±2%;
3. 题目给出 I/tr/几何/m,求 E 或 v(不给出另一输出);
4. 每题双重验证:(a) E=½mv² 恒等式(已 99.98% 通过);(b) 独立代理模型(RandomForest 交叉验证 E_MAPE 6.85%)预测值须在 7% 内与数据行一致,否则该样本剔除不用;
5. 元数据标注 `source_type: local_sim` + 验证证据。

### D5. 教科书/公开公式题构造规则

1. 仅用公开讲义/NRL Plasma Formulary/期刊公开公式;不复制教科书原文段落;
2. 题目自包含(给出全部常数与单位制);
3. 答案由构造者计算 + `scripts/verify_numeric.py` 独立路径复算(不同库/不同化简路径),相对偏差 < 容差一半才放行;
4. 概念题选项须"Google-proof":错误选项为常见误解(量纲错、系数错、条件错)。

### D6. Schema v1.0 冻结

沿用 design.md §2,增补:`answer.kind ∈ {numeric, choice, expression, rubric, code}`;code 题含 `code: {entry_point, test_file, timeout_s}`;每题 `verification: {methods: [...], evidence: {...}, verified_by: [...], verified_at}`。JSONL 一行一题,`schema_version: "1.0"`。

### D7. 里程碑映射(本项目"experiment"= benchmark 构造)

- E1: `scripts/validate_tasks.py` + `scripts/verify_numeric.py`(验证流水线)
- E2: staging 100 题(按 D1 配比)
- E3: 验证 → verified ≥50 题 + verification-log
- E4: harness v0.1(pip 包 + evaluate CLI + 确定性评分)
- E5: baseline(ark 端点 2-3 个模型,verified 子集)
- E6: 论文 + GitHub release v0.1.0

## Novelty Verification

> Phase 3(2026-08-31,两轮并发工作检索:2024-01 至 2026-08,arXiv + GitHub + NeurIPS 2025/2026 D&B 轨道)

**核查结论:"ICF 定量物理 benchmark + 双验证流水线 + SWE-bench 式 harness"组合未发现先例。新颖性成立(置信度 high)。**

| 检索到的最近邻 | 是什么 | 为什么不是我们要做的 |
|---|---|---|
| Co4ICF (KDD 2026, SJTU; HF 数据集 Oyhs/Co4ICFDataset) | ICF 物理信息代理模型 + RL 脉冲波形优化 | ML 优化方法+模拟数据集,非知识/定量 QA benchmark |
| LPI4AI (LPI-LLM 所用, 2024) | ICF 激光-等离子体不稳定性模拟数据集 | 时间序列预测数据集,非物理知识评测 |
| JAG ICF dataset (LLNL/macc, GitHub) | ICF 多模态模拟数据集 | ML 训练数据,无 QA/评分 |
| PDE foundation model ICF 逆估计 (2603.04606)、joint diffusion ICF (2601.21006) | ICF 模拟×基础模型 | 方法论文,非 benchmark |
| PKU-XLab FusionBench (2026, GitHub-only) | 聚变知识问答 10,605 题 | 无定量/推导/代码;无验证流水线;ICF 纵深 <5% |
| NuclearQAv2 (2606.27047) | 核领域结构化 QA | 裂变/核工程,无 ICF 定量 |
| Physics-o1 (NeurIPS 2026 D&B 投稿) | 奥赛物理语料 + 评测 harness CLI | 通用物理,聚变≈0;harness 设计可借鉴 |
| QuantiPhy (NeurIPS 2026 Competition, Stanford) | VLM 定量物理(视频尺度/速度估计) | 视觉模态,无聚变 |
| FrontierScience (OpenAI 2025-12) | 专家级科学推理双轨 | 通用科学;rubric 架构可借鉴 |
| PHYBench / SEEPHYS (NeurIPS 2025 D&B) | 物理感知/视觉推理 | 无聚变内容 |

**三条护城河复核**:(1) 题型:定量/推导/代码题在聚变领域无先例 ✅;(2) 验证:双验证流水线(独立复算+跨源核对)在科学 benchmark 中未见系统实现(SWE-bench Verified 是人工筛选,非独立复算)✅;(3) 领域:ICF 在任何 QA benchmark 中占比 <5% ✅。

**风险登记**:Co4ICF/LPI4AI 等 ICF×ML 数据集若未来扩展出 QA 轨道将构成竞争 → 论文 related work 需明确"模拟数据集 ≠ 知识 benchmark"的分野,并强调我们可吸收其公开数据出题(互补而非对立)。

## External Critical Review

_(待 Phase 4 填充)_

## Refined Proposal

_(待 Phase 4.5 填充,将链接 refine-logs/FINAL_PROPOSAL.md)_

## Next Steps

- [x] Phase 1 research-lit(本报告 Literature Landscape)
- [ ] Phase 2 idea-creator:在既定方向内细化设计决策(题目配比/难度/rubric 选型)+ 本地资料盘点结论纳入
- [ ] Phase 3 novelty-check(对标 PKU FusionBench、NuclearQAv2、FrontierScience)
- [ ] Phase 4 research-review(跨模型评审)
- [ ] Phase 4.5 research-refine-pipeline → EXPERIMENT_PLAN(=benchmark 构造/验证/harness/baseline 的执行计划)
- [ ] 主任务线:staging 题目构造 → 验证流水线 → harness → baseline → 论文
