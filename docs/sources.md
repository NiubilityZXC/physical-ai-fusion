# Physical-AI-Fusion 题目来源清单

> 每条来源状态:`待调研 | 已确认可用 | 已采题 | 已排除(原因)`
> 采题红线:仅公开资料;每题记录 license;本地结果必须过验证流水线(见 design.md §5)。
> 第二轮状态更新:2026-08-31(research-lit + 本地资料盘点完成)。

## A. 教科书 / 专著(ICF 核心)

| # | 来源 | 覆盖 topic | 状态 |
|---|---|---|---|
| A1 | Atzeni & Meyer-ter-Vehn, *The Physics of Inertial Fusion* (2004) | icf/ 全部,尤其 ignition-gain, rad-hydro, implosion | 已确认可用(标准公式出题点,见 IDEA_REPORT §E;引用公式不复制原文) |
| A2 | Lindl, *Inertial Confinement Fusion* (1998) | icf/lpi, target-design | 已确认可用(同上) |
| A3 | Freidberg, *Plasma Physics and Fusion Energy* (2007) | mcf/, plasma-basic/ | 已确认可用(β 极限、Greenwald、IPB98(y,2) 等公开定标律) |
| A4 | Zel'dovich & Raizer, *Physics of Shock Waves* | rad-hydro, eos-opacity | 已确认可用(自相似解、冲击波关系式) |
| A5 | Drake, *High-Energy-Density Physics* (2018) | rad-hydro, lpi, diagnostics | 已确认可用 |
| A6 | Kruer, *The Physics of Laser Plasma Interactions* | icf/lpi | 已确认可用(SBS/SRS 阈值等公开公式) |
| A7 | Liberman et al., *The Physics of High-Density Z-Pinch Plasmas* | zpinch/ | 已确认可用 |
| A8 | NRL Plasma Formulary(公开 PDF,US Naval Research Laboratory) | plasma-basic/ 全部 | 已确认可用(公开出版物,15-20 个标准公式出题基准) |

## B. 综述 / 公开报告

| # | 来源 | 覆盖 topic | 状态 |
|---|---|---|---|
| B1 | NIF / LLNL 公开报告与点火综述 | ignition-gain, diagnostics | **已确认可用(2026-08-31)**:点火序列 2022-12-05(2.05→3.15MJ)、2025-02-23(5.0MJ)、2025-04-07(8.6±0.45MJ,gain 4.13,纪录)、2025-06-22(2.4MJ)、2025-10-01(3.5MJ);来源 lasers.llnl.gov + LLNL FY2025 年报 |
| B2 | OMEGA / LLE 公开实验报告 | implosion, rt-rm-instability | 待调研(v1 可先用 NIF 序列,B2 留 v1.1) |
| B3 | 神光系列公开论文(强激光与粒子束、MRE 期刊) | icf/ 多 topic | 已确认可用(MRE 开放获取;具体算例数值引用时核原文) |
| B4 | IAEA / ITER 公开技术文档 | mcf/, fusion-engineering | 已确认可用(ITER 官方 Facts & Figures:R=6.2m、a=2.0m、B=5.3T、I=15MA、Q=10、500MW) |
| B5 | *Matter and Radiation at Extremes*、*Nuclear Fusion*、*POP* 开放获取综述 | 多 topic | 已确认可用 |

## C. 现有 AI/物理 Benchmark(定位空白 + 可借鉴格式)

| # | Benchmark | 与本项目关系 | 状态 |
|---|---|---|---|
| C1 | SciBench(arXiv 2307.10635) | 数值题+容差评分格式借鉴;聚变题≈0 | 已确认可用(格式参照) |
| C2 | GPQA(2311.12022)/ FrontierScience(OpenAI 2025-12) | 难度对标;rubric 评分架构借鉴;GPQA 已饱和(GPT-5.2 92%) | 已确认可用 |
| C3 | FEABench(2504.06260)/ LLM-SRBench(2504.10415) | 代码题/推导题评分借鉴 | 已确认可用 |
| C4 | SWE-bench(2310.06770) | 整体范式对标(harness、verified 子集) | 已确认可用 |
| C5 | TokaMark(2602.10132/2607.11915)、ConStellaration、Fusion Equilibrium Challenge | MCF 数据集;mcf/ v2 接入候选 | 已确认可用(v1 引用,v2 接入) |
| C6 | **PKU-XLab FusionBench**(GitHub,MIT,10,605 题) | **直接竞品(知识问答型)**:定量题 0.75%、无验证流水线、GitHub-only 无论文;差异化成立 | 已精读(快照在 docs/survey/,本地) |
| C7 | PHYSICS(2503.21821)/ OlympiadBench(2402.14008)/ Towards a Large Physics Benchmark(2507.21695) | 评分管线与规模参照 | 已确认可用 |
| C8 | NuclearQAv2(2606.27047)、NRC Reactor Exam(2607.22067)、Offline RL Plasma Control(2606.07550) | 核领域/控制侧同类;无 ICF 定量 | 已确认可用 |

## D. 本地资料(全部先经 staging 验证)

| # | 本地路径 | 内容 | 可做题目方向 | 状态 |
|---|---|---|---|---|
| D1 | ~/Rosseland_opa_*(10 个目录) | 平均原子模型(屏蔽氢模型)Fortran 管线 + Cuba 积分 + 多版本验证 | eos-opacity 数值题(平均电离度/占据数/能级)、code 题 | **已验证可用(2026-08-31)**:单核基线与修复版输出字节级一致(ne_in/ne_out/积分值/p 值;T_sbar/nsp_out/Enout 三文件一致);示例:T=58 eV → Z̄=10.17(Z=27 元素,27 阶段占据分布峰值在 10-11 价) |
| D2 | ~/FLASH_GPU_hydro_lab_20260715 + flash-deps + flash_eos_tools + flash-gpu-patch | FLASH 4.8 magnetoHD/ZPinch,2D 柱坐标 AMR(lrefine_max=7),15MA/150ns 铝套筒(OR=1cm、厚 4.5μm),ionmix4 EOS/不透明度表(DD/Al/Be),HLLD+USM-3T+磁扩散隐式 | simulation/ 设置解读题、rad-hydro 概念题、code 题(参数文件) | **已确认可用(算例参数,2026-08-31)**;输出物理量声明需复跑确认 → 仅用于"设置/参数/方法"题,不用于输出数值题 |
| D3 | ~/zpinch10000、zpinch_package_20260306、零维计算结果* | 零维 Z 箍缩数据集 10,944 行(2,736 优化质量 + 8,208 丝阵 20/30/40 mg/cm;I=40-60MA、tr=150-600ns)+ 8 模型代理训练结果 | zpinch/ 数值题(数据行 ground truth)、概念题(内插/外推、跨域泛化) | **已验证可用(2026-08-31)**:E=½mv² 物理恒等式 10,942/10,944 行通过(最坏相对偏差 1.01e-4,舍入级);代理指标经固定测试集与分组留出交叉验证(RF E_MAPE 6.85%、Poly2Ridge 0.037%) |
| D4 | ~/multiagent-capacitor(findings.md) | 脉冲电容器预测 ARIS 研究 | —(不作物理题源) | **已排除(2026-08-31)**:所有者审计总评 WARN,容量/ESR/RUL 目标未过 Data Gate → 不入库,作为"验证流水线拦截本地结果"的正面案例记录于 verification-log |
| D5 | ~/fusion_monitor、~/核聚变爬虫项目、~/fusion_crawler | 聚变资讯爬取管线 | 来源发现工具(非题目) | 已确认可用(工具) |
| D6 | ~/202610366208.8-脉冲电容器状态在线评估方法及装置-申请文件.docx | 专利申请公开文本(GM(1,1) 灰色模型寿命预测公式组) | zpinch/脉冲功率概念题 1-2 道(标注来源为专利申请公开文本) | 已确认可用(公开文本,引用口径:概念与公式,不声称其实验数据) |

## E. 公开数据集 / 代码库(可改造为题目)

| # | 来源 | 说明 | 状态 |
|---|---|---|---|
| E1 | FLASH 代码自带验证算例(Sedov、Sod、RT、KH、Shu-Osher) | 经典算例有解析解,天然数值题 | 已确认可用(本地 FLASH 4.8 含 magnetoHD/ZPinch 等 setup;Sedov/RT 解析解公式公开) |
| E2 | Su-Olson / Marshak 辐射输运半解析解 | 辐射流体 benchmark 标准解 | 已确认可用(公开文献) |
| E3 | NIST ASD(电离能/能级)、OPEN-ADAS、TOPS/OPAL 公开表 | eos-opacity 数据源(Saha 题、平均电离度比对) | 已确认可用(公开数据库) |
| E4 | 托卡马克公开放电数据库(TokaMark/MAST/DIII-D,CC BY 4.0) | mcf 数据题 | 已确认可用(v2 接入;v1 用官方标称参数) |
| E5 | ITER 官方 Facts & Figures(iter.org) | mcf/fusion-engineering 真实数据题 | 已确认可用 |
