# Physical-AI-Fusion v0.2 完整题目目录（verified 691 题，全文无删节）

> 生成方式:python3 scripts/gen_catalog.py;答案与验证证据与 data/verified/ 逐题一致。


---

## icf/diagnostics（22 题）


#### icf-diagnostics-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 中子产额能量:NIF 某发次发生 1.1e18 次 DT 反应,每次反应产生 1 个 14.1 MeV 中子。求中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **2.485e+06 J**（容差 ±2%）
   - 独立复算:`1.1e18*14.1e6*1.602176634e-19`


#### icf-diagnostics-0002

`concept` · `undergrad` · `exact_match` · 来源:textbook

> DT 反应 D+T→α+n 的能量分配:α 粒子与中子各带走多少能量?

**答案:** **A**
   ✅ A. α 3.5 MeV(20%),中子 14.1 MeV(80%)——由动量守恒,能量反比于质量
   　 B. α 与中子各 8.8 MeV
   　 C. α 14.1 MeV,中子 3.5 MeV
   　 D. 能量分配随温度变化


#### icf-diagnostics-0003

`concept` · `grad` · `exact_match` · 来源:textbook

> 下降散射中子比(DSR)诊断的原理:测量约 10-12 MeV(经弹性散射损失能量的)中子与 14.1 MeV 主中子之比,能得到什么物理量,为什么?

**答案:** **A**
   ✅ A. 燃料面密度 ρR——中子在燃料内弹性散射的概率正比于路径上的核子面密度
   　 B. 热斑温度——散射能损反映离子温度
   　 C. 电子密度——散射由电子屏蔽决定
   　 D. 激光能量利用效率


#### icf-diagnostics-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 黑腔辐射温度 300 eV 的黑体谱峰值波长:Wien 位移定律 λ_max=b/T,b=2.897771955e-3 m·K,1 eV=11604.525 K。求 λ_max(m),并说明其所在波段。

**答案:** **8.3236e-10 m**（容差 ±2%）
   - 独立复算:`2.897771955e-3/(300*11604.525)`


#### icf-diagnostics-0005

`concept` · `expert` · `exact_match` · 来源:paper

> 充 D₂(无氚)的诊断靶中,次级 DT 中子的产额为何能测量燃料 ρR?

**答案:** **A**
   ✅ A. D+D→T+p 产生的 1.01 MeV 氚核在燃料中慢化,慢化程度取决于路径密度;未慢化的氚与 D 反应产生 14.1 MeV(或更高)次级中子,其份额携带 ρR 信息
   　 B. 次级中子能量只与温度有关
   　 C. 次级中子是燃料泄漏的直接标志
   　 D. 次级中子由靶壳活化产生


#### icf-diagnostics-gen-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 4.6e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **1.039e+06 J**（容差 ±2%）
   - 独立复算:`4.5999999999999994e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 4.4e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **994000 J**（容差 ±2%）
   - 独立复算:`4.4000000000000006e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 1.8e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **406600 J**（容差 ±2%）
   - 独立复算:`1.8e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 3.4e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **768100 J**（容差 ±2%）
   - 独立复算:`3.4e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 3.2e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **722900 J**（容差 ±2%）
   - 独立复算:`3.2e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 1.2e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **271100 J**（容差 ±2%）
   - 独立复算:`1.2e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 3.9e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **881000 J**（容差 ±2%）
   - 独立复算:`3.9e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 2.9e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **655100 J**（容差 ±2%）
   - 独立复算:`2.9e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0009

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 4e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **903600 J**（容差 ±2%）
   - 独立复算:`4e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0011

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 5e+16 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **113000 J**（容差 ±2%）
   - 独立复算:`5e+16*14.1e6*1.602176634e-19`


#### icf-diagnostics-gen-0012

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 2e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **451800 J**（容差 ±2%）
   - 独立复算:`2e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-genb-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 4.7e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **1.062e+06 J**（容差 ±2%）
   - 独立复算:`4.7e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-genb-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 发次产生 4.3e+17 次 DT 反应。求 14.1 MeV 中子携带的总能量(J)。1 MeV=1.602176634e-13 J。

**答案:** **971400 J**（容差 ±2%）
   - 独立复算:`4.3e+17*14.1e6*1.602176634e-19`


#### icf-diagnostics-hard-0001

`concept` · `expert` · `exact_match` · 来源:paper

> 关于 ICF 中子谱诊断,正确的有(多选):

**答案:** **A/B/C**
   ✅ A. 14.1 MeV 主中子的谱形(多普勒展宽)可反推燃料离子温度
   ✅ B. 下降散射中子(约 10-12 MeV)与主中子之比(DSR)测量燃料 ρR
   ✅ C. 中子飞行时间(nTOF)谱仪利用不同能量中子的到达时间差分辨能谱
   　 D. 中子谱完全不能用于内爆对称性诊断


#### icf-diagnostics-hard-0002

`concept` · `grad` · `exact_match` · 来源:paper

> 关于 X 射线分幅相机(XRFC)在 ICF 中的作用,正确的是?

**答案:** **A**
   ✅ A. 以数十 ps 时间分辨记录内爆靶丸 X 光图像演化,用于测量内爆轨迹、对称性与停滞形态
   　 B. 只能拍静态照片
   　 C. 只能测中子
   　 D. 时间分辨率为毫秒级


#### icf-diagnostics-hard-0003

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于 VISAR(任意反射面速度干涉仪)在冲击波实验中的测量原理,正确的是?

**答案:** **A**
   ✅ A. 利用运动反射面的多普勒频移使干涉条纹移动,条纹位移与反射面速度成正比,从而测量冲击/自由面速度历史
   　 B. 直接测量温度
   　 C. 测量密度而非速度
   　 D. 只能测静态位移


#### icf-diagnostics-hard-0004

`concept` · `grad` · `exact_match` · 来源:paper

> 关于 ICF 中子产额测量的绝对定标,正确的有(多选):

**答案:** **A/B**
   ✅ A. 需要已知效率的探测器(如活化样品、塑料闪烁体)与几何因子
   ✅ B. 绝对产额误差直接影响靶增益的宣称
   　 C. 只需相对计数即可得到增益
   　 D. 定标与探测器位置无关


---

## icf/eos-opacity（156 题）


#### code-rosseland-0001

`code` · `grad` · `unit_test` · 来源:textbook

> 实现 Python 函数 rosseland_mean(kappa, weight, nu1, nu2),用数值积分计算 Rosseland 平均不透明度:1/κ_R = ∫(1/κ_ν)·w(ν)dν / ∫w(ν)dν,返回 κ_R(即 den/num 的倒数关系:返回 ∫w/∫(w/κ))。kappa 与 weight 是调用方传入的一元函数,ν1<ν2。测试将用 κ(ν)=1e3/ν³ 与 w(ν)=ν³e^(-ν) 在三组区间上与 2e5 网格精细梯形参考对比,要求相对误差<1e-3。只准用标准库。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_rosseland.py`，超时 120s


#### code-saha-0001

`code` · `grad` · `unit_test` · 来源:textbook

> 实现 saha_ionized_fraction(T_eV, n_total, chi):给定电子温度 T_eV(eV)、总粒子数密度 n_total(m^-3)、电离能 chi(eV),求氢等离子体的电离分数 x=n_{i+1}/n_total(两级 Saha,准中性 n_e=n_{i+1},g 比取 1)。提示:K=(2/Λ³)e^(-χ/T),Λ=h/√(2πm_e k_B T);解二次方程。只准用标准库。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_saha.py`，超时 120s


#### code-freepath-0001

`code` · `undergrad` · `unit_test` · 来源:textbook

> 实现 log_interp(x1, y1, x2, y2, x):在对数网格上等间距数据 (x1,y1),(x2,y2) 之间对 x 做线性插值并返回 y。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_freepath.py`，超时 120s


#### icf-eos-opacity-3001

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=253.5 g/cm³、T=1.66e+04 eV、光子能量 hν=1.581e+04 eV 处的 Rosseland 自由程 l=0.0219095 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.18004 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(253.513*0.0219095)`


#### icf-eos-opacity-3002

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=103.8 g/cm³、T=711.2 eV、光子能量 hν=1581 eV 处的 Rosseland 自由程 l=0.00210221 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **4.5848 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(103.753*0.00210221)`


#### icf-eos-opacity-3003

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=837.5 g/cm³、T=59.02 eV、光子能量 hν=948.4 eV 处的 Rosseland 自由程 l=3.17839e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **37.566 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(837.529*3.17839e-05)`


#### icf-eos-opacity-3004

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=0.05984 g/cm³、T=1923 eV、光子能量 hν=2042 eV 处的 Rosseland 自由程 l=93.6022 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.17853 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0598412*93.6022)`


#### icf-eos-opacity-3005

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=1127 g/cm³、T=7.396e+04 eV、光子能量 hν=340.4 eV 处的 Rosseland 自由程 l=0.000590893 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **1.5014 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(1127.2*0.000590893)`


#### icf-eos-opacity-3006

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=0.2661 g/cm³、T=4.498e+04 eV、光子能量 hν=1.799e+04 eV 处的 Rosseland 自由程 l=21.1659 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.17757 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.266073*21.1659)`


#### icf-eos-opacity-3007

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=0.05984 g/cm³、T=1380 eV、光子能量 hν=139 eV 处的 Rosseland 自由程 l=21.0385 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.7943 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0598412*21.0385)`


#### icf-eos-opacity-3008

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=2.148 g/cm³、T=2679 eV、光子能量 hν=645.7 eV 处的 Rosseland 自由程 l=0.0416618 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **11.175 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(2.14783*0.0416618)`


#### icf-eos-opacity-3009

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=1127 g/cm³、T=222.3 eV、光子能量 hν=2.042e+04 eV 处的 Rosseland 自由程 l=0.000116009 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **7.6473 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(1127.2*0.000116009)`


#### icf-eos-opacity-3010

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=0.01349 g/cm³、T=8.73e+04 eV、光子能量 hν=2636 eV 处的 Rosseland 自由程 l=369.188 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.20079 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0134896*369.188)`


#### icf-eos-opacity-3011

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=2.999e+04 g/cm³、T=2679 eV、光子能量 hν=2999 eV 处的 Rosseland 自由程 l=1.44836e-06 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **23.021 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(29991.6*1.44836e-06)`


#### icf-eos-opacity-3012

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=7.079 g/cm³、T=262.4 eV、光子能量 hν=3412 eV 处的 Rosseland 自由程 l=0.0265694 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **5.3164 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(7.07946*0.0265694)`


#### icf-eos-opacity-3013

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=5012 g/cm³、T=135.2 eV、光子能量 hν=1.225e+04 eV 处的 Rosseland 自由程 l=0.000627621 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.31791 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(5011.87*0.000627621)`


#### icf-eos-opacity-3014

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=1.183 g/cm³、T=1923 eV、光子能量 hν=158.1 eV 处的 Rosseland 自由程 l=0.0159627 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **52.953 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(1.18304*0.0159627)`


#### icf-eos-opacity-3015

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=0.08072 g/cm³、T=6.266e+04 eV、光子能量 hν=1.393e+04 eV 处的 Rosseland 自由程 l=7.13718 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **1.7357 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0807235*7.13718)`


#### icf-eos-opacity-3016

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=76.91 g/cm³、T=990.8 eV、光子能量 hν=158.1 eV 处的 Rosseland 自由程 l=1.09074e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **1192 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(76.913*1.09074e-05)`


#### icf-eos-opacity-3017

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=12.85 g/cm³、T=3162 eV、光子能量 hν=2636 eV 处的 Rosseland 自由程 l=0.00135228 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **57.535 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(12.8529*0.00135228)`


#### icf-eos-opacity-3018

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=1127 g/cm³、T=6138 eV、光子能量 hν=3412 eV 处的 Rosseland 自由程 l=1.19532e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **74.219 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(1127.2*1.19532e-05)`


#### icf-eos-opacity-3019

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 密度 ρ 轴上取 50 点对数网格:coord=10^(log10(0.01)+(log10(30000.0)-log10(0.01))·i/50),i=1..50。求 i=15 处的坐标值(g/cm³)。

**答案:** **0.87728 g/cm³**（容差 ±2%）
   - 独立复算:`10**(log10(0.01)+(log10(30000.0)-log10(0.01))*15/50)`


#### icf-eos-opacity-3020

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 密度 ρ 轴上取 50 点对数网格:coord=10^(log10(0.01)+(log10(30000.0)-log10(0.01))·i/50),i=1..50。求 i=7 处的坐标值(g/cm³)。

**答案:** **0.080686 g/cm³**（容差 ±2%）
   - 独立复算:`10**(log10(0.01)+(log10(30000.0)-log10(0.01))*7/50)`


#### icf-eos-opacity-3021

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 温度 T 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(200000.0)-log10(50.0))·i/50),i=1..50。求 i=8 处的坐标值(eV)。

**答案:** **188.49 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(200000.0)-log10(50.0))*8/50)`


#### icf-eos-opacity-3022

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 温度 T 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(200000.0)-log10(50.0))·i/50),i=1..50。求 i=12 处的坐标值(eV)。

**答案:** **365.99 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(200000.0)-log10(50.0))*12/50)`


#### icf-eos-opacity-3023

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 光子能量 hν 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(30000.0)-log10(50.0))·i/50),i=1..50。求 i=14 处的坐标值(eV)。

**答案:** **299.81 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(30000.0)-log10(50.0))*14/50)`


#### icf-eos-opacity-3024

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 光子能量 hν 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(30000.0)-log10(50.0))·i/50),i=1..50。求 i=17 处的坐标值(eV)。

**答案:** **440.09 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(30000.0)-log10(50.0))*17/50)`


#### icf-eos-opacity-3025

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=0.6516 g/cm³、T=222.3 eV,对 hν=4406 eV 光子的自由程 l=0.822045 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.012165 1**（容差 ±2%）
   - 独立复算:`0.01/0.822045`


#### icf-eos-opacity-3026

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=342 g/cm³、T=135.2 eV,对 hν=3873 eV 光子的自由程 l=5.0621e-05 cm。求厚度 L=0.1 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **1975.5 1**（容差 ±2%）
   - 独立复算:`0.1/5.0621e-05`


#### icf-eos-opacity-3027

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=0.01349 g/cm³、T=1.406e+04 eV,对 hν=340.4 eV 光子的自由程 l=298.155 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **3.354e-05 1**（容差 ±2%）
   - 独立复算:`0.01/298.155`


#### icf-eos-opacity-3028

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=12.85 g/cm³、T=1.435e+05 eV,对 hν=340.4 eV 光子的自由程 l=0.305737 cm。求厚度 L=0.001 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.0032708 1**（容差 ±2%）
   - 独立复算:`0.001/0.305737`


#### icf-eos-opacity-3029

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=342 g/cm³、T=3733 eV,对 hν=1.581e+04 eV 光子的自由程 l=0.000744989 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **13.423 1**（容差 ±2%）
   - 独立复算:`0.01/0.000744989`


#### icf-eos-opacity-3030

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=1127 g/cm³、T=1.03e+05 eV,对 hν=3873 eV 光子的自由程 l=0.000205726 cm。求厚度 L=0.001 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **4.8608 1**（容差 ±2%）
   - 独立复算:`0.001/0.000205726`


#### icf-eos-opacity-3031

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=9.528 g/cm³、hν=139 eV 下:T₁=365.6 eV 时自由程 l₁=0.000154157 cm,T₂=1629 eV 时 l₂=0.00161157 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.095656 1**（容差 ±2%）
   - 独立复算:`(0.000154157)/(0.00161157)`


#### icf-eos-opacity-3032

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=1.592 g/cm³、hν=2.323e+04 eV 下:T₁=2270 eV 时自由程 l₁=3.1811 cm,T₂=2.312e+04 eV 时 l₂=3.24945 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.97897 1**（容差 ±2%）
   - 独立复算:`(3.1811)/(3.24945)`


#### icf-eos-opacity-3033

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=0.6516 g/cm³、hν=2.999e+04 eV 下:T₁=510.5 eV 时自由程 l₁=1.32869 cm,T₂=222.3 eV 时 l₂=0.381865 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **3.4795 1**（容差 ±2%）
   - 独立复算:`(1.32869)/(0.381865)`


#### icf-eos-opacity-3034

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=1.183 g/cm³、hν=1799 eV 下:T₁=7244 eV 时自由程 l₁=0.0632898 cm,T₂=188.4 eV 时 l₂=0.0114738 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **5.516 1**（容差 ±2%）
   - 独立复算:`(0.0632898)/(0.0114738)`


#### icf-eos-opacity-3035

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=5012 g/cm³、hν=1393 eV 下:T₁=2.312e+04 eV 时自由程 l₁=3.23998e-06 cm,T₂=1380 eV 时 l₂=2.73033e-06 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **1.1867 1**（容差 ±2%）
   - 独立复算:`(3.23998e-06)/(2.73033e-06)`


#### icf-eos-opacity-3036

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=342 g/cm³、T=6.266e+04 eV、光子能量 hν=1076 eV 处的 Rosseland 自由程 l=0.0112654 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.25957 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(341.979*0.0112654)`


#### icf-eos-opacity-3037

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=0.02449 g/cm³、T=432.5 eV、光子能量 hν=2636 eV 处的 Rosseland 自由程 l=228.689 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.17855 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0244906*228.689)`


#### icf-eos-opacity-3038

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=461.3 g/cm³、T=1.435e+05 eV、光子能量 hν=7345 eV 处的 Rosseland 自由程 l=0.0121405 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.17855 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(461.318*0.0121405)`


#### icf-eos-opacity-3039

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=5.248 g/cm³、T=82.22 eV、光子能量 hν=3412 eV 处的 Rosseland 自由程 l=0.483545 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.39406 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(5.24807*0.483545)`


#### icf-eos-opacity-3040

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=0.1466 g/cm³、T=990.8 eV、光子能量 hν=299.9 eV 处的 Rosseland 自由程 l=19.8693 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.34341 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.146555*19.8693)`


#### icf-eos-opacity-3041

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=2.228e+04 g/cm³、T=5.309e+04 eV、光子能量 hν=1.079e+04 eV 处的 Rosseland 自由程 l=6.34767e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.70695 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(22284.4*6.34767e-05)`


#### icf-eos-opacity-3042

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=253.5 g/cm³、T=4.498e+04 eV、光子能量 hν=5000 eV 处的 Rosseland 自由程 l=0.0182331 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.21634 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(253.513*0.0182331)`


#### icf-eos-opacity-3043

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=0.05984 g/cm³、T=1.66e+04 eV、光子能量 hν=1581 eV 处的 Rosseland 自由程 l=42.0955 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.39698 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0598412*42.0955)`


#### icf-eos-opacity-3044

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=3.899 g/cm³、T=1169 eV、光子能量 hν=4406 eV 处的 Rosseland 自由程 l=0.333281 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.76947 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(3.89942*0.333281)`


#### icf-eos-opacity-3045

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=31.48 g/cm³、T=2270 eV、光子能量 hν=645.7 eV 处的 Rosseland 自由程 l=0.0010347 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **30.703 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(31.4775*0.0010347)`


#### icf-eos-opacity-3046

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=0.4831 g/cm³、T=1.191e+04 eV、光子能量 hν=568.9 eV 处的 Rosseland 自由程 l=3.01294 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.68708 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.483059*3.01294)`


#### icf-eos-opacity-3047

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=2046 g/cm³、T=2e+05 eV、光子能量 hν=340.4 eV 处的 Rosseland 自由程 l=0.000219638 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **2.2248 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(2046.44*0.000219638)`


#### icf-eos-opacity-3048

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=103.8 g/cm³、T=1.694e+05 eV、光子能量 hν=2042 eV 处的 Rosseland 自由程 l=0.0259538 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.37136 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(103.753*0.0259538)`


#### icf-eos-opacity-3049

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=9.528 g/cm³、T=1.694e+05 eV、光子能量 hν=64.57 eV 处的 Rosseland 自由程 l=0.0866731 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **1.2109 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(9.52796*0.0866731)`


#### icf-eos-opacity-3050

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=461.3 g/cm³、T=97.05 eV、光子能量 hν=3873 eV 处的 Rosseland 自由程 l=0.000227277 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **9.5377 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(461.318*0.000227277)`


#### icf-eos-opacity-3051

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=103.8 g/cm³、T=114.6 eV、光子能量 hν=387.3 eV 处的 Rosseland 自由程 l=2.0845e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **462.38 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(103.753*2.0845e-05)`


#### icf-eos-opacity-3052

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=139.6 g/cm³、T=1.66e+04 eV、光子能量 hν=6457 eV 处的 Rosseland 自由程 l=0.000788894 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **9.0778 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(139.637*0.000788894)`


#### icf-eos-opacity-3053

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=31.48 g/cm³、T=510.5 eV、光子能量 hν=232.3 eV 处的 Rosseland 自由程 l=3.19268e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **995.05 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(31.4775*3.19268e-05)`


#### icf-eos-opacity-3054

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 密度 ρ 轴上取 50 点对数网格:coord=10^(log10(0.01)+(log10(30000.0)-log10(0.01))·i/50),i=1..50。求 i=40 处的坐标值(g/cm³)。

**答案:** **1519.5 g/cm³**（容差 ±2%）
   - 独立复算:`10**(log10(0.01)+(log10(30000.0)-log10(0.01))*40/50)`


#### icf-eos-opacity-3055

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 密度 ρ 轴上取 50 点对数网格:coord=10^(log10(0.01)+(log10(30000.0)-log10(0.01))·i/50),i=1..50。求 i=44 处的坐标值(g/cm³)。

**答案:** **5010.3 g/cm³**（容差 ±2%）
   - 独立复算:`10**(log10(0.01)+(log10(30000.0)-log10(0.01))*44/50)`


#### icf-eos-opacity-3056

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 温度 T 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(200000.0)-log10(50.0))·i/50),i=1..50。求 i=39 处的坐标值(eV)。

**答案:** **32253 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(200000.0)-log10(50.0))*39/50)`


#### icf-eos-opacity-3057

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 温度 T 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(200000.0)-log10(50.0))·i/50),i=1..50。求 i=20 处的坐标值(eV)。

**答案:** **1379.7 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(200000.0)-log10(50.0))*20/50)`


#### icf-eos-opacity-3058

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 光子能量 hν 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(30000.0)-log10(50.0))·i/50),i=1..50。求 i=20 处的坐标值(eV)。

**答案:** **646 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(30000.0)-log10(50.0))*20/50)`


#### icf-eos-opacity-3059

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 光子能量 hν 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(30000.0)-log10(50.0))·i/50),i=1..50。求 i=16 处的坐标值(eV)。

**答案:** **387.24 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(30000.0)-log10(50.0))*16/50)`


#### icf-eos-opacity-3060

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=9.528 g/cm³、T=6.266e+04 eV,对 hν=568.9 eV 光子的自由程 l=0.336632 cm。求厚度 L=0.1 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.29706 1**（容差 ±2%）
   - 独立复算:`0.1/0.336632`


#### icf-eos-opacity-3061

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=0.877 g/cm³、T=114.6 eV,对 hν=6457 eV 光子的自由程 l=1.18484 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.00844 1**（容差 ±2%）
   - 独立复算:`0.01/1.18484`


#### icf-eos-opacity-3062

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=57.15 g/cm³、T=839.5 eV,对 hν=2.642e+04 eV 光子的自由程 l=0.0582117 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.17179 1**（容差 ±2%）
   - 独立复算:`0.01/0.0582117`


#### icf-eos-opacity-3063

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=253.5 g/cm³、T=8551 eV,对 hν=948.4 eV 光子的自由程 l=7.13309e-05 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **140.19 1**（容差 ±2%）
   - 独立复算:`0.01/7.13309e-05`


#### icf-eos-opacity-3064

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=7.079 g/cm³、T=6.266e+04 eV,对 hν=1.581e+04 eV 光子的自由程 l=0.078282 cm。求厚度 L=0.001 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.012774 1**（容差 ±2%）
   - 独立复算:`0.001/0.078282`


#### icf-eos-opacity-3065

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=42.36 g/cm³、T=4.498e+04 eV,对 hν=2.999e+04 eV 光子的自由程 l=0.0205417 cm。求厚度 L=0.1 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **4.8681 1**（容差 ±2%）
   - 独立复算:`0.1/0.0205417`


#### icf-eos-opacity-3066

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=23.33 g/cm³、hν=299.9 eV 下:T₁=1629 eV 时自由程 l₁=0.000343364 cm,T₂=82.22 eV 时 l₂=2.27496e-05 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **15.093 1**（容差 ±2%）
   - 独立复算:`(0.000343364)/(2.27496e-05)`


#### icf-eos-opacity-3067

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=6745 g/cm³、hν=6457 eV 下:T₁=5200 eV 时自由程 l₁=1.25672e-05 cm,T₂=365.6 eV 时 l₂=3.02983e-06 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **4.1478 1**（容差 ±2%）
   - 独立复算:`(1.25672e-05)/(3.02983e-06)`


#### icf-eos-opacity-3068

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=1.225e+04 g/cm³、hν=4406 eV 下:T₁=1169 eV 时自由程 l₁=2.87555e-06 cm,T₂=1.009e+04 eV 时 l₂=6.25825e-06 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.45948 1**（容差 ±2%）
   - 独立复算:`(2.87555e-06)/(6.25825e-06)`


#### icf-eos-opacity-3069

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=139.6 g/cm³、hν=122.5 eV 下:T₁=1169 eV 时自由程 l₁=2.63526e-06 cm,T₂=4406 eV 时 l₂=1.16709e-05 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.2258 1**（容差 ±2%）
   - 独立复算:`(2.63526e-06)/(1.16709e-05)`


#### icf-eos-opacity-3070

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=620.9 g/cm³、hν=64.57 eV 下:T₁=365.6 eV 时自由程 l₁=1.13123e-06 cm,T₂=1.435e+05 eV 时 l₂=1.90629e-05 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.059342 1**（容差 ±2%）
   - 独立复算:`(1.13123e-06)/(1.90629e-05)`


#### icf-eos-opacity-3071

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=1127 g/cm³、hν=8337 eV 下:T₁=1923 eV 时自由程 l₁=3.32659e-05 cm,T₂=1.009e+04 eV 时 l₂=0.000111928 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.29721 1**（容差 ±2%）
   - 独立复算:`(3.32659e-05)/(0.000111928)`


#### icf-eos-opacity-4001

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=0.4831 g/cm³、T=2270 eV、光子能量 hν=2042 eV 处的 Rosseland 自由程 l=11.4058 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.1815 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.483059*11.4058)`


#### icf-eos-opacity-4002

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=1.592 g/cm³、T=4.498e+04 eV、光子能量 hν=948.4 eV 处的 Rosseland 自由程 l=3.50686 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.17909 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(1.59221*3.50686)`


#### icf-eos-opacity-4003

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=2.891 g/cm³、T=7.396e+04 eV、光子能量 hν=500 eV 处的 Rosseland 自由程 l=1.90249 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.18184 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(2.89068*1.90249)`


#### icf-eos-opacity-4004

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=1.225e+04 g/cm³、T=262.4 eV、光子能量 hν=2323 eV 处的 Rosseland 自由程 l=2.68175e-06 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **30.45 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(12246.2*2.68175e-06)`


#### icf-eos-opacity-4005

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=42.36 g/cm³、T=2.312e+04 eV、光子能量 hν=1.799e+04 eV 处的 Rosseland 自由程 l=0.132766 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.17779 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(42.3643*0.132766)`


#### icf-eos-opacity-4006

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Be(Z=4)在 ρ=103.8 g/cm³、T=839.5 eV、光子能量 hν=2.642e+04 eV 处的 Rosseland 自由程 l=0.0537544 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.1793 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(103.753*0.0537544)`


#### icf-eos-opacity-4007

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=837.5 g/cm³、T=8.73e+04 eV、光子能量 hν=2999 eV 处的 Rosseland 自由程 l=0.00463556 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.25757 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(837.529*0.00463556)`


#### icf-eos-opacity-4008

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=253.5 g/cm³、T=262.4 eV、光子能量 hν=204.2 eV 处的 Rosseland 自由程 l=3.55453e-06 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **1109.7 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(253.513*3.55453e-06)`


#### icf-eos-opacity-4009

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=5.248 g/cm³、T=5200 eV、光子能量 hν=734.5 eV 处的 Rosseland 自由程 l=0.0449642 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **4.2377 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(5.24807*0.0449642)`


#### icf-eos-opacity-4010

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=5012 g/cm³、T=3.811e+04 eV、光子能量 hν=3412 eV 处的 Rosseland 自由程 l=0.000227116 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.87852 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(5011.87*0.000227116)`


#### icf-eos-opacity-4011

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=1.225e+04 g/cm³、T=510.5 eV、光子能量 hν=1.581e+04 eV 处的 Rosseland 自由程 l=4.1449e-06 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **19.701 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(12246.2*4.1449e-06)`


#### icf-eos-opacity-4012

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Al(Z=13)在 ρ=0.08072 g/cm³、T=3733 eV、光子能量 hν=387.3 eV 处的 Rosseland 自由程 l=23.6601 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.52358 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0807235*23.6601)`


#### icf-eos-opacity-4013

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=139.6 g/cm³、T=3162 eV、光子能量 hν=1076 eV 处的 Rosseland 自由程 l=2.21871e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **322.77 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(139.637*2.21871e-05)`


#### icf-eos-opacity-4014

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=0.1086 g/cm³、T=7.396e+04 eV、光子能量 hν=64.57 eV 处的 Rosseland 自由程 l=45.5376 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.20213 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.108643*45.5376)`


#### icf-eos-opacity-4015

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=0.1972 g/cm³、T=7.396e+04 eV、光子能量 hν=734.5 eV 处的 Rosseland 自由程 l=30.274 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **0.16747 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.197242*30.274)`


#### icf-eos-opacity-4016

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=2761 g/cm³、T=5.309e+04 eV、光子能量 hν=5000 eV 处的 Rosseland 自由程 l=4.36834e-05 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **8.2925 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(2760.58*4.36834e-05)`


#### icf-eos-opacity-4017

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=1521 g/cm³、T=5.309e+04 eV、光子能量 hν=204.2 eV 处的 Rosseland 自由程 l=7.85042e-06 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **83.774 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(1520.55*7.85042e-06)`


#### icf-eos-opacity-4018

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> SNOP 模型给出 Au(Z=79)在 ρ=0.04446 g/cm³、T=114.6 eV、光子能量 hν=340.4 eV 处的 Rosseland 自由程 l=0.130372 cm。求该点质量不透明度 κ=1/(ρ·l)(cm²/g)。

**答案:** **172.51 cm^2/g**（容差 ±2%）
   - 独立复算:`1/(0.0444631*0.130372)`


#### icf-eos-opacity-4019

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 密度 ρ 轴上取 50 点对数网格:coord=10^(log10(0.01)+(log10(30000.0)-log10(0.01))·i/50),i=1..50。求 i=13 处的坐标值(g/cm³)。

**答案:** **0.48312 g/cm³**（容差 ±2%）
   - 独立复算:`10**(log10(0.01)+(log10(30000.0)-log10(0.01))*13/50)`


#### icf-eos-opacity-4021

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 温度 T 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(200000.0)-log10(50.0))·i/50),i=1..50。求 i=16 处的坐标值(eV)。

**答案:** **710.61 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(200000.0)-log10(50.0))*16/50)`


#### icf-eos-opacity-4022

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 温度 T 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(200000.0)-log10(50.0))·i/50),i=1..50。求 i=34 处的坐标值(eV)。

**答案:** **14072 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(200000.0)-log10(50.0))*34/50)`


#### icf-eos-opacity-4023

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 光子能量 hν 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(30000.0)-log10(50.0))·i/50),i=1..50。求 i=29 处的坐标值(eV)。

**答案:** **2043.1 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(30000.0)-log10(50.0))*29/50)`


#### icf-eos-opacity-4024

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某不透明度表在 光子能量 hν 轴上取 50 点对数网格:coord=10^(log10(50.0)+(log10(30000.0)-log10(50.0))·i/50),i=1..50。求 i=18 处的坐标值(eV)。

**答案:** **500.15 eV**（容差 ±2%）
   - 独立复算:`10**(log10(50.0)+(log10(30000.0)-log10(50.0))*18/50)`


#### icf-eos-opacity-4025

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=2.148 g/cm³、T=6.266e+04 eV,对 hν=4406 eV 光子的自由程 l=2.35736 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.004242 1**（容差 ±2%）
   - 独立复算:`0.01/2.35736`


#### icf-eos-opacity-4026

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=0.2661 g/cm³、T=82.22 eV,对 hν=56.89 eV 光子的自由程 l=0.000515054 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **19.415 1**（容差 ±2%）
   - 独立复算:`0.01/0.000515054`


#### icf-eos-opacity-4027

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Al 等离子体 ρ=76.91 g/cm³、T=8551 eV,对 hν=1076 eV 光子的自由程 l=0.00793781 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **1.2598 1**（容差 ±2%）
   - 独立复算:`0.01/0.00793781`


#### icf-eos-opacity-4028

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=9099 g/cm³、T=6.266e+04 eV,对 hν=948.4 eV 光子的自由程 l=3.8479e-06 cm。求厚度 L=0.01 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **2598.8 1**（容差 ±2%）
   - 独立复算:`0.01/3.8479e-06`


#### icf-eos-opacity-4029

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=2761 g/cm³、T=1.959e+04 eV,对 hν=500 eV 光子的自由程 l=2.82453e-06 cm。求厚度 L=0.001 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **354.04 1**（容差 ±2%）
   - 独立复算:`0.001/2.82453e-06`


#### icf-eos-opacity-4030

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Au 等离子体 ρ=0.2661 g/cm³、T=1.191e+04 eV,对 hν=3412 eV 光子的自由程 l=0.732664 cm。求厚度 L=0.001 cm 的板对该光子的光学深度 τ=L/l,并判断光学薄(τ<1)还是光学厚(τ>1)。

**答案:** **0.0013649 1**（容差 ±2%）
   - 独立复算:`0.001/0.732664`


#### icf-eos-opacity-4031

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=6745 g/cm³、hν=1.393e+04 eV 下:T₁=1.406e+04 eV 时自由程 l₁=0.000152948 cm,T₂=2.735e+04 eV 时 l₂=0.000430143 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.35557 1**（容差 ±2%）
   - 独立复算:`(0.000152948)/(0.000430143)`


#### icf-eos-opacity-4032

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Al 在 ρ=0.6516 g/cm³、hν=1581 eV 下:T₁=3.811e+04 eV 时自由程 l₁=6.04361 cm,T₂=8551 eV 时 l₂=2.2936 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **2.635 1**（容差 ±2%）
   - 独立复算:`(6.04361)/(2.2936)`


#### icf-eos-opacity-4033

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=12.85 g/cm³、hν=1581 eV 下:T₁=2.312e+04 eV 时自由程 l₁=0.0151691 cm,T₂=365.6 eV 时 l₂=0.000474209 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **31.988 1**（容差 ±2%）
   - 独立复算:`(0.0151691)/(0.000474209)`


#### icf-eos-opacity-4034

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> Au 在 ρ=31.48 g/cm³、hν=7345 eV 下:T₁=1629 eV 时自由程 l₁=0.00350053 cm,T₂=1.03e+05 eV 时 l₂=0.0187849 cm。求两温度点不透明度之比 κ(T₂)/κ(T₁)。

**答案:** **0.18635 1**（容差 ±2%）
   - 独立复算:`(0.00350053)/(0.0187849)`


#### icf-eos-opacity-2001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=1.239, tep=3.284, tgama=2.366 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **0.0005087 1**（容差 ±1%）
   - 独立复算:`0.000508742`


#### icf-eos-opacity-2002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=0.720, tep=3.428, tgama=2.366 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **0.004848 1**（容差 ±1%）
   - 独立复算:`0.00484784`


#### icf-eos-opacity-2003

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=2.664, tep=4.509, tgama=2.644 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **0.0001587 1**（容差 ±1%）
   - 独立复算:`0.000158742`


#### icf-eos-opacity-2004

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=1.498, tep=3.788, tgama=3.810 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **0.003043 1**（容差 ±1%）
   - 独立复算:`0.00304286`


#### icf-eos-opacity-2005

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=3.829, tep=1.771, tgama=3.755 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **9.706e-05 1**（容差 ±1%）
   - 独立复算:`9.70628e-05`


#### icf-eos-opacity-2006

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=3.829, tep=5.157, tgama=3.921 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **0.0001785 1**（容差 ±1%）
   - 独立复算:`0.000178464`


#### icf-eos-opacity-2007

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=2.404, tep=2.924, tgama=1.755 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **1.618e-07 1**（容差 ±1%）
   - 独立复算:`1.61772e-07`


#### icf-eos-opacity-2008

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某金(Au, Z=79)等离子体不透明度数据库以等间距对数网格存储自由程。四列含义:rod=log₁₀(质量密度), tep=log₁₀(电子温度), tgama=log₁₀(光子能量), log₁₀(lnu)=log₁₀(自由程)。查表:rod=3.700, tep=5.013, tgama=2.421 对应的 log₁₀(lnu) 是多少(保留 4 位有效数字)?

**答案:** **2.785e-06 1**（容差 ±1%）
   - 独立复算:`2.7852e-06`


#### icf-eos-opacity-2009

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库给出某状态(rod=-1.352, tep=4.581, tgama=2.143)的 log₁₀(lnu)=144.693(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。

**答案:** **4.932e+142 m**（容差 ±2%）
   - 独立复算:`10**(144.693)/100`


#### icf-eos-opacity-2010

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库给出某状态(rod=-0.575, tep=2.636, tgama=3.977)的 log₁₀(lnu)=0.777886(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。

**答案:** **0.05996 m**（容差 ±2%）
   - 独立复算:`10**(0.777886)/100`


#### icf-eos-opacity-2011

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库给出某状态(rod=0.979, tep=1.843, tgama=2.532)的 log₁₀(lnu)=8.61384e-05(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。

**答案:** **0.01 m**（容差 ±2%）
   - 独立复算:`10**(8.61384e-05)/100`


#### icf-eos-opacity-2012

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库给出某状态(rod=1.239, tep=4.941, tgama=4.366)的 log₁₀(lnu)=0.0444935(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。

**答案:** **0.01108 m**（容差 ±2%）
   - 独立复算:`10**(0.0444935)/100`


#### icf-eos-opacity-2013

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库给出某状态(rod=-1.223, tep=3.212, tgama=3.255)的 log₁₀(lnu)=0.591938(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。

**答案:** **0.03908 m**（容差 ±2%）
   - 独立复算:`10**(0.591938)/100`


#### icf-eos-opacity-2014

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库给出某状态(rod=-1.482, tep=4.797, tgama=3.477)的 log₁₀(lnu)=60.7963(自由程以 cm 为单位)。求该自由程的物理值,以 m 表示(保留 3 位有效数字)。

**答案:** **6.256e+58 m**（容差 ±2%）
   - 独立复算:`10**(60.7963)/100`


#### icf-eos-opacity-2015

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,状态 A(rod=0.073, tep=2.996, tgama=3.199)的 log₁₀(lnu)=0.00926211;状态 B(rod=-1.093, tep=5.085, tgama=2.866)的 log₁₀(lnu)=81.5242。求自由程之比 lnu_A/lnu_B(保留 3 位有效数字)。

**答案:** **3.055e-82 1**（容差 ±2%）
   - 独立复算:`10**(0.00926211-(81.5242))`


#### icf-eos-opacity-2016

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,状态 A(rod=3.052, tep=5.301, tgama=3.032)的 log₁₀(lnu)=0.00104699;状态 B(rod=1.109, tep=4.653, tgama=2.699)的 log₁₀(lnu)=0.0948632。求自由程之比 lnu_A/lnu_B(保留 3 位有效数字)。

**答案:** **0.8057 1**（容差 ±2%）
   - 独立复算:`10**(0.00104699-(0.0948632))`


#### icf-eos-opacity-2017

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,状态 A(rod=1.498, tep=4.004, tgama=2.810)的 log₁₀(lnu)=0.00113782;状态 B(rod=2.275, tep=4.581, tgama=4.199)的 log₁₀(lnu)=0.00205632。求自由程之比 lnu_A/lnu_B(保留 3 位有效数字)。

**答案:** **0.9979 1**（容差 ±2%）
   - 独立复算:`10**(0.00113782-(0.00205632))`


#### icf-eos-opacity-2018

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,状态 A(rod=0.850, tep=2.563, tgama=2.199)的 log₁₀(lnu)=6.13243e-05;状态 B(rod=-0.964, tep=1.987, tgama=2.199)的 log₁₀(lnu)=0.0464562。求自由程之比 lnu_A/lnu_B(保留 3 位有效数字)。

**答案:** **0.8987 1**（容差 ±2%）
   - 独立复算:`10**(6.13243e-05-(0.0464562))`


#### icf-eos-opacity-2019

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,rod=-1.093, tep=1.987 时:tgama=3.810 对应 log₁₀(lnu)=1.06633,tgama=3.866 对应 log₁₀(lnu)=1.30333。在 log 空间对 tgama 做线性插值,估计 tgama=3.8380 处的 log₁₀(lnu)(保留 4 位有效数字)。

**答案:** **1.185 1**（容差 ±2%）
   - 独立复算:`(1.06633+1.30333)/2`


#### icf-eos-opacity-2020

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,rod=-1.741, tep=3.932 时:tgama=3.088 对应 log₁₀(lnu)=121.131,tgama=3.144 对应 log₁₀(lnu)=99.2772。在 log 空间对 tgama 做线性插值,估计 tgama=3.1160 处的 log₁₀(lnu)(保留 4 位有效数字)。

**答案:** **110.2 1**（容差 ±2%）
   - 独立复算:`(121.131+99.2772)/2`


#### icf-eos-opacity-2021

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,rod=2.664, tep=3.284 时:tgama=2.977 对应 log₁₀(lnu)=3.91213e-06,tgama=3.032 对应 log₁₀(lnu)=4.30043e-06。在 log 空间对 tgama 做线性插值,估计 tgama=3.0045 处的 log₁₀(lnu)(保留 4 位有效数字)。

**答案:** **4.106e-06 1**（容差 ±2%）
   - 独立复算:`(3.91213e-06+4.30043e-06)/2`


#### icf-eos-opacity-2022

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 金等离子体数据库中,rod=2.664, tep=2.563 时:tgama=2.810 对应 log₁₀(lnu)=1.91091e-05,tgama=2.866 对应 log₁₀(lnu)=2.1832e-05。在 log 空间对 tgama 做线性插值,估计 tgama=2.8380 处的 log₁₀(lnu)(保留 4 位有效数字)。

**答案:** **2.047e-05 1**（容差 ±2%）
   - 独立复算:`(1.91091e-05+2.1832e-05)/2`


#### icf-eos-opacity-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 氢等离子体的两级 Saha 估算:基态与一次电离两能级,n_{i+1}·n_e/n_i=K,K=(2/Λ³)·(g₁/g₀)·exp(-χ/kT),Λ=h/√(2πm_e·kT) 为热德布罗意波长。取 T=3 eV,χ=13.6 eV,g₁/g₀=1,n_e=1e28 m^-3(固体密度量级)。求电离度之比 r=n_{i+1}/n_i=K/n_e,并判断电离态(几乎全电离/部分电离/几乎中性)。常数:h=6.62607015e-34 J·s,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K,1 eV=11604.525 K。

**答案:** **0.0337 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*3*11604.525))**3)) * exp(-13.6/3) / 1e28`


#### icf-eos-opacity-0002

`figure` · `expert` · `numeric_tolerance` · 来源:local_sim

> 下表是某平均原子模型(屏蔽氢模型)对 Z=27 元素在 T=58 eV 下计算的各电离阶段占据概率分布(阶段 0-16,更高阶段概率可忽略):
阶段: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
概率: 1.818e-12, 2.266e-10, 1.410e-08, 6.062e-07, 1.643e-05, 2.799e-04, 2.985e-03, 1.977e-02, 8.044e-02, 0.19846, 0.29170, 0.24969, 0.12070, 3.154e-02, 4.164e-03, 2.461e-04, 4.864e-06
求该温度下的平均电离度 Z̄=Σi·p_i/Σp_i(保留 4 位有效数字)。

**答案:** **10.1716 1**（容差 ±1%）
   - 独立复算:`(0*1.818e-12+1*2.266e-10+2*1.410e-08+3*6.062e-07+4*1.643e-05+5*2.799e-04+6*2.985e-03+7*1.977e-02+8*8.044e-02+9*0.19846+10*0.29170+11*0.24969+12*0.12070+13*3.154e-02+14*4.164e-03+15*2.461e-04+16*4.864e-06)/(1.818e-12+2.266e-10+1.410e-08+6.062e-07+1.643e-05+2.799e-04+2.985e-03+1.977e-02+8.044e-02+0.19846+0.29170+0.24969+0.12070+3.154e-02+4.164e-03+2.461e-04+4.864e-06)`


#### icf-eos-opacity-0003

`concept` · `grad` · `exact_match` · 来源:textbook

> Rosseland 平均不透明度与 Planck 平均不透明度的定义和适用场景有何区别?

**答案:** **A**
   ✅ A. Rosseland 平均是对 1/κ_ν 加权(调和平均),适用于光学厚介质中的辐射扩散;Planck 平均是对 κ_ν 直接加权(算术平均),适用于光学薄介质的发射/吸收
   　 B. Rosseland 平均是算术平均,Planck 平均是调和平均
   　 C. 两者数学上完全等价,只是名字不同
   　 D. Planck 平均只适用于磁约束等离子体


#### icf-eos-opacity-0004

`derivation` · `expert` · `rubric_judge` · 来源:textbook

> 从辐射扩散近似(光学厚介质)出发,推导 Rosseland 平均不透明度的定义式 1/κ_R = [∫(1/κ_ν)(∂B_ν/∂T)dν] / [∫(∂B_ν/∂T)dν],并说明为什么透明度窗口(低 κ_ν 频段)主导辐射泄漏。

**答案:** **rubric 判分（权重和=1）:**
   - [0.25] 写出扩散近似下辐射通量 F_ν = -(c/3κ_νρ)∇E_ν 或等价形式
   - [0.25] 在 LTE 下 E_ν∝B_ν(T),对频率积分并把总通量写成 -c/(3κ_Rρ)∇E 形式
   - [0.25] 比较系数得到 1/κ_R 的调和平均定义式
   - [0.25] 论证 1/κ 加权使低不透明度频段(窗口)贡献最大,决定泄漏


#### icf-eos-opacity-0005

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子-离子库仑对数:n_e=1e24 cm^-3(ICF 晕区密度量级),T=1 keV。用 NRL Plasma Formulary 公式 lnΛ=23-0.5·ln(n_e[cm^-3])+1.5·ln(T[eV])。

**答案:** **5.7277 1**（容差 ±2%）
   - 独立复算:`23 - 0.5*log(1e24) + 1.5*log(1e3)`


#### icf-eos-opacity-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 求压缩 DT 等离子体(n=1e29 m^-3,T=5 keV)的德拜长度 λ_D=√(ε0·kT/(n·e²))(m)。常数:ε0=8.8541878128e-12 F/m,k_B=1.380649e-23 J/K,e=1.602176634e-19 C,1 eV=11604.525 K。

**答案:** **1.6623e-09 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12 * 1.380649e-23 * 5000*11604.525 / (1e29 * (1.602176634e-19)**2))`


#### icf-eos-opacity-0007

`concept` · `expert` · `exact_match` · 来源:textbook

> 为什么 Rosseland 平均不透明度对'透明度窗口'(某些频率段 κ_ν 特别低)特别敏感,而 Planck 平均不敏感?

**答案:** **A**
   ✅ A. Rosseland 是 1/κ_ν 的加权平均,低 κ_ν 频段的 1/κ_ν 很大,主导整个积分——辐射优先从窗口泄漏;Planck 是 κ_ν 的算术加权,窗口贡献自然很小
   　 B. 因为窗口处光子能量最高,只影响 Rosseland 权重
   　 C. 因为 Planck 平均只计算束缚-束缚跃迁
   　 D. 两种平均对窗口同样敏感,题干前提错误


#### icf-eos-opacity-0008

`derivation` · `grad` · `rubric_judge` · 来源:textbook

> 从化学势相等(电离平衡 i ⇌ i+1 + e)出发推导 Saha 方程 n_{i+1}·n_e/n_i = (2/Λ³)·(g_{i+1}/g_i)·exp(-χ/kT),其中 Λ 为电子热德布罗意波长。

**答案:** **rubric 判分（权重和=1）:**
   - [0.2] 写出电离平衡条件 μ_i = μ_{i+1} + μ_e
   - [0.25] 用理想气体化学势(含配分函数/简并度)展开三项
   - [0.25] 电子平动配分函数给出 2/Λ³ 因子(自旋简并 2)
   - [0.2] 整理得 Saha 方程并明确 χ 为电离能
   - [0.1] 指出适用条件(LTE、理想气体、可忽略压致电离)


#### icf-eos-opacity-gen-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=3 eV,n_e=7.6e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **5.502e-09 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*3*11604.525))**3))*exp(-54.4/3)/7.6e+28`


#### icf-eos-opacity-gen-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=3 eV,n_e=3.1e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **1.349e-08 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*3*11604.525))**3))*exp(-54.4/3)/3.1e+28`


#### icf-eos-opacity-gen-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=24.6 eV,T=5 eV,n_e=9e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.005474 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*5*11604.525))**3))*exp(-24.6/5)/9e+28`


#### icf-eos-opacity-gen-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=13.6 eV,T=10 eV,n_e=2.5e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **1.96 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*10*11604.525))**3))*exp(-13.6/10)/2.5e+28`


#### icf-eos-opacity-gen-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=24.6 eV,T=2 eV,n_e=2.2e+27 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **3.533e-05 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*2*11604.525))**3))*exp(-24.6/2)/2.2e+27`


#### icf-eos-opacity-gen-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=3 eV,n_e=2.2e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **1.901e-08 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*3*11604.525))**3))*exp(-54.4/3)/2.2e+28`


#### icf-eos-opacity-gen-0007

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=2 eV,n_e=6.3e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **4.171e-13 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*2*11604.525))**3))*exp(-54.4/2)/6.3e+28`


#### icf-eos-opacity-gen-0008

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=13.6 eV,T=3 eV,n_e=9.1e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.003704 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*3*11604.525))**3))*exp(-13.6/3)/9.1e+28`


#### icf-eos-opacity-gen-0009

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=13.6 eV,T=5 eV,n_e=5.1e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.08718 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*5*11604.525))**3))*exp(-13.6/5)/5.1e+28`


#### icf-eos-opacity-gen-0010

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=5 eV,n_e=4.9e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **2.594e-05 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*5*11604.525))**3))*exp(-54.4/5)/4.9e+28`


#### icf-eos-opacity-gen-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=3 eV,n_e=9.4e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **4.448e-09 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*3*11604.525))**3))*exp(-54.4/3)/9.4e+28`


#### icf-eos-opacity-gen-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=13.6 eV,T=10 eV,n_e=7.8e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.6282 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*10*11604.525))**3))*exp(-13.6/10)/7.8e+28`


#### icf-eos-opacity-genb-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=13.6 eV,T=2 eV,n_e=8.4e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.0002264 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*2*11604.525))**3))*exp(-13.6/2)/8.4e+28`


#### icf-eos-opacity-genb-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=10 eV,n_e=9e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.009205 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*10*11604.525))**3))*exp(-54.4/10)/9e+28`


#### icf-eos-opacity-genb-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=24.6 eV,T=5 eV,n_e=5.3e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.009296 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*5*11604.525))**3))*exp(-24.6/5)/5.3e+28`


#### icf-eos-opacity-genc-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 两级 Saha:χ=54.4 eV,T=10 eV,n_e=4.1e+28 m⁻³,g₁/g₀=1。K=(2/Λ³)·e^(-χ/T),Λ=h/√(2πm_e·kT)。求 r=n_{i+1}/n_i=K/n_e。常数:h=6.62607015e-34,m_e=9.1093837015e-31 kg,k_B=1.380649e-23 J/K。

**答案:** **0.02021 1**（容差 ±5%）
   - 独立复算:`(2/((6.62607015e-34/sqrt(2*pi*9.1093837015e-31*1.380649e-23*10*11604.525))**3))*exp(-54.4/10)/4.1e+28`


#### icf-eos-opacity-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于平均原子模型(average atom)在 EOS/不透明度计算中的角色,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 它用单一'代表性原子'的自洽场近似描述等离子体平均电离状态与占据数
   ✅ B. 屏蔽氢模型(screened hydrogenic)是其简化版本,用解析屏蔽常数估计能级
   　 C. 平均原子模型给出逐条谱线的精确位置
   ✅ D. 其输出(平均电离度、占据数)可驱动不透明度与 EOS 表


#### icf-eos-opacity-hard-0002

`concept` · `grad` · `exact_match` · 来源:textbook

> 在 LTE 与非 LTE(non-LTE)不透明度计算的适用性上,正确的是?

**答案:** **A**
   ✅ A. 高密度(碰撞主导)时 LTE 近似较好;低密度晕区/快速变化区需 non-LTE 速率方程模型
   　 B. LTE 在所有 ICF 区域都精确成立
   　 C. non-LTE 计算更简单
   　 D. LTE 与 non-LTE 结果总相同


#### icf-eos-opacity-hard-0003

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于压致电离(pressure ionization)在高密度等离子体中的意义,正确的是?

**答案:** **A**
   ✅ A. 高密度下粒子间相互作用使连续谱下移、束缚态消失,电离度高于孤立原子 Saha 预测,是稠密 ICF 等离子体 EOS 的关键修正
   　 B. 压致电离只发生在真空中
   　 C. 压致电离使电离度降低
   　 D. 压致电离与密度无关


---

## icf/ignition-gain（24 题）


#### icf-ignition-gain-gen-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.8 g/cm²,T=5 keV。求乘积值并判断是否达到 1.5。

**答案:** **4 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.8*5`


#### icf-ignition-gain-gen-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.8 g/cm²,T=8 keV。求乘积值并判断是否达到 1.5。

**答案:** **6.4 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.8*8`


#### icf-ignition-gain-gen-0003

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.5 g/cm²,T=8 keV。求乘积值并判断是否达到 1.5。

**答案:** **4 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.5*8`


#### icf-ignition-gain-gen-0004

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.2 g/cm²,T=8 keV。求乘积值并判断是否达到 1.5。

**答案:** **1.6 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.2*8`


#### icf-ignition-gain-gen-0007

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.5 g/cm²,T=4 keV。求乘积值并判断是否达到 1.5。

**答案:** **2 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.5*4`


#### icf-ignition-gain-gen-0008

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.5 g/cm²,T=5 keV。求乘积值并判断是否达到 1.5。

**答案:** **2.5 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.5*5`


#### icf-ignition-gain-gen-0009

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.3 g/cm²,T=5 keV。求乘积值并判断是否达到 1.5。

**答案:** **1.5 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.3*5`


#### icf-ignition-gain-gen-0012

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.3 g/cm²,T=8 keV。求乘积值并判断是否达到 1.5。

**答案:** **2.4 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.3*8`


#### icf-ignition-gain-genb-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.8 g/cm²,T=4 keV。求乘积值并判断是否达到 1.5。

**答案:** **3.2 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.8*4`


#### icf-ignition-gain-genb-0003

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 热斑点火的简单乘积判据(题设):ρR(g/cm²)×T(keV) 超过约 1.5 视为接近自加热条件。某热斑 ρR=0.2 g/cm²,T=4 keV。求乘积值并判断是否达到 1.5。

**答案:** **0.8 g/cm^2 keV**（容差 ±2%）
   - 独立复算:`0.2*4`


#### icf-ignition-gain-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于燃烧传播(burn propagation)与能量增益上限,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 当热斑满足点火条件后,α 沉积加热可引发燃烧波向周围冷燃料传播,放大产额
   ✅ B. 燃烧传播使增益对热斑条件的依赖变得非线性(阈值附近增益陡变)
   　 C. 只要热斑点火,全部燃料必然燃烧完
   ✅ D. 燃料 ρR 决定燃烧深度/燃耗分数


#### icf-ignition-gain-hard-0002

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于增益定义中的能量分母,正确的说法是?

**答案:** **A**
   ✅ A. 靶增益通常定义为聚变产额/入射激光能量,而不是除以靶丸吸收能量;后者称为吸收增益
   　 B. 靶增益的分母是燃料动能
   　 C. 靶增益与吸收增益总是相等
   　 D. 增益定义与能量分母无关


#### icf-ignition-gain-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:public-data

> 2022 年 12 月 5 日 NIF 首次实现点火：激光输入 2.05 MJ，聚变产额 3.15 MJ（LLNL 官方公布值）。靶增益定义为 G = 聚变产额 / 入射激光能量。求 G。

**答案:** **1.54 1**（容差 ±3%）
   - 独立复算:`3.15/2.05`


#### icf-ignition-gain-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:public-data

> 2025 年 4 月 7 日 NIF 打出历史最高产额纪录：激光输入 2.08 MJ（峰值功率 456 TW），聚变产额 8.6 ± 0.45 MJ（LLNL 官方公布）。求该发的靶增益（取产额中心值）。

**答案:** **4.13 1**（容差 ±3%）
   - 独立复算:`8.6/2.08`


#### icf-ignition-gain-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:public-data

> DT 聚变反应 D+T→α(3.5 MeV)+n(14.1 MeV) 每次释放 17.6 MeV。NIF 首次点火发次产额 3.15 MJ，全部按 DT 反应计。求该发次发生的 DT 反应次数（也即发射的 14.1 MeV 中子总数）。1 eV = 1.602176634e-19 J。

**答案:** **1.117e+18 1**（容差 ±2%）
   - 独立复算:`3.15e6 / (17.6e6 * 1.602176634e-19)`


#### icf-ignition-gain-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 取 DT 聚变点火的 Lawson 条件近似式 n·τ_E ≥ 1.5e20 m^-3·s（适用 T ≈ 15 keV 附近）。某磁约束装置芯部密度 n = 1e20 m^-3，求达到该 Lawson 条件所需的最小能量约束时间 τ_E，以 s 为单位。

**答案:** **1.5 s**（容差 ±5%）
   - 独立复算:`1.5e20/1e20`


#### icf-ignition-gain-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:paper

> ICF 热点（hot spot）点火的公开量级：热点压强 p ≈ 350 Gbar、温度 T ≈ 5 keV。把热点视为完全电离 DT（每个离子贡献 1 电子+1 离子两个粒子），由 p = 2·n_i·k_B·T 估计热点离子数密度 n_i，以 m^-3 为单位。1 bar = 1e5 Pa，1 eV = 1.602176634e-19 J。

**答案:** **2.18e+31 m^-3**（容差 ±10%）
   - 独立复算:`350e9*1e5 / (2 * 1.602176634e-19 * 5e3)`


#### icf-ignition-gain-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 燃料燃耗分数常用近似 φ = ρR/(ρR + H_B)，其中面密度 ρR 以 g/cm^2 计、DT 取 H_B = 6 g/cm^2（Atzeni 式）。某内爆燃料 ρR = 1.5 g/cm^2，求燃耗分数 φ，以百分数（%）为单位。

**答案:** **20 %**（容差 ±5%）
   - 独立复算:`100*1.5/(1.5+6)`


#### icf-ignition-gain-0007

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> DT 单位质量聚变能：每次反应 17.6 MeV、反应物质量约 5 u（D≈2u+T≈3u），即每克 DT 完全燃烧释放约 3.39e11 J。某靶丸含 DT 燃料 1 mg，按上题燃耗公式 φ = ρR/(ρR+6) 且 ρR = 1.5 g/cm^2（φ = 0.20），求聚变产额，以 MJ 为单位。

**答案:** **67.8 MJ**（容差 ±5%）
   - 独立复算:`1e-3 * (1.5/7.5) * 3.39e11 / 1e6`


#### icf-ignition-gain-0008

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于 NIF 间接驱动能量链，下列说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. 激光先注入黑腔（hohlraum）转化为 X 射线，再由 X 射线烧蚀靶丸外壳驱动内爆
   ✅ B. NIF 黑腔峰值辐射温度的公开量级约为 300 eV
   ✅ C. 靶丸烧蚀产生的内爆由'火箭效应'（烧蚀物外喷的反冲）驱动
   　 D. 间接驱动中激光能量的大部分最终转化为燃料动能


#### icf-ignition-gain-topup-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:public-data

> 2025 年 2 月 23 日 NIF 发次:输入激光 2.05 MJ,聚变产额 5.0 MJ(LLNL 公开)。求该发次靶增益(保留 3 位有效数字)。

**答案:** **2.439 1**（容差 ±2%）
   - 独立复算:`5.0/2.05`


#### icf-ignition-gain-topup-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:public-data

> 2025 年 10 月 1 日 NIF 第 10 次点火发次:输入激光 2.065 MJ,聚变产额 3.5 MJ(LLNL 公开)。求该发次靶增益(保留 3 位有效数字)。

**答案:** **1.695 1**（容差 ±2%）
   - 独立复算:`3.5/2.065`


#### icf-ignition-gain-topup-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:public-data

> NIF 2025-04-07 纪录发次:输入 2.08 MJ,产额 8.6 MJ。若其中 α 沉积能量(产额的 3.5/17.6 份额)全部用于加热 0.2 mg DT 燃料,求燃料获得的比能(specific energy,J/kg,取 α 份额 0.1989)。

**答案:** **8.55e+09 J/kg**（容差 ±3%）
   - 独立复算:`8.6e6*(3.5/17.6)/2e-4`


#### icf-ignition-gain-topup-0004

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 某 ICF 靶丸含 DT 燃料 0.25 mg。若燃耗分数为 20%,求燃烧的 DT 质量(mg)。

**答案:** **0.05 mg**（容差 ±1%）
   - 独立复算:`0.25*0.2`


---

## icf/implosion（23 题）


#### icf-implosion-gen-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=2e+07 cm/s,壳层质量比 m₀/m_f=3。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **2.197e+07 cm/s**（容差 ±2%）
   - 独立复算:`20000000.0*log(3)`


#### icf-implosion-gen-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=1e+07 cm/s,壳层质量比 m₀/m_f=5。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **1.609e+07 cm/s**（容差 ±2%）
   - 独立复算:`10000000.0*log(5)`


#### icf-implosion-gen-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=3e+07 cm/s,壳层质量比 m₀/m_f=10。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **6.908e+07 cm/s**（容差 ±2%）
   - 独立复算:`30000000.0*log(10)`


#### icf-implosion-gen-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=1e+07 cm/s,壳层质量比 m₀/m_f=10。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **2.303e+07 cm/s**（容差 ±2%）
   - 独立复算:`10000000.0*log(10)`


#### icf-implosion-gen-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=1e+07 cm/s,壳层质量比 m₀/m_f=2。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **6.931e+06 cm/s**（容差 ±2%）
   - 独立复算:`10000000.0*log(2)`


#### icf-implosion-gen-0009

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=1e+07 cm/s,壳层质量比 m₀/m_f=3。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **1.099e+07 cm/s**（容差 ±2%）
   - 独立复算:`10000000.0*log(3)`


#### icf-implosion-gen-0010

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=3e+07 cm/s,壳层质量比 m₀/m_f=3。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **3.296e+07 cm/s**（容差 ±2%）
   - 独立复算:`30000000.0*log(3)`


#### icf-implosion-gen-0012

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=3e+07 cm/s,壳层质量比 m₀/m_f=2。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **2.079e+07 cm/s**（容差 ±2%）
   - 独立复算:`30000000.0*log(2)`


#### icf-implosion-genb-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀火箭:排出速度 u=2e+07 cm/s,壳层质量比 m₀/m_f=5。按 v=u·ln(m₀/m_f) 求内爆速度(cm/s),并换算为 km/s。

**答案:** **3.219e+07 cm/s**（容差 ±2%）
   - 独立复算:`20000000.0*log(5)`


#### icf-implosion-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于 ICF 内爆减速阶段热斑形成的物理,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 动能通过 PdV 功转化为热斑内能,热斑压强反抗进一步压缩
   ✅ B. 热斑形成时燃料中心区压力与壳层压力趋于平衡(近似等压)
   　 C. 热斑加热完全来自外部激光直接加热
   ✅ D. 减速阶段 RT 不稳定性可能把冷燃料混入热斑,抑制点火


#### icf-implosion-hard-0002

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于内爆减速阶段的'停滞'(stagnation)与热斑-壳层界面,正确的有(多选):

**答案:** **A/B/C**
   ✅ A. 停滞时内爆动能最大化转化为热斑内能,界面处压力近似连续
   ✅ B. 界面 RT 混合会把高密度冷材料注入热斑,降低其温度与产额
   ✅ C. 停滞点收敛比越大,界面不稳定性风险越高
   　 D. 停滞与内爆轨迹无关,是预先给定的


#### icf-implosion-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:public-data

> NIF 型靶丸初始半径 R₀=1.1 mm,内爆后热斑半径 R_f=50 μm。求收敛比(convergence ratio)CR=R₀/R_f。

**答案:** **22 1**（容差 ±2%）
   - 独立复算:`1.1/0.05`


#### icf-implosion-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 热斑点火对面密度的要求:热斑密度 ρ=100 g/cm³、半径 R=30 μm=0.003 cm。求面密度 ρR(g/cm²),并与 3.5 MeV α 粒子在 DT 中的射程量级(~0.3 g/cm²)比较说明其意义。

**答案:** **0.3 g/cm^2**（容差 ±2%）
   - 独立复算:`100*0.003`


#### icf-implosion-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 把内爆燃料近似为等熵压缩的均匀球(γ=5/3),压强随半径标度 P∝R^(-3γ)。收敛比 CR=10 时,终态压强与初态压强之比 P₂/P₁ 是多少?

**答案:** **100000 1**（容差 ±2%）
   - 独立复算:`10**(3*5/3)`


#### icf-implosion-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 壳层动能估算:壳层(每单位长度)质量 m=1 mg/cm,内爆速度 v=3.5e7 cm/s(350 km/s)。按 E=½mv²(cgs:E[MJ/cm]=0.5e-3·m[mg/cm]·v²/1e13)求动能(MJ/cm)。

**答案:** **0.06125 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*1*(3.5e7)**2/1e13`


#### icf-implosion-0005

`concept` · `grad` · `exact_match` · 来源:textbook

> ICF 热斑(hot spot)实现自加点火需要同时满足若干最低条件。下列关于热斑点火条件的说法,正确的有哪些(多选)?

**答案:** **A/B/D**
   ✅ A. 热斑温度足够高(约 4-5 keV 以上),使 DT 反应率足以克服韧致辐射损失
   ✅ B. 热斑面密度 ρR 足够大(约 0.3 g/cm² 以上),使 α 粒子沉积于热斑内
   　 C. 热斑必须被磁场约束到秒级时间尺度
   ✅ D. 热斑压强由 PdV 功在内爆减速阶段建立


#### icf-implosion-0006

`concept` · `undergrad` · `exact_match` · 来源:textbook

> ICF 内爆的驱动效率为何很低(激光能量只有百分之几变成燃料动能)?最根本的物理原因是什么?

**答案:** **A**
   ✅ A. 烧蚀驱动本质是火箭:大部分能量用于把烧蚀物向外喷射,壳层获得的动量来自反冲,火箭效率受排出速度与壳层速度之比限制
   　 B. 激光在黑腔壁上全部被反射损失
   　 C. 燃料的比热太大,难以加热
   　 D. 靶丸太重,无法加速


#### icf-implosion-0007

`derivation` · `expert` · `rubric_judge` · 来源:textbook

> 从烧蚀火箭模型推导 ICF 壳体内爆速度:设烧蚀物排出速度 u(烧蚀面参考系)近似恒定,壳层质量从 m₀ 减到 m_f,推导 v = u·ln(m₀/m_f) 形式的关系,并讨论提高内爆速度的途径及其代价(如剩余质量过小对 RT 稳定性的影响)。

**答案:** **rubric 判分（权重和=1）:**
   - [0.25] 写出变质量体动量方程 m·dv/dt = -u·dm/dt(符号约定正确)
   - [0.25] 积分得到 v = u·ln(m₀/m_f)
   - [0.2] 说明 u 由烧蚀物理(烧蚀压/烧蚀率)决定
   - [0.15] 讨论:提高 v 需大 m₀/m_f(烧掉更多质量)或更高 u
   - [0.15] 指出剩余壳层过薄/过轻会加剧 RT 破裂风险的权衡


#### icf-sim-gen-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 等熵压缩均匀球(γ=5/3),收敛比 CR=30。温度标度 T∝ρ^(γ-1),ρ∝CR³,即 T∝CR^(3(γ-1))。求 T₂/T₁。

**答案:** **900 1**（容差 ±2%）
   - 独立复算:`30**(3*(5/3-1))`


#### icf-sim-gen-0022

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 等熵压缩均匀球(γ=5/3),收敛比 CR=40。温度标度 T∝ρ^(γ-1),ρ∝CR³,即 T∝CR^(3(γ-1))。求 T₂/T₁。

**答案:** **1600 1**（容差 ±2%）
   - 独立复算:`40**(3*(5/3-1))`


#### icf-sim-gen-0023

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 等熵压缩均匀球(γ=5/3),收敛比 CR=25。温度标度 T∝ρ^(γ-1),ρ∝CR³,即 T∝CR^(3(γ-1))。求 T₂/T₁。

**答案:** **625 1**（容差 ±2%）
   - 独立复算:`25**(3*(5/3-1))`


#### icf-sim-gen-0025

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 等熵压缩均匀球(γ=5/3),收敛比 CR=20。温度标度 T∝ρ^(γ-1),ρ∝CR³,即 T∝CR^(3(γ-1))。求 T₂/T₁。

**答案:** **400 1**（容差 ±2%）
   - 独立复算:`20**(3*(5/3-1))`


#### icf-sim-genc-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 等熵压缩均匀球(γ=5/3),收敛比 CR=15。温度标度 T∝ρ^(γ-1),ρ∝CR³,即 T∝CR^(3(γ-1))。求 T₂/T₁。

**答案:** **225 1**（容差 ±2%）
   - 独立复算:`15**(3*(5/3-1))`


---

## icf/lpi（20 题）


#### icf-lpi-gen-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=0.351 μm,T_e=2 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **1.425e+15 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(2/2)*(0.5/0.351)`


#### icf-lpi-gen-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=0.527 μm,T_e=2 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **9.488e+14 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(2/2)*(0.5/0.527)`


#### icf-lpi-gen-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=1.06 μm,T_e=2 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **4.717e+14 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(2/2)*(0.5/1.06)`


#### icf-lpi-gen-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=0.527 μm,T_e=1 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **4.744e+14 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(1/2)*(0.5/0.527)`


#### icf-lpi-gen-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=1.06 μm,T_e=3 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **7.075e+14 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(3/2)*(0.5/1.06)`


#### icf-lpi-gen-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=1.06 μm,T_e=1 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **2.358e+14 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(1/2)*(0.5/1.06)`


#### icf-lpi-gen-0010

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=0.351 μm,T_e=3 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **2.137e+15 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(3/2)*(0.5/0.351)`


#### icf-lpi-genb-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 工程经验估计:受激散射阈值强度 I_th≈1e15·(T_e/2keV)·(0.5μm/λ) W/cm²(题设公式)。λ=0.351 μm,T_e=1 keV。求 I_th(W/cm²),并说明为何 SRS/SBS 在 NIF 参数下需要关注。

**答案:** **7.123e+14 W/cm^2**（容差 ±2%）
   - 独立复算:`1e15*(1/2)*(0.5/0.351)`


#### icf-lpi-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于受激布里渊散射(SBS)与受激拉曼散射(SRS)的区别,正确的有(多选):

**答案:** **A/B/C**
   ✅ A. SBS 的散射波是离子声波,频率下移小(声子能量);SRS 的散射波是电子等离子体波,频率下移大
   ✅ B. SBS 可在整个次临界密度区发生,SRS 限于 n≤n_c/4
   ✅ C. SRS 更容易产生超热电子
   　 D. SBS 与 SRS 都需要密度恰好等于 n_c/4


#### icf-lpi-hard-0002

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于激光成丝(filamentation)的物理驱动,正确的是?

**答案:** **A**
   ✅ A. 有质动力把等离子体推出高光强区,使局部折射率变化并进一步聚焦光强,形成正反馈
   　 B. 由磁场自发形成
   　 C. 由重力不稳定性驱动
   　 D. 由电子回旋共振驱动


#### icf-lpi-hard-0003

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于双等离子体子衰变(TPD)的特征,正确的有(多选):

**答案:** **A/C**
   ✅ A. 入射光衰变为两个电子等离子体波,频率均接近 ω0/2,故阈值出现在 n_c/4 附近
   　 B. TPD 是纯电磁过程,不加热等离子体
   ✅ C. TPD 与 SRS 一样产生超热电子,是预热的重要来源
   　 D. TPD 只发生在 n>n_c 的过密区


#### icf-lpi-hard-0004

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于临界密度面在 ICF 中的物理意义,正确的有(多选):

**答案:** **A/B/C**
   ✅ A. 激光只能传播到临界密度面附近,能量沉积主要发生在次临界晕区
   ✅ B. 临界密度由激光波长决定(波长越短,临界密度越高)
   ✅ C. 四分之一临界密度面是 TPD/SRS 的关键位置
   　 D. 超过临界密度后激光完全不被吸收


#### icf-lpi-hard-0005

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于激光束平滑技术(RPP、SSD、PSD、CPP)的作用,正确的有(多选):

**答案:** **A/B/C**
   ✅ A. 随机相位板(RPP)把束斑打散为小散斑,降低大尺度不均匀性
   ✅ B. 光谱色散平滑(SSD)使散斑随时间快速变化,抑制成丝/不稳定性增长
   ✅ C. 偏振平滑(PSD/CPP)减少散斑间相干,进一步抑制 SBS
   　 D. 平滑技术会显著降低激光总能量


#### icf-lpi-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 激光在等离子体中传播的临界密度近似为 n_c[cm^-3] = 1.1e21 / λ_μm²。NIF 使用三倍频激光 λ=351 nm=0.351 μm,求对应的临界密度(cm^-3)。

**答案:** **8.9283e+21 cm^-3**（容差 ±2%）
   - 独立复算:`1.1e21/0.351**2`


#### icf-lpi-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> OMEGA 激光装置使用二倍频 λ=527 nm=0.527 μm。双等离子体子衰变(TPD)和受激拉曼散射(SRS)最易在四分之一临界密度附近发生。求 0.527 μm 激光对应的 n_c/4(cm^-3)。

**答案:** **9.9018e+20 cm^-3**（容差 ±2%）
   - 独立复算:`1.1e21/0.527**2/4`


#### icf-lpi-0003

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于激光-等离子体参数不稳定性(LPI)发生的密度区域,下列哪些说法正确?(多选)

**答案:** **A/B/C**
   ✅ A. 双等离子体子衰变(TPD)发生在 n_c/4 附近,因为衰变产生的两个等离子体波频率都接近 ω0/2
   ✅ B. 受激拉曼散射(SRS)发生在 n ≤ n_c/4 区域,因为散射光波频率 ω_s = ω0 - ω_pe 必须能在等离子体中传播
   ✅ C. 受激布里渊散射(SBS)可在整个次临界密度区域发生
   　 D. TPD 的直接产物是软 X 射线光子


#### icf-lpi-0004

`concept` · `expert` · `exact_match` · 来源:textbook

> SRS 和 TPD 产生的热电子(几十 keV)为什么对 ICF 内爆有害?

**答案:** **A**
   ✅ A. 热电子射程长,穿过烧蚀层预热 DT 燃料,提高燃料熵,降低可达到的压缩度和面密度,从而抑制点火
   　 B. 热电子会与激光直接相互作用,把激光反射出黑腔
   　 C. 热电子使靶丸带正电,静电斥力阻止内爆
   　 D. 热电子主要造成诊断设备损坏,对物理过程无影响


#### icf-lpi-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 求电子数密度 n_e=1e21 cm^-3=1e27 m^-3 处的电子等离子体频率 ω_pe=√(n_e·e²/(ε0·m_e))(rad/s)。常数:e=1.602176634e-19 C,ε0=8.8541878128e-12 F/m,m_e=9.1093837015e-31 kg。

**答案:** **1.7841e+15 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(1e27*(1.602176634e-19)**2/(8.8541878128e-12*9.1093837015e-31))`


#### icf-lpi-0006

`derivation` · `expert` · `rubric_judge` · 来源:textbook

> 从电磁波在冷等离子体中的色散关系 ω²=ω_pe²+c²k² 出发,推导激光临界密度表达式 n_c(以激光波长 λ 表示),并估算系数(给出 n_c[cm^-3]≈1.1e21/λ_μm² 的推导)。

**答案:** **rubric 判分（权重和=1）:**
   - [0.25] 写出 k→0(截止)条件 ω=ω_pe 作为临界条件
   - [0.3] 代入 ω=2πc/λ 与 ω_pe 定义解出 n_c=4π²c²ε0m_e/(e²λ²)
   - [0.3] 正确完成单位换算得到 n_c[cm^-3]≈1.1e21/λ_μm²(系数在±10% 内)
   - [0.15] 说明 n>n_c 时电磁波倏逝(evanescent)的物理图像


#### icf-lpi-0007

`derivation` · `grad` · `rubric_judge` · 来源:textbook

> 推导受激拉曼散射(SRS)的三波匹配条件:入射光(ω0,k0)衰变为散射光(ωs,ks)与电子等离子体波(ωpe,k_epw)。写出频率与波数匹配条件,并由此说明为何 SRS 只发生在 n ≤ n_c/4。

**答案:** **rubric 判分（权重和=1）:**
   - [0.25] 频率匹配 ω0=ωs+ωpe
   - [0.2] 波数匹配 k0=ks+k_epw
   - [0.3] 散射光可传播条件 ωs≥ωpe 推出 ω0≥2ωpe
   - [0.25] 由 ω0≥2ωpe 得到 n≤n_c/4 结论


---

## icf/rad-hydro（30 题）


#### icf-rad-hydro-gen-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=200 eV 辐射驱动,t=3 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.1731 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*3e-9)`


#### icf-rad-hydro-gen-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=300 eV 辐射驱动,t=10 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.3161 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*10e-9)`


#### icf-rad-hydro-gen-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=300 eV 辐射驱动,t=1 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.09997 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*1e-9)`


#### icf-rad-hydro-gen-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=300 eV 辐射驱动,t=3 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.1731 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*3e-9)`


#### icf-rad-hydro-gen-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=150 eV 辐射驱动,t=1 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.09997 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*1e-9)`


#### icf-rad-hydro-gen-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=150 eV 辐射驱动,t=3 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.1731 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*3e-9)`


#### icf-rad-hydro-gen-0010

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=200 eV 辐射驱动,t=1 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.09997 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*1e-9)`


#### icf-rad-hydro-gen-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=200 eV 辐射驱动,t=10 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.3161 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*10e-9)`


#### icf-rad-hydro-gen-0013

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> Rankine-Hugoniot:γ=5/3 气体,激波马赫数 M=20。(1) 强激波极限压缩比 (γ+1)/(γ-1)=? (2) 该 M 下波后流速与激波速之比 u₂/u_s=(γ-1)/(γ+1)+2/((γ+1)M²)=? 两问都答,以比值为答案(u₂/u_s)。

**答案:** **0.2519 1**（容差 ±2%）
   - 独立复算:`(5/3-1)/(5/3+1)+2/((5/3+1)*20**2)`


#### icf-rad-hydro-gen-0014

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> Rankine-Hugoniot:γ=5/3 气体,激波马赫数 M=5。(1) 强激波极限压缩比 (γ+1)/(γ-1)=? (2) 该 M 下波后流速与激波速之比 u₂/u_s=(γ-1)/(γ+1)+2/((γ+1)M²)=? 两问都答,以比值为答案(u₂/u_s)。

**答案:** **0.28 1**（容差 ±2%）
   - 独立复算:`(5/3-1)/(5/3+1)+2/((5/3+1)*5**2)`


#### icf-rad-hydro-gen-0015

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> Rankine-Hugoniot:γ=5/3 气体,激波马赫数 M=2。(1) 强激波极限压缩比 (γ+1)/(γ-1)=? (2) 该 M 下波后流速与激波速之比 u₂/u_s=(γ-1)/(γ+1)+2/((γ+1)M²)=? 两问都答,以比值为答案(u₂/u_s)。

**答案:** **0.4375 1**（容差 ±2%）
   - 独立复算:`(5/3-1)/(5/3+1)+2/((5/3+1)*2**2)`


#### icf-rad-hydro-gen-0018

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> Rankine-Hugoniot:γ=5/3 气体,激波马赫数 M=10。(1) 强激波极限压缩比 (γ+1)/(γ-1)=? (2) 该 M 下波后流速与激波速之比 u₂/u_s=(γ-1)/(γ+1)+2/((γ+1)M²)=? 两问都答,以比值为答案(u₂/u_s)。

**答案:** **0.2575 1**（容差 ±2%）
   - 独立复算:`(5/3-1)/(5/3+1)+2/((5/3+1)*10**2)`


#### icf-rad-hydro-genb-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> Marshak 波粗估:辐射扩散系数 D_R≈c·l_R/3,取 Rosseland 自由程 l_R=1e-3 cm(题设值),T=150 eV 辐射驱动,t=10 ns。估计波前位置 x_f≈√(D_R·t)(cm)。

**答案:** **0.3161 cm**（容差 ±3%）
   - 独立复算:`sqrt(2.99792458e10*0.001/3*10e-9)`


#### icf-rad-hydro-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于辐射热波(Marshak 波)与流体激波在 ICF 靶中的相互作用,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 辐射热波可先于激波加热材料,改变其初始状态(预热)
   ✅ B. 预热会提高燃料熵,使后续压缩效率下降
   　 C. 辐射热波与激波完全独立,互不影响
   ✅ D. 控制预热是间接驱动靶设计的核心问题之一


#### icf-rad-hydro-hard-0002

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于 ICF 中的能量输运机制,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 电子热传导在烧蚀晕区起关键作用,需用通量限制(flux limiter)处理非局域效应
   ✅ B. 辐射输运在高 Z 壁材料中以多群扩散近似为主
   　 C. 热传导在所有区域都是局域线性的
   ✅ D. 激光能量沉积主要通过逆韧致吸收


#### icf-rad-hydro-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> NIF 黑腔峰值辐射温度约 300 eV。求该温度黑体的辐射出射度 F=σ_SB·T⁴(W/m²)。常数:σ_SB=5.670374419e-8 W/(m²·K⁴),1 eV=11604.525 K。

**答案:** **8.331e+18 W/m^2**（容差 ±2%）
   - 独立复算:`5.670374419e-8 * (300*11604.525)**4`


#### icf-rad-hydro-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 求 300 eV 黑体辐射场的辐射压强 P=a_rad·T⁴/3(Pa),并换算为 Mbar(1 Mbar=1e11 Pa)。常数:辐射常数 a_rad=7.5657e-16 J/(m³·K⁴),1 eV=11604.525 K。

**答案:** **3.7058e+10 Pa**（容差 ±2%）
   - 独立复算:`7.5657e-16 * (300*11604.525)**4 / 3`


#### icf-rad-hydro-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 强激波估算:烧蚀压 p=100 Mbar=1e13 Pa 驱动密度 ρ=1 g/cm³=1000 kg/m³ 的材料(比热比 γ=5/3)。按强激波关系 v_s=√((γ+1)/2·p/ρ),求激波速度(m/s)。

**答案:** **115470 m/s**（容差 ±2%）
   - 独立复算:`sqrt((5/3+1)/2 * 1e13/1000)`


#### icf-rad-hydro-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 强激波后温度:DT 气体(平均原子量 2.5 u)中激波速度 v_s=1e5 m/s,γ=5/3。按 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B 求激波后温度(K),并换算为 eV。常数:u=1.67262192369e-27 kg(近似取 m_p),k_B=1.380649e-23 J/K,1 eV=11604.525 K。

**答案:** **567890 K**（容差 ±2%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2 * (2.5*1.67262192369e-27) * (1e5)**2 / 1.380649e-23`


#### icf-rad-hydro-0005

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于 Marshak 波(辐射热波),下列说法正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 它是由辐射输运(光子扩散)驱动的热波,不需要物质运动即可传播
   ✅ B. 在自相似解中波前位置随时间近似按 x∝t^(1/2) 标度
   　 C. 它要求像激波一样的密度间断面
   ✅ D. 黑腔壁(高 Z 材料)中 X 射线加热波的行为可用 Marshak 波描述


#### icf-rad-hydro-0006

`concept` · `undergrad` · `exact_match` · 来源:textbook

> ICF 间接驱动黑腔(hohlraum)内壁为什么选用金(Au)等高 Z 材料?

**答案:** **A**
   ✅ A. 高 Z 材料不透明度大、对激光能量转换效率高,并能有效再辐射软 X 射线,提高腔内 X 射线约束与转换效率
   　 B. 高 Z 材料密度大,可以提高黑腔的惯性从而延长约束时间
   　 C. 高 Z 材料导热快,防止黑腔局部过热
   　 D. 金的化学性质最稳定,容易加工


#### icf-rad-hydro-0007

`derivation` · `expert` · `rubric_judge` · 来源:textbook

> 从 Rankine-Hugoniot 守恒关系(质量、动量、能量)出发,推导理想气体(比热比 γ)强激波极限(M→∞)下的密度压缩比 ρ₂/ρ₁=(γ+1)/(γ-1),并给出 γ=5/3 时的数值。

**答案:** **rubric 判分（权重和=1）:**
   - [0.2] 写出激波面三个守恒通量条件(质量、动量、能量)
   - [0.2] 引入强激波近似(上游压力/内能可忽略)
   - [0.25] 联立消去激波速度得到压缩比方程
   - [0.2] 得到极限 ρ₂/ρ₁=(γ+1)/(γ-1)
   - [0.15] 代入 γ=5/3 得 4,并说明单原子气体压缩极限为 4 的物理意义


#### icf-rad-hydro-0008

`derivation` · `expert` · `rubric_judge` · 来源:paper

> 推导 Marshak 波(辐射热波进入常密度冷介质)的自相似标度:从辐射扩散近似下的能量方程出发,说明波前位置 x_f 与时间的标度关系 x_f∝t^(1/2) 及其物理来源(辐射扩散系数随温度强增长)。

**答案:** **rubric 判分（权重和=1）:**
   - [0.25] 写出辐射扩散近似 ∂E/∂t = ∂/∂x[(c/3κρ)∂E/∂x] 或等价形式
   - [0.2] 指出不透明度 κ 随温度变化导致扩散系数为温度的增函数
   - [0.3] 用量纲/自相似变量(η=x/√t)论证波前 x_f∝t^(1/2)
   - [0.25] 说明该标度与热传导热波的异同(辐射扩散系数 T 依赖导致波前更陡)


#### icf-sim-gen-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=100 Mbar 驱动 ρ=1000 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **65.25 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*100e11/1000))/1.380649e-23/11604.525`


#### icf-sim-gen-0007

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=100 Mbar 驱动 ρ=3000 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **21.75 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*100e11/3000))/1.380649e-23/11604.525`


#### icf-sim-gen-0008

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=50 Mbar 驱动 ρ=1000 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **32.62 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*50e11/1000))/1.380649e-23/11604.525`


#### icf-sim-gen-0009

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=200 Mbar 驱动 ρ=250 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **522 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*200e11/250))/1.380649e-23/11604.525`


#### icf-sim-gen-0010

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=200 Mbar 驱动 ρ=3000 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **43.5 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*200e11/3000))/1.380649e-23/11604.525`


#### icf-sim-genb-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=50 Mbar 驱动 ρ=3000 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **10.87 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*50e11/3000))/1.380649e-23/11604.525`


#### icf-sim-genb-0009

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ICF 烧蚀激波:压强 p=50 Mbar 驱动 ρ=250 kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。

**答案:** **130.5 eV**（容差 ±3%）
   - 独立复算:`2*(5/3-1)/(5/3+1)**2*(2.5*1.67262192369e-27)*(((5/3+1)/2*50e11/250))/1.380649e-23/11604.525`


---

## icf/rt-rm-instability（44 题）


#### code-rt-scan-0001

`code` · `expert` · `unit_test` · 来源:textbook

> 实现两个函数:(1) rt_growth(k, A, g, L, Va, alpha=0.9, beta=3.1) 返回 Takabe 烧蚀修正 RT 增长率 α√(Akg/(1+AkL))−βkV_a;(2) stabilization_wavenumber(A, g, L, Va, alpha=0.9, beta=3.1) 返回使增长率为零的临界波数 k(解析求根)。只准用标准库。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_rtscan.py`，超时 120s


#### icf-rt-rm-instability-gen-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.89,λ=30 μm(k=2094 cm⁻¹),g=2e+15 cm/s²,L=1e-02 cm,v_a=5e+04 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **7.795e+07 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.89*2094.3951023931954*2000000000000000.0/(1+0.89*2094.3951023931954*0.01))-3*2094.3951023931954*50000.0`


#### icf-rt-rm-instability-gen-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.77,λ=30 μm(k=2094 cm⁻¹),g=2e+15 cm/s²,L=2e-02 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-1.605e+09 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.77*2094.3951023931954*2000000000000000.0/(1+0.77*2094.3951023931954*0.02))-3*2094.3951023931954*300000.0`


#### icf-rt-rm-instability-gen-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.73,λ=100 μm(k=628.3 cm⁻¹),g=5e+14 cm/s²,L=5e-03 cm,v_a=5e+04 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **1.432e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.73*628.3185307179588*500000000000000.0/(1+0.73*628.3185307179588*0.005))-3*628.3185307179588*50000.0`


#### icf-rt-rm-instability-gen-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.77,λ=30 μm(k=2094 cm⁻¹),g=2e+15 cm/s²,L=5e-03 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-1.348e+09 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.77*2094.3951023931954*2000000000000000.0/(1+0.77*2094.3951023931954*0.005))-3*2094.3951023931954*300000.0`


#### icf-rt-rm-instability-gen-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.89,λ=100 μm(k=628.3 cm⁻¹),g=5e+14 cm/s²,L=1e-02 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-3.801e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.89*628.3185307179588*500000000000000.0/(1+0.89*628.3185307179588*0.01))-3*628.3185307179588*300000.0`


#### icf-rt-rm-instability-gen-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.78,λ=30 μm(k=2094 cm⁻¹),g=5e+14 cm/s²,L=2e-02 cm,v_a=1e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-4.881e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.78*2094.3951023931954*500000000000000.0/(1+0.78*2094.3951023931954*0.02))-3*2094.3951023931954*100000.0`


#### icf-rt-rm-instability-gen-0007

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.8,λ=50 μm(k=1257 cm⁻¹),g=5e+14 cm/s²,L=1e-02 cm,v_a=5e+04 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **3.431e+06 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.8*1256.6370614359175*500000000000000.0/(1+0.8*1256.6370614359175*0.01))-3*1256.6370614359175*50000.0`


#### icf-rt-rm-instability-gen-0008

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.73,λ=30 μm(k=2094 cm⁻¹),g=1e+15 cm/s²,L=1e-02 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-1.609e+09 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.73*2094.3951023931954*1000000000000000.0/(1+0.73*2094.3951023931954*0.01))-3*2094.3951023931954*300000.0`


#### icf-rt-rm-instability-gen-0009

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.78,λ=30 μm(k=2094 cm⁻¹),g=2e+15 cm/s²,L=1e-02 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-1.494e+09 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.78*2094.3951023931954*2000000000000000.0/(1+0.78*2094.3951023931954*0.01))-3*2094.3951023931954*300000.0`


#### icf-rt-rm-instability-gen-0010

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.74,λ=100 μm(k=628.3 cm⁻¹),g=5e+14 cm/s²,L=2e-02 cm,v_a=1e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-5.328e+07 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.74*628.3185307179588*500000000000000.0/(1+0.74*628.3185307179588*0.02))-3*628.3185307179588*100000.0`


#### icf-rt-rm-instability-gen-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.95,λ=80 μm(k=785.4 cm⁻¹),g=2e+15 cm/s²,L=5e-03 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-2.014e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.95*785.3981633974483*2000000000000000.0/(1+0.95*785.3981633974483*0.005))-3*785.3981633974483*300000.0`


#### icf-rt-rm-instability-gen-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.72,λ=50 μm(k=1257 cm⁻¹),g=1e+15 cm/s²,L=5e-03 cm,v_a=5e+04 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **1.757e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.72*1256.6370614359175*1000000000000000.0/(1+0.72*1256.6370614359175*0.005))-3*1256.6370614359175*50000.0`


#### icf-rt-rm-instability-gen-0013

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+07 cm/s,初始扰动 η₀=5e-04 cm,λ=50 μm(k=1257 cm⁻¹),A=0.86。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **5.404e+06 cm/s**（容差 ±2%）
   - 独立复算:`1256.6370614359173*0.86*10000000.0*0.0005`


#### icf-rt-rm-instability-gen-0014

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=1e-04 cm,λ=20 μm(k=3142 cm⁻¹),A=0.59。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **185400 cm/s**（容差 ±2%）
   - 独立复算:`3141.592653589793*0.59*1000000.0*0.0001`


#### icf-rt-rm-instability-gen-0015

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=5e-04 cm,λ=50 μm(k=1257 cm⁻¹),A=0.58。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **364400 cm/s**（容差 ±2%）
   - 独立复算:`1256.6370614359173*0.58*1000000.0*0.0005`


#### icf-rt-rm-instability-gen-0016

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=1e-04 cm,λ=50 μm(k=1257 cm⁻¹),A=0.7。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **87960 cm/s**（容差 ±2%）
   - 独立复算:`1256.6370614359173*0.7*1000000.0*0.0001`


#### icf-rt-rm-instability-gen-0017

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=1e-04 cm,λ=100 μm(k=628.3 cm⁻¹),A=0.79。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **49640 cm/s**（容差 ±2%）
   - 独立复算:`628.3185307179587*0.79*1000000.0*0.0001`


#### icf-rt-rm-instability-gen-0018

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=1e-04 cm,λ=100 μm(k=628.3 cm⁻¹),A=0.92。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **57810 cm/s**（容差 ±2%）
   - 独立复算:`628.3185307179587*0.92*1000000.0*0.0001`


#### icf-rt-rm-instability-gen-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=5e-04 cm,λ=20 μm(k=3142 cm⁻¹),A=0.72。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **1.131e+06 cm/s**（容差 ±2%）
   - 独立复算:`3141.592653589793*0.72*1000000.0*0.0005`


#### icf-rt-rm-instability-gen-0020

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=5e+06 cm/s,初始扰动 η₀=1e-04 cm,λ=20 μm(k=3142 cm⁻¹),A=0.57。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **895400 cm/s**（容差 ±2%）
   - 独立复算:`3141.592653589793*0.57*5000000.0*0.0001`


#### icf-rt-rm-instability-gen-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=5e+06 cm/s,初始扰动 η₀=5e-04 cm,λ=20 μm(k=3142 cm⁻¹),A=0.92。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **7.226e+06 cm/s**（容差 ±2%）
   - 独立复算:`3141.592653589793*0.92*5000000.0*0.0005`


#### icf-rt-rm-instability-gen-0022

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=5e+06 cm/s,初始扰动 η₀=5e-04 cm,λ=50 μm(k=1257 cm⁻¹),A=0.81。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **2.545e+06 cm/s**（容差 ±2%）
   - 独立复算:`1256.6370614359173*0.81*5000000.0*0.0005`


#### icf-rt-rm-instability-gen-0023

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+07 cm/s,初始扰动 η₀=1e-03 cm,λ=100 μm(k=628.3 cm⁻¹),A=0.82。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **5.152e+06 cm/s**（容差 ±2%）
   - 独立复算:`628.3185307179587*0.82*10000000.0*0.001`


#### icf-rt-rm-instability-gen-0024

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=5e-04 cm,λ=20 μm(k=3142 cm⁻¹),A=0.6。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **942500 cm/s**（容差 ±2%）
   - 独立复算:`3141.592653589793*0.6*1000000.0*0.0005`


#### icf-rt-rm-instability-genb-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.71,λ=50 μm(k=1257 cm⁻¹),g=1e+15 cm/s²,L=1e-02 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-8.611e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.71*1256.6370614359175*1000000000000000.0/(1+0.71*1256.6370614359175*0.01))-3*1256.6370614359175*300000.0`


#### icf-rt-rm-instability-genb-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.91,λ=30 μm(k=2094 cm⁻¹),g=1e+15 cm/s²,L=2e-02 cm,v_a=1e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-4.297e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.91*2094.3951023931954*1000000000000000.0/(1+0.91*2094.3951023931954*0.02))-3*2094.3951023931954*100000.0`


#### icf-rt-rm-instability-genb-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.88,λ=100 μm(k=628.3 cm⁻¹),g=2e+15 cm/s²,L=1e-02 cm,v_a=3e+05 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-1.951e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.88*628.3185307179588*2000000000000000.0/(1+0.88*628.3185307179588*0.01))-3*628.3185307179588*300000.0`


#### icf-rt-rm-instability-genb-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=5e+06 cm/s,初始扰动 η₀=1e-04 cm,λ=20 μm(k=3142 cm⁻¹),A=0.89。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **1.398e+06 cm/s**（容差 ±2%）
   - 独立复算:`3141.592653589793*0.89*5000000.0*0.0001`


#### icf-rt-rm-instability-genb-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=5e+06 cm/s,初始扰动 η₀=1e-03 cm,λ=50 μm(k=1257 cm⁻¹),A=0.58。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **3.644e+06 cm/s**（容差 ±2%）
   - 独立复算:`1256.6370614359173*0.58*5000000.0*0.001`


#### icf-rt-rm-instability-genb-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=1e-03 cm,λ=100 μm(k=628.3 cm⁻¹),A=0.8。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **502700 cm/s**（容差 ±2%）
   - 独立复算:`628.3185307179587*0.8*1000000.0*0.001`


#### icf-rt-rm-instability-genc-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 烧蚀稳定化 RT(Takabe 式 γ=0.9·√(Akg/(1+AkL))-3kv_a):A=0.82,λ=30 μm(k=2094 cm⁻¹),g=5e+14 cm/s²,L=1e-02 cm,v_a=5e+04 cm/s。求 γ(s⁻¹),并说明与经典 √(Akg) 的差异。

**答案:** **-1.185e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*sqrt(0.82*2094.3951023931954*500000000000000.0/(1+0.82*2094.3951023931954*0.01))-3*2094.3951023931954*50000.0`


#### icf-rt-rm-instability-genc-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> RM 线性冲击后增长:激波速度跃变 Δu=1e+06 cm/s,初始扰动 η₀=5e-04 cm,λ=50 μm(k=1257 cm⁻¹),A=0.88。按 δv=k·A·Δu·η₀ 求扰动增长初速(cm/s)。

**答案:** **552900 cm/s**（容差 ±2%）
   - 独立复算:`1256.6370614359173*0.88*1000000.0*0.0005`


#### icf-rt-rm-instability-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于 ICF 中烧蚀稳定化 RT 的物理机制,下列哪些正确(多选)?

**答案:** **A/B/C**
   ✅ A. 烧蚀流把扰动对流出增长最快的烧蚀面,形成对流稳定化
   ✅ B. 密度梯度标长 L 的展宽降低了有效 Atwood 数与增长率
   ✅ C. 火焰抛光(fire polishing)通过热传导抹平小尺度温度扰动
   　 D. 烧蚀使所有波长的 RT 完全稳定,无需表面质量要求


#### icf-rt-rm-instability-hard-0002

`concept` · `grad` · `exact_match` · 来源:paper

> RM 与 RT 在 ICF 内爆不同阶段的相对重要性,正确的说法是?

**答案:** **A**
   ✅ A. RM 在冲击通过界面(如首次冲击、反弹冲击)时注入扰动种子;RT 在持续加速/减速阶段放大扰动
   　 B. RM 只在减速阶段重要
   　 C. RT 只在加速阶段重要
   　 D. 两者在所有阶段同等重要


#### icf-rt-rm-instability-hard-0003

`concept` · `expert` · `exact_match` · 来源:paper

> 关于 RT 非线性阶段(气泡-尖钉结构)的特征,正确的有(多选):

**答案:** **A/B/C**
   ✅ A. 轻流体气泡上升速度趋于饱和(与 √(g/k) 同量级),重流体尖钉持续加速
   ✅ B. 非线性阶段扰动谱向长波转移(气泡合并)
   ✅ C. 混合层宽度可用 h≈α·A·g·t² 估计(α 为经验常数)
   　 D. 非线性阶段增长率仍由线性公式精确给出


#### icf-rt-rm-instability-hard-0004

`concept` · `expert` · `exact_match` · 来源:paper

> 关于 ICF 中'混合'(mix)对性能的抑制机制,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 烧蚀层材料混入燃料提高其辐射损失(尤其高 Z 混合),冷却热斑
   ✅ B. 混合降低燃料 ρR 的有效压缩,稀释反应率
   　 C. 混合只影响对称性,不影响产额
   ✅ D. 混合的主要来源是界面 RT/RM 不稳定性的非线性发展


#### icf-rt-rm-instability-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 内爆减速阶段，稠密燃料（ρ2 = 10 g/cm^3）与低密度热点（ρ1 = 1 g/cm^3）界面处于有效加速度 g = 1e15 cm/s^2 中。扰动波长 λ = 50 μm。按经典 Rayleigh–Taylor 线性增长率 γ = sqrt(A·k·g)，其中 Atwood 数 A = (ρ2−ρ1)/(ρ2+ρ1)、k = 2π/λ。求 γ，以 s^-1 为单位。

**答案:** **1.014e+09 s^-1**（容差 ±2%）
   - 独立复算:`((9/11) * (2*pi/0.005) * 1e15)**0.5`


#### icf-rt-rm-instability-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> NIF 型靶丸中 DT 冰层（ρ = 0.25 g/cm^3）与 CH 烧蚀层（ρ = 1.0 g/cm^3）相邻。求该界面的 Atwood 数 A = (ρ_h−ρ_l)/(ρ_h+ρ_l)（重流体减轻轻流体取正）。

**答案:** **0.6 1**（容差 ±2%）
   - 独立复算:`(1.0-0.25)/(1.0+0.25)`


#### icf-rt-rm-instability-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:paper

> 烧蚀稳定化的 Rayleigh–Taylor 增长率用 Takabe 公式 γ = α·sqrt(A·k·g/(1+A·k·L)) − β·k·v_a，取 α = 0.9、β = 3。参数：A = 0.82，k = 1256.6 cm^-1（λ = 50 μm），g = 1e15 cm/s^2，密度标长 L = 10 μm = 1e-3 cm，烧蚀速度 v_a = 1e5 cm/s。求 γ，以 s^-1 为单位。

**答案:** **2.64e+08 s^-1**（容差 ±5%）
   - 独立复算:`0.9*((0.82*1256.6*1e15)/(1+0.82*1256.6*1e-3))**0.5 - 3*1256.6*1e5`


#### icf-rt-rm-instability-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:paper

> Richtmyer–Meshkov 线性理论：激波（界面速度跳变 Δu = 1e7 cm/s）通过具有初始余弦扰动（振幅 η0 = 10 μm，k = 1256.6 cm^-1）的界面，界面 Atwood 数 A = 0.82。按冲击后线性增长速率 δv = k·A·Δu·η0 求扰动增长的初始速率，以 cm/s 为单位。

**答案:** **1.029e+07 cm/s**（容差 ±5%）
   - 独立复算:`1256.6 * 0.82 * 1e7 * 1e-3`


#### icf-rt-rm-instability-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:paper

> Rayleigh–Taylor 非线性阶段气泡振幅的经验估计 h ≈ α_b·A·g·t^2，取 α_b = 0.05。参数：A = 0.82，g = 1e15 cm/s^2，t = 5 ns。求 h，以 μm 为单位。

**答案:** **10.2 μm**（容差 ±10%）
   - 独立复算:`0.05*0.82*1e15*(5e-9)**2 * 1e4`


#### icf-rt-rm-instability-0006

`concept` · `grad` · `exact_match` · 来源:paper

> 关于 ICF 中 Rayleigh–Taylor 与 Richtmyer–Meshkov 不稳定性，下列说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. 经典 RT 中短波长扰动增长更快（γ ∝ sqrt(k)）
   ✅ B. 烧蚀（ablation）与有限密度标长可显著稳定短波长 RT 增长
   ✅ C. RM 不稳定性由激波通过界面时的斜压涡量沉积产生
   　 D. RT 不稳定性只发生在内爆加速阶段，减速阶段不会发生


#### icf-rt-rm-instability-0007

`derivation` · `grad` · `rubric_judge` · 来源:textbook

> 从两种无黏不可压缩流体的界面小扰动分析出发，推导经典 Rayleigh–Taylor 线性色散关系并给出 γ = sqrt(A·k·g)。要求：写出两侧速度势形式、界面运动学与动力学衔接条件、行列式为零得色散关系、定义 Atwood 数并给出重流体在轻流体上方时的增长率。

**答案:** **rubric 判分（权重和=1）:**
   - [0.2] 设界面两侧速度势 φ1、φ2 ∝ exp(∓kz) 并叠加 ∝ exp(i kx + γt) 的扰动
   - [0.2] 界面运动学条件：法向速度连续且等于界面位移的时间导数
   - [0.25] 界面动力学条件：压强连续（含静水压差 ρ·g·η）
   - [0.2] 联立得色散关系 γ² = k·g·(ρ2−ρ1)/(ρ2+ρ1)
   - [0.15] 定义 A = (ρ2−ρ1)/(ρ2+ρ1) 并给出 γ = sqrt(A·k·g)，指明不稳定条件（重流体受加速度朝向轻流体）


---

## icf/target-design（27 题）


#### icf-target-design-gen-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=2.5 mm、长 L=5.0 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **117.8 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*2.5*5.0+2*pi*2.5**2`


#### icf-target-design-gen-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=2.72 mm、长 L=9.43 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **207.6 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*2.72*9.43+2*pi*2.72**2`


#### icf-target-design-gen-0004

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=2.5 mm、长 L=10.0 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **196.3 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*2.5*10.0+2*pi*2.5**2`


#### icf-target-design-gen-0006

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=3.0 mm、长 L=9.43 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **234.3 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*3.0*9.43+2*pi*3.0**2`


#### icf-target-design-gen-0010

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=3.0 mm、长 L=5.0 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **150.8 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*3.0*5.0+2*pi*3.0**2`


#### icf-target-design-gen-0011

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=2.72 mm、长 L=10.0 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **217.4 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*2.72*10.0+2*pi*2.72**2`


#### icf-target-design-genb-0003

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 圆柱黑腔(半径 R=3.0 mm、长 L=10.0 mm)的总内表面积(侧壁+两端盖,mm²)。

**答案:** **245 mm^2**（容差 ±2%）
   - 独立复算:`2*pi*3.0*10.0+2*pi*3.0**2`


#### icf-target-design-hard-0001

`concept` · `expert` · `exact_match` · 来源:paper

> 关于 ICF 靶丸烧蚀层材料选择(CH、Be、HDC/金刚石),正确的有(多选):

**答案:** **A/B/C**
   ✅ A. HDC 密度高、烧蚀压大,可实现更高内爆速度,但制备难
   ✅ B. Be 对 X 光不透明度高可屏蔽预热,且力学性能好
   ✅ C. CH(塑料)最早使用、制备成熟,但密度低
   　 D. 材料选择与内爆性能无关


#### icf-target-design-hard-0002

`concept` · `grad` · `exact_match` · 来源:textbook

> 间接驱动黑腔上激光入射孔(LEH)的设计权衡是?

**答案:** **A**
   ✅ A. LEH 越大激光耦合越容易但 X 光泄漏损失越大;需在耦合效率与 X 光约束之间折中
   　 B. LEH 越大越好,无损失
   　 C. LEH 越小越好,无耦合问题
   　 D. LEH 与能量平衡无关


#### icf-target-design-hard-0003

`concept` · `expert` · `exact_match` · 来源:report

> 关于靶丸充气管/支撑膜(tent)对性能的影响,正确的有(多选):

**答案:** **A/B**
   ✅ A. 超薄支撑膜(tent,纳米级聚合物)支撑 DT 冰层,其厚度影响内爆对称性与性能
   ✅ B. 更薄的 tent 减少对壳层动力学的扰动,是靶丸工艺改进方向
   　 C. tent 对性能完全无影响
   　 D. tent 的主要作用是导热


#### icf-sim-gen-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.05 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.12,吸收能量转化为燃料动能的效率 η_ke=0.07。求燃料动能(J)。

**答案:** **14640 J**（容差 ±2%）
   - 独立复算:`2049999.9999999998*0.85*0.12*0.07`


#### icf-sim-gen-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=1.80 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.15,吸收能量转化为燃料动能的效率 η_ke=0.07。求燃料动能(J)。

**答案:** **16070 J**（容差 ±2%）
   - 独立复算:`1800000.0*0.85*0.15*0.07`


#### icf-sim-gen-0013

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=1.80 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.1,吸收能量转化为燃料动能的效率 η_ke=0.05。求燃料动能(J)。

**答案:** **7650 J**（容差 ±2%）
   - 独立复算:`1800000.0*0.85*0.1*0.05`


#### icf-sim-gen-0014

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.20 MJ,X 光转换 η_x=0.9,靶丸吸收 η_abs=0.15,吸收能量转化为燃料动能的效率 η_ke=0.05。求燃料动能(J)。

**答案:** **14850 J**（容差 ±2%）
   - 独立复算:`2200000.0*0.9*0.15*0.05`


#### icf-sim-gen-0015

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.20 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.1,吸收能量转化为燃料动能的效率 η_ke=0.05。求燃料动能(J)。

**答案:** **9350 J**（容差 ±2%）
   - 独立复算:`2200000.0*0.85*0.1*0.05`


#### icf-sim-genb-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=1.80 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.12,吸收能量转化为燃料动能的效率 η_ke=0.07。求燃料动能(J)。

**答案:** **12850 J**（容差 ±2%）
   - 独立复算:`1800000.0*0.85*0.12*0.07`


#### icf-sim-genb-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=1.80 MJ,X 光转换 η_x=0.9,靶丸吸收 η_abs=0.15,吸收能量转化为燃料动能的效率 η_ke=0.07。求燃料动能(J)。

**答案:** **17010 J**（容差 ±2%）
   - 独立复算:`1800000.0*0.9*0.15*0.07`


#### icf-sim-genb-0014

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=1.80 MJ,X 光转换 η_x=0.9,靶丸吸收 η_abs=0.1,吸收能量转化为燃料动能的效率 η_ke=0.05。求燃料动能(J)。

**答案:** **8100 J**（容差 ±2%）
   - 独立复算:`1800000.0*0.9*0.1*0.05`


#### icf-sim-genc-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.20 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.12,吸收能量转化为燃料动能的效率 η_ke=0.05。求燃料动能(J)。

**答案:** **11220 J**（容差 ±2%）
   - 独立复算:`2200000.0*0.85*0.12*0.05`


#### icf-sim-genc-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.05 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.12,吸收能量转化为燃料动能的效率 η_ke=0.05。求燃料动能(J)。

**答案:** **10460 J**（容差 ±2%）
   - 独立复算:`2049999.9999999998*0.85*0.12*0.05`


#### icf-sim-genc-0013

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.20 MJ,X 光转换 η_x=0.85,靶丸吸收 η_abs=0.15,吸收能量转化为燃料动能的效率 η_ke=0.07。求燃料动能(J)。

**答案:** **19640 J**（容差 ±2%）
   - 独立复算:`2200000.0*0.85*0.15*0.07`


#### icf-sim-genc-0014

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 间接驱动能量链:激光 E=2.20 MJ,X 光转换 η_x=0.9,靶丸吸收 η_abs=0.1,吸收能量转化为燃料动能的效率 η_ke=0.07。求燃料动能(J)。

**答案:** **13860 J**（容差 ±2%）
   - 独立复算:`2200000.0*0.9*0.1*0.07`


#### icf-target-design-0001

`concept` · `undergrad` · `exact_match` · 来源:textbook

> ICF 的间接驱动与直接驱动各是什么?主要优缺点是什么?

**答案:** **A**
   ✅ A. 直接驱动:激光直照靶丸;效率高但辐照不均匀性要求苛刻。间接驱动:激光先在黑腔内转化为 X 射线再驱动;均匀性好但能量效率低
   　 B. 直接驱动用电子束,间接驱动用激光
   　 C. 间接驱动靶丸不需要烧蚀层
   　 D. 直接驱动不能用于 DT 燃料


#### icf-target-design-0002

`concept` · `grad` · `exact_match` · 来源:textbook

> NIF 靶丸内 DT 冰层的均匀性为何直接影响点火性能?

**答案:** **A**
   ✅ A. 冰层厚度不均匀会成为 RT 不稳定性种子并破坏热斑球形度;均匀 ρR 是燃烧传播的前提
   　 B. 冰层不均匀只影响美观,不影响物理
   　 C. 冰层必须导电以屏蔽电磁干扰
   　 D. 冰层均匀性与中子产额无关


#### icf-target-design-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:report

> 间接驱动能量链估算:NIF 激光输入 2.05 MJ,黑腔 X 射线转换效率 90%,靶丸吸收其中 10%。求靶丸实际吸收的驱动能量(J)。

**答案:** **184500 J**（容差 ±2%）
   - 独立复算:`2.05e6*0.9*0.1`


#### icf-target-design-0004

`concept` · `expert` · `exact_match` · 来源:report

> 在 HDC/CH 烧蚀层中掺入少量高 Z 元素(如 W、Si)的设计目的包括哪些(多选)?

**答案:** **A/B**
   ✅ A. 提高对硬 X 射线(M 带)的不透明度,减少燃料预热
   ✅ B. 调节烧蚀面密度梯度,改善 RT 稳定性
   　 C. 增加靶丸的机械强度
   　 D. 提高激光能量利用效率


#### icf-target-design-0005

`numeric` · `undergrad` · `numeric_tolerance` · 来源:public-data

> DT 冰层质量估算:靶丸半径 R=1.1 mm,DT 冰层厚 ΔR=65 μm,冰密度 ρ=0.25 g/cm³。按薄壳近似 m=4πR²·ΔR·ρ 求冰层质量(mg)。

**答案:** **0.2471 mg**（容差 ±3%）
   - 独立复算:`4*pi*(0.11)**2*0.0065*0.25*1000`


---

## fusion-engineering（6 题）


#### fusion-engineering-0001

`concept` · `undergrad` · `exact_match` · 来源:report

> 为什么 DT 聚变电站必须配备氚增殖包层,而不能依赖外部供给?

**答案:** **A**
   ✅ A. 氚半衰期仅 12.3 年,自然界存量极微,需在包层中通过 Li-6(n,α)T 反应用聚变中子在线增殖,且 TBR>1 才能自持
   　 B. 因为氚是裂变产物,只能人工合成
   　 C. 因为氚的价格太贵,买不起
   　 D. 因为氚的化学性质活泼,必须现场生产


#### fusion-engineering-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 500 MW 聚变功率连续运行一年消耗的氚质量:DT 反应每次消耗 1 个氚原子,反应率=P/(17.6 MeV)。求年消耗氚质量(kg)。常数:1 eV=1.602176634e-19 J,氚原子质量 m_T=3.016×1.6605390666e-27 kg,一年=365×86400 s。

**答案:** **28.01 kg**（容差 ±3%）
   - 独立复算:`(500e6/(17.6e6*1.602176634e-19)) * (365*86400) * (3.016*1.6605390666e-27)`


#### fusion-engineering-0003

`concept` · `grad` · `exact_match` · 来源:paper

> 聚变堆第一壁/包层结构材料为什么普遍选用低活化铁素体/马氏体钢(RAF/M)而不是奥氏体不锈钢?

**答案:** **A**
   ✅ A. 14 MeV 中子辐照下 dpa 损伤更小且活化产物半衰期短、废热低,便于近距维护与核废料管理
   　 B. 铁素体钢熔点更高,可以承受更高表面温度
   　 C. 奥氏体不锈钢太贵
   　 D. 铁素体钢抗腐蚀性更好


#### fusion-engineering-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 氚增殖比(TBR)估算:设每个 DT 中子进入包层后,Be(n,2n) 倍增使可用中子数×1.3,其中被 Li-6 俘获产氚的概率为 0.75(每次俘获产 1 个氚)。求 TBR,并判断该包层能否支持氚自持(TBR>1)。

**答案:** **0.975 1**（容差 ±2%）
   - 独立复算:`1.3*0.75`


#### fusion-engineering-0005

`concept` · `expert` · `exact_match` · 来源:paper

> 液态金属 LiPb 与氟盐 FLiBe 作为氚增殖剂的优缺点对比,下列说法正确的有(多选):

**答案:** **A/B/C**
   ✅ A. LiPb 氚溶解度低易提取,但导电液态金属在强磁场下有 MHD 流阻/压降问题
   ✅ B. FLiBe 电绝缘、化学稳定性好,但含铍有毒且熔点较高需要加热维护
   ✅ C. LiPb 含 Pb 可兼作中子倍增剂(n,2n)
   　 D. FLiBe 的氚增殖比一定高于 LiPb,与设计无关


#### fusion-engineering-0006

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> ITER 级磁体储能密度估算:磁场能量密度 u=B²/(2μ0)。求 B=5.3 T 时的 u(J/m³)。常数:μ0=4π×1e-7 H/m。

**答案:** **1.1177e+07 J/m^3**（容差 ±2%）
   - 独立复算:`5.3**2/(2*4*pi*1e-7)`


---

## mcf（53 题）


#### code-limits-0001

`code` · `grad` · `unit_test` · 来源:textbook

> 实现两个函数:(1) troyon_beta_max(params, beta_N=2.8):params 为含 I(MA)、a(m)、B(T) 的 dict,返回 Troyon β 极限(%);(2) greenwald_density(params):返回 Greenwald 密度极限(1e20 m^-3)。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_limits.py`，超时 120s


#### mcf-sim-gen-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=12 MA,B=4 T,P=100 MW,n=8×1e19 m⁻³,M=2.5,R=1.65 m,a=1.0 m(ε=a/R),κ=1.5。求 τ_E(s)。

**答案:** **0.2235 s**（容差 ±5%）
   - 独立复算:`0.0562*12**0.93*4**0.15*100**-0.69*8**0.41*2.5**0.19*1.65**1.97*(1.0/1.65)**0.58*1.5**0.78`


#### mcf-sim-gen-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=3 MA,B=2.5 T,P=100 MW,n=10×1e19 m⁻³,M=2.5,R=1.65 m,a=1.0 m(ε=a/R),κ=1.7。求 τ_E(s)。

**答案:** **0.06931 s**（容差 ±5%）
   - 独立复算:`0.0562*3**0.93*2.5**0.15*100**-0.69*10**0.41*2.5**0.19*1.65**1.97*(1.0/1.65)**0.58*1.7**0.78`


#### mcf-sim-gen-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=12 MA,B=4 T,P=30 MW,n=5×1e19 m⁻³,M=2.5,R=6.2 m,a=1.0 m(ε=a/R),κ=1.9。求 τ_E(s)。

**答案:** **3.203 s**（容差 ±5%）
   - 独立复算:`0.0562*12**0.93*4**0.15*30**-0.69*5**0.41*2.5**0.19*6.2**1.97*(1.0/6.2)**0.58*1.9**0.78`


#### mcf-sim-gen-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=15 MA,B=4 T,P=73 MW,n=8×1e19 m⁻³,M=2.5,R=6.2 m,a=1.0 m(ε=a/R),κ=1.9。求 τ_E(s)。

**答案:** **2.587 s**（容差 ±5%）
   - 独立复算:`0.0562*15**0.93*4**0.15*73**-0.69*8**0.41*2.5**0.19*6.2**1.97*(1.0/6.2)**0.58*1.9**0.78`


#### mcf-sim-gen-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=12 MA,B=2.5 T,P=30 MW,n=5×1e19 m⁻³,M=2.5,R=1.65 m,a=1.0 m(ε=a/R),κ=1.9。求 τ_E(s)。

**答案:** **0.474 s**（容差 ±5%）
   - 独立复算:`0.0562*12**0.93*2.5**0.15*30**-0.69*5**0.41*2.5**0.19*1.65**1.97*(1.0/1.65)**0.58*1.9**0.78`


#### mcf-sim-gen-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=7.5 MA,B=4 T,P=10 MW,n=8×1e19 m⁻³,M=2.5,R=6.2 m,a=2.0 m(ε=a/R),κ=1.5。求 τ_E(s)。

**答案:** **6.654 s**（容差 ±5%）
   - 独立复算:`0.0562*7.5**0.93*4**0.15*10**-0.69*8**0.41*2.5**0.19*6.2**1.97*(2.0/6.2)**0.58*1.5**0.78`


#### mcf-sim-gen-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=2.0 m,R=3 m,B_t=5.3 T,I=3 MA。求 q。

**答案:** **11.78 1**（容差 ±3%）
   - 独立复算:`2.0*5.3/(3*(4*pi*1e-7*3e6/(2*pi*2.0)))`


#### mcf-sim-gen-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=2.0 m,R=1.7 m,B_t=5.3 T,I=3 MA。求 q。

**答案:** **20.78 1**（容差 ±3%）
   - 独立复算:`2.0*5.3/(1.7*(4*pi*1e-7*3e6/(2*pi*2.0)))`


#### mcf-sim-gen-0009

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=2.0 m,R=1.7 m,B_t=5.3 T,I=15 MA。求 q。

**答案:** **4.157 1**（容差 ±3%）
   - 独立复算:`2.0*5.3/(1.7*(4*pi*1e-7*15e6/(2*pi*2.0)))`


#### mcf-sim-gen-0010

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=1.0 m,R=6.2 m,B_t=5.3 T,I=3 MA。求 q。

**答案:** **1.425 1**（容差 ±3%）
   - 独立复算:`1.0*5.3/(6.2*(4*pi*1e-7*3e6/(2*pi*1.0)))`


#### mcf-sim-gen-0011

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=0.5 m,R=6.2 m,B_t=2 T,I=15 MA。求 q。

**答案:** **0.02688 1**（容差 ±3%）
   - 独立复算:`0.5*2/(6.2*(4*pi*1e-7*15e6/(2*pi*0.5)))`


#### mcf-sim-gen-0012

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=1.0 m,R=3 m,B_t=2 T,I=1 MA。求 q。

**答案:** **3.333 1**（容差 ±3%）
   - 独立复算:`1.0*2/(3*(4*pi*1e-7*1e6/(2*pi*1.0)))`


#### mcf-sim-gen-0013

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=10 keV,B_t=5.3 T,环径比 ε=0.2。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.006096 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*10e3*11604.525)/(1.602176634e-19*5.3)/sqrt(0.2)`


#### mcf-sim-gen-0014

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=1 keV,B_t=2 T,环径比 ε=0.32。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.004039 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*1e3*11604.525)/(1.602176634e-19*2)/sqrt(0.32)`


#### mcf-sim-gen-0015

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=5 keV,B_t=2 T,环径比 ε=0.32。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.009031 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*5e3*11604.525)/(1.602176634e-19*2)/sqrt(0.32)`


#### mcf-sim-gen-0016

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=1 keV,B_t=2 T,环径比 ε=0.2。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.005109 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*1e3*11604.525)/(1.602176634e-19*2)/sqrt(0.2)`


#### mcf-sim-gen-0017

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=1 keV,B_t=5.3 T,环径比 ε=0.32。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.001524 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*1e3*11604.525)/(1.602176634e-19*5.3)/sqrt(0.32)`


#### mcf-sim-gen-0018

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=10 keV,B_t=2 T,环径比 ε=0.2。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.01616 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*10e3*11604.525)/(1.602176634e-19*2)/sqrt(0.2)`


#### mcf-sim-gen-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=2×10²⁰ m⁻³,取 <σv>=6e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **1.692e+07 W/m^3**（容差 ±2%）
   - 独立复算:`(2e20/2)**2*6e-22*17.6e6*1.602176634e-19`


#### mcf-sim-gen-0020

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=0.5×10²⁰ m⁻³,取 <σv>=3e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **528700 W/m^3**（容差 ±2%）
   - 独立复算:`(0.5e20/2)**2*3e-22*17.6e6*1.602176634e-19`


#### mcf-sim-gen-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=0.5×10²⁰ m⁻³,取 <σv>=6e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **1.057e+06 W/m^3**（容差 ±2%）
   - 独立复算:`(0.5e20/2)**2*6e-22*17.6e6*1.602176634e-19`


#### mcf-sim-gen-0022

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=2×10²⁰ m⁻³,取 <σv>=1e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **2.82e+06 W/m^3**（容差 ±2%）
   - 独立复算:`(2e20/2)**2*1e-22*17.6e6*1.602176634e-19`


#### mcf-sim-gen-0023

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=2×10²⁰ m⁻³,取 <σv>=3e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **8.459e+06 W/m^3**（容差 ±2%）
   - 独立复算:`(2e20/2)**2*3e-22*17.6e6*1.602176634e-19`


#### mcf-sim-gen-0025

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=0.5×10²⁰ m⁻³,取 <σv>=1e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **176200 W/m^3**（容差 ±2%）
   - 独立复算:`(0.5e20/2)**2*1e-22*17.6e6*1.602176634e-19`


#### mcf-sim-genb-0001

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=3 MA,B=5.3 T,P=30 MW,n=10×1e19 m⁻³,M=2.5,R=3 m,a=1.0 m(ε=a/R),κ=1.9。求 τ_E(s)。

**答案:** **0.4458 s**（容差 ±5%）
   - 独立复算:`0.0562*3**0.93*5.3**0.15*30**-0.69*10**0.41*2.5**0.19*3**1.97*(1.0/3)**0.58*1.9**0.78`


#### mcf-sim-genb-0002

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=15 MA,B=5.3 T,P=100 MW,n=12×1e19 m⁻³,M=2.5,R=3 m,a=1.0 m(ε=a/R),κ=1.5。求 τ_E(s)。

**答案:** **0.7776 s**（容差 ±5%）
   - 独立复算:`0.0562*15**0.93*5.3**0.15*100**-0.69*12**0.41*2.5**0.19*3**1.97*(1.0/3)**0.58*1.5**0.78`


#### mcf-sim-genb-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=3 MA,B=5.3 T,P=30 MW,n=12×1e19 m⁻³,M=2.5,R=1.65 m,a=2.0 m(ε=a/R),κ=1.9。求 τ_E(s)。

**答案:** **0.3128 s**（容差 ±5%）
   - 独立复算:`0.0562*3**0.93*5.3**0.15*30**-0.69*12**0.41*2.5**0.19*1.65**1.97*(2.0/1.65)**0.58*1.9**0.78`


#### mcf-sim-genb-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=7.5 MA,B=5.3 T,P=10 MW,n=8×1e19 m⁻³,M=2.5,R=3 m,a=1.0 m(ε=a/R),κ=1.7。求 τ_E(s)。

**答案:** **1.866 s**（容差 ±5%）
   - 独立复算:`0.0562*7.5**0.93*5.3**0.15*10**-0.69*8**0.41*2.5**0.19*3**1.97*(1.0/3)**0.58*1.7**0.78`


#### mcf-sim-genb-0005

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=3 MA,B=2.5 T,P=30 MW,n=12×1e19 m⁻³,M=2.5,R=6.2 m,a=1.0 m(ε=a/R),κ=1.5。求 τ_E(s)。

**答案:** **0.979 s**（容差 ±5%）
   - 独立复算:`0.0562*3**0.93*2.5**0.15*30**-0.69*12**0.41*2.5**0.19*6.2**1.97*(1.0/6.2)**0.58*1.5**0.78`


#### mcf-sim-genb-0006

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I=15 MA,B=2.5 T,P=100 MW,n=8×1e19 m⁻³,M=2.5,R=6.2 m,a=0.6 m(ε=a/R),κ=1.7。求 τ_E(s)。

**答案:** **1.323 s**（容差 ±5%）
   - 独立复算:`0.0562*15**0.93*2.5**0.15*100**-0.69*8**0.41*2.5**0.19*6.2**1.97*(0.6/6.2)**0.58*1.7**0.78`


#### mcf-sim-genb-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=1.0 m,R=6.2 m,B_t=5.3 T,I=15 MA。求 q。

**答案:** **0.2849 1**（容差 ±3%）
   - 独立复算:`1.0*5.3/(6.2*(4*pi*1e-7*15e6/(2*pi*1.0)))`


#### mcf-sim-genb-0010

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=2.0 m,R=6.2 m,B_t=5.3 T,I=3 MA。求 q。

**答案:** **5.699 1**（容差 ±3%）
   - 独立复算:`2.0*5.3/(6.2*(4*pi*1e-7*3e6/(2*pi*2.0)))`


#### mcf-sim-genb-0012

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a=2.0 m,R=6.2 m,B_t=5.3 T,I=1 MA。求 q。

**答案:** **17.1 1**（容差 ±3%）
   - 独立复算:`2.0*5.3/(6.2*(4*pi*1e-7*1e6/(2*pi*2.0)))`


#### mcf-sim-genb-0013

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=5 keV,B_t=5.3 T,环径比 ε=0.32。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.003408 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*5e3*11604.525)/(1.602176634e-19*5.3)/sqrt(0.32)`


#### mcf-sim-genb-0014

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=5 keV,B_t=5.3 T,环径比 ε=0.2。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.004311 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*5e3*11604.525)/(1.602176634e-19*5.3)/sqrt(0.2)`


#### mcf-sim-genb-0018

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 通行/香蕉轨道估计:质子 T=5 keV,B_t=2 T,环径比 ε=0.2。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。

**答案:** **0.01142 m**（容差 ±5%）
   - 独立复算:`sqrt(2*1.67262192369e-27*1.380649e-23*5e3*11604.525)/(1.602176634e-19*2)/sqrt(0.2)`


#### mcf-sim-genb-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=1×10²⁰ m⁻³,取 <σv>=1e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **705000 W/m^3**（容差 ±2%）
   - 独立复算:`(1e20/2)**2*1e-22*17.6e6*1.602176634e-19`


#### mcf-sim-genb-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=1×10²⁰ m⁻³,取 <σv>=6e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **4.23e+06 W/m^3**（容差 ±2%）
   - 独立复算:`(1e20/2)**2*6e-22*17.6e6*1.602176634e-19`


#### mcf-sim-genb-0024

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 50-50 DT 芯部:n=1×10²⁰ m⁻³,取 <σv>=3e-22 m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。

**答案:** **2.115e+06 W/m^3**（容差 ±2%）
   - 独立复算:`(1e20/2)**2*3e-22*17.6e6*1.602176634e-19`


#### mcf-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:public-data

> ITER 的设计目标：聚变功率 P_fus = 500 MW，外部加热功率 P_heat = 50 MW。聚变增益定义为 Q = P_fus / P_heat（聚变功率与外部加热功率之比）。求 ITER 的设计 Q 值。

**答案:** **10 1**（容差 ±3%）
   - 独立复算:`500/50`


#### mcf-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:paper

> Troyon β 极限（无壁理想 MHD 约束）的经验公式为 β_max[%] = β_N · I_p/(a·B)，其中归一化 β 取 β_N = 2.8（无量纲），I_p 为等离子体电流（MA），a 为小半径（m），B 为环向磁场（T）。某 ITER 类托卡马克 I_p = 15 MA、a = 2.0 m、B = 5.3 T，求其 Troyon β 上限，以百分数（%）为单位。

**答案:** **3.9623 %**（容差 ±5%）
   - 独立复算:`2.8*15/(2.0*5.3)`


#### mcf-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:paper

> Greenwald 密度极限给出托卡马克线平均电子密度的经验上限 n_G = I_p/(π a²)，其中 I_p 以 MA 计、a 为小半径（m），所得 n_G 以 1e20 m^-3 为单位。取 ITER 类参数 I_p = 15 MA、a = 2.0 m，求 n_G（以 1e20 m^-3 为单位）。

**答案:** **1.1937 1e20 m^-3**（容差 ±5%）
   - 独立复算:`15/(pi*2.0**2)`


#### mcf-0004

`numeric` · `expert` · `numeric_tolerance` · 来源:paper

> IPB98(y,2) ELMy H 模能量约束定标为 τ_E = 0.0562 · I^0.93 · B^0.15 · P^(-0.69) · n^0.41 · M^0.19 · R^1.97 · ε^0.58 · κ^0.78，单位制：τ_E 为 s，I 为 MA，B 为 T，P 为加热功率（MW），n 为线平均密度（1e19 m^-3），M 为平均离子质量数（u），R 为大半径（m），ε = a/R 为反环径比（无量纲），κ 为截面拉长比（无量纲）。取 ITER 参数 I = 15 MA、B = 5.3 T、P = 100 MW、n = 10（即 1e20 m^-3）、M = 2.5（DT 平均）、R = 6.2 m、a = 2.0 m（故 ε = 2/6.2）、κ = 1.7，求 τ_E，以 s 为单位。

**答案:** **3.262 s**（容差 ±5%）
   - 独立复算:`0.0562*15**0.93*5.3**0.15*100**-0.69*10**0.41*2.5**0.19*6.2**1.97*(2/6.2)**0.58*1.7**0.78`


#### mcf-0005

`concept` · `undergrad` · `exact_match` · 来源:textbook

> 聚变增益 Q = P_fus / P_heat（聚变功率与外部加热功率之比）的不同里程碑对应不同物理状态。下列说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. Q = 1 称为得失相当（breakeven）：聚变功率恰好等于外部加热功率
   ✅ B. Q = 10 是 ITER 的设计目标：500 MW 聚变功率对应 50 MW 外部加热
   ✅ C. Q → ∞ 对应点火：α 粒子自加热足以平衡全部能量损失，可完全关闭外部加热
   　 D. Q = 5 即满足点火条件，此后不再需要任何外部加热


#### mcf-0006

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于托卡马克芯部锯齿振荡（sawtooth oscillation）的物理成因，下列说法正确的是（单选）：

**答案:** **A**
   ✅ A. 电流爬升使磁轴附近安全因子 q 降到 1 以下，q = 1 有理面内的 m = 1/n = 1 内部扭曲模不稳定并通过磁重联快速重排芯部（crash），芯部温度与密度被再分布，随后 q 剖面恢复、循环重复
   　 B. 由 H 模台基区边界局域模（ELM）周期性爆发直接造成芯部温度锯齿
   　 C. 由环向场线圈电源的周期性纹波引起磁轴位置周期性摆动
   　 D. 锯齿 crash 之后芯部温度反而升高，因为重联释放的磁能全部沉积在磁轴处


#### mcf-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> Alfvén 速度定义为 v_A = B/√(μ0 ρ)。某托卡马克芯部：B = 5.3 T；质量密度 ρ = n_i · M · m_p，其中离子数密度 n_i = 1e20 m^-3，平均离子质量数 M = 2.5（DT 混合），质子质量 m_p = 1.6726e-27 kg；真空磁导率 μ0 = 4π×10^-7 H/m。求 v_A，以 m/s 为单位。

**答案:** **7.311e+06 m/s**（容差 ±5%）
   - 独立复算:`5.3/sqrt(4*pi*1e-7*1e20*2.5*1.6726e-27)`


#### mcf-0008

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 等离子体 β 定义为热压与磁压之比 β = p/(B²/2μ0)。某托卡马克芯部电子与离子温度均为 T = 10 keV（即 kT = 1e4 eV），电子与离子数密度各为 1e20 m^-3，故总压强 p = 2·n·kT（电子加离子贡献）；B = 5.3 T；1 eV = 1.6022e-19 J；μ0 = 4π×10^-7 H/m。求 β（无量纲）。

**答案:** **0.02867 1**（容差 ±5%）
   - 独立复算:`2*1e20*(1.6022e-19*1e4)/(5.3**2/(2*4*pi*1e-7))`


#### mcf-0009

`concept` · `grad` · `exact_match` · 来源:textbook

> 托卡马克为什么必须同时具有环向磁场与极向磁场？下列说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. 纯环向场中 ∇B 漂移与曲率漂移引起垂直方向电荷分离，产生的 E×B 漂移把等离子体整体向外推出，单靠环向场无法形成 MHD 平衡
   ✅ B. 环向场与极向场合成的螺旋磁力线提供旋转变换（rotational transform），使带电粒子沿磁面运动平均掉单向漂移
   ✅ C. 两个场共同决定安全因子 q 剖面，q 的大小与剪切对抑制理想及电阻 MHD 不稳定性（如扭曲模、撕裂模）至关重要
   　 D. 极向场由环向场线圈（TF coils）直接产生，作用是压缩环向磁通以节省中心螺线管伏秒


#### mcf-0010

`numeric` · `expert` · `numeric_tolerance` · 来源:public-data

> DT 聚变反应 D + T → α + n 每次释放 17.6 MeV，且每次反应消耗 1 个氚核。某聚变堆以聚变功率 P_fus = 500 MW 连续燃烧 t = 400 s。求该发次消耗的氚质量，以 kg 为单位。1 eV = 1.602176634e-19 J；氚原子质量取 3.016 u，1 u = 1.6605390666e-27 kg。

**答案:** **0.0003553 kg**（容差 ±3%）
   - 独立复算:`500e6/(17.6e6*1.602176634e-19)*400*3.016*1.6605390666e-27`


#### mcf-0011

`concept` · `undergrad` · `exact_match` · 来源:textbook

> 与 DD 燃料相比，DT 燃料被认为是第一代聚变堆的首选。下列关于 DT 相对 DD 优势的说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. DT 反应截面峰值出现在约 100 keV 以下的温度区间，远低于 DD 达到可比反应率所需的有效温度
   ✅ B. DT 每次反应释放 17.6 MeV，Q 值显著高于 DD 各分支（每分支约 3-4 MeV）
   ✅ C. DT 的点火条件（Lawson 判据）对应约 10-20 keV，明显低于 DD 点火所需温度
   　 D. DT 反应不产生中子，对堆材料的活化与中子损伤远小于 DD


#### mcf-0012

`derivation` · `expert` · `rubric_judge` · 来源:paper

> 从无壁理想 MHD 稳定性出发，定性推导托卡马克 Troyon β 极限的形式 β_max ∝ I_p/(a·B)：即最大可达 β（热压/磁压）随等离子体电流 I_p 线性增长、随小半径 a 与环向场 B 反比下降。要求说明涉及的两种不稳定性约束及它们如何联立给出该标度。

**答案:** **rubric 判分（权重和=1）:**
   - [0.2] 写出 β = p/(B²/2μ0) 的定义，并由径向力平衡 ∇p = j×B 说明压强梯度必须由等离子体电流提供的洛伦兹力支撑，故可维持的压强随电流增长
   - [0.25] 给出扭曲模（kink）稳定约束：边缘安全因子 q_a 不能过低（Kruskal–Shafranov 条件推广为 q_a ≳ 2），由 q_a ∝ a²B/(R·I_p) 得电流上限 I_p ∝ a²B/(R·q_a)
   - [0.25] 给出气球模（ballooning）稳定约束：归一化压强梯度 α = -q²R(2μ0/B²)dp/dr 有界，故 β 上限 ∝ (a/R)·q^-2 量级，即 q 越小（电流越大）允许的 β 越高
   - [0.2] 联立两约束并在 q_a 取最小允许值（约 2）处寻优，消去 q 与 R，得 β_max ∝ I_p/(a·B) 的标度形式
   - [0.1] 引入由数值/实验确定的归一化系数 β_N（上限约 2.8-3.5），写出工程形式 β_max[%] = β_N·I_p[MA]/(a[m]·B[T])


#### mcf-0013

`derivation` · `expert` · `rubric_judge` · 来源:paper

> 从物理图像与量纲分析出发，论证托卡马克密度上限的 Greenwald 形式 n_G ∝ I_p/a²：即线平均密度极限跟随平均电流密度而非总电流。要求给出边缘辐射失稳/电流通道收缩的物理图像，并写出经验定标式。

**答案:** **rubric 判分（权重和=1）:**
   - [0.2] 说明实验事实：密度升高超过某上限时触发 MARFE/辐射崩塌与破裂，且上限与等离子体电流强相关，这是经验定标的观测基础
   - [0.2] 给出物理图像：密度升高使边缘辐射功率增大，当辐射接近输入功率时电流通道收缩、电流剖面峰化，有效电流密度升高
   - [0.25] 论证电流通道收缩使边缘 q 降低、低 m 撕裂模/锁模被触发直至破裂，稳定运行要求密度与电流密度之比有界
   - [0.25] 量纲论证：装置中唯一可构造密度量纲的宏观组合正比于平均电流密度 j = I_p/(πa²)，故 n_G ∝ I_p/a²，与电流密度而非总电流挂钩
   - [0.1] 写出经验定标 n_G[1e20 m^-3] = I_p[MA]/(π·a[m]²)，并说明其工程意义：运行点须保持 n/n_G < 1，ITER 等装置按此预留密度裕度


---

## plasma-basic（126 题）


#### code-nrl-calc-0001

`code` · `undergrad` · `unit_test` · 来源:textbook

> 实现 nrl_bundle(n, T_eV, B, species='e'):给定密度 n(m^-3)、温度 T_eV(eV)、磁场 B(T),返回元组 (ω_pe, λ_D, r_L):电子等离子体频率(rad/s)、德拜长度(m)、热拉莫尔半径(m,species='e' 电子 / 'p' 质子)。只准用标准库。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_nrl.py`，超时 120s


#### plasma-basic-gen-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=2.77e+20 cm⁻³,T=100 eV。

**答案:** **6.372 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(2.77e+20)+1.5*log(100)`


#### plasma-basic-gen-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+26 m⁻³,T=1 eV。

**答案:** **7.434e-10 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*1*11604.525/(1e+26*1.602176634e-19**2))`


#### plasma-basic-gen-0003

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=1 T,ρ=3.4e-07 kg/m³。

**答案:** **1.53e+06 m/s**（容差 ±2%）
   - 独立复算:`1/sqrt(4*pi*1e-7*3.4e-07)`


#### plasma-basic-gen-0004

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=9.22e+18 m⁻³(rad/s)。

**答案:** **1.713e+11 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(9.22e+18*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-gen-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=5.21e+20 cm⁻³,T=100 eV。

**答案:** **6.057 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(5.21e+20)+1.5*log(100)`


#### plasma-basic-gen-0006

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+17 m⁻³,T=100 eV。

**答案:** **0.0002351 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*100*11604.525/(1e+17*1.602176634e-19**2))`


#### plasma-basic-gen-0007

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+27 m⁻³,T=100 eV。

**答案:** **2.351e-09 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*100*11604.525/(1e+27*1.602176634e-19**2))`


#### plasma-basic-gen-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=1.58e+18 cm⁻³,T=100 eV。

**答案:** **8.956 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(1.58e+18)+1.5*log(100)`


#### plasma-basic-gen-0009

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=3.4e+22 m⁻³(rad/s)。

**答案:** **1.04e+13 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(3.4e+22*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-gen-0010

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=1.18e+24 m⁻³(rad/s)。

**答案:** **6.128e+13 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(1.18e+24*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-gen-0011

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=5.3 T,ρ=4.2e-07 kg/m³。

**答案:** **7.295e+06 m/s**（容差 ±2%）
   - 独立复算:`5.3/sqrt(4*pi*1e-7*4.2e-07)`


#### plasma-basic-gen-0012

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=6.93e+24 m⁻³(rad/s)。

**答案:** **1.485e+14 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(6.93e+24*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-gen-0014

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=1 T,ρ=4.2e-07 kg/m³。

**答案:** **1.376e+06 m/s**（容差 ±2%）
   - 独立复算:`1/sqrt(4*pi*1e-7*4.2e-07)`


#### plasma-basic-gen-0015

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=1.12e+24 cm⁻³,T=100 eV。

**答案:** **2.22 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(1.12e+24)+1.5*log(100)`


#### plasma-basic-gen-0016

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=1.13e+22 m⁻³(rad/s)。

**答案:** **5.997e+12 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(1.13e+22*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-gen-0017

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=9.17e+18 cm⁻³,T=10 eV。

**答案:** **4.623 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(9.17e+18)+1.5*log(10)`


#### plasma-basic-gen-0018

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=1 T,ρ=8.7e-07 kg/m³。

**答案:** **956400 m/s**（容差 ±2%）
   - 独立复算:`1/sqrt(4*pi*1e-7*8.7e-07)`


#### plasma-basic-gen-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=2.75e+15 cm⁻³,T=1000 eV。

**答案:** **15.59 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(2750000000000000.0)+1.5*log(1000)`


#### plasma-basic-gen-0020

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=2.18e+20 m⁻³(rad/s)。

**答案:** **8.33e+11 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(2.18e+20*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-gen-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=2.64e+17 cm⁻³,T=1000 eV。

**答案:** **13.3 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(2.64e+17)+1.5*log(1000)`


#### plasma-basic-gen-0022

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+26 m⁻³,T=100 eV。

**答案:** **7.434e-09 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*100*11604.525/(1e+26*1.602176634e-19**2))`


#### plasma-basic-gen-0023

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=0.1 T,ρ=4.1e-07 kg/m³。

**答案:** **139300 m/s**（容差 ±2%）
   - 独立复算:`0.1/sqrt(4*pi*1e-7*4.1e-07)`


#### plasma-basic-gen-0024

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=2.41e+22 cm⁻³,T=1000 eV。

**答案:** **7.593 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(2.41e+22)+1.5*log(1000)`


#### plasma-basic-gen-0025

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=0.1 T,ρ=7.3e-08 kg/m³。

**答案:** **330200 m/s**（容差 ±2%）
   - 独立复算:`0.1/sqrt(4*pi*1e-7*7.3e-08)`


#### plasma-basic-genb-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=1.21e+27 m⁻³(rad/s)。

**答案:** **1.962e+15 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(1.21e+27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-genb-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=1.38e+19 cm⁻³,T=100 eV。

**答案:** **7.872 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(1.38e+19)+1.5*log(100)`


#### plasma-basic-genb-0003

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=1.5e+27 m⁻³(rad/s)。

**答案:** **2.185e+15 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(1.5e+27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-genb-0004

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=5.3 T,ρ=7.8e-07 kg/m³。

**答案:** **5.353e+06 m/s**（容差 ±2%）
   - 独立复算:`5.3/sqrt(4*pi*1e-7*7.8e-07)`


#### plasma-basic-genb-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=4.81e+24 cm⁻³,T=10 eV。

**答案:** **-1.962 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(4.81e+24)+1.5*log(10)`


#### plasma-basic-genb-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=1.34e+16 cm⁻³,T=10 eV。

**答案:** **7.887 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(1.34e+16)+1.5*log(10)`


#### plasma-basic-genb-0007

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=5.3 T,ρ=3.7e-07 kg/m³。

**答案:** **7.773e+06 m/s**（容差 ±2%）
   - 独立复算:`5.3/sqrt(4*pi*1e-7*3.7e-07)`


#### plasma-basic-genb-0008

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=1 T,ρ=2.4e-07 kg/m³。

**答案:** **1.821e+06 m/s**（容差 ±2%）
   - 独立复算:`1/sqrt(4*pi*1e-7*2.4e-07)`


#### plasma-basic-genb-0009

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=1 T,ρ=2.1e-07 kg/m³。

**答案:** **1.947e+06 m/s**（容差 ±2%）
   - 独立复算:`1/sqrt(4*pi*1e-7*2.1e-07)`


#### plasma-basic-genb-0010

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=1 T,ρ=3e-07 kg/m³。

**答案:** **1.629e+06 m/s**（容差 ±2%）
   - 独立复算:`1/sqrt(4*pi*1e-7*3e-07)`


#### plasma-basic-genb-0012

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=2.19e+18 cm⁻³,T=10000 eV。

**答案:** **15.7 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(2.19e+18)+1.5*log(10000)`


#### plasma-basic-genb-0013

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=1.7e+22 m⁻³(rad/s)。

**答案:** **7.356e+12 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(1.7e+22*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-genb-0014

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=5.3 T,ρ=6.7e-07 kg/m³。

**答案:** **5.776e+06 m/s**（容差 ±2%）
   - 独立复算:`5.3/sqrt(4*pi*1e-7*6.7e-07)`


#### plasma-basic-genb-0015

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+27 m⁻³,T=1 eV。

**答案:** **2.351e-10 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*1*11604.525/(1e+27*1.602176634e-19**2))`


#### plasma-basic-genb-0016

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=5.64e+22 cm⁻³,T=1000 eV。

**答案:** **7.168 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(5.64e+22)+1.5*log(1000)`


#### plasma-basic-genb-0017

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=1.27e+14 cm⁻³,T=100 eV。

**答案:** **13.67 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(127000000000000.0)+1.5*log(100)`


#### plasma-basic-genb-0019

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+19 m⁻³,T=100 eV。

**答案:** **2.351e-05 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*100*11604.525/(1e+19*1.602176634e-19**2))`


#### plasma-basic-genb-0020

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求阿尔文速度 v_A=B/√(μ₀ρ):B=0.1 T,ρ=5e-07 kg/m³。

**答案:** **126200 m/s**（容差 ±2%）
   - 独立复算:`0.1/sqrt(4*pi*1e-7*5e-07)`


#### plasma-basic-genb-0021

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=3.55e+23 cm⁻³,T=100 eV。

**答案:** **2.795 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(3.55e+23)+1.5*log(100)`


#### plasma-basic-genb-0022

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+18 m⁻³,T=1 eV。

**答案:** **7.434e-06 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*1*11604.525/(1e+18*1.602176634e-19**2))`


#### plasma-basic-genb-0023

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e=7.52e+19 cm⁻³,T=10000 eV。

**答案:** **13.93 1**（容差 ±3%）
   - 独立复算:`23-0.5*log(7.52e+19)+1.5*log(10000)`


#### plasma-basic-genb-0024

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n=1e+26 m⁻³,T=1000 eV。

**答案:** **2.351e-08 m**（容差 ±2%）
   - 独立复算:`sqrt(8.8541878128e-12*1.380649e-23*1000*11604.525/(1e+26*1.602176634e-19**2))`


#### plasma-basic-genb-0025

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n=7.21e+24 m⁻³(rad/s)。

**答案:** **1.515e+14 rad/s**（容差 ±2%）
   - 独立复算:`sqrt(7.21e+24*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))`


#### plasma-basic-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:report

> 氢等离子体温度 T_e = 1 keV、电子密度 n_e = 1e20 cm^-3。用定义 λ_D = sqrt(ε0 · k_B·T / (n_e · e^2))（k_B·T 取 1 keV 对应的焦耳数）计算电子德拜长度 λ_D，答案以 cm 为单位。常数：ε0 = 8.8541878e-12 F/m，e = 1.602176634e-19 C，1 eV = 1.602176634e-19 J。

**答案:** **2.3509e-06 cm**（容差 ±2%）
   - 独立复算:`(8.8541878e-12 * 1.602176634e-16 / (1e26 * 1.602176634e-19**2))**0.5 * 100`


#### plasma-basic-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:report

> 电子密度 n_e = 1e20 cm^-3（= 1e26 m^-3）的等离子体，其电子等离子体频率 f_pe = ω_pe/(2π)，ω_pe = sqrt(n_e·e^2/(ε0·m_e))。求 f_pe，以 GHz 为单位。常数：e = 1.602176634e-19 C，m_e = 9.1093837e-31 kg，ε0 = 8.8541878e-12 F/m。

**答案:** **89780 GHz**（容差 ±2%）
   - 独立复算:`sqrt(1e26 * 1.602176634e-19**2 / (8.8541878e-12 * 9.1093837e-31)) / (2*pi) / 1e9`


#### plasma-basic-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:report

> ITER 中心螺线管区典型磁场 B = 5.3 T。求该磁场下的电子回旋频率 f_ce = eB/(2π m_e)，以 GHz 为单位。常数：e = 1.602176634e-19 C，m_e = 9.1093837e-31 kg。

**答案:** **148.4 GHz**（容差 ±2%）
   - 独立复算:`1.602176634e-19 * 5.3 / (2*pi*9.1093837e-31) / 1e9`


#### plasma-basic-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:report

> 用 NRL Plasma Formulary 给出的库仑对数表达式 lnΛ = 24 − ln( sqrt(n_e[cm^-3]) / T_e[eV] )，计算 n_e = 1e20 cm^-3、T_e = 1 keV 氢等离子体的 lnΛ（自然对数）。

**答案:** **7.88 1**（容差 ±3%）
   - 独立复算:`24 - log(sqrt(1e20)/1e3)`


#### plasma-basic-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ITER 芯部氘等离子体密度 n = 1e20 m^-3，磁场 B = 5.3 T。取氘离子质量 m_D = 3.3435e-27 kg，求阿尔芬速度 v_A = B/sqrt(μ0·n·m_D)，以 m/s 为单位。μ0 = 4π×1e-7 H/m。

**答案:** **8.18e+06 m/s**（容差 ±2%）
   - 独立复算:`5.3 / (4*pi*1e-7 * 1e20 * 3.3435e-27)**0.5`


#### plasma-basic-0006

`numeric` · `undergrad` · `numeric_tolerance` · 来源:report

> 定义电子热速度 v_th = sqrt(k_B·T / m_e)（每自由度均方根速率）。T_e = 1 keV 时 v_th 是多少 m/s？常数：1 eV = 1.602176634e-19 J，m_e = 9.1093837e-31 kg。

**答案:** **1.326e+07 m/s**（容差 ±2%）
   - 独立复算:`(1.602176634e-16 / 9.1093837e-31)**0.5`


#### plasma-basic-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:report

> 氘等离子体（m_D = 3.3435e-27 kg）中 T_e = 1 keV、Z = 1，按 c_s = sqrt(Z·T_e / m_i)（T_e 用焦耳）求离子声速 c_s，以 m/s 为单位。1 eV = 1.602176634e-19 J。

**答案:** **218900 m/s**（容差 ±2%）
   - 独立复算:`(1.602176634e-16 / 3.3435e-27)**0.5`


#### plasma-basic-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:report

> 托卡马克边缘 B = 5 T，10 keV 电子的垂直热运动取 v_⊥ = sqrt(k_B·T/m_e)。求电子拉莫尔半径 r_L = m_e·v_⊥/(e·B)，以 mm 为单位。常数：e = 1.602176634e-19 C，m_e = 9.1093837e-31 kg，1 eV = 1.602176634e-19 J。

**答案:** **0.0477 mm**（容差 ±3%）
   - 独立复算:`9.1093837e-31 * (1.602176634e-15/9.1093837e-31)**0.5 / (1.602176634e-19*5) * 1000`


#### plasma-basic-0009

`concept` · `undergrad` · `exact_match` · 来源:textbook

> 关于德拜屏蔽与等离子体准中性，下列说法正确的有（多选）：

**答案:** **A/C**
   ✅ A. 在远大于德拜长度的空间尺度上，等离子体近似保持电中性（准中性）
   　 B. 德拜长度与电子密度的平方根成正比
   ✅ C. 德拜球内粒子数 N_D = n·λ_D^3 远大于 1 是等离子体表现出集体行为的条件
   　 D. 德拜屏蔽必须依赖外加磁场才能发生


#### plasma-basic-0010

`derivation` · `grad` · `rubric_judge` · 来源:textbook

> 从第一性原理推导冷等离子体中电子等离子体振荡频率 ω_pe。模型：均匀离子背景（密度 n_e）中电子薄片整体位移 x。要求给出恢复电场、运动方程、谐振条件与最终表达式。

**答案:** **rubric 判分（权重和=1）:**
   - [0.3] 由高斯定理/泊松方程得到位移产生的电荷面密度 σ = n_e·e·x 及恢复电场 E = n_e·e·x/ε0
   - [0.25] 写出单电子运动方程 m_e·ẍ = −e·E = −(n_e·e^2/ε0)·x
   - [0.25] 识别简谐振子形式 ẍ = −ω_pe²·x 并读出 ω_pe² = n_e·e²/(ε0·m_e)
   - [0.2] 给出最终式 ω_pe = sqrt(n_e·e²/(ε0·m_e)) 并指出其与振幅无关（线性）


#### plasma-basic-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> ITER 芯部参数：n_e = 1e20 m^-3，T_e = T_i = 10 keV，B = 5.3 T。等离子体比压定义为 β = p/(B²/2μ0)，其中压强 p = n_e·(T_e+T_i)（温度以焦耳计，含电子+离子双组分）。求 β，以百分数（%）为单位。常数：μ0 = 4π×1e-7 H/m，1 eV = 1.602176634e-19 J。

**答案:** **2.87 %**（容差 ±3%）
   - 独立复算:`100 * 1e20 * 2 * 1.602176634e-15 / (5.3**2 / (2*4*pi*1e-7))`


#### plasma-basic-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:report

> 两步计算 Spitzer 电阻率。第一步：用 lnΛ = 24 − ln(sqrt(n_e[cm^-3])/T_e[eV]) 计算 n_e = 1e20 cm^-3、T_e = 10 keV 的库仑对数。第二步：用 NRL 公式 η = 1.03e-4 · Z · lnΛ · T_e[eV]^(-3/2) Ω·m（Z = 1）求 Spitzer 电阻率，以 Ω·m 为单位。

**答案:** **1.049e-09 Ω·m**（容差 ±5%）
   - 独立复算:`1.03e-4 * (24 - log(sqrt(1e20)/1e4)) * (1e4)**(-1.5)`


#### plasma-instabilities-gen-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.726,扰动波长 λ=120 μm,等效加速度 g=4.36e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **4.071e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.726*(2*pi/120e-6)*436000000000000.06)`


#### plasma-instabilities-gen-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.891,扰动波长 λ=80 μm,等效加速度 g=2.79e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **4.419e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.891*(2*pi/80e-6)*279000000000000.0)`


#### plasma-instabilities-gen-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.794,扰动波长 λ=30 μm,等效加速度 g=4.12e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **8.277e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.794*(2*pi/30e-6)*412000000000000.0)`


#### plasma-instabilities-gen-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.738,扰动波长 λ=120 μm,等效加速度 g=4.07e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **3.966e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.738*(2*pi/120e-6)*407000000000000.0)`


#### plasma-instabilities-gen-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=2.6e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-gen-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=3.8e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-gen-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=2.5e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-gen-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=6.9e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-gen-0009

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e=2.9 keV)作为共振速度量级(m/s)。

**答案:** **2.258e+07 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1.380649e-23*2.9e3*11604.525/9.1093837015e-31)`


#### plasma-instabilities-gen-0010

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e=0.6 keV)作为共振速度量级(m/s)。

**答案:** **1.027e+07 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1.380649e-23*0.6e3*11604.525/9.1093837015e-31)`


#### plasma-instabilities-gen-0011

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e=3.9 keV)作为共振速度量级(m/s)。

**答案:** **2.619e+07 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1.380649e-23*3.9e3*11604.525/9.1093837015e-31)`


#### plasma-instabilities-gen-0013

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e=3.3 keV,Z=4,m_i=9 u(u=1.6726e-27 kg)。

**答案:** **374800 m/s**（容差 ±2%）
   - 独立复算:`sqrt(4*1.380649e-23*3.3e3*11604.525/(9*1.67262192369e-27))`


#### plasma-instabilities-gen-0015

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e=0.3 keV,Z=4,m_i=9 u(u=1.6726e-27 kg)。

**答案:** **113000 m/s**（容差 ±2%）
   - 独立复算:`sqrt(4*1.380649e-23*0.3e3*11604.525/(9*1.67262192369e-27))`


#### plasma-instabilities-gen-0016

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e=0.5 keV,Z=1,m_i=1 u(u=1.6726e-27 kg)。

**答案:** **218800 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1*1.380649e-23*0.5e3*11604.525/(1*1.67262192369e-27))`


#### plasma-instabilities-gen-0017

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=4.6 T(rad/s)。

**答案:** **8.091e+11 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*4.6/9.1093837015e-31`


#### plasma-instabilities-gen-0018

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=5.6 T(rad/s)。

**答案:** **9.849e+11 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*5.6/9.1093837015e-31`


#### plasma-instabilities-gen-0019

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=1.6 T(rad/s)。

**答案:** **2.814e+11 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*1.6/9.1093837015e-31`


#### plasma-instabilities-gen-0020

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=9.8 T(rad/s)。

**答案:** **1.724e+12 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*9.8/9.1093837015e-31`


#### plasma-instabilities-gen-0021

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=1.6 keV,B=5 T,L_n=1.8 m;漂移频率 ω*≈k_y·v_De,k_y=128 m⁻¹。求 ω*(rad/s)。

**答案:** **22760 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*1.6e3*11604.525/1.602176634e-19/5)/1.8*128.0`


#### plasma-instabilities-gen-0022

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=2.1 keV,B=5 T,L_n=1.2 m;漂移频率 ω*≈k_y·v_De,k_y=149 m⁻¹。求 ω*(rad/s)。

**答案:** **52150 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*2.1e3*11604.525/1.602176634e-19/5)/1.2*149.0`


#### plasma-instabilities-gen-0023

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=1.6 keV,B=5 T,L_n=0.9 m;漂移频率 ω*≈k_y·v_De,k_y=200 m⁻¹。求 ω*(rad/s)。

**答案:** **71110 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*1.6e3*11604.525/1.602176634e-19/5)/0.9*200.0`


#### plasma-instabilities-gen-0024

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=3.0 keV,B=5 T,L_n=1.8 m;漂移频率 ω*≈k_y·v_De,k_y=156 m⁻¹。求 ω*(rad/s)。

**答案:** **52000 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*3.0e3*11604.525/1.602176634e-19/5)/1.8*156.0`


#### plasma-instabilities-gen-0025

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=1.3 keV,B=5 T,L_n=0.8 m;漂移频率 ω*≈k_y·v_De,k_y=93 m⁻¹。求 ω*(rad/s)。

**答案:** **30230 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*1.3e3*11604.525/1.602176634e-19/5)/0.8*93.0`


#### plasma-instabilities-genb-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.702,扰动波长 λ=30 μm,等效加速度 g=3.97e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **7.64e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.702*(2*pi/30e-6)*397000000000000.0)`


#### plasma-instabilities-genb-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.586,扰动波长 λ=30 μm,等效加速度 g=3.83e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **6.856e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.586*(2*pi/30e-6)*383000000000000.0)`


#### plasma-instabilities-genb-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.713,扰动波长 λ=20 μm,等效加速度 g=7.00e+13 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **3.96e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.713*(2*pi/20e-6)*69999999999999.99)`


#### plasma-instabilities-genb-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> ICF 减速阶段烧蚀面 Atwood 数 A=0.954,扰动波长 λ=50 μm,等效加速度 g=3.61e+14 m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。

**答案:** **6.579e+09 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(0.954*(2*pi/50e-6)*361000000000000.0)`


#### plasma-instabilities-genb-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=7.7e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-genb-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=5.7e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-genb-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=7.9e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-genb-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀=4.0e+06 m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e=1.6022e-19 C,ε₀=8.8542e-12,m_e=9.1094e-31 kg。

**答案:** **8.92e+14 s^-1**（容差 ±2%）
   - 独立复算:`sqrt(1e27*1.602176634e-19**2/(8.8541878128e-12*9.1093837015e-31))/2`


#### plasma-instabilities-genb-0009

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e=3.5 keV)作为共振速度量级(m/s)。

**答案:** **2.481e+07 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1.380649e-23*3.5e3*11604.525/9.1093837015e-31)`


#### plasma-instabilities-genb-0010

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e=2.6 keV)作为共振速度量级(m/s)。

**答案:** **2.138e+07 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1.380649e-23*2.6e3*11604.525/9.1093837015e-31)`


#### plasma-instabilities-genb-0012

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e=0.8 keV)作为共振速度量级(m/s)。

**答案:** **1.186e+07 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1.380649e-23*0.8e3*11604.525/9.1093837015e-31)`


#### plasma-instabilities-genb-0013

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e=2.4 keV,Z=4,m_i=9 u(u=1.6726e-27 kg)。

**答案:** **319600 m/s**（容差 ±2%）
   - 独立复算:`sqrt(4*1.380649e-23*2.4e3*11604.525/(9*1.67262192369e-27))`


#### plasma-instabilities-genb-0015

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e=4.8 keV,Z=1,m_i=2.5 u(u=1.6726e-27 kg)。

**答案:** **428900 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1*1.380649e-23*4.8e3*11604.525/(2.5*1.67262192369e-27))`


#### plasma-instabilities-genb-0016

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e=2.7 keV,Z=1,m_i=2.5 u(u=1.6726e-27 kg)。

**答案:** **321600 m/s**（容差 ±2%）
   - 独立复算:`sqrt(1*1.380649e-23*2.7e3*11604.525/(2.5*1.67262192369e-27))`


#### plasma-instabilities-genb-0017

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=1.5 T(rad/s)。

**答案:** **2.638e+11 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*1.5/9.1093837015e-31`


#### plasma-instabilities-genb-0018

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=7.3 T(rad/s)。

**答案:** **1.284e+12 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*7.3/9.1093837015e-31`


#### plasma-instabilities-genb-0019

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=16.2 T(rad/s)。

**答案:** **2.849e+12 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*16.2/9.1093837015e-31`


#### plasma-instabilities-genb-0020

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 求电子回旋频率 Ω_ce=eB/m_e:B=1.9 T(rad/s)。

**答案:** **3.342e+11 rad/s**（容差 ±2%）
   - 独立复算:`1.602176634e-19*1.9/9.1093837015e-31`


#### plasma-instabilities-genb-0021

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=2.9 keV,B=5 T,L_n=1.3 m;漂移频率 ω*≈k_y·v_De,k_y=144 m⁻¹。求 ω*(rad/s)。

**答案:** **64250 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*2.9e3*11604.525/1.602176634e-19/5)/1.3*144.0`


#### plasma-instabilities-genb-0022

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=2.0 keV,B=5 T,L_n=1.6 m;漂移频率 ω*≈k_y·v_De,k_y=178 m⁻¹。求 ω*(rad/s)。

**答案:** **44500 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*2.0e3*11604.525/1.602176634e-19/5)/1.6*178.0`


#### plasma-instabilities-genb-0023

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=2.5 keV,B=5 T,L_n=1.9 m;漂移频率 ω*≈k_y·v_De,k_y=167 m⁻¹。求 ω*(rad/s)。

**答案:** **43950 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*2.5e3*11604.525/1.602176634e-19/5)/1.9*167.0`


#### plasma-instabilities-genb-0024

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=0.8 keV,B=5 T,L_n=1.1 m;漂移频率 ω*≈k_y·v_De,k_y=114 m⁻¹。求 ω*(rad/s)。

**答案:** **16580 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*0.8e3*11604.525/1.602176634e-19/5)/1.1*114.0`


#### plasma-instabilities-genb-0025

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e=0.5 keV,B=5 T,L_n=0.8 m;漂移频率 ω*≈k_y·v_De,k_y=157 m⁻¹。求 ω*(rad/s)。

**答案:** **19630 rad/s**（容差 ±5%）
   - 独立复算:`(1.380649e-23*0.5e3*11604.525/1.602176634e-19/5)/0.8*157.0`


#### plasma-inst-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于离子温度梯度(ITG)驱动的微不稳定性,下列说法正确的是(多选):

**答案:** **A/C**
   ✅ A. 它由离子温度梯度与曲率漂移(或 bad curvature)耦合驱动,是托卡马克离子通道湍流的主要候选
   　 B. 其线性增长率与电子温度梯度成正比
   ✅ C. 其典型极向波长量级为离子拉莫尔半径ρ_i(即 k_⊥ρ_i~0.1-1)
   　 D. 它在平坦密度剖面下必然被完全抑制


#### plasma-inst-hard-0002

`concept` · `expert` · `exact_match` · 来源:textbook

> 捕获电子模(TEM)与 ITG 的一个关键区分特征是传播方向。正确的是?

**答案:** **A**
   ✅ A. TEM(电子方向/电子逆磁方向)与 ITG(离子方向)沿相反方向传播,是线性与非线性诊断的重要区分
   　 B. TEM 与 ITG 传播方向相同,无法区分
   　 C. TEM 沿离子逆磁方向传播
   　 D. TEM 不传播,是驻波


#### plasma-inst-hard-0003

`concept` · `grad` · `exact_match` · 来源:textbook

> 撕裂模(tearing mode)的物理图像中,下列哪些正确(多选)?

**答案:** **A/B/C**
   ✅ A. 它改变磁场拓扑,在有理面(q=m/n)处形成磁岛
   ✅ B. 它由电阻率(或电子惯性)使理想 MHD 的冻结约束失效而允许磁重联
   ✅ C. 经典撕裂模增长率随电阻率按 η^(3/5) 标度(Furth-Killeen-Rosenbluth)
   　 D. 它只发生在真空中,与等离子体无关


#### plasma-inst-hard-0004

`concept` · `expert` · `exact_match` · 来源:paper

> 新古典撕裂模(NTM)与经典撕裂模的本质区别是?

**答案:** **A**
   ✅ A. NTM 由磁岛导致的自举电流(bootstrap current)亏损驱动/放大,具有阈值特性(需要有限大小的种子岛)
   　 B. NTM 不需要种子扰动,是线性不稳
   　 C. NTM 与自举电流无关
   　 D. NTM 只在外部线圈驱动时出现


#### plasma-inst-hard-0005

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于理想 MHD 气球模(ballooning)不稳定性,下列正确的是(多选):

**答案:** **A/B/C**
   ✅ A. 它在坏曲率区(向外凸出)被压力梯度驱动,具有沿场强变化的结构
   ✅ B. 其阈值常用归一化压力梯度 α 与磁剪切 s 的 s-α 图刻画
   ✅ C. 它与高 n(环向模数大)相关联,属于短波 MHD
   　 D. 它只在无剪切磁场中发生


#### plasma-inst-hard-0006

`concept` · `grad` · `exact_match` · 来源:textbook

> 互换不稳定性(interchange)与 RT 不稳定性的关系,正确的是?

**答案:** **A**
   ✅ A. 在磁化等离子体中,压力梯度与坏曲率的组合等效于'重力'驱动的 RT;低 β 近似下可用有效重力 g_eff~c_s²/R_c 描述
   　 B. 互换不稳定性和重力完全无关
   　 C. 它只发生在磁零点
   　 D. 它总是比气球模增长更慢


#### plasma-inst-hard-0007

`concept` · `expert` · `exact_match` · 来源:paper

> 鱼骨模(fishbone)不稳定性的驱动机制是?

**答案:** **A**
   ✅ A. 高能(捕获)粒子与内扭曲模(m/n=1/1)的共振耦合,周期性地把快粒子能量倾泻出来
   　 B. 电子温度梯度直接驱动
   　 C. 外加 RMP 线圈驱动
   　 D. 等离子体旋转剪切驱动


#### plasma-inst-hard-0008

`concept` · `grad` · `exact_match` · 来源:textbook

> 消防水带(firehose)与镜像(mirror)不稳定性发生的物理条件是什么?

**答案:** **A**
   ✅ A. 压力各向异性:p_∥ 与 p_⊥ 之差超过磁场张力/压力阈值;firehose 在 p_∥>p_⊥ 过大时,mirror 在 p_⊥>p_∥ 过大时
   　 B. 两者都只在等温等离子体中发生
   　 C. 两者都需要碰撞耗散
   　 D. 两者只发生在 z 箍缩中


#### plasma-inst-hard-0009

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于回旋动理学(gyrokinetics)近似,下列哪些是其实际假设(多选):

**答案:** **A/B/C**
   ✅ A. 涨落频率远小于回旋频率(ω≪Ω_ci),从而可以对回旋运动平均
   ✅ B. 涨落垂直波长远小于平行波长(k_⊥≫k_∥,各向异性)
   ✅ C. 涨落幅值小(δf/f≪1),可用 δf 展开
   　 D. 完全忽略所有波与粒子的相互作用


#### plasma-inst-hard-0010

`concept` · `expert` · `exact_match` · 来源:paper

> 电子温度梯度(ETG)模与 ITG 相比,典型区别是?

**答案:** **A**
   ✅ A. ETG 在电子拉莫尔半径尺度(k_⊥ρ_e~1)驱动电子通道热输运,且与 ITG 共存于不同尺度
   　 B. ETG 与 ITG 尺度完全相同
   　 C. ETG 只存在于仿星器
   　 D. ETG 不能驱动湍流输运


#### plasma-inst-hard-0011

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于尾隆(bump-on-tail)不稳定性,正确的物理论述是(多选):

**答案:** **A/B/C**
   ✅ A. 它要求速度分布函数在共振速度处有正斜率(∂f/∂v>0)区域
   ✅ B. 它通过逆朗道阻尼把自由能从束流转移给静电波
   ✅ C. 它的饱和机制包括共振粒子的捕获与分布函数平台化(quasilinear plateau)
   　 D. 它属于流体不稳定性,与速度分布形状无关


#### plasma-inst-hard-0012

`concept` · `expert` · `exact_match` · 来源:paper

> Weibel 不稳定性(无磁场横向电磁模)的自由能来源是?

**答案:** **A**
   ✅ A. 速度空间的温度(动量)各向异性,产生横向电流扰动并自增强形成丝状磁场结构
   　 B. 密度梯度
   　 C. 外加磁场剪切
   　 D. 重力


#### plasma-inst-hard-0013

`concept` · `grad` · `exact_match` · 来源:textbook

> 关于声波(离子声波)朗道阻尼,正确的说法是?

**答案:** **A**
   ✅ A. 当 T_e≫T_i 时离子声波弱阻尼可以传播;T_e≈T_i 时强离子朗道阻尼使其迅速衰减
   　 B. 离子声波在所有温度比下都无阻尼
   　 C. 朗道阻尼需要碰撞
   　 D. T_i 越高,离子声波越容易传播


#### plasma-inst-hard-0014

`concept` · `grad` · `exact_match` · 来源:textbook

> 磁化等离子体中哨声(whistler)波的特征是?

**答案:** **A**
   ✅ A. 右旋偏振、频率低于电子回旋频率、色散关系 ω∝k²(长波段近似),群速度随频率增加
   　 B. 左旋偏振且只能在 ω>Ω_ce 传播
   　 C. 是静电波
   　 D. 频率与 k 无关


#### plasma-inst-hard-0015

`concept` · `expert` · `exact_match` · 来源:textbook

> 关于漂移波不稳定性的'普适'(universal)驱动机制,下列正确的是(多选):

**答案:** **A/B/C**
   ✅ A. 密度梯度本身即可在耗散(碰撞/ Landau 共振)存在时使漂移波不稳
   ✅ B. 漂移波在无耗散的理想极限下必然稳定
   ✅ C. 电子对电场的绝热响应是漂移波准电中性的基础
   　 D. 漂移波必须有磁场曲率才存在


#### plasma-inst-hard-0016

`concept` · `grad` · `exact_match` · 来源:paper

> 关于电阻性壁模(RWM)在先进托卡马克中的意义,正确的是?

**答案:** **A**
   ✅ A. 当理想 MHD 外扭曲模在有导电壁时本已稳定,但无壁理想不稳定时,RWM 以壁电阻时间尺度增长,需要主动反馈控制
   　 B. RWM 与壁材料电阻无关
   　 C. RWM 只影响低 β 运行
   　 D. RWM 是理想 MHD 模,与耗散无关


#### plasma-inst-hard-0017

`concept` · `grad` · `exact_match` · 来源:paper

> 关于边缘局域模(ELM),正确的有(多选):

**答案:** **A/B/C**
   ✅ A. 它是 H 模式台基区准周期性的 MHD 爆发,剥离台基顶部压力剖面的一部分
   ✅ B. I 型 ELM 与 peeling-ballooning 稳定性边界的跨越相关
   ✅ C. 它会带来第一壁/偏滤器瞬时热负荷,是 ITER 关心的问题
   　 D. ELM 可以靠增加台基压力梯度彻底消除而不损失约束


#### plasma-inst-hard-0018

`concept` · `expert` · `exact_match` · 来源:paper

> 关于动理学阿尔文波(KAW),正确的有(多选):

**答案:** **A/C**
   ✅ A. 当 k_⊥ρ_i~1 时,阿尔文波获得垂直电场分量并伴随朗道阻尼/电子共振,成为湍流-粒子能量交换通道
   　 B. KAW 是纯 MHD 波,与粒子无共振
   ✅ C. KAW 在太阳风/托卡马克小尺度湍流谱的耗散区被认为有重要作用
   　 D. KAW 的频率永远高于离子回旋频率


#### plasma-inst-hard-0019

`concept` · `grad` · `exact_match` · 来源:paper

> 关于误差场(error field)与锁模,正确的有(多选):

**答案:** **A/B/D**
   ✅ A. 线圈安装误差导致的非轴对称磁场可在有理面共振,穿透等离子体并锁住旋转
   ✅ B. 锁模常触发撕裂模并可能引发破裂
   　 C. 误差场只影响仿星器,不影响托卡马克
   ✅ D. 误差场校正线圈(EFC)可补偿误差场


#### plasma-inst-hard-0020

`concept` · `expert` · `exact_match` · 来源:paper

> 关于动理学气球模(KBM)与离子尺度湍流的关系,正确的说法是?

**答案:** **A**
   ✅ A. 当归一化压力梯度 α 接近理想气球模阈值时,KBM 可在离子尺度(k_⊥ρ_i~1)被激发,并与 ITG 谱系连接
   　 B. KBM 与理想气球模无关
   　 C. KBM 只在电子尺度发生
   　 D. KBM 不受 α 影响


---

## simulation（66 题）


#### code-sedov-0001

`code` · `undergrad` · `unit_test` · 来源:textbook

> 实现 sedov_radius(E, ts, rho, beta=1.15):给定爆炸能量 E(J)、初始密度 rho(kg/m³)、系数 beta,返回各时刻 t(s)的 Sedov-Taylor 激波半径列表 R=β(Et²/ρ)^(1/5)(m)。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_sedov.py`，超时 120s


#### icf-sim-gen-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+05 J,t=30 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.01785 m**（容差 ±2%）
   - 独立复算:`1.15*(100000.0*(30e-9)**2/0.1)**0.2`


#### icf-sim-gen-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+04 J,t=10 ns,环境密度 ρ=1.29 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.004351 m**（容差 ±2%）
   - 独立复算:`1.15*(10000.0*(10e-9)**2/1.29)**0.2`


#### icf-sim-gen-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+06 J,t=3 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.01126 m**（容差 ±2%）
   - 独立复算:`1.15*(1000000.0*(3e-9)**2/0.1)**0.2`


#### icf-sim-gen-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+04 J,t=1 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.002889 m**（容差 ±2%）
   - 独立复算:`1.15*(10000.0*(1e-9)**2/0.1)**0.2`


#### icf-sim-gen-0016

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=1 μm,|v|=3e+05 m/s,c_s=1e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **1.538e-13 s**（容差 ±2%）
   - 独立复算:`0.2*1e-6/(300000.0+1000000.0)`


#### icf-sim-gen-0017

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=1 μm,|v|=1e+06 m/s,c_s=3e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **5e-14 s**（容差 ±2%）
   - 独立复算:`0.2*1e-6/(1000000.0+3000000.0)`


#### icf-sim-gen-0018

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=5 μm,|v|=3e+05 m/s,c_s=3e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **3.03e-13 s**（容差 ±2%）
   - 独立复算:`0.2*5e-6/(300000.0+3000000.0)`


#### icf-sim-gen-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=5 μm,|v|=1e+05 m/s,c_s=5e+05 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **1.667e-12 s**（容差 ±2%）
   - 独立复算:`0.2*5e-6/(100000.0+500000.0)`


#### icf-sim-gen-0020

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=5 μm,|v|=3e+05 m/s,c_s=5e+05 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **1.25e-12 s**（容差 ±2%）
   - 独立复算:`0.2*5e-6/(300000.0+500000.0)`


#### icf-sim-genb-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+05 J,t=10 ns,环境密度 ρ=1.0 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.007256 m**（容差 ±2%）
   - 独立复算:`1.15*(100000.0*(10e-9)**2/1.0)**0.2`


#### icf-sim-genb-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+03 J,t=30 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.007105 m**（容差 ±2%）
   - 独立复算:`1.15*(1000.0*(30e-9)**2/0.1)**0.2`


#### icf-sim-genb-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+03 J,t=30 ns,环境密度 ρ=1.29 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.00426 m**（容差 ±2%）
   - 独立复算:`1.15*(1000.0*(30e-9)**2/1.29)**0.2`


#### icf-sim-genb-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+06 J,t=10 ns,环境密度 ρ=1.0 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.0115 m**（容差 ±2%）
   - 独立复算:`1.15*(1000000.0*(10e-9)**2/1.0)**0.2`


#### icf-sim-genb-0016

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=0.5 μm,|v|=3e+05 m/s,c_s=1e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **7.692e-14 s**（容差 ±2%）
   - 独立复算:`0.2*0.5e-6/(300000.0+1000000.0)`


#### icf-sim-genb-0017

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=1 μm,|v|=3e+05 m/s,c_s=3e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **6.061e-14 s**（容差 ±2%）
   - 独立复算:`0.2*1e-6/(300000.0+3000000.0)`


#### icf-sim-genb-0018

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=1 μm,|v|=1e+05 m/s,c_s=3e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **6.452e-14 s**（容差 ±2%）
   - 独立复算:`0.2*1e-6/(100000.0+3000000.0)`


#### icf-sim-genb-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=5 μm,|v|=1e+06 m/s,c_s=5e+05 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **6.667e-13 s**（容差 ±2%）
   - 独立复算:`0.2*5e-6/(1000000.0+500000.0)`


#### icf-sim-genb-0020

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=2 μm,|v|=1e+06 m/s,c_s=3e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **1e-13 s**（容差 ±2%）
   - 独立复算:`0.2*2e-6/(1000000.0+3000000.0)`


#### icf-sim-genc-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+04 J,t=30 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.01126 m**（容差 ±2%）
   - 独立复算:`1.15*(10000.0*(30e-9)**2/0.1)**0.2`


#### icf-sim-genc-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+05 J,t=10 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.0115 m**（容差 ±2%）
   - 独立复算:`1.15*(100000.0*(10e-9)**2/0.1)**0.2`


#### icf-sim-genc-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+03 J,t=30 ns,环境密度 ρ=1.0 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.004483 m**（容差 ±2%）
   - 独立复算:`1.15*(1000.0*(30e-9)**2/1.0)**0.2`


#### icf-sim-genc-0004

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+06 J,t=10 ns,环境密度 ρ=1.29 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.01093 m**（容差 ±2%）
   - 独立复算:`1.15*(1000000.0*(10e-9)**2/1.29)**0.2`


#### icf-sim-genc-0005

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 实验室点爆炸(Sedov):E=1e+03 J,t=1 ns,环境密度 ρ=0.1 kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。

**答案:** **0.001823 m**（容差 ±2%）
   - 独立复算:`1.15*(1000.0*(1e-9)**2/0.1)**0.2`


#### icf-sim-genc-0017

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=5 μm,|v|=1e+05 m/s,c_s=1e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **9.091e-13 s**（容差 ±2%）
   - 独立复算:`0.2*5e-6/(100000.0+1000000.0)`


#### icf-sim-genc-0019

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=0.5 μm,|v|=1e+06 m/s,c_s=1e+06 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **5e-14 s**（容差 ±2%）
   - 独立复算:`0.2*0.5e-6/(1000000.0+1000000.0)`


#### icf-sim-genc-0020

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟:Δx=2 μm,|v|=3e+05 m/s,c_s=5e+05 m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。

**答案:** **5e-13 s**（容差 ±2%）
   - 独立复算:`0.2*2e-6/(300000.0+500000.0)`


#### sim-hard-0001

`concept` · `expert` · `exact_match` · 来源:textbook

> 在 ICF 辐射流体模拟中,多群扩散(MGD)模型相对灰体(单群)模型的关键改进是?

**答案:** **A**
   ✅ A. 把光子按能量分组,各群有独立的不透明度与温度耦合,能描述谱硬化/谱软化与透明度窗口效应
   　 B. MGD 不需求解电子温度
   　 C. MGD 消除了对不透明度表的依赖
   　 D. MGD 只能用于理想气体


#### sim-hard-0002

`concept` · `grad` · `exact_match` · 来源:paper

> AMR(自适应网格加密)在 ICF 内爆模拟中的主要收益与代价是?

**答案:** **A**
   ✅ A. 收益:在烧蚀面/界面附近集中分辨率以捕捉薄层与大梯度,避免全域均匀细网格的成本;代价:加密判据/插值会引入额外数值误差与负载均衡问题
   　 B. AMR 总是比均匀网格精确
   　 C. AMR 只能用于静态问题
   　 D. AMR 消除了对 CFL 的限制


#### sim-hard-0003

`concept` · `expert` · `exact_match` · 来源:paper

> 在磁流体模拟中保持 ∇·B=0 的主要数值方法及其差异是?

**答案:** **A**
   ✅ A. 约束输运(CT):交错网格上面通量演化,散度误差保持到机器精度;8-波/GLM 散度清洗:通过对流-扩散把散度误差输运/耗散出域,实现简单但不严格
   　 B. HLLD 求解器自动保证 ∇·B=0,无需任何额外机制
   　 C. 只要网格足够细,散度误差自然消失
   　 D. 人工粘性可以保证 ∇·B=0


#### sim-hard-0004

`concept` · `grad` · `exact_match` · 来源:textbook

> 在离子-电子双温(2T)辐射流体模型中,何时必须使用三温(3T:电子/离子/辐射)模型?

**答案:** **A**
   ✅ A. 当辐射场显著偏离 Planck 谱或与物质温度解耦(如黑腔、烧蚀晕)时,辐射需独立温度/能群演化而非 T_r=T_e 假设
   　 B. 任何情况下 2T 与 3T 结果都相同
   　 C. 只有在真空中才需要 3T
   　 D. 3T 模型计算更简单,所以总是优先


#### sim-hard-0005

`concept` · `grad` · `exact_match` · 来源:textbook

> V&V(verification & validation)在 ICF/MCF 模拟中的含义,正确的是?

**答案:** **A**
   ✅ A. Verification:求解方程是否正确(算例对解析/基准解的比对);Validation:求解的方程是否正确(对实验数据的比对)
   　 B. Verification 是对实验的比对,Validation 是对解析解的比对
   　 C. 两者是同义词
   　 D. V&V 只适用于湍流模型


#### sim-hard-0006

`concept` · `expert` · `exact_match` · 来源:textbook

> PIC 模拟中的数值加热(numerical heating)主要来源于?

**答案:** **A**
   ✅ A. 有限大小粒子与网格插值引入的离散误差导致的非物理能量增长,与网格尺寸相对德拜长度/粒子数不足相关
   　 B. 物理碰撞
   　 C. 辐射冷却
   　 D. 边界反射


#### sim-hard-0007

`concept` · `grad` · `exact_match` · 来源:textbook

> 在蒙特卡洛中子学模拟(openmc)中,下列哪些是降低方差的常用手段(多选)?

**答案:** **A/B/C**
   ✅ A. 隐式捕获(implicit capture)替代真实吸收
   ✅ B. 俄罗斯轮盘赌与分裂(splitting)
   ✅ C. 权重窗口(weight window)与源偏倚
   　 D. 简单地把粒子数减半


#### sim-hard-0008

`concept` · `expert` · `exact_match` · 来源:paper

> 谱(PSATD)求解器相对 Yee FDTD 在激光-等离子体模拟中的优势与代价是?

**答案:** **A**
   ✅ A. 优势:更高阶/更低数值色散,长距离传输保相;代价:全局变换带来并行通信开销,且边界处理(如 PEC/周期)更复杂
   　 B. PSATD 无条件稳定,无 CFL 限制
   　 C. PSATD 不需要网格
   　 D. PSATD 总是更快


#### sim-hard-0009

`concept` · `grad` · `exact_match` · 来源:paper

> 回旋动理学通量管(flux tube)模拟的边界条件通常是?

**答案:** **A**
   ✅ A. 径向与极向用 twist-and-shift 周期边界(考虑磁剪切),平行方向周期或特定连接条件
   　 B. 所有方向都是导体壁
   　 C. 所有方向都是真空出流
   　 D. 无边界条件,因为通量管无限大


#### sim-hard-0010

`concept` · `expert` · `exact_match` · 来源:paper

> 在 ICF 集成模拟(如 HYDRA/LARED 类)中,'post-shot' 模拟与实验数据对比的主要挑战是?

**答案:** **A**
   ✅ A. 需要同时再现多种诊断(产额、X 光图像、谱、时间),且对初始条件(靶丸缺陷、驱动历史)与不透明度/EOS 模型高度敏感,单一调参难以同时满足
   　 B. 只要网格够细就能自动吻合
   　 C. 实验数据本身不可靠
   　 D. 后处理模拟不需要不透明度表


#### sim-hard-0011

`concept` · `grad` · `exact_match` · 来源:paper

> 在托卡马克输运模拟(如 TGYRO/TORAX)中,芯部-台基(核心-边缘)耦合的主要困难是?

**答案:** **A**
   ✅ A. 芯部湍流输运与台基 MHD 极限的时间尺度与物理机制不同,边界条件(台基高度)对芯部剖面有全局影响,需要自洽迭代
   　 B. 芯部与台基完全独立,无耦合
   　 C. 台基高度由极向磁场唯一决定
   　 D. 芯部输运与磁场无关


#### sim-hard-0012

`concept` · `grad` · `exact_match` · 来源:paper

> 为什么回旋动理学模拟常用拉格朗日(粒子)或欧拉(网格)两类方案,各自优势是?

**答案:** **A**
   ✅ A. 粒子法:相空间噪声低、易处理复杂几何;网格法:无统计噪声、谱清晰,但内存随维数爆炸
   　 B. 粒子法没有噪声
   　 C. 网格法不需要边界条件
   　 D. 两者完全等价


#### sim-hard-0013

`concept` · `grad` · `exact_match` · 来源:paper

> 在 ICF 靶丸一维模拟中,为什么常引入'流体力学效率'或'laser absorption efficiency'可调参数,其风险是?

**答案:** **A**
   ✅ A. 它们吸收未解析物理(LPI 散射、能量份额)的不确定度;风险:单一发次调参可能掩盖物理缺失,必须多发次交叉检验
   　 B. 这些参数是纯数值收敛参数,与物理无关
   　 C. 它们总是可以精确测量
   　 D. 引入它们会使模拟无条件准确


#### sim-hard-0014

`concept` · `expert` · `exact_match` · 来源:paper

> 在磁约束平衡重建(EFIT 类)中,为什么需要多种诊断联合约束而不能只靠磁探针?

**答案:** **A**
   ✅ A. 磁探针只提供边界信息,芯部电流/压力剖面需 MSE、 Thomson、磁轴约束等联合反演,否则解不唯一
   　 B. 磁探针足以唯一确定全部平衡
   　 C. EFIT 不需要任何诊断
   　 D. 联合约束只为提高计算速度


#### sim-hard-0015

`concept` · `grad` · `exact_match` · 来源:paper

> 在不透明度表(如 ionmix 格式)驱动的辐射流体模拟中,表外插值(温度/密度超出表范围)的主要风险是?

**答案:** **A**
   ✅ A. 外推可能产生非物理不透明度,导致辐射输运失真;应限制在表范围内或扩展表
   　 B. 外推总是安全的
   　 C. 不透明度表没有范围限制
   　 D. 外推只影响计算速度


#### sim-hard-0016

`concept` · `expert` · `exact_match` · 来源:paper

> 在磁约束湍流模拟中,'zonal flow'(带状流)对湍流输运的作用是?

**答案:** **A**
   ✅ A. 带状流是由湍流自发产生的对称剪切流,通过剪切破碎涡旋抑制湍流与输运,是湍流自调节的核心机制
   　 B. 带状流总是增强输运
   　 C. 带状流只存在于仿星器
   　 D. 带状流与湍流无关


#### sim-hard-0017

`concept` · `grad` · `exact_match` · 来源:textbook

> 在磁流体模拟中使用'理想 MHD'与'电阻 MHD'的差异,正确的有(多选):

**答案:** **A/B**
   ✅ A. 电阻 MHD 允许磁重联与撕裂模,理想 MHD 保持磁通冻结
   ✅ B. 理想 MHD 中磁力线拓扑不能改变
   　 C. 电阻率总是使所有不稳定性增长更快
   　 D. 电阻 MHD 更适合长时间平衡模拟


#### sim-hard-0018

`concept` · `grad` · `exact_match` · 来源:paper

> 在激光-等离子体模拟中,为什么 SMEI/丝化(self-focusing)会影响 LPI 评估?

**答案:** **A**
   ✅ A. 成丝提高局部光强,改变 SBS/SRS 的阈值与饱和水平,使一维模型低估或不稳定性空间分布失真
   　 B. 成丝与 LPI 无关
   　 C. 成丝总是被吸收消除
   　 D. 成丝只发生在真空中


#### sim-hard-0019

`concept` · `expert` · `exact_match` · 来源:paper

> 在动理学模拟中,为什么'全 f'(full-f)方法在强梯度台基区有优势?

**答案:** **A**
   ✅ A. 台基区扰动幅值可与平衡相当,δf 小扰动假设失效,full-f 直接演化全部分布函数无需展开
   　 B. full-f 计算更便宜
   　 C. δf 在台基区总是精确的
   　 D. full-f 不能处理湍流


#### sim-hard-0020

`concept` · `grad` · `exact_match` · 来源:paper

> 在 ICF/MCF 模拟的可重复性(reproducibility)管理中,下列哪些是公认的良好实践(多选)?

**答案:** **A/B/C**
   ✅ A. 固定代码版本、输入文件与随机种子并记录哈希
   ✅ B. 用容器/环境规范固化运行环境
   ✅ C. 用参考解/基准算例做回归测试
   　 D. 依赖口头描述即可复现


#### simulation-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> Sedov-Taylor 点爆炸波:能量 E=1e6 J 在空气(ρ=1.29 kg/m³)中瞬间释放,求 t=10 ns 时的激波半径 R=β(Et²/ρ)^(1/5),取 β=1.15。

**答案:** **0.010906 m**（容差 ±2%）
   - 独立复算:`1.15*(1e6*(1e-8)**2/1.29)**0.2`


#### simulation-0002

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 显式流体模拟的 CFL 时间步:网格 Δx=1.245e-6 m,流速 |v|=3e5 m/s,声速 c_s=1e6 m/s。按 dt=CFL·Δx/(|v|+c_s),CFL=0.2,求 dt(s)。

**答案:** **1.9154e-13 s**（容差 ±2%）
   - 独立复算:`0.2*1.245e-6/(3e5+1e6)`


#### simulation-0003

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> 磁扩散时间估算:熔融铝电导率 σ=4e6 S/m,特征厚度 L=4.5 μm(薄套筒壁)。按 t=μ0·σ·L² 求磁场穿透该壁层的扩散时间(s),并说明其与驱动电流上升时间(~150 ns)的相对大小意味着什么。

**答案:** **1.0179e-10 s**（容差 ±5%）
   - 独立复算:`4*pi*1e-7*4e6*(4.5e-6)**2`


#### simulation-0004

`concept` · `grad` · `exact_match` · 来源:local_sim

> 本机 FLASH 4.8 的 Z 箍缩算例用如下 setup 编译:./setup magnetoHD/ZPinch -2d +cylindrical +ug species=fill,line,vacu +mtmmmt +usm3t +mgd mgd_meshgroups=6 +hdf5typeio。对其中各选项的含义,下列说法正确的有(多选):

**答案:** **A/B/C/D**
   ✅ A. +cylindrical 表示柱坐标(r-z)几何,-2d 表示二维
   ✅ B. +mtmmmt 表示多温多物质多群磁流体(三温:电子/离子/辐射)模块
   ✅ C. +usm3t 表示 unsplit staggered mesh 三温 MHD 求解器
   ✅ D. mgd_meshgroups=6 表示多群扩散辐射输运分 6 个能群,而该算例运行时 useRadTrans=.false. 表示实际未开启辐射输运


#### simulation-0005

`concept` · `expert` · `exact_match` · 来源:paper

> MHD 数值模拟中,为什么常把 HLLD(或 HLLC)近似黎曼求解器与约束输运(CT)配合使用?

**答案:** **A**
   ✅ A. HLLD 能分辨接触间断与阿尔文中间波,比 HLL 少耗散;CT 在交错网格上演化面通量,把 ∇·B=0 保持到机器精度,避免磁单极误差积累
   　 B. HLLD 求解器自动保证 ∇·B=0,不需要 CT
   　 C. CT 只用于提高计算速度,与散度无关
   　 D. HLLD 无法处理磁场,只能用于纯流体


#### simulation-0006

`derivation` · `grad` · `rubric_judge` · 来源:textbook

> 用量纲分析推导 Sedov-Taylor 爆炸波半径的自相似标度:设爆炸仅由释放能量 E、时间 t、环境密度 ρ 刻画,推导 R∝(E t²/ρ)^(1/5) 并给出量纲自洽性验证。

**答案:** **rubric 判分（权重和=1）:**
   - [0.25] 列出三个刻画量 E、t、ρ 及其量纲([E]=ML²T⁻²,[t]=T,[ρ]=ML⁻³)
   - [0.25] 设 R=E^a t^b ρ^c,写出量纲方程
   - [0.3] 解得 a=1/5,b=2/5,c=-1/5,即 R∝(Et²/ρ)^(1/5)
   - [0.2] 说明该标度与 γ 无关只由量纲决定,γ 只进入数值系数 β


#### simulation-0007

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> AMR 有效分辨率:FLASH 网格块为 8×8 单元,模拟域宽 1.02 m 划分为 8 个基础块(即基础分辨率 Δx₀=1.02/8 m),允许逐层二分加密至 lrefine_max=7。求第 7 层的有效网格宽度 Δx(m)。

**答案:** **0.0019922 m**（容差 ±2%）
   - 独立复算:`1.02/(8*2**6)`


#### swe-issue-0001

`numeric` · `grad` · `numeric_tolerance` · 来源:paper

> PIC 模拟 WarpX 的 Yee(标准 FDTD)求解器在二维下必须满足 Courant 条件 c·dt ≤ 1/√(1/dx²+1/dz²)。取 dx=dz=1 μm 均匀网格,求满足 CFL 的最大时间步 c·dt(以无量纲 CFL 数 c·dt/dx 表示)。

**答案:** **0.7071 1**（容差 ±1%）
   - 独立复算:`1/sqrt(2)`


#### swe-issue-0002

`concept` · `grad` · `exact_match` · 来源:paper

> WarpX 在处理相对论性流动等离子体的数值切伦科夫不稳定性(NCI)时,官方文档推荐的标准组合是?

**答案:** **A**
   ✅ A. 对电磁场施加 Godfrey/bilinear 滤波(gather 前滤波)并配合 Vay 粒子推进器或 Galilean 坐标
   　 B. 简单把网格加密 10 倍
   　 C. 改用全隐式粒子推进
   　 D. 关闭电流沉积


#### swe-issue-0003

`concept` · `expert` · `exact_match` · 来源:paper

> 为什么 WarpX 默认用 Esirkepov 电流沉积而不是普通电荷守恒面密度后处理?

**答案:** **A**
   ✅ A. Esirkepov 格式在 Yee 网格上按连续性方程构造电流,保证离散电荷守恒(无需额外散度修正),与 FDTD 的 ∇·E=ρ/ε₀ 一致性相容
   　 B. Esirkepov 格式计算更快
   　 C. 它能消除 NCI
   　 D. 它能提高粒子能量精度


#### swe-issue-0004

`concept` · `grad` · `exact_match` · 来源:report

> DESY 关于 WarpX RZ 几何激光传输的公开报告中记录:提高角向模态数到 m=4 时模拟崩溃,而 PSATD 求解器不出现该问题。报告给出的修复与解释对应下列哪项?

**答案:** **A**
   ✅ A. 把 warpx.cfl 降到 1 以下可消除 FDTD 的崩溃;PSATD 的色散特性不同故无此现象
   　 B. 必须改用 3D 几何
   　 C. 是硬件故障,与算法无关
   　 D. 增加粒子数即可解决


#### swe-issue-0005

`numeric` · `undergrad` · `numeric_tolerance` · 来源:paper

> 蒙特卡洛中子输运(openmc)中,k 有效(k-eff)的本征值估计常用批(代)平均:连续 4 代的估计值为 1.021、1.019、1.024、1.017。求批均值。

**答案:** **1.02025 1**（容差 ±0%）
   - 独立复算:`(1.021+1.019+1.024+1.017)/4`


#### swe-issue-0006

`concept` · `grad` · `exact_match` · 来源:paper

> openmc 中 Shannon entropy(香农熵)通常被用来做什么?

**答案:** **A**
   ✅ A. 诊断裂变源空间分布是否已收敛(判据之一,与代间漂移一起决定略去多少个非活跃代)
   　 B. 计算中子能谱硬度
   　 C. 统计光子产额
   　 D. 优化体素网格


#### swe-issue-0007

`concept` · `expert` · `exact_match` · 来源:paper

> openmc issue #1472 报告了 OpenMC 与 MCNP 在中子-光子耦合输运上的显著差异。这类跨代码基准对比(cross-code benchmark)对中子学软件的意义是?

**答案:** **A**
   ✅ A. 独立实现之间的系统差异比对是发现物理模型/数据评估/实现缺陷的核心验证手段(verification & validation)
   　 B. 主要为了比较运行速度
   　 C. 为了统一输入格式
   　 D. 没有必要,MCNP 是错误参考


#### swe-issue-0008

`concept` · `expert` · `exact_match` · 来源:paper

> DESC issue #1940 中,plot_fsa 对对称平衡给出的 λ(几何因子)与手工场线积分结果不一致。关于磁通面平均(flux-surface average)的定义,下列哪项正确?

**答案:** **A**
   ✅ A. 通面平均 ⟨f⟩=∮ f dl/B / ∮ dl/B(沿闭合磁力线的 1/B 加权平均),对称情形下应与解析公式严格一致;实现差异往往源于坐标系或加权因子
   　 B. 通面平均就是对体积的简单平均
   　 C. 通面平均只在仿星器中定义,托卡马克中无意义
   　 D. λ 是任意常数,与平衡无关


#### swe-issue-0009

`numeric` · `grad` · `numeric_tolerance` · 来源:paper

> 谱平衡代码中力平衡误差的常用度量是相对体积力平衡误差 F_err = |⟨|J×B-∇p|²⟩/⟨|∇p|²⟩|^(1/2)。若 ⟨|J×B-∇p|²⟩=2.5e-3(归一化),⟨|∇p|²⟩=1.0,求 F_err。

**答案:** **0.05 1**（容差 ±2%）
   - 独立复算:`sqrt(2.5e-3/1.0)`


#### swe-issue-0010

`concept` · `grad` · `exact_match` · 来源:paper

> 自由边界平衡代码 FreeGS 求解 Grad-Shafranov 方程时,'自由边界'指的是?

**答案:** **A**
   ✅ A. 等离子体边界(最后闭合磁面)由总电流分布与外线圈共同自洽决定,而非预先给定
   　 B. 网格边界可以任意移动
   　 C. 边界条件在每一步都随机化
   　 D. 等离子体没有边界


#### swe-issue-0011

`concept` · `expert` · `exact_match` · 来源:textbook

> 回旋动理学(gyrokinetic)湍流模拟(如 GS2)采用 δf(增量)方法的主要原因是?

**答案:** **A**
   ✅ A. 湍流涨落幅值远小于平衡分布,直接对全量 f 演化会损失精度;δf 只需演化小扰动,数值噪声更低
   　 B. δf 方法计算量更大但更简单
   　 C. 全量 f 无法写成代码
   　 D. δf 是为了避免磁场项


#### swe-issue-0012

`numeric` · `expert` · `numeric_tolerance` · 来源:textbook

> gyrokinetic 通量管(flux tube)模拟的典型尺度:平行方向取 ~2π·qR(q=1.4,R=3 m),垂直方向取 ~100·ρ_i(ρ_i=2e-3 m)。求平行与垂直方向特征长度之比(用前者总长 2πqR 对后者 100ρ_i 估计)。

**答案:** **131.9 1**（容差 ±3%）
   - 独立复算:`2*pi*1.4*3/(100*2e-3)`


---

## zpinch（94 题）


#### code-evbatch-0001

`code` · `undergrad` · `unit_test` · 来源:textbook

> 实现两个函数:(1) kinetic_energies(pairs):输入 (m[mg/cm], v[cm/s]) 列表,返回对应动能 E[MJ/cm] 列表(cgs:E=0.5e-3·m·v²/1e13);(2) velocity_from_energy(m, E):由 m[mg/cm] 与 E[MJ/cm] 反算速率(cm/s)。

**答案:** **unit_test**:入口 `solution.py`，测试 `harness/tests/code_tests/test_code_evbatch.py`，超时 120s


#### zpinch-3001

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=525 ns,套筒半径 5.0 cm,泡沫半径 0.8 cm,套筒线质量 m=40.00 mg/cm。模拟给出该工况套筒动能 E=6.1188 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **5.53118e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*6.1188/40.0)`


#### zpinch-3002

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=45 MA,电流上升时间 tr=325 ns,套筒半径 5.0 cm,泡沫半径 0.6 cm,套筒线质量 m=20.00 mg/cm。模拟给出该工况套筒动能 E=2.7267 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **5.22178e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*2.7267/20.0)`


#### zpinch-3003

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=55 MA,电流上升时间 tr=250 ns,套筒半径 5.0 cm,泡沫半径 0.5 cm,套筒线质量 m=6.60 mg/cm。模拟给出该工况套筒动能 E=6.5227 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **1.40591e+08 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*6.5227/6.6)`


#### zpinch-3004

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=55 MA,电流上升时间 tr=400 ns,套筒半径 5.0 cm,泡沫半径 0.8 cm,套筒线质量 m=30.00 mg/cm。模拟给出该工况套筒动能 E=4.7546 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **5.63004e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*4.7546/30.0)`


#### zpinch-3005

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=350 ns,套筒半径 5.0 cm,泡沫半径 0.6 cm,套筒线质量 m=15.90 mg/cm。模拟给出该工况套筒动能 E=7.1249 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **9.46686e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*7.1249/15.9)`


#### zpinch-3006

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=55 MA,电流上升时间 tr=350 ns,套筒半径 7.0 cm,泡沫半径 0.5 cm,套筒线质量 m=20.00 mg/cm。模拟给出该工况套筒动能 E=3.9700 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **6.30079e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*3.97/20.0)`


#### zpinch-3007

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=42 MA,电流上升时间 tr=350 ns,套筒半径 4.0 cm,泡沫半径 0.6 cm,套筒线质量 m=13.05 mg/cm。模拟给出该工况套筒动能 E=3.1847 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **6.98625e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*3.1847/13.05)`


#### zpinch-3008

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=400 ns,套筒半径 6.0 cm,泡沫半径 0.5 cm,套筒线质量 m=13.65 mg/cm。模拟给出该工况套筒动能 E=8.4032 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **1.10961e+08 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*8.4032/13.65)`


#### zpinch-3009

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=40 MA,电流上升时间 tr=250 ns,套筒半径 7.0 cm,泡沫半径 0.8 cm,套筒线质量 m=40.00 mg/cm。模拟给出该工况套筒动能 E=1.8008 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **3.00067e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*1.8008/40.0)`


#### zpinch-3010

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=250 ns,套筒半径 7.0 cm,泡沫半径 0.8 cm,套筒线质量 m=20.00 mg/cm。模拟给出该工况套筒动能 E=1.9536 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **4.41995e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*1.9536/20.0)`


#### zpinch-3011

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=58 MA,电流上升时间 tr=550 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,套筒线质量 m=20.00 mg/cm。模拟给出该工况套筒动能 E=5.1225 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **7.15716e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*5.1225/20.0)`


#### zpinch-3012

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=175 ns,套筒半径 5.0 cm,泡沫半径 0.5 cm,套筒线质量 m=40.00 mg/cm。模拟给出该工况套筒动能 E=0.7118 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **1.88653e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*0.7118/40.0)`


#### zpinch-3013

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=58 MA,tr=225 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,线质量 m=20.00 mg/cm,内爆速率达到 7.1990e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **5.1826 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*20.0*(7.1990e+07)**2/1e13`


#### zpinch-3014

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=50 MA,tr=175 ns,套筒半径 7.0 cm,泡沫半径 0.8 cm,线质量 m=30.00 mg/cm,内爆速率达到 4.4103e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **2.9176 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*30.0*(4.4103e+07)**2/1e13`


#### zpinch-3015

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=50 MA,tr=275 ns,套筒半径 6.0 cm,泡沫半径 0.5 cm,线质量 m=30.00 mg/cm,内爆速率达到 2.4285e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **0.88464 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*30.0*(2.4285e+07)**2/1e13`


#### zpinch-3016

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=60 MA,tr=575 ns,套筒半径 5.0 cm,泡沫半径 0.7 cm,线质量 m=40.00 mg/cm,内爆速率达到 5.7315e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **6.57 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*40.0*(5.7315e+07)**2/1e13`


#### zpinch-3017

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=45 MA,tr=425 ns,套筒半径 5.0 cm,泡沫半径 0.5 cm,线质量 m=30.00 mg/cm,内爆速率达到 4.6509e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **3.2446 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*30.0*(4.6509e+07)**2/1e13`


#### zpinch-3018

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=52 MA,tr=550 ns,套筒半径 5.0 cm,泡沫半径 0.7 cm,线质量 m=30.90 mg/cm,内爆速率达到 5.7138e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **5.044 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*30.9*(5.7138e+07)**2/1e13`


#### zpinch-3019

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=40 MA,tr=600 ns,套筒半径 7.0 cm,泡沫半径 0.6 cm,线质量 m=10.10 mg/cm,内爆速率达到 8.5502e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **3.6918 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*10.1*(8.5502e+07)**2/1e13`


#### zpinch-3020

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=48 MA,tr=525 ns,套筒半径 6.0 cm,泡沫半径 0.5 cm,线质量 m=40.00 mg/cm,内爆速率达到 4.1122e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **3.382 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*40.0*(4.1122e+07)**2/1e13`


#### zpinch-3021

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=40 MA,tr=425 ns,套筒半径 5.0 cm,泡沫半径 0.7 cm,线质量 m=10.70 mg/cm,内爆速率达到 7.3977e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **2.9278 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*10.7*(7.3977e+07)**2/1e13`


#### zpinch-3022

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=50 MA,tr=600 ns,套筒半径 5.0 cm,泡沫半径 0.6 cm,线质量 m=20.00 mg/cm,内爆速率达到 6.8380e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **4.6758 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*20.0*(6.8380e+07)**2/1e13`


#### zpinch-3023

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=2.1725e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **217.2 μm/ns**（容差 ±2%）
   - 独立复算:`2.1725e+07*1e4/1e9`


#### zpinch-3024

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=4.2918e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **429.2 μm/ns**（容差 ±2%）
   - 独立复算:`4.2918e+07*1e4/1e9`


#### zpinch-3025

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=3.0183e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **301.8 μm/ns**（容差 ±2%）
   - 独立复算:`3.0183e+07*1e4/1e9`


#### zpinch-3026

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=7.3617e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **736.2 μm/ns**（容差 ±2%）
   - 独立复算:`7.3617e+07*1e4/1e9`


#### zpinch-3027

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=4.5776e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **457.8 μm/ns**（容差 ±2%）
   - 独立复算:`4.5776e+07*1e4/1e9`


#### zpinch-3028

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=5.0720e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **507.2 μm/ns**（容差 ±2%）
   - 独立复算:`5.0720e+07*1e4/1e9`


#### zpinch-3029

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=3.4328e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **343.3 μm/ns**（容差 ±2%）
   - 独立复算:`3.4328e+07*1e4/1e9`


#### zpinch-3030

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=1.8946e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **189.5 μm/ns**（容差 ±2%）
   - 独立复算:`1.8946e+07*1e4/1e9`


#### zpinch-3031

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=500 ns,套筒半径 7.0 cm,泡沫半径 0.8 cm,m=40.00 mg/cm)下:I=40 MA 时动能 E₁=0.7131 MJ/cm,I=60 MA 时 E₂=5.2519 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **4.92 1**（容差 ±3%）
   - 独立复算:`log(5.2519/0.7131)/log(60/40)`


#### zpinch-3032

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=575 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,m=20.00 mg/cm)下:I=40 MA 时动能 E₁=2.9796 MJ/cm,I=60 MA 时 E₂=5.2116 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **1.38 1**（容差 ±3%）
   - 独立复算:`log(5.2116/2.9796)/log(60/40)`


#### zpinch-3033

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=325 ns,套筒半径 5.0 cm,泡沫半径 0.6 cm,m=40.00 mg/cm)下:I=40 MA 时动能 E₁=0.5383 MJ/cm,I=60 MA 时 E₂=4.2652 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **5.1 1**（容差 ±3%）
   - 独立复算:`log(4.2652/0.5383)/log(60/40)`


#### zpinch-3034

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=150 ns,套筒半径 5.0 cm,泡沫半径 0.8 cm,m=30.00 mg/cm)下:I=40 MA 时动能 E₁=1.4227 MJ/cm,I=60 MA 时 E₂=0.6860 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **-1.8 1**（容差 ±3%）
   - 独立复算:`log(0.686/1.4227)/log(60/40)`


#### zpinch-3035

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=325 ns,套筒半径 6.0 cm,泡沫半径 0.8 cm,m=30.00 mg/cm)下:I=40 MA 时动能 E₁=0.4846 MJ/cm,I=60 MA 时 E₂=3.7849 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **5.07 1**（容差 ±3%）
   - 独立复算:`log(3.7849/0.4846)/log(60/40)`


#### zpinch-3036

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=5.3363 MJ/cm。把它表示为 kJ/cm。

**答案:** **5336.3 kJ/cm**（容差 ±2%）
   - 独立复算:`5.3363*1000`


#### zpinch-3037

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=4.8255 MJ/cm。把它表示为 kJ/cm。

**答案:** **4825.5 kJ/cm**（容差 ±2%）
   - 独立复算:`4.8255*1000`


#### zpinch-3038

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=3.9588 MJ/cm。把它表示为 kJ/cm。

**答案:** **3958.8 kJ/cm**（容差 ±2%）
   - 独立复算:`3.9588*1000`


#### zpinch-3039

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=2.5034 MJ/cm。把它表示为 kJ/cm。

**答案:** **2503.4 kJ/cm**（容差 ±2%）
   - 独立复算:`2.5034*1000`


#### zpinch-3040

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=4.9839 MJ/cm。把它表示为 kJ/cm。

**答案:** **4983.9 kJ/cm**（容差 ±2%）
   - 独立复算:`4.9839*1000`


#### zpinch-2001

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=450 ns,套筒半径 7.0 cm,泡沫半径 0.8 cm,套筒线质量 m=30.00 mg/cm。模拟给出该工况套筒动能 E=5.5994 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **6.10977e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*5.5994/30.0)`


#### zpinch-2002

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=55 MA,电流上升时间 tr=500 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,套筒线质量 m=40.00 mg/cm。模拟给出该工况套筒动能 E=5.8601 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **5.41299e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*5.8601/40.0)`


#### zpinch-2003

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=60 MA,电流上升时间 tr=350 ns,套筒半径 6.0 cm,泡沫半径 0.8 cm,套筒线质量 m=11.30 mg/cm。模拟给出该工况套筒动能 E=6.7569 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **1.09358e+08 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*6.7569/11.3)`


#### zpinch-2004

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=45 MA,电流上升时间 tr=550 ns,套筒半径 6.0 cm,泡沫半径 0.5 cm,套筒线质量 m=30.00 mg/cm。模拟给出该工况套筒动能 E=3.8477 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **5.06471e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*3.8477/30.0)`


#### zpinch-2005

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=42 MA,电流上升时间 tr=450 ns,套筒半径 7.0 cm,泡沫半径 0.5 cm,套筒线质量 m=20.00 mg/cm。模拟给出该工况套筒动能 E=2.3262 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **4.82307e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*2.3262/20.0)`


#### zpinch-2006

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=48 MA,电流上升时间 tr=150 ns,套筒半径 7.0 cm,泡沫半径 0.7 cm,套筒线质量 m=30.00 mg/cm。模拟给出该工况套筒动能 E=0.8995 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **2.44881e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*0.8995/30.0)`


#### zpinch-2007

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=52 MA,电流上升时间 tr=425 ns,套筒半径 6.0 cm,泡沫半径 0.8 cm,套筒线质量 m=12.70 mg/cm。模拟给出该工况套筒动能 E=5.1735 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **9.02621e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*5.1735/12.7)`


#### zpinch-2008

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=42 MA,电流上升时间 tr=300 ns,套筒半径 7.0 cm,泡沫半径 0.7 cm,套筒线质量 m=2.90 mg/cm。模拟给出该工况套筒动能 E=3.8949 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **1.63894e+08 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*3.8949/2.9)`


#### zpinch-2009

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=42 MA,电流上升时间 tr=325 ns,套筒半径 4.0 cm,泡沫半径 0.7 cm,套筒线质量 m=40.00 mg/cm。模拟给出该工况套筒动能 E=1.4404 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **2.68365e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*1.4404/40.0)`


#### zpinch-2010

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=40 MA,电流上升时间 tr=300 ns,套筒半径 7.0 cm,泡沫半径 0.8 cm,套筒线质量 m=2.65 mg/cm。模拟给出该工况套筒动能 E=3.2424 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **1.56432e+08 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*3.2424/2.65)`


#### zpinch-2011

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=52 MA,电流上升时间 tr=400 ns,套筒半径 5.0 cm,泡沫半径 0.6 cm,套筒线质量 m=20.00 mg/cm。模拟给出该工况套筒动能 E=5.3671 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **7.32605e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*5.3671/20.0)`


#### zpinch-2012

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝(Z=13)套筒内爆的零维模拟工况:驱动电流峰值 I=50 MA,电流上升时间 tr=300 ns,套筒半径 6.0 cm,泡沫半径 0.7 cm,套筒线质量 m=30.00 mg/cm。模拟给出该工况套筒动能 E=1.1536 MJ/cm。按 E=½mv²(cgs)求内爆速率(以 cm/s 表示的速率值,取正)。

**答案:** **2.77321e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2e16*1.1536/30.0)`


#### zpinch-2013

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=40 MA,tr=475 ns,套筒半径 7.0 cm,泡沫半径 0.5 cm,线质量 m=40.00 mg/cm,内爆速率达到 1.7437e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **0.6081 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*40.0*(1.7437e+07)**2/1e13`


#### zpinch-2014

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=52 MA,tr=400 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,线质量 m=25.00 mg/cm,内爆速率达到 6.5400e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **5.3464 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*25.0*(6.5400e+07)**2/1e13`


#### zpinch-2015

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=52 MA,tr=350 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,线质量 m=20.00 mg/cm,内爆速率达到 7.3097e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **5.3432 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*20.0*(7.3097e+07)**2/1e13`


#### zpinch-2016

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=60 MA,tr=250 ns,套筒半径 5.0 cm,泡沫半径 0.5 cm,线质量 m=8.00 mg/cm,内爆速率达到 1.3930e+08 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **7.7618 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*8.0*(1.3930e+08)**2/1e13`


#### zpinch-2017

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=42 MA,tr=575 ns,套筒半径 4.0 cm,泡沫半径 0.5 cm,线质量 m=33.90 mg/cm,内爆速率达到 4.5469e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **3.5043 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*33.9*(4.5469e+07)**2/1e13`


#### zpinch-2018

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=45 MA,tr=325 ns,套筒半径 4.0 cm,泡沫半径 0.6 cm,线质量 m=30.00 mg/cm,内爆速率达到 4.1925e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **2.6366 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*30.0*(4.1925e+07)**2/1e13`


#### zpinch-2019

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=45 MA,tr=450 ns,套筒半径 6.0 cm,泡沫半径 0.5 cm,线质量 m=9.65 mg/cm,内爆速率达到 9.8976e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **4.7267 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*9.65*(9.8976e+07)**2/1e13`


#### zpinch-2020

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=55 MA,tr=575 ns,套筒半径 6.0 cm,泡沫半径 0.8 cm,线质量 m=30.00 mg/cm,内爆速率达到 6.1290e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **5.6347 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*30.0*(6.1290e+07)**2/1e13`


#### zpinch-2021

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=50 MA,tr=325 ns,套筒半径 4.0 cm,泡沫半径 0.8 cm,线质量 m=20.00 mg/cm,内爆速率达到 6.0673e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **3.6812 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*20.0*(6.0673e+07)**2/1e13`


#### zpinch-2022

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩铝套筒零维模拟工况:I=55 MA,tr=425 ns,套筒半径 6.0 cm,泡沫半径 0.8 cm,线质量 m=14.00 mg/cm,内爆速率达到 9.0063e+07 cm/s。按 E=½mv² 求套筒动能(MJ/cm)。cgs 换算:E[MJ/cm]=0.5e-3·m[mg/cm]·(v[cm/s])²/1e13。

**答案:** **5.6779 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5e-3*14.0*(9.0063e+07)**2/1e13`


#### zpinch-2023

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=2.9375e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **293.8 μm/ns**（容差 ±2%）
   - 独立复算:`2.9375e+07*1e4/1e9`


#### zpinch-2024

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=5.3262e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **532.6 μm/ns**（容差 ±2%）
   - 独立复算:`5.3262e+07*1e4/1e9`


#### zpinch-2025

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=2.4024e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **240.2 μm/ns**（容差 ±2%）
   - 独立复算:`2.4024e+07*1e4/1e9`


#### zpinch-2026

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=5.7138e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **571.4 μm/ns**（容差 ±2%）
   - 独立复算:`5.7138e+07*1e4/1e9`


#### zpinch-2027

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=3.2945e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **329.4 μm/ns**（容差 ±2%）
   - 独立复算:`3.2945e+07*1e4/1e9`


#### zpinch-2028

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=4.9491e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **494.9 μm/ns**（容差 ±2%）
   - 独立复算:`4.9491e+07*1e4/1e9`


#### zpinch-2029

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=2.7904e+07 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **279 μm/ns**（容差 ±2%）
   - 独立复算:`2.7904e+07*1e4/1e9`


#### zpinch-2030

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某零维模拟给出套筒内爆速率 v=2.2065e+08 cm/s。请把它换算为 μm/ns(微米/纳秒)。提示:1 cm = 1e4 μm,1 s = 1e9 ns。

**答案:** **2206 μm/ns**（容差 ±2%）
   - 独立复算:`2.2065e+08*1e4/1e9`


#### zpinch-2031

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=375 ns,套筒半径 6.0 cm,泡沫半径 0.7 cm,m=20.00 mg/cm)下:I=40 MA 时动能 E₁=1.4584 MJ/cm,I=60 MA 时 E₂=6.7191 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **3.77 1**（容差 ±3%）
   - 独立复算:`log(6.7191/1.4584)/log(60/40)`


#### zpinch-2032

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=175 ns,套筒半径 7.0 cm,泡沫半径 0.6 cm,m=40.00 mg/cm)下:I=40 MA 时动能 E₁=1.0914 MJ/cm,I=60 MA 时 E₂=5.2232 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **3.86 1**（容差 ±3%）
   - 独立复算:`log(5.2232/1.0914)/log(60/40)`


#### zpinch-2033

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=375 ns,套筒半径 6.0 cm,泡沫半径 0.6 cm,m=40.00 mg/cm)下:I=40 MA 时动能 E₁=0.4835 MJ/cm,I=60 MA 时 E₂=4.0044 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **5.21 1**（容差 ±3%）
   - 独立复算:`log(4.0044/0.4835)/log(60/40)`


#### zpinch-2034

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=350 ns,套筒半径 4.0 cm,泡沫半径 0.6 cm,m=40.00 mg/cm)下:I=40 MA 时动能 E₁=1.3604 MJ/cm,I=60 MA 时 E₂=5.9656 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **3.65 1**（容差 ±3%）
   - 独立复算:`log(5.9656/1.3604)/log(60/40)`


#### zpinch-2035

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 零维模拟同族工况(tr=375 ns,套筒半径 6.0 cm,泡沫半径 0.5 cm,m=20.00 mg/cm)下:I=40 MA 时动能 E₁=1.5246 MJ/cm,I=60 MA 时 E₂=7.6595 MJ/cm。设 E∝I^α,求 α(保留 3 位有效数字)。

**答案:** **3.98 1**（容差 ±3%）
   - 独立复算:`log(7.6595/1.5246)/log(60/40)`


#### zpinch-2036

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=3.4611 MJ/cm。把它表示为 kJ/cm。

**答案:** **3461.1 kJ/cm**（容差 ±2%）
   - 独立复算:`3.4611*1000`


#### zpinch-2037

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=4.6395 MJ/cm。把它表示为 kJ/cm。

**答案:** **4639.5 kJ/cm**（容差 ±2%）
   - 独立复算:`4.6395*1000`


#### zpinch-2038

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=2.1462 MJ/cm。把它表示为 kJ/cm。

**答案:** **2146.2 kJ/cm**（容差 ±2%）
   - 独立复算:`2.1462*1000`


#### zpinch-2039

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=0.5346 MJ/cm。把它表示为 kJ/cm。

**答案:** **534.6 kJ/cm**（容差 ±2%）
   - 独立复算:`0.5346*1000`


#### zpinch-2040

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某工况套筒动能 E=3.9359 MJ/cm。把它表示为 kJ/cm。

**答案:** **3935.9 kJ/cm**（容差 ±2%）
   - 独立复算:`3.9359*1000`


#### zpinch-0001

`numeric` · `undergrad` · `numeric_tolerance` · 来源:local_sim

> 某 Z 箍缩零维（0D）内爆模型的本地数据表给出一个工况：套筒线质量 m = 20 mg/cm，内爆动能 E = 0.3202 MJ/cm。动能与内爆速率满足 E = ½·m·v²，cgs 单位制下即 E[erg/cm] = 0.5·m[mg/cm]×1e-3·v²[cm/s]，且 1 MJ = 1e13 erg（因此 v = √(2e16·E[MJ/cm]/m[mg/cm])）。求内爆速率 v，以 cm/s 为单位。

**答案:** **1.7894e+07 cm/s**（容差 ±2%）
   - 独立复算:`sqrt(2*0.3202e13/(20*1e-3))`


#### zpinch-0002

`numeric` · `grad` · `numeric_tolerance` · 来源:local_sim

> Z 箍缩零维模型的反问题：某工况套筒线质量 m = 30 mg/cm，设计要求内爆速率达到 v = 2e7 cm/s（200 km/s）。按动能关系 E = ½·m·v²（cgs：E[erg/cm] = 0.5·m[g/cm]·v²[cm/s]，1 MJ = 1e13 erg），求所需内爆动能 E，以 MJ/cm 为单位。

**答案:** **0.6 MJ/cm**（容差 ±2%）
   - 独立复算:`0.5*30e-3*(2e7)**2/1e13`


#### zpinch-0003

`numeric` · `grad` · `numeric_tolerance` · 来源:paper

> Z 箍缩等离子体处于 Bennett 平衡时，轴向电流满足 I = √(8π·N·k_B·T/μ0)，其中 N 为粒子线密度（单位长度总粒子数）、T 为温度。取 N = 1e22 m^-1、T = 1 keV（1 eV 对应 11604.5 K；k_B = 1.380649e-23 J/K；μ0 = 4π×1e-7 H/m）。求平衡电流 I，以 A 为单位。

**答案:** **179010 A**（容差 ±2%）
   - 独立复算:`sqrt(8*pi*1e22*1.380649e-23*11604.5/(4*pi*1e-7))`


#### zpinch-0004

`concept` · `grad` · `exact_match` · 来源:paper

> 关于 Z 箍缩等离子体的两类理想 MHD 不稳定性——m = 0（sausage，腊肠模）与 m = 1（kink，扭曲模），下列说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. m = 0 模表现为等离子体柱的轴对称局部颈缩，发展下去可使柱体截断（necking）
   ✅ B. m = 1 模表现为等离子体柱整体横向弯曲/位移（螺旋状偏移），而非局部变细
   ✅ C. 外加足够强的轴向（纵向）磁场可借助磁张力与磁冻结的致稳作用抑制这两类模的增长
   　 D. m = 1 模的增长率总是远高于 m = 0 模，因此实验中必然是 kink 模先于 sausage 模出现


#### zpinch-0005

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 长直 Z 箍缩等离子体柱表面的角向（方位）磁场由安培定律给出 B_θ = μ0·I/(2π·r)。某装置峰值电流 I = 15 MA，箍缩柱半径 r = 1 cm。取 μ0/(2π) = 2e-7 H/m。求柱面磁场 B_θ，以 T 为单位。

**答案:** **300 T**（容差 ±2%）
   - 独立复算:`2e-7*15e6/1e-2`


#### zpinch-0006

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 磁压（magnetic pressure）p_B = B²/(2μ0)。接上题，柱面磁场 B = 300 T，μ0 = 4π×1e-7 H/m。求该磁场对应的磁压 p_B，以 Pa 为单位（参考：1 Mbar = 1e11 Pa）。

**答案:** **3.581e+10 Pa**（容差 ±2%）
   - 独立复算:`300**2/(2*4*pi*1e-7)`


#### zpinch-0007

`numeric` · `undergrad` · `numeric_tolerance` · 来源:textbook

> 脉冲功率装置的初级储能为电容器组，储能 E = ½·C·V²。某 Marx 发生器单级等效电容 C = 100 μF，充电电压 V = 100 kV。求该级储能 E，以 J 为单位。

**答案:** **500000 J**（容差 ±2%）
   - 独立复算:`0.5*100e-6*(100e3)**2`


#### zpinch-0008

`numeric` · `grad` · `numeric_tolerance` · 来源:textbook

> 脉冲功率主放电回路可近似为 LC 振荡回路，其放电角频率 ω = 1/√(L·C)。设回路总电感 L = 10 nH、总电容 C = 100 μF。求放电角频率 ω，以 rad/s 为单位。

**答案:** **1e+06 rad/s**（容差 ±2%）
   - 独立复算:`1/sqrt(10e-9*100e-6)`


#### zpinch-0009

`concept` · `expert` · `exact_match` · 来源:report

> 某脉冲电容器状态在线评估方法（专利申请公开文本 202610366208.8）采用 GM(1,1) 灰色模型预测电容器寿命：对退化特征量原始序列 x^(0) 作一次累加生成（1-AGO）得 x^(1)，建立白化微分方程 dx^(1)/dt + a·x^(1) = b，其中 a 为发展系数、b 为灰作用量。下列说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. 建模前须对原始序列作级比检验（λ(k)=x^(0)(k-1)/x^(0)(k)），判断序列是否落入可建模覆盖区间、是否适合 GM(1,1) 建模
   ✅ B. 发展系数 a < 0 时累加序列呈单调增长形态，对应退化特征随放电次数累积、电容器趋于失效
   ✅ C. 背景值取相邻两个累加生成值的均值，即 z^(1)(k) = 0.5·(x^(1)(k)+x^(1)(k-1))
   　 D. 灰作用量 b 是电容器寿命的物理上限，其数值直接等于额定充放电循环次数


#### zpinch-0010

`concept` · `grad` · `exact_match` · 来源:paper

> Z 箍缩丝阵/套筒在内爆加速阶段的磁瑞利–泰勒（MRT）不稳定性是限制 X 射线产额与内爆品质的关键因素。下列关于其物理来源与抑制手段的说法正确的有（多选）：

**答案:** **A/B/C**
   ✅ A. 物理上等效于加速界面处重流体压于轻流体之上的 RT 不稳定性：磁压加速的等离子体/磁通侵入套筒物质，加速阶段外轻内重的等效位形触发扰动增长
   ✅ B. 对丝阵/套筒进行预热（preheat）可提高初始温度与声速、降低有效 Atwood 数并引入可压缩性致稳，从而抑制 MRT
   ✅ C. 外加轴向磁场可借助磁张力对短波长扰动的致稳作用抑制 MRT 增长
   　 D. MRT 只能通过把电流上升时间压到零来消除，动态黑腔、脉冲波形优化等手段均无效


#### zpinch-0011

`numeric` · `expert` · `numeric_tolerance` · 来源:local_sim

> 标度律拟合：某 Z 箍缩零维模型在电流上升时间 tr = 150 ns、套筒线质量 m = 20 mg/cm 且几何相同的两个工况下给出：驱动电流 I = 40 MA 时内爆动能 E = 0.3202 MJ/cm；I = 60 MA 时 E = 2.305 MJ/cm。设标度律 E ∝ I^α，求幂指数 α（无量纲）。

**答案:** **4.869 1**（容差 ±5%）
   - 独立复算:`log(2.305/0.3202)/log(60/40)`


#### zpinch-0012

`concept` · `undergrad` · `exact_match` · 来源:local_sim

> 某团队仅用本地零维模拟的 2736 条 source 域数据训练 Z 箍缩产额代理模型，直接用于 8208 条 target 域数据时内爆动能预测误差 E_MAPE 高达 188.7%；把 target 域数据并入训练集重新训练后，误差降到约 9–14%。对该跨域泛化失败现象的分析，下列说法正确的有（多选）：

**答案:** **A/B/D**
   ✅ A. source 训练集的参数分布（如线质量、电流等输入范围）未覆盖 target 域，模型被迫在分布外（OOD）区域外推，导致误差暴涨
   ✅ B. 失败主因是数据覆盖问题而非模型结构问题：补充目标域数据比更换更复杂的网络架构更关键
   　 C. 188.7% 的 MAPE 说明神经网络本质上无法拟合 Z 箍缩物理，数据驱动代理模型路线应予放弃
   ✅ D. 合并源域与目标域数据后误差降到约 9–14%，说明在覆盖目标域的分布内插值时代理模型可达到工程可用精度


#### zpinch-0013

`derivation` · `grad` · `rubric_judge` · 来源:textbook

> 从径向磁压–热压平衡出发，推导圆柱对称 Z 箍缩的 Bennett 平衡关系 I² = (8π/μ0)·N·k_B·T，其中 I 为轴向总电流、N 为单位长度总粒子线密度、T 为均匀温度（压强 p = n·k_B·T，n 为总粒子数密度）。要求给出角向磁场形式、径向力平衡方程、对全截面配分积分的关键步骤与最终表达式。

**答案:** **rubric 判分（权重和=1）:**
   - [0.2] 由安培定律给出角向磁场 B_θ(r) = μ0·I(r)/(2π·r)，柱外 B_θ = μ0·I/(2π·r)，I(r) 为半径 r 内包围的电流
   - [0.25] 写出径向力平衡 dp/dr = −j_z·B_θ，代入 j_z = (1/(μ0·r))·d(r·B_θ)/dr，化为 dp/dr = −(1/(2μ0·r²))·d(r²·B_θ²)/dr
   - [0.25] 两边乘 r² 后从 0 到 ∞ 积分，利用边界条件 p(∞)=0 与 r²·B_θ²→μ0²·I²/(4π²)，得 ∫p·r·dr = μ0·I²/(16π²)
   - [0.15] 引入等温状态方程 p = n·k_B·T 与线密度定义 N = ∫n·2π·r·dr，代入得 k_B·T·N/(2π) = μ0·I²/(16π²)
   - [0.15] 整理得 Bennett 关系 I² = (8π/μ0)·N·k_B·T，并指明其物理含义：角向磁场的自箍缩磁压力与等离子体热膨胀压力相平衡
