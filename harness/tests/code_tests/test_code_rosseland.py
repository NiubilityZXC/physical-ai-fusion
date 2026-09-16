"""test for code-rosseland-0001: Rosseland mean via numerical integration.
The reference analytic result for kappa(nu)=C/nu^3 on [nu1,nu2]:
  1/kappa_R = ∫(1/kappa)(∂B/∂T)dν / ∫(∂B/∂T)dν
We test the student's numerical integration against a high-resolution
reference computed here by a different (fine-grid trapezoid) method.
"""
import math
import solution


def kappa(nu):
    return 1.0e3 / nu**3  # C=1000 arbitrary units


def weight(nu):
    # dB/dT weighting ~ nu^3 exp(-nu) shape for these tests (dimensionless proxy)
    return nu**3 * math.exp(-nu)


def reference(nu1, nu2, n=200000):
    h = (nu2 - nu1) / n
    num = 0.5 * (weight(nu1) / kappa(nu1) + weight(nu2) / kappa(nu2))
    den = 0.5 * (weight(nu1) + weight(nu2))
    for i in range(1, n):
        x = nu1 + i * h
        num += weight(x) / kappa(x)
        den += weight(x)
    num *= h
    den *= h
    return den / num


def main():
    for nu1, nu2 in [(0.5, 5.0), (1.0, 8.0), (0.2, 3.0)]:
        got = solution.rosseland_mean(kappa, weight, nu1, nu2)
        ref = reference(nu1, nu2)
        rel = abs(got - ref) / ref
        assert rel < 1e-3, f"[{nu1},{nu2}] got {got:.6g} ref {ref:.6g} rel {rel:.2e}"
    print("ALL PASS")


if __name__ == "__main__":
    main()
