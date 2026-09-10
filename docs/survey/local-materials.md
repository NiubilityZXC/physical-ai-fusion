# 本地资料盘点报告(2026-08-31,inline 调研)

> 用途:staging 出题的本地素材底稿。所有数值已对照原始文件。
> 数据治理:本地素材出题必须过 design.md §5 验证流水线;下表"验证状态"栏给出当前证据等级。

## 1. 零维 Z 箍缩数据集(zpinch/,主资产,已验证)

**原始数据**:`~/zpinch_package_20260306/零维表格转换 (2).xlsx`(两个 sheet 共 10,944 行,stdlib 解析于 2026-08-31)

| sheet | 行数 | I (MA) | tr (ns) | m (mg/cm) | E (MJ/cm) | v (cm/s) |
|---|---|---|---|---|---|---|
| 丝阵质量20_30_40mgcm | 8,208 | 40–60 | 150–600 | 20.00–40.00 | 0.2792–8.9478 | −9.46e7…−1.18e7 |
| 对应优化质量 | 2,736 | 40–60 | 150–600 | 0.60–81.55(优化) | 2.3773–8.9484 | −3.64e8…−3.62e7 |

列:`I, tr, liner_r(cm), foam_r(cm), m, E, v`;Z=13(铝)。v 为负=向内(内爆)。

**验证状态(高)**:
- 物理恒等式 E=½mv²(即 v=−√(2e16·E/m),cgs 单位换算)逐行复核:**10,942/10,944 通过**,最坏相对偏差 1.01e-4(舍入级)→ 数据内部自洽,可作 ground truth。
- 代理模型交叉验证(固定测试集 SEED=2026 + 分组留出):
  - 合并训练:LightGBM E_MAE=0.1122 MJ/cm(绝对最优)、RandomForest E_MAPE=6.8456%(相对最优)
  - 单源训练(2,736)→ 目标域外推失败(E_MAPE 188.7%);合并训练后目标域 9.4–14% → 跨域泛化教学案例
  - 优化质量 sheet:Poly2Ridge E_MAPE=0.037%(随机/按 I 留出/按 tr 留出三口径均第一)→ 近幂律标度,可出"标度律拟合"题
- 质量覆盖:[0.60, 81.55] mg/cm;每工况质量点中位数 1→4(合并后);最小动能 0.2792 MJ/cm

**可出题方向**:数据行直接出数值题(E 或 v 给定其余参数);E=½mv² 单位换算题;标度律估算题(Poly2Ridge 启示的幂律形式);跨域泛化概念题。

## 2. FLASH 15MA 铝套筒 Z 箍缩算例(simulation/,中置信)

**出处**:`~/FLASH_GPU_hydro_lab_20260715/flash.par.gpu`(完整读取)+ `.agent_flash.log`(初始化日志)

- setup:`./setup -auto magnetoHD/ZPinch -2d +cylindrical +ug species=fill,line,vacu +mtmmmt +usm3t +mgd mgd_meshgroups=6 +hdf5typeio`(FLASH 4.8)
- 几何:铝空心套筒 OR=1 cm、壁厚 4.5 μm(sim_thickness=0.00045 cm)、高 1 cm;内半径 0.99955 cm;填充 DD 气体 ρ=1e-7 g/cm³
- 驱动:Ipeak=15 MA、上升 150 ns(current.dat 外给);tmax=1.3 μs;CFL=0.2
- 材料/EOS:套筒 Al(A=26.9815385, Z=13, ρ=2.70 g/cm³),ionmix4 表 al-imx-003.cn4;DD 燃料 DD-006-imx.cn4;真空 Be-006-imx.cn4(吸收/发射置 0)
- 数值:order=2、MC 限制器、HLLD、人工粘性 0.1、USM-3T MHD、磁扩散隐式(HYPRE_GMRES)、AMR 按 dens(0.15/0.05)加密至 l=7(dx_min=1.245e-4 cm)
- 温度换算点:par 中 5802.26105(注释 0.5 eV)↔ 1 eV=11604.5 K;注释掉的 2.901130525e6 K=250 eV(预热选项)
- GPU:混合 MPI/OpenMP(threadHydroBlockList),checkpoint 到 0018

**验证状态(中)**:参数文件与日志一致(EOS 表加载、网格初始化成功);**输出物理量(速度/温度/产额)未独立复跑** → 只出"设置/参数/方法/单位换算"题,不出输出数值题(待复跑后升级)。

## 3. Rosseland 不透明度平均原子模型(eos-opacity/,已验证)

**出处**:`~/Rosseland_opa_auto/Rosseland_opa_auto/`(Fortran:SNOP_op_Ross2.F/functions.F/par_register.F;Cuba-4.2.2 Vegas 积分)

- 模型:屏蔽氢平均原子模型(screen hydrogenic;输入 Z 与电子层数 n 自动生电子排布,与手工排布对比一致——备注.txt 2026-05-07)
- 输出文件(T=58 eV 单点运行):
  - `T_sbar.txt`:**T=58 eV → 平均电离度 Z̄=10.171552725303085**
  - `nsp_out.txt`:27 个电离阶段(0…26,即 Z=27=钴)占据概率分布;峰值在 10 价(0.2917)与 11 价(0.2497);3 价以下/16 价以上可忽略
  - `Enout.txt`:各阶段能量(eV 量级);最高阶段 ≈9.173 keV(与 Co K 层结合能量级一致)
- 数据文件:oscillator_strengths.txt(振子强度)、screen_constants.txt(屏蔽常数)
- **验证状态(高)**:`~/Rosseland_opa_auto_baseline_check/` 强制单核复跑:原版与修复版 ne_in/ne_out/neval/fail/积分值/误差/p 值完全一致,T_sbar/nsp_out/Enout 三文件**字节级一致**;性能:277.94 s(单核)→ 6.53 s(128 核,nbatch 1000→1e6),42.56× 加速

**可出题方向**:Rosseland/Planck 平均定义推导题;Z̄ 计算与解读数值题(可重跑 Fortran 生成任意 T 点答案);占据分布读数题;Saha 方程对比题;屏蔽氢模型概念题;Cuba Vegas 积分 code 题。

## 4. 脉冲功率 / 电容器(限概念题)

- **专利申请公开文本**(202610366208.8):GM(1,1) 灰色模型寿命预测完整公式组(发展系数 a、灰作用量 b、背景值 z1(k)=½(x1(k)+x1(k−1))、临界放电次数 k临界=−1/a·ln[...]、平均相对精度 P0=1−Δ̄);应用场景含可控核聚变;ns/μs 级放电、单次几十至上百 kJ。
- **~/multiagent-capacitor ARIS 结果**:**已排除**。所有者审计(findings.md)总评 WARN;容量/ESR/RUL 目标未过 Data Gate;5.04GB 应力包目标语义未决。→ 不入库,写入 verification-log 作为拦截案例。
- 教科书级脉冲功率题(½CV²、LC 回路 ω=1/√(LC)、阻尼判据 R vs 2√(L/C)、趋肤深度)用公开公式出,不依赖本地数据。

## 5. 爬虫/资讯管线(工具,非题源)

~/fusion_monitor(queries.txt/sources.txt/README)、~/核聚变爬虫项目(output/ 下 2026 年 1-2 月 fusion_*.xlsx/pptx 日报)、~/fusion_crawler。用途:后续来源发现;日报以政策/融资/新闻为主,**不含可出题的物理硬数据**(抽查),不直接出题。

## 6. 待办(后续版本)

- FLASH 算例复跑(GPU)→ 输出数值题升级(需 GPU 时间,v1.1)
- ~/Rosseland_opa_new_hetero、~/free_path_service_portable(自由程不透明度服务,:8790)调研 → eos-opacity code 题候选(v1.1)
- 零维 .doc 原始报告(strings 提取)补充 0D 模型方程细节(当前已从 xlsx+指标 JSON+解读.md 获得全部必需数值,非阻塞)
