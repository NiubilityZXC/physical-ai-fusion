"""test for code-freepath-0001: log-space linear interpolation."""
import solution


def main():
    pts = [(1.755, 0.320513), (1.921, 0.703219)]
    x = (1.755 + 1.921) / 2
    got = solution.log_interp(pts[0][0], pts[0][1], pts[1][0], pts[1][1], x)
    exp = (0.320513 + 0.703219) / 2
    assert abs(got - exp) < 1e-9, f"got {got} expected {exp}"
    got2 = solution.log_interp(0.0, 1.0, 4.0, 3.0, 1.0)
    assert abs(got2 - 1.5) < 1e-9
    print("ALL PASS")


if __name__ == "__main__":
    main()
