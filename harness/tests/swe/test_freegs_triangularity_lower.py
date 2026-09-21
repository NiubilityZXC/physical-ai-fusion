"""FAIL_TO_PASS test for FreeGS issue #128 (triangularityLower).

Physics: lower triangularity delta_lower = (R0 - R_P4)/a where R_P4 is the R
coordinate of the BOTTOM (minimum-Z) point of the LCFS. The buggy
implementation used argmax(Zlcfs) (the TOP point). This test recomputes the
expected value from the equilibrium's own separatrix and geometric quantities
but with the independently-correct argmin selection, so it passes on fixed
code and fails on the argmax bug.
"""
import numpy as np


def _shaped_equilibrium():
    """Shaped free-boundary equilibrium with two X-points (fast, 65x65)."""
    import freegs
    tokamak = freegs.machine.TestTokamak()
    eq = freegs.Equilibrium(tokamak=tokamak,
                            Rmin=0.1, Rmax=2.0,
                            Zmin=-1.0, Zmax=1.0,
                            nx=65, ny=65,
                            boundary=freegs.boundary.freeBoundaryHagenow)
    profiles = freegs.jtor.ConstrainPaxisIp(eq, 1e3, 2e5, 2.0)
    xpoints = [(1.1, -0.6), (1.1, 0.8)]
    isoflux = [(1.1, -0.6, 1.1, 0.6)]
    constrain = freegs.control.constrain(xpoints=xpoints, isoflux=isoflux)
    freegs.solve(eq, profiles, constrain, show=False)
    return eq


def test_triangularity_lower_uses_bottom_point():
    eq = _shaped_equilibrium()
    sep = eq.separatrix(npoints=360)          # array [:,2] along the LCFS
    Rlcfs = np.asarray(sep[:, 0], dtype=float)
    Zlcfs = np.asarray(sep[:, 1], dtype=float)
    R0 = eq.Rgeometric(npoints=360)
    a = eq.minorRadius(npoints=360)
    expected = (R0 - Rlcfs[np.argmin(Zlcfs)]) / a          # correct: BOTTOM
    buggy = (R0 - Rlcfs[np.argmax(Zlcfs)]) / a             # issue #128: TOP
    assert abs(expected - buggy) > 0.02, (
        f"test equilibrium is not discriminating enough: lower={expected:.4f}, top-form={buggy:.4f}")
    got = eq.triangularityLower()
    assert abs(got - expected) < 1e-9, (
        f"triangularityLower()={got:.6f} != argmin-derived {expected:.6f} "
        f"(issue #128: bottom point must use argmin(Zlcfs), not argmax)")
