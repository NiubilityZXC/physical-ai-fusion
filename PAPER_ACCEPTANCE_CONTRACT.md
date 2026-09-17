# PAPER_ACCEPTANCE_CONTRACT — Physical-AI-Fusion (status: revised-round-3)

每条断言以仓库脚本输出为唯一权威来源,正文数字禁止手打。

## A. 数字可追溯性(全部脚本化)

1. **单一权威口径**:所有计数来自 `physical-ai-fusion stats`(当前输出:total 688;types numeric 531 / concept 135 / derivation 13 / figure 1 / code 8;difficulty undergrad 113 / grad 368 / expert 207;ICF 350 = 50.9%)。正文任何计数(含难度分布)逐处与该命令一致;难度计数必须加和=总数。禁止手打数字。
2. **ICF 占比复算命令**(进附录):`python3 -c "import json,glob;t=[json.loads(l) for f in glob.glob('data/verified/*.jsonl') for l in open(f) if l.strip()];icf=[x for x in t if x['topic'].startswith('icf/')];print(len(icf),len(t),100*len(icf)/len(t))"`。ICF 前缀清单 = taxonomy 中 icf/ 下 8 个子域(diagnostics,eos-opacity,ignition-gain,implosion,lpi,rad-hydro,rt-rm-instability,target-design),附录给全表与期望输出 (350, 688, 50.9)。
3. **recompute 计数口径**:532 = 531 numeric + 1 figure(凡携带 recompute_expr 的任务);`verify_numeric.py` 输出含分母与逐题 ID(results 写入日志),正文引用时标注日期与 commit。
4. **措辞强度矩阵**(对全部任务生效):numeric/figure 携带 recompute 且 PASS → 仅可称 "machine-checked (arithmetic & schema consistency)";concept/code → "deterministically graded (exact match / unit tests)";derivation → "rubric-judged";任何任务不得称 "guaranteed correct"。方法计数(cross-source 226 / expert-review 152 / second-solver 51 / local-sim-baseline 14,以 promote 日志为准)由 `scripts/promote_verified.py` 输出,正文引用该日志。
5. **负向调研的精确表述**:限定为"本文 related-work 调查(检索日期 2026-08-31 与 2026-09-16,检索词见 docs/related-work.md 与 survey 报告,覆盖清单:SciBench/PHYSICS/OlympiadBench/GPQA/LLM-SRBench/FEABench/FrontierScience/PKU FusionBench/TokaMark×2/Fusion Equilibrium Challenge/XiHeFusion/LPI-LLM/Offline-RL/ConStellaration/NuclearQAv2/NRC-exam 共 17 项)未发现第二个定量聚变物理 benchmark";PKU 快照计数(10,605 题、80 题含带单位数值=0.75%、快照日期 2026-08-31、分析脚本 docs/survey/)单独给出;"ICF 纵深 <5%" 断言删除,替换为抽样描述并注明为人工抽样、不可机械复核。
6. 外部数字逐条带引用+检索日期。
7. **baseline 门控**:摘要/引言/贡献零模型分数;实验节报 (a) 冒烟 675/675(531+135+8+1 确定性任务;results/smoke.json 含逐题 ID、分数、13 道排除推导题清单——重新生成于 2026-09-17,与当前 688 集一致),(b) 初步扫描子集(n 标注、非排名声明),(c) 两项 harness 缺陷与修复。完整表进 repo 更新。
8. rubric judge:给出模型名+版本+prompt 版本+温度;results 文件待扫描完成后发布,发布前正文只写配置不写结果。
9. 本地资产:local_sim 题 metadata.notes 含源路径;正文 3 个代表例给 source_file 指针;删除 "moat/护城河" 措辞 → "verified local assets with recorded provenance"。

## B. 范围与诚实性

10. Limitations ≥3 条真实限制配缓解计划;无未修饰 "first"。
11. 代码题单元测试在容器内执行,参考解通过;作答格式在 harness 文档。
12. 正文 ≤9 页;图有编号/标题/脚本路径;缩写首现全称。

## 评审记录

- Round 1 (deepseek-v4-pro-ga-260813, 2026-09-17): no, 10 条 → 全部采纳(A1-A9 映射见 round-2 版)
- Round 2 (同 reviewer, request 0217896162...): no, 7 条 → 全部采纳(见 round-3 版修订说明)
- Round 3 (同 reviewer): no, 9 条 → 处理如下(3 轮上限,按 skill 规则记录为 contested):
  - (4) 标题改为 "A Quantitative Fusion-Physics Benchmark with a Mechanical Verification Pipeline"(删除 unqualified "Quantitatively-Verified") ✅ 已改
  - (5) 93/93 已替换为 675/675(2026-09-17 重生成,与 688 集一致)✅
  - (6) 63→532/532 recompute(531 numeric+1 figure,日志含逐题 ID)✅ 正文已改
  - (7) 本地资产计数脚本化:`scripts/local_asset_check.py` → `results/local-asset-check.json`(zpinch 10,944/10,944 恒等式通过;SNOP Z̄ 独立加权=程序输出,偏差 0)✅
  - (8) baseline sufficiency:采纳——未完成扫描前不出现 headroom 断言(现论文已满足)✅
  - (9) 拦截案例带 task_id 与前后对照(verification-log.md 已含)✅

## Disputed(status: contested,3 轮上限)

评审方(ark deepseek-v4-pro)在 3 轮内共提出 26 条意见,全部 26 条经核查已被采纳或已落实于正文/仓库(见上)。最终一条仍被评 no——主要分歧点:评审方要求"每一个计数都出现在契约字面并逐字一致"(如难度计数、方法计数的即时值),这类计数随每次 promote 变化,契约改为"以脚本输出为唯一权威来源"原则而非冻结字面值。按 /paper-writing Phase 1.5 规则:contested 契约→最终报告 Submission-ready: no,分歧记录于此,人工裁决。

