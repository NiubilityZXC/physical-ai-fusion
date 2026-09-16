"""Reference solutions for the 8 code tasks (self-test: all must pass their tests)."""

# code-rosseland-0001
def rosseland_mean(kappa, weight, nu1, nu2, n=20000):
    h = (nu2 - nu1) / n
    num = den = 0.0
    for i in range(n + 1):
        x = nu1 + i * h
        w = weight(x) / kappa(x)
        d = weight(x)
        f = 0.5 if i in (0, n) else 1.0
        num += f * w
        den += f * d
    num *= h
    den *= h
    return den / num


# code-saha-0001
def saha_ionized_fraction(T_eV, n_total, chi):
    import math
    H = 6.62607015e-34
    ME = 9.1093837015e-31
    KB = 1.380649e-23
    T = T_eV * 11604.525
    lam = H / math.sqrt(2 * math.pi * ME * KB * T)
    K = (2.0 / lam**3) * math.exp(-chi / T_eV)
    return (-K + math.sqrt(K * K + 4 * K * n_total)) / (2 * n_total)


# code-sedov-0001
def sedov_radius(E, ts, rho, beta=1.15):
    return [beta * (E * t * t / rho) ** 0.2 for t in ts]


# code-rt-scan-0001
def rt_growth(k, A, g, L, Va, alpha=0.9, beta=3.1):
    import math
    return alpha * math.sqrt(A * k * g / (1 + A * k * L)) - beta * k * Va


def stabilization_wavenumber(A, g, L, Va, alpha=0.9, beta=3.1):
    import math
    # 解析求根: alpha*sqrt(A*k*g/(1+A*k*L)) = beta*k*Va
    # => alpha^2 A k g / (1 + A k L) = beta^2 k^2 Va^2
    # => alpha^2 A g = beta^2 Va^2 k (1 + A k L)
    # => A L k^2 + k - alpha^2 A g / (beta^2 Va^2) = 0
    a = A * L
    b = 1.0
    c = -(alpha * alpha * A * g) / (beta * beta * Va * Va)
    disc = math.sqrt(b * b - 4 * a * c)
    return (-b + disc) / (2 * a)


# code-nrl-calc-0001
def nrl_bundle(n, T_eV, B, species="e"):
    import math
    E = 1.602176634e-19
    KB = 1.380649e-23
    ME = 9.1093837015e-31
    MP = 1.67262192369e-27
    EPS0 = 8.8541878128e-12
    T = T_eV * 11604.525
    wpe = math.sqrt(n * E * E / (EPS0 * ME))
    ld = math.sqrt(EPS0 * KB * T / (n * E * E))
    m = ME if species == "e" else MP
    rl = math.sqrt(m * KB * T) / (E * B)
    return wpe, ld, rl


# code-evbatch-0001
def kinetic_energies(pairs):
    return [0.5e-3 * m * v * v / 1e13 for m, v in pairs]


def velocity_from_energy(m, E):
    import math
    return math.sqrt(2e16 * E / m)


# code-freepath-0001
def log_interp(x1, y1, x2, y2, x):
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


# code-limits-0001
def troyon_beta_max(params, beta_N=2.8):
    return beta_N * params["I"] / (params["a"] * params["B"])


def greenwald_density(params):
    import math
    return params["I"] / (math.pi * params["a"] ** 2)
