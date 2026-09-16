"""test for code-limits-0001: Troyon beta and Greenwald density limits."""
import math
import solution


def main():
    iter_params = {"I": 15.0, "a": 2.0, "B": 5.3}
    beta = solution.troyon_beta_max(iter_params, beta_N=2.8)
    assert abs(beta - 2.8 * 15.0 / (2.0 * 5.3)) / (2.8 * 15.0 / (2.0 * 5.3)) < 1e-9
    nG = solution.greenwald_density(iter_params)
    assert abs(nG - 15.0 / (math.pi * 4.0)) / (15.0 / (math.pi * 4.0)) < 1e-9
    print("ALL PASS")


if __name__ == "__main__":
    main()
