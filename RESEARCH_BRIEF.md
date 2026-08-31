# Research Brief — Physical-AI-Fusion

> 输入给 `/research-pipeline` 的详细上下文。长文档一律按路径引用,勿复制进本文件。

## Problem Statement

物理 AI(AI4Science / LLM-for-Physics)评测存在一个明显缺口:**没有侧重核聚变、尤其是惯性约束聚变(ICF)的定量 benchmark**。通用物理 benchmark(SciBench、GPQA、PHYSICS、OlympiadBench)中聚变题占比≈0;唯一已知的聚变专属 benchmark(PKU-XLab FusionBench,2026,1 star/1 commit)只有判断/选择/填空三类知识问答,无定量计算、无代码题、无答案验证流水线。ICF 的核心内容(点火物理、RT/RM 不稳定性、激光-等离子体相互作用、辐射流体力学、EOS/不透明度、内爆动力学)在任何现有 benchmark 中均缺失。

同时,现有 benchmark 的答案正确性普遍只靠出题人自查;我们拥有本地模拟/计算资产(FLASH 辐射流体、Rosseland 不透明度、Z 箍缩、脉冲电容器),可以实现"独立复算 + 双来源交叉"的验证流水线——这是方法学上的差异化护城河。

## Background

- **Field**: AI4Science / LLM Benchmark
- **Sub-area**: 核聚变物理(侧重 ICF),兼顾 MCF / Z 箍缩 / 等离子体基础
- **Key papers/resources 已调研**: 见 `docs/related-work.md`(PKU FusionBench 竞品分析、NeurIPS 2026 Fusion Equilibrium Challenge、TokaMark、LPI-LLM、SciBench/GPQA/PHYSICS 对比);出题来源清单见 `docs/sources.md`(Atzeni、Lindl、Drake、Kruer 教科书 + MRE/POP/计算物理/强激光与粒子束期刊 + LLNL/NIF 公开报告)
- **What I already tried**: 项目骨架 + 完整设计文档已就位:`docs/design.md`(题目 Schema v1、topic 体系 ICF≥50%、验证流水线 6 步、SWE-bench 式 harness 架构、M0–M6 里程碑)
- **What didn't work**: 无(项目刚完成 M0/M1)

## Constraints

- **Compute**: 本地 GPU 工作站(FLASH 算例可复跑);LLM API(Anthropic 兼容);无大规模集群
- **Timeline**: 先产出完整投稿级稿件,再定具体投稿窗口
- **Target venue**: NeurIPS(datasets & benchmarks 方向)
- **数据红线**: 仅公开资料;本地结果必须过验证流水线(staging→verified)才能入库;不收录涉密/出口管制内容

## What I'm Looking For

- [ ] New research direction from scratch
- [ ] Improvement on existing method
- [ ] Diagnostic study / analysis paper
- [x] Other: **Benchmark 构建 + Benchmark 论文**。方向已确定(见 CLAUDE.md 与本 brief),`/idea-discovery` 阶段的任务是:文献调研补全、竞品差异化核实(novelty-check 对标 PKU FusionBench 等)、在既定方向内细化 benchmark 设计决策(题目配比、难度分布、评分 rubrics),**不要推翻已定方向**。

## Domain Knowledge

- ICF 出题物理点与 topic 体系:`docs/design.md` §3(icf/ 8 个子域 + mcf/、zpinch/、plasma-basic/、fusion-engineering/、simulation/)
- 本地可验证资产(全部先经 staging 验证):
  - `~/Rosseland_opa_*`(10 个目录):Rosseland 不透明度计算管线 + Cuba 积分库 + 多版本验证结果 → eos-opacity 数值/code 题
  - `~/FLASH_GPU_hydro_lab_20260715`、`~/flash-deps`、`~/flash_eos_tools`、`~/flash-gpu-patch`:FLASH AMR 源码 + 15MA 铝套筒算例 → simulation/ code 题、rad-hydro 算例
  - `~/zpinch10000`、`~/zpinch_package_20260306`、`~/zpinch-tree`:Z 箍缩模拟与树形图应用 → zpinch/ 题
  - `~/multiagent-capacitor`(RESEARCH_BRIEF + results):脉冲电容器研究 → zpinch/ 脉冲功率题
  - `~/fusion_monitor`:聚变资讯爬虫管线(来源发现工具)
- 已有理论公式题素材:RM 不稳定性线性增长律 δv∝kyΔuη、声波耦合 e^(−kyL) 衰减律等(见 `docs/related-work.md` §3)

## Non-Goals

- 不做知识问答型 benchmark(与 PKU FusionBench 错位竞争,只做定量计算/推导/代码/图表题)
- 不做 MCF 诊断 ML 竞赛类任务(与 NeurIPS 2026 Fusion Equilibrium Challenge 错位)
- 不收录任何涉密或受出口管制的数据
- Stage 2 的"experiment"在本项目中 = benchmark 题目构造、验证流水线实现、harness 实现与 baseline 评测,而非训练模型

## Existing Results

- `docs/design.md` — 完整架构设计(对标 SWE-bench 的逐条映射)
- `docs/sources.md` — 来源清单 A–E 组(教科书/综述/竞品/本地资料/公开数据集)
- `docs/related-work.md` — 第一轮调研 + 空白定位 4 条论文卖点
- GitHub: github.com/NiubilityZXC/physical-ai-fusion(公开,持续同步)
