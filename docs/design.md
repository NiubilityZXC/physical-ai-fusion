# Fusion-Bench 架构设计(SWE-bench 风格)

> 状态:v0.1 草案(2026-08-27)
> 目标:易用性 = SWE-bench;领域 = AI-for-Physics,侧重 ICF。

## 1. 对标分析:SWE-bench 做对了什么

| 特性 | SWE-bench 做法 | Fusion-Bench 对应设计 |
|---|---|---|
| 一条命令评测 | `python -m swebench.harness.run_evaluation --predictions_path preds.json` | `fusion-bench evaluate --predictions preds.jsonl` |
| 数据格式 | 每实例一条 JSON(instance_id, problem_statement, patch, test_patch) | 每题一行 JSONL(task_id, topic, question, answer, grading, metadata) |
| 可复现环境 | 每实例 Docker 镜像 + conda spec | 代码题:每 topic 一个 Docker 镜像;非代码题无需环境 |
| 确定性评分 | FAIL_TO_PASS/PASS_TO_PASS 单测 | 数值题容差带;代码题单测;推导题固定 judge(模型+prompt 版本锁定) |
| Verified 子集 | 人工筛选 500 题 | `data/verified/` 全部双验证(独立复算 + 交叉核对) |
| 排行榜 | 官方 leaderboard + 论文主表 | GitHub Pages 排行榜(后期),论文主表只报 verified |

## 2. 题目 Schema(v1)

```json
{
  "task_id": "icf-rt-0001",
  "schema_version": "1.0",
  "topic": "icf/rt-instability",
  "type": "numeric | derivation | concept | code | figure",
  "difficulty": "undergrad | grad | expert",
  "question": "...(支持 LaTeX/图片路径)",
  "answer": {
    "kind": "numeric",
    "value": 3.2e14,
    "unit": "neutron/sr",
    "tolerance_rel": 0.02
  },
  "grading": {
    "mode": "numeric_tolerance | unit_test | rubric_judge",
    "rubric_id": null
  },
  "metadata": {
    "source": "Atzeni & Meyer-ter-Vehn, The Physics of Inertial Fusion, Eq.(6.42)",
    "source_type": "textbook | paper | report | local_sim | local_experiment",
    "license": "fair-use-quote | cc-by | public-domain",
    "verified_by": ["independent-recompute", "cross-source"],
    "verified_at": "2026-09-01",
    "notes": "本地 FLASH 算例 Al_shell_OR1cm_15MA 复算一致"
  }
}
```

## 3. Topic 体系(初版,ICF 占大头)

```
icf/                    ← 目标占比 ≥ 50%
  ignition-gain/        点火条件、Lawson 判据、能量增益
  rt-rm-instability/    RT/RM 不稳定性、ablation 稳定化
  lpi/                  激光-等离子体相互作用(SBS/SRS/TPD/成丝)
  rad-hydro/            辐射流体力学、Marshak 波、热波
  eos-opacity/          状态方程、Rosseland/Planck 不透明度 ← 本地 Rosseland 资料
  implosion/            内爆动力学、hot spot、收敛比
  target-design/        靶丸设计、驱动对称性
  diagnostics/          中子/X 射线诊断、背光成像
mcf/                    磁约束:平衡、输运、MHD
zpinch/                 Z 箍缩、magLIF、脉冲功率 ← 本地 zpinch/capacitor 资料
plasma-basic/           等离子体基础(轨道理论、双流体、动理论)
fusion-engineering/     材料、氚增殖、包层
simulation/             计算物理题:FLASH/AMR、数值格式、验证算例 ← 本地 FLASH 资料
```

## 4. 评测 Harness 组件

```
harness/
  fusion_bench/
    __init__.py
    cli.py            # fusion-bench evaluate/inspect/stats
    grader/
      numeric.py      # 容差带评分
      code.py         # 容器内单测
      judge.py        # LLM judge(固定配置,记录 judge 版本)
    loader.py         # JSONL 加载 + schema 校验
    report.py         # 分数聚合(topic/difficulty 分层),输出 JSON + markdown
  tests/
  pyproject.toml
Dockerfile            # 单容器运行全部评测
```

- **安装**:`pip install -e harness/` 或 `docker run fusion-bench`。
- **预测格式**:`{"task_id": "...", "response": "..."}` 一行一条,与 SWE-bench 的 preds 完全同构。
- **输出**:`results.json`(总分 + 分 topic + 分难度 + per-task 明细)。

## 5. 验证流水线(staging → verified 的唯一通道)

1. **自动 schema 校验**(`scripts/validate_tasks.py`):字段、单位、量纲合理性。
2. **独立复算**(`scripts/verify_numeric.py`):数值题用独立实现(不同库/不同路径)重算,相对偏差 < 容差一半才放行。
3. **交叉核对**:答案须与 ≥2 个独立来源一致(教科书+文献,或文献+本地模拟)。
4. **本地结果专项**:本地模拟/实验数据必须先复跑确认可复现(记录 commit、输入文件 hash),再比对公认基准。
5. 全部通过后写入 `metadata.verified_by/verified_at`,从 `staging/` 移入 `verified/`。
6. `docs/verification-log.md` 记录每题验证过程,可追溯。

## 6. 里程碑

| 阶段 | 目标 | 产出 |
|---|---|---|
| M0 | 项目骨架 + ARIS 就位 | ✅ 已完成(2026-08-27) |
| M1 | 来源调研 + 现有 benchmark 空白分析 | docs/sources.md, docs/related-work.md |
| M2 | 首批 100 题(staging)+ 验证流水线跑通 | data/staging/, scripts/ |
| M3 | verified 子集 ≥ 50 题 + harness v0.1 可评测 | data/verified/, harness/ |
| M4 | baseline 评测(3-5 个主流模型) | results/ |
| M5 | NeurIPS 论文初稿(ARIS paper-writing) | paper/ |
| M6 | 审稿迭代 + 公开 release v1.0 | GitHub release |
