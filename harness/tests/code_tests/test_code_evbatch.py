"""test for code-evbatch-0001: batch (m,v) -> E conversion (cgs)."""
import math
import solution


def main():
    pairs = [(20.0, 1.7894e7), (30.0, 2.0e7), (2.05, 1.7398e8), (40.0, 3.1124e7)]
    got = solution.kinetic_energies(pairs)
    assert len(got) == len(pairs)
    for g, (m, v) in zip(got, pairs):
        e = 0.5e-3 * m * v * v / 1e13
        assert abs(g - e) / e < 1e-9, f"m={m} v={v}: got {g:.6g} ref {e:.6g}"
    # inverse direction
    v0 = solution.velocity_from_energy(20.0, got[0])
    assert abs(v0 - pairs[0][1]) / pairs[0][1] < 1e-6
    print("ALL PASS")


if __name__ == "__main__":
    main()
