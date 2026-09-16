"""test for code-nrl-calc-0001: NRL formulary bundle."""
import math
import solution

E = 1.602176634e-19
KB = 1.380649e-23
ME = 9.1093837015e-31
MP = 1.67262192369e-27
EPS0 = 8.8541878128e-12
EVK = 11604.525


def main():
    n, T_eV, B = 1e20, 1000.0, 5.0
    wpe, ld, rl = solution.nrl_bundle(n, T_eV, B, species="p")
    assert abs(wpe - math.sqrt(n * E**2 / (EPS0 * ME))) < 1e6
    assert abs(ld - math.sqrt(EPS0 * KB * T_eV * EVK / (n * E**2))) / math.sqrt(EPS0 * KB * T_eV * EVK / (n * E**2)) < 1e-6
    assert abs(rl - math.sqrt(MP * KB * T_eV * EVK) / (E * B)) / (math.sqrt(MP * KB * T_eV * EVK) / (E * B)) < 1e-6
    print("ALL PASS")


if __name__ == "__main__":
    main()
