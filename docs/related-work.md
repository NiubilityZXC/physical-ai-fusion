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

- [ ] 精读 PKU FusionBench 数据集(题目分布、ICF 占比、答案质量),写对比表
- [ ] Atzeni 教科书具体可出题章节清单
- [ ] NIF 点火公开数据(yield、hot spot 参数)可引用口径
- [ ] FLASH 自带验证算例(Sedov/RT/KH)清单 → simulation/ 题源
- [ ] 托卡马克公开数据库(TokaMark/MAST)接入方式
