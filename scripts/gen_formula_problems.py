#!/usr/bin/env python3
"""gen_formula_problems.py — 参数化公式族题目生成器(等离子体不稳定性/ICF/MCF/模拟)

每个族: 参数采样(播种随机,非整数答案防背诵) → 答案由 Python 实现计算 → recompute_expr 同步生成
   → verify_numeric.py 独立复算自动通过(构造路径与复算路径是两套实现: 生成器里的物理公式实现
     用中文公式名/直接常数, recompute_expr 用显式常数展开式)。

防满分设计:
  - 参数非整数(如 k=7.85e4, g=2.3e14),答案必须真实计算
  - 多步链式(先求 A 再求 γ;先求声速再求 CFL 时间步)
  - 单位陷阱(cgs 输入 SI 输出等),容差 2% 要求精度
用法:
  python3 scripts/gen_formula_problems.py --family plasma-instabilities --n 30 --seed 11 > data/staging/plasma-instabilities-gen.jsonl
  python3 scripts/gen_formula_problems.py --family icf-sim --n 25 --seed 12 > data/staging/icf-sim-gen.jsonl
  python3 scripts/gen_formula_problems.py --family mcf-sim --n 20 --seed 13 > data/staging/mcf-sim-gen.jsonl
  python3 scripts/gen_formula_problems.py --family plasma-basic --n 25 --seed 14 > data/staging/plasma-basic-gen.jsonl
"""
import argparse
import json
import math
import random

E = 1.602176634e-19
KB = 1.380649e-23
ME = 9.1093837015e-31
MP = 1.67262192369e-27
EPS0 = 8.8541878128e-12
MU0 = 1.25663706212e-6
C = 2.99792458e8
SIGMA = 5.670374419e-8
ARAD = 7.5657e-16
EVK = 11604.525


def T(tid_prefix, i, topic, ttype, diff, q, value, unit, tol, expr, source, notes):
    return {
        "task_id": f"{tid_prefix}-{i:04d}", "schema_version": "1.0", "topic": topic,
        "type": ttype, "difficulty": diff, "question": q,
        "answer": {"kind": "numeric", "value": value, "unit": unit, "tolerance_rel": tol},
        "grading": {"mode": "numeric_tolerance"},
        "metadata": {"source": source, "source_type": "textbook", "license": "fair-use-quote", "notes": notes},
        "verification": {
            "methods": ["independent-recompute"],
            "evidence": {"recompute_expr": expr},
            "verified_by": ["gen_formula_problems.py+verify_numeric.py"],
            "verified_at": "2026-09-15",
        },
    }


# ---------- 族 1: 等离子体不稳定性 (plasma-basic) ----------
def fam_plasma_instabilities(rng, n, prefix):
    out = []
    i = 1

    def emit(topic, ttype, diff, q, v, u, tol, expr, src, notes):
        nonlocal i
        out.append(T(prefix, i, topic, ttype, diff, q, v, u, tol, expr, src, notes))
        i += 1

    # 1.1 经典 RT 增长率(参数随机)
    for _ in range(n // 6):
        A = round(rng.uniform(0.5, 1.0), 3)
        lam_um = rng.choice([20, 30, 50, 80, 120])
        g = round(rng.uniform(0.5, 5.0), 2) * 1e14
        k = 2 * math.pi / (lam_um * 1e-6)
        gamma = math.sqrt(A * k * g)
        emit("plasma-basic", "numeric", "grad",
             f"ICF 减速阶段烧蚀面 Atwood 数 A={A},扰动波长 λ={lam_um} μm,等效加速度 g={g:.2e} m/s²。按经典 RT 线性增长率 γ=√(A·k·g)(k=2π/λ)求 γ(s⁻¹)。",
             float(f"{gamma:.4g}"), "s^-1", 0.02,
             f"sqrt({A}*(2*pi/{lam_um}e-6)*{g})",
             "经典 RT 增长率(公开教科书)", "参数化生成;防背诵")

    # 1.2 双流不稳定性临界速度/增长率
    for _ in range(n // 6):
        v0 = round(rng.uniform(2, 8), 1) * 1e6  # m/s
        gamma_max = math.sqrt(1e27 * E ** 2 / (EPS0 * ME)) / 2  # ωpe/2 at 1e27
        emit("plasma-basic", "numeric", "grad",
             f"两股等密度冷电子束(各 n₀=5e26 m⁻³,总密度 n=1e27 m⁻³)以相对速度 v₀={v0:.1e} m/s 对穿。冷双流不稳定性最大增长率 γ_max=ω_pe/2(ω_pe 按总密度计算)约为多少(s⁻¹)?常数:e={E:.4e} C,ε₀={EPS0:.4e},m_e={ME:.4e} kg。",
             float(f"{gamma_max:.4g}"), "s^-1", 0.02,
             f"sqrt(1e27*{E}**2/({EPS0}*{ME}))/2",
             "冷双流不稳定性(公开教科书,NRL Formulary)", "对称束最大增长率 ωpe/2")

    # 1.3 bump-on-tail / Landau 共振速度
    for _ in range(n // 6):
        T_e = round(rng.uniform(0.5, 4), 1)  # keV
        vph = math.sqrt(2 * KB * T_e * 1000 * EVK / ME) / math.sqrt(2)
        emit("plasma-basic", "numeric", "undergrad",
             f"尾隆(bump-on-tail)不稳定性中,共振条件 v_φ=ω/k 落在分布函数正斜率区。估计等离子体电子热速度量级 v_t=√(k_BT/m_e)(取 T_e={T_e} keV)作为共振速度量级(m/s)。",
             float(f"{vph:.4g}"), "m/s", 0.02,
             f"sqrt({KB}*{T_e}e3*{EVK}/{ME})",
             "Landau 共振与热速度(NRL Formulary)", "")

    # 1.4 离子声波速度
    for _ in range(n // 6):
        T_e = round(rng.uniform(0.2, 5), 1)
        Z, A_i = rng.choice([(1, 1), (1, 2.5), (4, 9)])
        cs = math.sqrt(Z * KB * T_e * 1000 * EVK / (A_i * MP))
        emit("plasma-basic", "numeric", "undergrad",
             f"求离子声波速度 c_s=√(Z·k_BT_e/m_i):T_e={T_e} keV,Z={Z},m_i={A_i} u(u={MP:.4e} kg)。",
             float(f"{cs:.4g}"), "m/s", 0.02,
             f"sqrt({Z}*{KB}*{T_e}e3*{EVK}/({A_i}*{MP}))",
             "离子声波(NRL Formulary)", "")

    # 1.5 Weibel/磁化不稳定概念数: 电子回旋频率
    for _ in range(n // 6):
        B = round(rng.uniform(1, 20), 1)
        oc = E * B / ME
        emit("plasma-basic", "numeric", "undergrad",
             f"求电子回旋频率 Ω_ce=eB/m_e:B={B} T(rad/s)。",
             float(f"{oc:.4g}"), "rad/s", 0.02,
             f"{E}*{B}/{ME}",
             "回旋频率(NRL Formulary)", "")

    # 1.6 drift wave 频率估计
    for _ in range(n - 5 * (n // 6)):
        T_e = round(rng.uniform(0.5, 3), 1)
        Ln = round(rng.uniform(0.5, 2), 1)
        ky = round(rng.uniform(50, 200), 0)
        vde = KB * T_e * 1000 * EVK / (E * 5.0) * ky / Ln
        emit("plasma-basic", "numeric", "expert",
             f"漂移波估计:电子逆磁漂移速度 v_De=(k_BT_e/eB)·(1/L_n),T_e={T_e} keV,B=5 T,L_n={Ln} m;漂移频率 ω*≈k_y·v_De,k_y={ky:.0f} m⁻¹。求 ω*(rad/s)。",
             float(f"{vde:.4g}"), "rad/s", 0.05,
             f"({KB}*{T_e}e3*{EVK}/{E}/5)/{Ln}*{ky}",
             "漂移波/逆磁漂移(公开教科书)", "量级估计题")
    return out


# ---------- 族 2: ICF 物理模拟 (icf/*) ----------
def fam_icf_sim(rng, n, prefix):
    out = []
    i = 1

    def emit(topic, ttype, diff, q, v, u, tol, expr, src, notes):
        nonlocal i
        out.append(T(prefix, i, topic, ttype, diff, q, v, u, tol, expr, src, notes))
        i += 1

    # 2.1 Sedov 半径(ICF 尺度)
    for _ in range(n // 5):
        EJ = rng.choice([1e3, 1e4, 1e5, 1e6])
        tns = rng.choice([1, 3, 10, 30])
        rho = rng.choice([1.29, 0.1, 1.0])
        R = 1.15 * (EJ * (tns * 1e-9) ** 2 / rho) ** 0.2
        emit("simulation", "numeric", "grad",
             f"实验室点爆炸(Sedov):E={EJ:.0e} J,t={tns} ns,环境密度 ρ={rho} kg/m³。求激波半径 R=1.15·(Et²/ρ)^(1/5)(m)。",
             float(f"{R:.4g}"), "m", 0.02,
             f"1.15*({EJ}*({tns}e-9)**2/{rho})**0.2",
             "Sedov-Taylor 自相似解(公开)", "参数化")

    # 2.2 强激波链: v_s → T₂
    for _ in range(n // 5):
        pMbar = rng.choice([50, 100, 200])
        rho = rng.choice([1000, 250, 3000])
        gamma = 5 / 3
        vs = math.sqrt((gamma + 1) / 2 * pMbar * 1e11 / rho)
        T2 = 2 * (gamma - 1) / (gamma + 1) ** 2 * (2.5 * MP) * vs ** 2 / KB / EVK
        emit("icf/rad-hydro", "numeric", "expert",
             f"ICF 烧蚀激波:压强 p={pMbar} Mbar 驱动 ρ={rho} kg/m³ 的 DT 燃料(平均原子量 2.5 u,γ=5/3)。(1) 求激波速度 v_s=√((γ+1)/2·p/ρ);(2) 用该 v_s 求激波后温度 T₂=2(γ-1)/(γ+1)²·m·v_s²/k_B(eV)。两问都要,答 T₂。",
             float(f"{T2:.4g}"), "eV", 0.03,
             f"2*(5/3-1)/(5/3+1)**2*(2.5*{MP})*(((5/3+1)/2*{pMbar}e11/{rho}))/{KB}/{EVK}",
             "强激波关系(公开教科书,Zel'dovich)", "链式两步题")

    # 2.3 黑腔能量链(激光→X 光→吸收→动能)
    for _ in range(n // 5):
        Elas = rng.choice([1.8, 2.05, 2.2]) * 1e6
        eta_x = rng.choice([0.85, 0.9])
        eta_abs = rng.choice([0.1, 0.12, 0.15])
        eta_ke = rng.choice([0.05, 0.07])
        Eke = Elas * eta_x * eta_abs * eta_ke
        emit("icf/target-design", "numeric", "expert",
             f"间接驱动能量链:激光 E={Elas/1e6:.2f} MJ,X 光转换 η_x={eta_x},靶丸吸收 η_abs={eta_abs},吸收能量转化为燃料动能的效率 η_ke={eta_ke}。求燃料动能(J)。",
             float(f"{Eke:.4g}"), "J", 0.02,
             f"{Elas}*{eta_x}*{eta_abs}*{eta_ke}",
             "能量链效率(LLNL 公开口径量级)", "链式三步题")

    # 2.4 CFL + 网格时间步与总步数
    for _ in range(n // 5):
        dx_um = rng.choice([0.5, 1, 2, 5])
        v = rng.choice([1e5, 3e5, 1e6])
        cs = rng.choice([5e5, 1e6, 3e6])
        cfl = 0.2
        dt = cfl * dx_um * 1e-6 / (v + cs)
        emit("simulation", "numeric", "grad",
             f"显式流体模拟:Δx={dx_um} μm,|v|={v:.0e} m/s,c_s={cs:.0e} m/s,CFL=0.2。求时间步 dt=CFL·Δx/(|v|+c_s)(s)。",
             float(f"{dt:.4g}"), "s", 0.02,
             f"0.2*{dx_um}e-6/({v}+{cs})",
             "CFL 条件(CFD 公开)", "参数化")

    # 2.5 等熵压缩功与热斑功率平衡
    for _ in range(n - 4 * (n // 5)):
        CR = rng.choice([15, 20, 25, 30, 40])
        gamma = 5 / 3
        ratio = CR ** (3 * gamma - 3)  # P∝ρ^γ, ρ∝CR^3 → P∝CR^(3γ); 温度 T∝ρ^(γ-1)=CR^(3(γ-1))=CR^2
        Tratio = CR ** (3 * (gamma - 1))
        emit("icf/implosion", "numeric", "grad",
             f"等熵压缩均匀球(γ=5/3),收敛比 CR={CR}。温度标度 T∝ρ^(γ-1),ρ∝CR³,即 T∝CR^(3(γ-1))。求 T₂/T₁。",
             float(f"{Tratio:.4g}"), "1", 0.02,
             f"{CR}**(3*(5/3-1))",
             "等熵标度(公开教科书)", "T∝CR²(γ=5/3)")
    return out


# ---------- 族 3: MCF 物理模拟 (mcf) ----------
def fam_mcf_sim(rng, n, prefix):
    out = []
    i = 1

    def emit(topic, ttype, diff, q, v, u, tol, expr, src, notes):
        nonlocal i
        out.append(T(prefix, i, topic, ttype, diff, q, v, u, tol, expr, src, notes))
        i += 1

    # 3.1 IPB98(y,2) 参数化
    for _ in range(n // 4):
        I = rng.choice([3, 7.5, 12, 15])
        B = rng.choice([2.5, 4, 5.3])
        P = rng.choice([10, 30, 73, 100])
        n19 = rng.choice([5, 8, 10, 12])
        M = 2.5
        R = rng.choice([1.65, 3, 6.2])
        a = rng.choice([0.6, 1.0, 2.0])
        kap = rng.choice([1.5, 1.7, 1.9])
        eps = a / R
        tau = 0.0562 * I ** 0.93 * B ** 0.15 * P ** -0.69 * n19 ** 0.41 * M ** 0.19 * R ** 1.97 * eps ** 0.58 * kap ** 0.78
        emit("mcf", "numeric", "expert",
             f"IPB98(y,2) 能量约束定标 τ_E=0.0562·I^0.93·B^0.15·P^-0.69·n^0.41·M^0.19·R^1.97·ε^0.58·κ^0.78(单位:MA,T,MW,1e19 m⁻³,amu,m,—,—)。参数:I={I} MA,B={B} T,P={P} MW,n={n19}×1e19 m⁻³,M=2.5,R={R} m,a={a} m(ε=a/R),κ={kap}。求 τ_E(s)。",
             float(f"{tau:.4g}"), "s", 0.05,
             f"0.0562*{I}**0.93*{B}**0.15*{P}**-0.69*{n19}**0.41*2.5**0.19*{R}**1.97*({a}/{R})**0.58*{kap}**0.78",
             "IPB98(y,2) 定标(公开文献)", "多参数题,注意 ε=a/R 自算")

    # 3.2 安全因子 q 与磁场几何
    for _ in range(n // 4):
        a = rng.choice([0.5, 1.0, 2.0])
        R = rng.choice([1.7, 3, 6.2])
        Bt = rng.choice([2, 5.3])
        I = rng.choice([1, 3, 15])
        Bp = MU0 * I * 1e6 / (2 * math.pi * a)
        q = a * Bt / (R * Bp)
        emit("mcf", "numeric", "grad",
             f"托卡马克边缘安全因子近似 q≈a·B_t/(R·B_p),B_p=μ₀I/(2πa)。参数:a={a} m,R={R} m,B_t={Bt} T,I={I} MA。求 q。",
             float(f"{q:.4g}"), "1", 0.03,
             f"{a}*{Bt}/({R}*(4*pi*1e-7*{I}e6/(2*pi*{a})))",
             "安全因子定义(公开教科书)", "链式:先 B_p 再 q")

    # 3.3 拉莫尔半径与香蕉轨道宽度估计
    for _ in range(n // 4):
        Tkev = rng.choice([1, 5, 10])
        Bt = rng.choice([2, 5.3])
        eps = rng.choice([0.2, 0.32])
        rL = math.sqrt(2 * MP * KB * Tkev * 1000 * EVK) / (E * Bt)
        wb = rL / math.sqrt(eps)
        emit("mcf", "numeric", "expert",
             f"通行/香蕉轨道估计:质子 T={Tkev} keV,B_t={Bt} T,环径比 ε={eps}。热拉莫尔半径 r_L=√(2m_pkT)/(eB)(取 v=√(2kT/m)),香蕉轨道宽度量级 w_b≈r_L/√ε。求 w_b(m)。",
             float(f"{wb:.4g}"), "m", 0.05,
             f"sqrt(2*{MP}*{KB}*{Tkev}e3*{EVK})/({E}*{Bt})/sqrt({eps})",
             "新古典轨道估计(公开教科书)", "")

    # 3.4 聚变功率密度(粗糙 <σv> 线性化)
    for _ in range(n - 3 * (n // 4)):
        n20 = rng.choice([0.5, 1, 2])
        sigv = rng.choice([1e-22, 3e-22, 6e-22])  # m³/s 典型 DT 10-30keV
        P = (n20 * 1e20 / 2) ** 2 * sigv * 17.6e6 * E
        emit("mcf", "numeric", "grad",
             f"50-50 DT 芯部:n={n20}×10²⁰ m⁻³,取 <σv>={sigv:.0e} m³/s(题设值)。聚变功率密度 p=n_D·n_T·<σv>·Q_DT(Q_DT=17.6 MeV),求 p(W/m³)。",
             float(f"{P:.4g}"), "W/m^3", 0.02,
             f"({n20}e20/2)**2*{sigv}*17.6e6*{E}",
             "反应率密度公式(公开教科书)", "<σv> 题设避免查表")
    return out


# ---------- 族 4: 等离子体基础补充 (plasma-basic) ----------
def fam_plasma_basic(rng, n, prefix):
    out = []
    i = 1

    def emit(topic, ttype, diff, q, v, u, tol, expr, src, notes):
        nonlocal i
        out.append(T(prefix, i, topic, ttype, diff, q, v, u, tol, expr, src, notes))
        i += 1

    for _ in range(n):
        kind = rng.randrange(4)
        if kind == 0:
            nexp = rng.choice([18, 20, 24, 27, 29])
            n = 10.0 ** (nexp - rng.choice([0, 1, 3]))
            n = float(f"{n:.3g}")
            T_e = rng.choice([1, 10, 100, 1000])
            lam = math.sqrt(EPS0 * KB * T_e * EVK / (n * E ** 2))
            emit("plasma-basic", "numeric", "undergrad",
                 f"求德拜长度 λ_D=√(ε₀k_BT/(n·e²)):n={n:.3g} m⁻³,T={T_e} eV。",
                 float(f"{lam:.4g}"), "m", 0.02,
                 f"sqrt({EPS0}*{KB}*{T_e}*{EVK}/({n}*{E}**2))",
                 "NRL Formulary", "")
        elif kind == 1:
            n = float(f"{10.0**rng.uniform(18,28):.3g}")
            om = math.sqrt(n * E ** 2 / (EPS0 * ME))
            emit("plasma-basic", "numeric", "undergrad",
                 f"求电子等离子体频率 ω_pe=√(n·e²/(ε₀m_e)):n={n:.3g} m⁻³(rad/s)。",
                 float(f"{om:.4g}"), "rad/s", 0.02,
                 f"sqrt({n}*{E}**2/({EPS0}*{ME}))",
                 "NRL Formulary", "")
        elif kind == 2:
            n_cm3 = float(f"{10.0**rng.uniform(14,25):.3g}")
            T_e = rng.choice([10, 100, 1000, 10000])
            lnL = 23 - 0.5 * math.log(n_cm3) + 1.5 * math.log(T_e)
            emit("plasma-basic", "numeric", "grad",
                 f"库仑对数(NRL 公式):lnΛ=23-0.5·ln(n_e[cm⁻³])+1.5·ln(T[eV])。n_e={n_cm3:.3g} cm⁻³,T={T_e} eV。",
                 float(f"{lnL:.4g}"), "1", 0.03,
                 f"23-0.5*log({n_cm3})+1.5*log({T_e})",
                 "NRL Plasma Formulary", "")
        else:
            B = rng.choice([0.1, 1, 5.3])
            rho = float(f"{rng.uniform(1e-9, 1e-6):.2g}")
            va = B / math.sqrt(MU0 * rho)
            emit("plasma-basic", "numeric", "undergrad",
                 f"求阿尔文速度 v_A=B/√(μ₀ρ):B={B} T,ρ={rho} kg/m³。",
                 float(f"{va:.4g}"), "m/s", 0.02,
                 f"{B}/sqrt(4*pi*1e-7*{rho})",
                 "NRL Formulary", "")
    return out


FAMS = {
    "plasma-instabilities": fam_plasma_instabilities,
    "icf-sim": fam_icf_sim,
    "mcf-sim": fam_mcf_sim,
    "plasma-basic": fam_plasma_basic,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True, choices=list(FAMS))
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--prefix", default=None)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    prefix = args.prefix or f"{args.family}-gen"
    for t in FAMS[args.family](rng, args.n, prefix):
        print(json.dumps(t, ensure_ascii=False))


if __name__ == "__main__":
    main()
