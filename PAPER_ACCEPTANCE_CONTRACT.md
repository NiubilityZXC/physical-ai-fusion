# PAPER_ACCEPTANCE_CONTRACT — Physical-AI-Fusion (status: proposed)

每条断言必须可通过阅读最终 PDF + 仓库内结果文件机械核查。

## A. 数字可追溯性

1. 摘要/正文给出的题目总数 = `physical-ai-fusion stats` 输出的任务数(当前 106);统计口径(verified split)在正文显式说明。
2. ICF 占比 52% 可由 data/verified/ 逐题 topic 字段复算;正文给出复算方法。
3. 题型分布(62 numeric / 30 concept / 13 derivation / 1 figure)与 `physical-ai-fusion stats` 输出一致。
4. "63 道带 recompute_expr 的数值题全部通过独立复算"与 verify_numeric.py 输出(63 PASS / 0 FAIL)一致;正文引用该数字时注明日期/版本。
5. 难度分布(27 undergrad / 48 grad / 31 expert)与 stats 输出一致。
6. baseline 主表中每个分数都可由 results/*.json 的 per_task 明细复算(附复算命令);若 baseline 未能在截稿前完成,正文不得出现任何模型分数,并把 baseline 列入 Limitations 与 Future Work。
7. "PKU FusionBench 10,605 题中含带单位数值的题 80(0.75%)"给出分析脚本/快照路径(docs/survey/),并注明其快照日期与"README 声明含填空题但快照中无"的不一致。

## B. 验证流水线可核查性

8. 晋级门四步(schema 校验/独立复算/双方法要求/日志)与 scripts/*.py 的实际行为一致;正文不夸大(例如不得声称"人工双验证",实际为构造者+确定性复算+交叉来源)。
9. 三个拦截案例(Saha 修正为 0.0337、Debye 修正为 1.6623e-9 m、电容器数据集整体拒绝)与 docs/verification-log.md 及 data/verified/icf-eos-opacity.jsonl 当前内容一致。
10. 本地资产数字可核查:zpinch 10,944 行、恒等式 10,942/10,944 通过;SNOP T=58 eV Z̄=10.1716(占据分布加权=程序输出);均注明"本地模拟资产,验证方法见附录"。

## C. Harness 与可用性

11. 烟囱测试数字(参考预测在 93/93 确定性题目满分)与 results/smoke.json 一致;正文明确 13 道推导题未计入(87.7% 的构成)。
12. 所有缩写首次出现处给出全称(ICF、MCF、MHD、RT、RM、LPI、SBS、SRS、TPD、MGD、AMR、EOS、DSR、TBR 等)。
13. "SWE-bench 式"表述配特性映射表(T2),不得裸用"完全等同"措辞;明确指出不同点(rubric judge、本地数据治理)。

## D. 范围与限制

14. Limitations 至少列出 3 条真实限制:题目规模(v0.1 106 题)、推导题依赖 LLM judge(单独报告)、本地题源输出声明未复跑(仅参数题);每条配缓解计划。
15. 标题与摘要不出现 "first" 的无修饰断言;允许 "to our knowledge, the first quantitative, verification-pipelined fusion benchmark" 并配 related work 支撑句。
16. 不声称代码题/数据接入题已在 v0.1 实现(它们列入 Future Work)。

## E. 形式与合规

17. 正文 ≤ 9 页(不计参考文献),appendix 另计;NeurIPS 官方样式;匿名版可行(当前为非匿名 workshop 版也可,但样式必须是 neurips)。
18. references.bib 每条被 \cite 的条目都真实存在(arXiv id/DOI/URL 可解析);PKU FusionBench 引 GitHub URL;LLNL 数据引 lasers.llnl.gov。
19. 每图有编号、标题与来源说明(F1/F2 由脚本生成,脚本入 scripts/);表中数据与脚本输出一致。

(契约冻结前评审:ark deepseek-v4-pro 跨族评审 1-3 轮)
