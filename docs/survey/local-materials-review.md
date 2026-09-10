# 本地资料出题素材审查(2026-08-31)

> 审查人:ARIS idea-discovery 阶段(主会话 + 前序关闭会话产物合并)
> 结论格式:✅可出题(需过验证流水线)/ ⚠️仅灵感 / ❌不可用
> 所有"✅可出题"条目进入 staging 前仍须按 design.md §5 验证(独立复算/交叉核对)。

## 1. Z 箍缩零维计算数据(✅ 高价值,已部分自验证)

**数据源**:`~/零维计算结果(对应优化质量)_40MA-60MA_150ns-600ns.doc`(2,736 行)+ `~/zpinch_package_20260306/零维表格转换 (2).xlsx`(两 sheet:对应优化质量 2,736 + 丝阵质量20_30_40mgcm 8,208 = 10,944 行)

**参数网格(从 .doc 原文提取)**:
- I ∈ {40,42.5,…,60} MA(9 值);tr ∈ {150,…,600} ns(19 值);liner_r ∈ {4,5,6,7} cm;foam_r ∈ {0.5,0.6,0.7,0.8} cm → 9×19×4×4=2,736
- 列:I(MA), tr(ns), liner_r(cm), foam_r(cm), m(mg/cm), E(MJ/cm), v(cm/s)
- 样例行:`40MA, 150ns, 4cm, 0.5cm → m=2.05, E=3.1024 MJ/cm, v=-1.7398e8 cm/s`(负号=向内)

**已验证事实**:
- FACT | E=½mv² 物理恒等式全体样本自洽,反算 MAPE=0.00103%(source)/0.00101%(target) | ai_xlsx_cross_test_outputs/summary_metrics.json | numeric 题基底 | high
- FACT | 合并训练最佳:LightGBM E_MAE=0.1122 MJ/cm;RandomForest E_MAPE=6.8456%(固定 test=1,643,SEED=2026) | zpinch10000/合并训练结果解读.md | ML 概念题 | high
- FACT | 单域训练跨域失效:source-only 训练→target 外测 E_MAPE≈188.7%;合并训练后 target 子集降至 9.4-14% | 同上 | concept 题(域外泛化) | high
- FACT | 对应优化质量 sheet 最佳 Poly2Ridge E_MAPE=0.0374%,按 I/tr 分组留出仍 0.037% → 0D 数据低阶多项式/幂律主导 | 图文训练报告.docx | concept 题 | high
- FACT | m 覆盖 [0.60,81.55] mg/cm;E 最小 0.2792 MJ/cm;Z=13(铝);特征含 area_diff=π(liner²−foam²) | combined_training_summary_中文总结.txt | numeric 题参数范围 | high
- FACT | 速度量级 1–3.6×10⁸ cm/s(100–360 km/s),动能 2.4–4.0 MJ/cm(I=40MA 段) | .doc 原文 | numeric 题 | mid(需抽行复算)

**可出题方向**:zpinch/ numeric(由 E,m 求 v;由网格插值估 E)、concept(驱动电流↔动能标度、内外爆符号约定、 surrogate 训练域内外差异)、code(给定若干行数据做物理一致性校验脚本)。

## 2. FLASH 15MA 铝套筒 Z 箍缩算例(✅ 配置/概念题;数值题需复跑)

**数据源**:`~/FLASH_GPU_hydro_lab_20260715/flash.par.gpu` + `.agent_flash.log` + checkpoint/plot 文件

**已确认事实(出自 par 文件与日志)**:
- FACT | 算例:Al 空心套筒 OR=1cm、壁厚 4.5μm、高 1cm;Ipeak=15MA、上升 150ns;2D 柱坐标 AMR lrefine_max=7(最细 dx=1.245e-4 cm) | flash.par.gpu 第1行、日志 Grid_init 表 | concept/figure 题 | high
- FACT | 求解器配置:magnetoHD/ZPinch、usm3t(非分裂交错网格三温)、HLLD Riemann、MC 限制器、order=2、CFL=0.2、人工粘性 0.1、隐式磁扩散 | flash.par.gpu | concept 题(数值方法) | high
- FACT | 物性:套筒 Al(A=26.98,Z=13)2.70 g/cm³;填充 DD 1e-7 g/cm³;EOS/不透明度用 IONMIX4 表(DD-006-imx.cn4 / al-imx-003.cn4);MGD 6 群(0.1eV–100keV 分界) | flash.par.gpu | concept 题 | high
- FACT | 温度单位换算:par 中 5802.26105 K = 0.5 eV(1 eV=11604.5 K);被注释的 2.9e6 K=250 eV(预热选项) | flash.par.gpu 注释 | numeric 题(单位换算) | high
- FACT | GPU 化:threadHydroBlockList 混合 MPI/OpenMP;另有 opacity_freePath 外挂探针接口(指向 Rosseland_opa_new_hetero,8790 端口) | flash.par.gpu 尾部 | code 题素材 | mid

**注意**:checkpoint/plot 的物理结果(内爆速度、stagnation 时间)未提取,HDF5 需专门工具;harness 若出数值题须先复跑或从 trajectory.dat 提取。

## 3. Rosseland 不透明度平均原子模型(✅ 已验证基线)

**数据源**:`~/Rosseland_opa_auto/Rosseland_opa_auto/`(SNOP_op_Ross2.F,Fortran+Cuba-4.2.2 Vegas 积分)

**已确认事实**:
- FACT | 单核强制下原版与修复版输出字节级一致(T_sbar.txt/nsp_out.txt/Enout.txt),ne_in/ne_out/neval/fail/积分值/误差/p 值完全一致 | baseline_check/original_default_check.log + 备注.txt | 验证流水线"可复现性"范例 | high
- FACT | Co(Z=27)在 T=58 eV 下平均电离度 Z̄=10.1716;电离度分布峰值在第 10–11 电离阶(占比 0.29/0.25) | T_sbar.txt、nsp_out.txt | numeric 题(平均电离) | high
- FACT | 各电离阶能量 Enout:0 阶 −14.42、1 阶 −12.68、高阶至 9,173(第 26 阶,≈K 壳层量级,单位推定 eV,需源码确认) | Enout.txt | numeric/derivation 题 | mid
- FACT | 128 核全核运行 6.53s vs 单核 277.94s,加速 42.56×;Vegas nbatch 1000→1e6 | README_运行方法.txt | HPC concept 题 | high
- FACT | 输入:原子序数 Z+核外电子层数 n → 电子排布;与手排代码交叉一致(2026-5-7 备注) | 备注.txt | code 题 | high

**可出题方向**:eos-opacity numeric(Z̄ 计算、Rosseland/Planck 权重)、derivation(屏蔽氢模型能级公式、Saha 递推)、code(电子排布生成器正确性)。

## 4. 脉冲电容器 / 脉冲功率(⚠️ 仅作公开物理题灵感)

**数据源**:`~/multiagent-capacitor/`(ARIS 电容器预后研究)

- 其内部审计(findings.md)明确:数据目标定义、物理身份、终止语义均未通过 Data Gate,**本地数值结果不可作为 benchmark 答案**(❌ 直接采题)。
- 可作灵感:脉冲功率标准公开物理(½CV²、LC 放电、趋肤、ESR 退化)走教科书公开口径出题,标注 source_type=public。
- 其 ARIS 审计方法论(claim gap 清单、不可推断未来信息原则)可作为本项目 integrity-forensics 阶段的参照。

## 5. 聚变资讯爬虫(⚠️ 来源发现工具)

- `~/核聚变爬虫项目/output/` 有逐日 fusion_*.xlsx(政策/融资/新闻资讯为主),**不含可出题物理硬数据**;`~/fusion_monitor/{queries.txt,sources.txt}` 已确认为来源发现工具(sources.md D5)。
- 行动:不从爬虫结果直接出题;把其覆盖的源(MRE、强激光、Nuclear Fusion 等)并入 sources.md B 组。

## 6. 待办(下一轮补充)

- [ ] FLASH checkpoint/plot 的 trajectory.dat 数值提取(stagnation 时间、峰值速度)→ 若得数值可出 rad-hydro 真实算例题
- [ ] Rosseland_opa_new_hetero(free_path 服务,8790 端口)与 equally/ 目录结构盘点
- [ ] 零维数据 20/30/40 mg/cm sheet 的 .doc 数值行抽取(目前仅有 source sheet 网格)
- [ ] `~(50MA)一种全流程自动化监测…50MA级聚变装置.docx` 公开文本的概念题素材提取
