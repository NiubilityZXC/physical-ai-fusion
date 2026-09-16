"""test for code-rt-scan-0001: Takabe growth rate + stabilization boundary."""
import math
import solution


def takabe(k, A, g, L, Va, alpha=0.9, beta=3.1):
    return alpha * math.sqrt(A * k * g / (1 + A * k * L)) - beta * k * Va


def main():
    params = dict(A=1.0, g=1e14, L=1e-5, Va=1e3)
    for k in (5e4, 1e5, 1.2566e5, 2e5):
        got = solution.rt_growth(k, **params)
        ref = takabe(k, **params)
        assert abs(got - ref) / max(abs(ref), 1) < 1e-6, f"k={k}: got {got:.6g} ref {ref:.6g}"
    root = solution.stabilization_wavenumber(**params)
    assert abs(takabe(root, **params)) / takabe(1e3, **params) < 1e-6, (
        f"root {root:.6g} does not zero the growth rate")
    print("ALL PASS")


if __name__ == "__main__":
    main()
