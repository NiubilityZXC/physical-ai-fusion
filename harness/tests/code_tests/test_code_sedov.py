"""test for code-sedov-0001: Sedov-Taylor radius time series."""
import solution


def main():
    cases = [
        (1e6, 1.29, 1.15, [1e-9, 1e-8, 1e-7], [4.3522e-3, 1.0932e-2, 2.7464e-2]),
        (1e14, 1.29, 1.15, [1e-5, 1e-4], [6.893, 17.315]),
    ]
    for E, rho, beta, ts, expected in cases:
        got = solution.sedov_radius(E, ts, rho, beta)
        assert len(got) == len(expected), "length mismatch"
        for g, e in zip(got, expected):
            assert abs(g - e) / e < 2e-3, f"E={E} t: got {g:.6g} expected {e:.6g}"
    print("ALL PASS")


if __name__ == "__main__":
    main()
