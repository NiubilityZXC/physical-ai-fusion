"""test for code-saha-0001: two-level Saha ionized fraction for hydrogen.
Reference computed here by direct quadratic solve:
  n_{i+1} n_e / n_i = K, quasi-neutral n_e = n_{i+1}, total n = n_i + n_{i+1}
  => x = n_{i+1}/n = (-K + sqrt(K^2 + 4 K n)) / (2 n)
"""
import math
import solution

H = 6.62607015e-34
ME = 9.1093837015e-31
KB = 1.380649e-23
EVK = 11604.525


def reference(T_eV, n_total, chi=13.6):
    T = T_eV * EVK
    lam = H / math.sqrt(2 * math.pi * ME * KB * T)
    K = (2.0 / lam**3) * math.exp(-chi / T_eV)
    return (-K + math.sqrt(K * K + 4 * K * n_total)) / (2 * n_total)


def main():
    for T_eV, n in [(1.0, 1e22), (2.0, 1e22), (3.0, 1e28), (5.0, 1e26), (10.0, 1e20)]:
        got = solution.saha_ionized_fraction(T_eV, n, 13.6)
        ref = reference(T_eV, n)
        assert abs(got - ref) / max(ref, 1e-30) < 1e-3, (
            f"T={T_eV} n={n}: got {got:.6g} ref {ref:.6g}")
    print("ALL PASS")


if __name__ == "__main__":
    main()
