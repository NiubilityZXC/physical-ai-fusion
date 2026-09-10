# 相关工作与空白定位(v0.1,2026-08-27 第一轮调研)

> 结论先行:**"通用物理 benchmark 多、聚变专属 benchmark 刚出现但全是知识问答型、ICF 定量计算/代码型 benchmark 是空白"** —— 这正是我们的位置。
> ⚠️ ~~命名冲突~~ **已解决(2026-08-27)**:PKU-XLab 已有 [FusionBench](https://github.com/PKU-XLab/FusionBench)(知识问答型),为避免撞名,本项目已更名为 **Physical-AI-Fusion**(仓库:github.com/NiubilityZXC/physical-ai-fusion),强调"物理 AI"大领域定位 + 聚变纵深。

## 1. 通用科学/物理 Benchmark(格式可借鉴,聚变题≈0)

| Benchmark | 内容 | 对我们的意义 |
|---|---|---|
| SciBench | 大学理科计算题(物理 217 题) | 数值题+容差评分格式借鉴 |
| GPQA (Diamond) | PhD 级选择题为 448 题,专家 81%,头部模型已 95%+ | "Google-proof" 出题原则借鉴;已饱和 → 需要新难 benchmark 的论据 |
| PHYSICS (arXiv 2503.21821) | 物理 PhD 资格考试题,SymPy 自动评分 | 开放计算题评分管线借鉴 |
| OlympiadBench | 奥赛级双语多模态 | 难度分层与标注规范借鉴 |
| ScienceEval | 聚合 11 个 benchmark 的一键评测框架 | "一键跑全套"的 UX 对标 |
| FrontierScience (OpenAI, 2025-12) | 专家级科学推理 | 最新同类工作,需持续跟踪 |

## 2. 聚变/等离子体专属(直接竞品 + 互补)

| 工作 | 类型 | 与我们的关系 |
|---|---|---|
| **FusionBench (PKU-XLab)** | 核聚变知识问答(判断/选择/填空),MIT 协议 | **直接竞品但极早期**(1 star / 1 commit / 0 fork,2026)。覆盖等离子体、MCF、激光 ICF,JSON 数据集,支持多 LLM 自动评分与分领域统计;**无人工/复算验证流程,无定量计算与代码题**。我们差异化:ICF 纵深 + 数值/推导/代码题 + 双验证流水线 + SWE-bench 式 harness。论文必须对比 |
| Fusion Equilibrium Challenge (NeurIPS 2026 Competition, Sophelio×DIII-D×UKAEA) | 托卡马克磁平衡重建竞赛,133GB 实验数据 | 证明 NeurIPS 社区对聚变 AI 有需求;它是 MCF 诊断 ML 任务,我们是物理知识/计算 benchmark,互补 |
| TokaMark robustness benchmark (arXiv 2607.11915) | MAST 11,573 次放电的诊断模型鲁棒性 | MCF 诊断侧;我们的 mcf/ 子域可引用其数据 |
| LPI-LLM (arXiv 2407.11098) | LLM+储备池预测 ICF 激光-等离子体不稳定性热电子 | ICF×LLM 应用先例,related work 引用 |

## 3. ICF 可出题公开资料(第一轮已确认存在)

- **期刊(开放/可引用)**:*Matter and Radiation at Extremes*(AIP,ICF 论文密集,如燃料离子扩散、冲击驱动内爆)、《计算物理》(LARED-S 二维辐射流体算例,含具体数值:YOC 55.2% 等)、《强激光与粒子束》(LARED 集成程序考核算例、神光Ⅲ黑腔辐射温度角分布数据)。
- **机构公开报告**:LLNL 官网技术文章(NIF tent 膜厚度系列 300→12 nm 对性能影响,POP 论文对应)。
- **理论公式题来源**:RM 不稳定性线性增长律 δv∝kyΔuη、声波耦合 e^(−kyL) 衰减律等(中国物理学会期刊),适合出推导题+数值题。
- **教科书**(待获取具体章节):Atzeni、Lindl、Drake、Kruer(见 sources.md A 组)。

## 4. 空白定位(论文卖点)

1. **题型空白**:现有聚变 benchmark 全是知识问答;没有"定量计算 + 公式推导 + 可执行代码"的聚变 benchmark。
2. **领域空白**:ICF(点火物理、RT/RM、LPI、辐射流体、EOS/不透明度)在任何现有 benchmark 中占比 ≈ 0。
3. **方法空白**:没有 benchmark 采用"本地模拟复算 + 双来源交叉"的验证流水线来保证答案正确性 —— 我们有本地 FLASH/Rosseland/zpinch 数据,这是护城河。
4. **生态空白**:SWE-bench 式"一条命令评测 + verified 子集 + 版本化 release"在物理 AI 领域尚无对应物。

## 5. 下一轮调研任务

- [x] 精读 PKU FusionBench 数据集(题目分布、ICF 占比、答案质量),写对比表 → **已完成(2026-08-31)**:全库 10,605 题(单选 4,081/多选 6,021/判断 503);无 ICF 独立类目;ICF 宽口径关键词命中 13.9% 但多为约束方式概念题;**含带单位数值的题仅 80/10,605(0.75%),定量计算题≈0**;无验证流水线;GitHub-only 无论文。对比表已入 idea-stage/IDEA_REPORT.md §B 精读框。数据集快照:docs/survey/pku-fusionbench-dataset-snapshot.json(本地,不入 git)
- [x] Atzeni 教科书具体可出题章节清单 → 已转为"标准公式出题点清单"(Lawson/triple product、RT 增长率、Takabe 修正、SBS/SRS 阈值、Marshak 波、Sedov、Saha、Rosseland 平均、NRL Plasma Formulary 15-20 式),见 IDEA_REPORT §E
- [x] NIF 点火公开数据(yield、hot spot 参数)可引用口径 → **已确认(2026-08-31)**:2022-12-05 首点火 2.05→3.15MJ(gain≈1.5);2025 序列:02-23 5.0MJ/2.44、04-07 **8.6±0.45MJ / 2.08MJ / gain 4.13(纪录,连续梯度掺杂 W:HDC)**、06-22 2.4MJ、10-01 3.5MJ/1.74(第 10 次点火)。来源 lasers.llnl.gov + LLNL FY2025 年报 → icf/ignition-gain 真实数据题
- [x] FLASH 自带验证算例(Sedov/RT/KH)清单 → simulation/ 题源 → 已确认:Sedov/Sod/RT/KH/Shu-Osher 经典算例 + Su-Olson/Marshak 辐射输运半解析解 + 本地 magnetoHD/ZPinch 15MA 铝套筒活算例(flash.par.gpu 参数全提取)
- [x] 托卡马克公开数据库(TokaMark/MAST)接入方式 → TokaMark arXiv 2602.10132(14 任务)+ 2607.11915(鲁棒性,11,573 放电)+ Fusion Equilibrium Challenge(9,121 shots,DIII-D+MAST,CC BY 4.0,HuggingFace)已登记;mcf/ 子域 v1 先用 ITER 官方参数与定标律公式题,数据集接入留 v2

## 6. 第二轮新发现的相关工作(2026-08-31,均已经 verify_papers.py 三层核验)

| 工作 | 出处 | 定位 |
|---|---|---|
| TOKAMARK (IBM×UKAEA×STFC) | arXiv 2602.10132 | MAST 托卡马克 AI benchmark,14 任务,MCF 诊断 ML 侧 |
| Offline RL for Plasma Control | arXiv 2606.07550 | 等离子体控制 RL codebase+benchmark |
| NuclearQAv2 | arXiv 2606.27047 | 核领域结构化 QA(无 ICF 定量) |
| NRC Reactor Operator Exam | arXiv 2607.22067 | 裂变堆执照考试多模态 benchmark |
| ConStellaration | (pending) | 仿星器边界数据集+优化 benchmark |
| FusionMAE | Nat. Comms. Phys. doi:10.1038/s42005-026-02626-3 | 聚变诊断控制自监督基础模型 |
| LLM-SRBench | arXiv 2504.10415 | 科学方程发现(推导题参照) |
| FEABench | arXiv 2504.06260 | 多物理 FEA 推理(代码题评分参照) |
| Towards a Large Physics Benchmark | arXiv 2507.21695 | 大规模物理题(规模参照) |
| FrontierScience (OpenAI) | cdn.openai.com(2025-12) | 奥赛+PhD 研究双轨,rubric 评分架构直接借鉴;GPT-5.2 Olympiad 77%/Research 25% |

**新颖性结论(2026-08-31)**:2024-2026 可检索范围内,**不存在第二个 ICF 定量计算/推导/代码 benchmark**;聚变专属评测均为知识问答或 MCF 诊断 ML 任务。本项目"ICF 纵深 × 定量题型 × 双验证流水线 × SWE-bench 式 harness"定位成立。
