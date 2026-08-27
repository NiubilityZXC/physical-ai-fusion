# Fusion-Bench:面向核聚变的物理 AI Benchmark(NeurIPS 论文项目)

## 项目目标

1. 打造一个 AI-for-Physics 领域的 benchmark,侧重**核聚变**,尤其是**惯性约束聚变(ICF)**,内容占比尽量大。
2. 产出一篇 NeurIPS 论文(benchmark / datasets track)。
3. 易用性对标 SWE-bench:一条命令安装、一条命令评测、确定性评分、提供 verified 子集。
4. 全部产物同步到 GitHub(数据 + 评测框架 + 论文)。

## 内容范围

- **核心(ICF)**:点火物理与能量增益、Rayleigh–Taylor / Richtmyer–Meshkov 不稳定性、激光–等离子体相互作用(SBS/SRS/TPD)、辐射流体力学与状态方程、不透明度(Rosseland/Planck)、内爆动力学与 hot spot 物理、靶丸设计、诊断(中子/X 射线/背光)。
- **兼顾**:磁约束聚变(托卡马克平衡、输运、MHD 不稳定性)、Z 箍缩、等离子体物理基础(单次粒子轨道、双流体力学、动理论)、聚变工程(材料、氚增殖、包层)。
- **题目类型**:数值计算题(有确定解析/半解析答案)、概念辨析、公式推导、代码题(小型模拟/数据处理)、图表解读。

## 题目来源与数据治理(红线)

1. **公开资料**:教科书(Atzeni《The Physics of Inertial Fusion》、Freidberg《Plasma Physics and Fusion Energy》等)、综述文章、公开会议报告(NIF/OMEGA/神光)、公开数据集、经典模拟代码的验证算例。
2. **本地结果**:`staging/` 暂存,**必须通过验证流水线确认正确后才能进 `verified/`**,验证方式包括独立复算、双来源交叉核对、与文献值比对。
3. 每道题的元数据必须记录:`source`(出处)、`license`、`verified_by`、`verified_at`、`difficulty`、`topic`。
4. 只收录公开资料,**不收录任何涉密或受出口管制的数据**。

## 目录结构

```
paper/        NeurIPS 论文(LaTeX)
data/staging/   待验证题目(禁止直接引用)
data/verified/  已验证题目(benchmark 正式数据集,JSONL)
harness/      评测框架(SWE-bench 风格:pip install + run_evaluation CLI)
docs/         设计文档、来源清单(sources.md)、验证记录(verification-log.md)
scripts/      数据采集/验证/统计脚本
.claude/skills/  ARIS skills(符号链接,由 install_aris.sh 管理,勿手改)
```

## 工作流(ARIS 驱动)

本项目用 ARIS(Auto Research in Sleep)完成端到端研究:

1. `idea-discovery` / `research-lit` — 调研现有物理/聚变 benchmark,定位空白。
2. 题目构造:`experiment-plan` 设计题目 schema;批量构造入 `staging/`。
3. 验证:`experiment-audit` / `integrity-forensics` + `scripts/verify_*.py` 独立复算,合格者入 `verified/`。
4. `paper-plan` → `paper-writing` 撰写论文;`auto-review-loop` 迭代审稿。
5. `research-wiki` 积累所有来源与中间结论。

## 评测框架设计原则(SWE-bench 风格)

- `pip install fusion-bench` 或单容器即可运行;`fusion-bench evaluate --predictions preds.jsonl` 一条命令出分。
- 评分确定性:数值题给容差带;推导题用 rubric + LLM judge(固定 judge 模型与 prompt 版本);代码题在容器内跑单测。
- 提供 `verified` 子集(全部人工+独立复算双验证)与 `full` 全集,论文主表只报 verified。
- 数据版本化:每次 release 打 tag,JSONL 带 schema 版本号。
<!-- ARIS:BEGIN -->
## ARIS Skill Scope
ARIS skills installed in this project: 83 entries.
Manifest: `.aris/installed-skills.txt` (lists every skill ARIS installed and its upstream target).
For ARIS workflows, prefer the project-local skills under `.claude/skills/` over global skills.
Do not modify or delete files inside any skill that is a symlink (symlinks point into `/home/user/multiagent-capacitor/Auto-claude-code-research-in-sleep`).
Update with: `bash /home/user/multiagent-capacitor/Auto-claude-code-research-in-sleep/tools/install_aris.sh`  (re-runnable; reconciles new/removed skills).
<!-- ARIS:END -->
