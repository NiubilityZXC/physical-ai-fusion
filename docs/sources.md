# Fusion-Bench 题目来源清单

> 每条来源状态:`待调研 | 已确认可用 | 已采题 | 已排除(原因)`
> 采题红线:仅公开资料;每题记录 license;本地结果必须过验证流水线(见 design.md §5)。

## A. 教科书 / 专著(ICF 核心)

| # | 来源 | 覆盖 topic | 状态 |
|---|---|---|---|
| A1 | Atzeni & Meyer-ter-Vehn, *The Physics of Inertial Fusion* (2004) | icf/ 全部,尤�其 ignition-gain, rad-hydro, implosion | 待调研 |
| A2 | Lindl, *Inertial Confinement Physics* (1998) | icf/lpi, target-design | 待调研 |
| A3 | Freidberg, *Plasma Physics and Fusion Energy* (2007) | mcf/, plasma-basic/ | 待调研 |
| A4 | Zel'dovich & Raizer, *Physics of Shock Waves* | rad-hydro, eos-opacity | 待调研 |
| A5 | Drake, *High-Energy-Density Physics* (2018) | rad-hydro, lpi, diagnostics | 待调研 |
| A6 | Kruer, *The Physics of Laser Plasma Interactions* | icf/lpi | 待调研 |
| A7 | Liberman et al., *The Physics of High-Density Z-Pinch Plasmas* | zpinch/ | 待调研 |

## B. 综述 / 公开报告

| # | 来源 | 覆盖 topic | 状态 |
|---|---|---|---|
| B1 | NIF / LLNL 公开报告与点火综述(Nature 2022 点火论文及后续) | ignition-gain, diagnostics | 待调研 |
| B2 | OMEGA / LLE 公开实验报告 | implosion, rt-rm-instability | 待调研 |
| B3 | 神光系列公开论文(强激光与粒子束、MRE 期刊) | icf/ 多 topic | 待调研 |
| B4 | IAEA / ITER 公开技术文档 | mcf/, fusion-engineering | 待调研 |
| B5 | *Matter and Radiation at Extremes*、*Nuclear Fusion*、*POP* 开放获取综述 | 多 topic | 待调研 |

## C. 现有 AI/物理 Benchmark(定位空白 + 可借鉴格式)

| # | Benchmark | 与 Fusion-Bench 关系 | 状态 |
|---|---|---|---|
| C1 | SciBench(大学科学题) | 格式借鉴;聚变题极少 → 空白 | 待调研 |
| C2 | JEOPARDY / GPQA 物理部分 | 难度对标 | 待调研 |
| C3 | FEABench / 计算物理类评测 | 代码题格式借鉴 | 待调研 |
| C4 | SWE-bench | 整体范式对标 | 已确认可用 |
| C5 | 等离子体/聚变领域已有 ML 数据集(托卡马克放电库等) | 可能直接改造为题目 | 待调研 |

## D. 本地资料(全部先经 staging 验证)

| # | 本地路径 | 内容 | 可做题目方向 | 状态 |
|---|---|---|---|---|
| D1 | ~/Rosseland_opa_*(10 个目录) | Rosseland 不透明度计算管线 + 多版本验证结果 + Cuba 积分库 | eos-opacity 数值题、code 题 | 待验证 |
| D2 | ~/FLASH_GPU_hydro_lab_20260715 + flash-deps + flash_eos_tools + flash-gpu-patch | FLASH AMR 源码、15MA 铝套筒算例、EOS 工具 | simulation/ code 题、rad-hydro 算例 | 待验证 |
| D3 | ~/zpinch10000、zpinch_package_20260306、zpinch-tree | Z 箍缩模拟/树形图应用 | zpinch/ 数值与概念题 | 待验证 |
| D4 | ~/multiagent-capacitor(RESEARCH_BRIEF + results) | 脉冲电容器 ARIS 研究成果 | zpinch/ 脉冲功率题 | 待验证 |
| D5 | ~/fusion_monitor(crawler + pipeline + queries.txt) | 聚变资讯爬取管线 | 来源发现工具(非题目) | 已确认可用 |

## E. 公开数据集 / 代码库(可改造为题目)

| # | 来源 | 说明 | 状态 |
|---|---|---|---|
| E1 | FLASH 代码自带验证算例(Sedov、RT 等) | 经典算例有解析解,天然数值题 | 待调研 |
| E2 | HYDRA/xRAGE 公开验证问题 | ICF 辐射流体基准 | 待调研 |
| E3 | 公开不透明度数据库(TOPS/NIST/OPEN-ADAS) | eos-opacity 数据源 | 待调研 |
| E4 | 托卡马克公开放电数据库 | mcf 数据题 | 待调研 |
