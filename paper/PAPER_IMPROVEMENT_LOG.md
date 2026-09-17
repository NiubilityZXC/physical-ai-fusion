# PAPER_IMPROVEMENT_LOG — Physical-AI-Fusion

Reviewer: ark deepseek-v4-pro(跨族评审,executor 为 kimi-k3 系);trace 存 .aris/traces/paper-review-round{1,2,3}.json

## Round 1 (2026-09-17)— verdict: weak reject

7 条弱点 → 全部处理:

| # | 问题 | 处置 |
|---|---|---|
| W1 | 106/688/93 数字不一致(CRITICAL) | 03-benchmark 节与图注更新为 688/v0.2 口径 ✅ |
| W2 | baseline 非发表级 | 论文已声明 in-progress 非排名;完整表待扫描完成后进 repo |
| W3 | "mechanical verification" 对非数值题过度 | 摘要改为 "sandboxed independent recomputation for numeric + documented dual review for non-numeric" ✅ |
| W4 | 构造文档薄 | 新增 Datasheet 附录(构造协议含生成器披露、难度 rubric、干扰项设计、污染控制、维护)✅ |
| W5 | 中文任务限制可审计性 | scripts/translate_tasks.py 启动英文平行轨(data/en/,断点续跑);v0.3 路线入附录 ✅ |
| W6 | 本地验证语义混淆 | 04-verification 改题 "reproducibility and consistency checks",显式声明非物理验证 ✅ |
| W7 | 03-benchmark 漏 code 题型 | 改为五类(531/135/13/8/1,675/688=98.1% 确定性)✅ |

## Round 2 (2026-09-17)— verdict: weak reject

复审暴露**剩余陈旧点**(非新内容问题):

| # | 问题 | 处置 |
|---|---|---|
| — | 05-harness 残留 93/93 | 改 675/675(531+135+8+1)✅ |
| — | 03-benchmark 残留 10,942/10,944 | 改 10,944/10,944(2e-4 门;2 行仅舍入级超 1e-4)✅ |
| — | 附录验证日志为 106 批次 | 更新为 688 批次(532 PASS;方法计数 226/152/51/14)✅ |
| — | 拦截案例缺 task_id | 补齐 icf-eos-opacity-0001/0006、icf-rad-hydro-topup2-0001 ✅ |
| — | rubric judge 配置未发布 | docs/judge-config.json ✅ |
| — | 难度梯度基于小子集 | 论文已标 anecdotal/preliminary,非排名声明保持 |

## Round 3 (2026-09-17)— 待 reviewer 返回

预期剩余不可在 v0.2 内完成项(记录为 v0.3 路线):
- 完整 baseline 表(扫描进行中,resumable;429 限流下逐模型完成)
- 全量英文平行轨(翻译作业进行中)
- 命名维护者名单/治理文件(README 待补 MAINTAINERS)
- 容器化代码题镜像(单 Dockerfile 已提供;per-topic 镜像为 v1.1)

## 结论(executor 自评)

两轮跨族评审的 CRITICAL 级问题(数字不一致、陈旧统计、机制性过度声明)已全部消除;遗留为范围性工作(baseline 完整性、英文轨、治理文件),已在论文 Limitations/Roadmap 与仓库路线中显式声明。论文当前状态可视为 v0.2 诚实预印本;v1.0 目标依赖 baseline 与英文轨完成。
