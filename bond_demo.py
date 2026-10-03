"""Offline fixed-rate bond example. Synthetic inputs; not a trading tool.

Assumes valuation exactly on a coupon date, level coupons, nominal annual
YTM compounded at the coupon frequency, and principal repayment at maturity.
No accrued interest, default, calls, taxes, fees, or market-data services.
AI-assisted portfolio example, added 2026-10-03.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO


@dataclass(frozen=True)
class BondMetrics:
    price: float
    macaulay_duration: float
    modified_duration: float
    convexity: float


def bond_metrics(par: float, coupon: float, ytm: float, years: float,
                 frequency: int = 2) -> BondMetrics:
    """Return price, durations (years), and convexity (years squared).

    Rates are decimals, e.g. 0.05, not 5. Only whole coupon periods are
    supported; this deliberately does not approximate settlement conventions.
    """
    if isinstance(frequency, bool) or frequency not in (1, 2, 4, 12):
        raise ValueError("frequency must be 1, 2, 4, or 12")
    if not isinstance(frequency, int):
        raise ValueError("frequency must be an integer")
    if not all(math.isfinite(x) for x in (par, coupon, ytm, years)):
        raise ValueError("all inputs must be finite")
    if par <= 0 or years <= 0 or coupon < 0 or 1 + ytm / frequency <= 0:
        raise ValueError("invalid par, maturity, coupon, or discount factor")
    periods = round(years * frequency)
    if periods < 1 or periods > 1200 or not math.isclose(
            periods, years * frequency, abs_tol=1e-9, rel_tol=0):
        raise ValueError("maturity must span 1 to 1200 whole coupon periods")
    base = 1 + ytm / frequency
    coupon_cash = par * coupon / frequency
    cashflows = [(k, coupon_cash + (par if k == periods else 0))
                 for k in range(1, periods + 1)]
    try:
        discounted = [(k, cash / base ** k) for k, cash in cashflows]
        price = math.fsum(pv for _, pv in discounted)
        macaulay = math.fsum(k / frequency * pv for k, pv in discounted) / price
        modified = macaulay / base
        convexity = math.fsum(k * (k + 1) / frequency ** 2 * pv
                             for k, pv in discounted) / (price * base ** 2)
    except (OverflowError, ZeroDivisionError) as exc:
        raise ValueError("inputs exceed numerical range") from exc
    if price <= 0 or not all(math.isfinite(x) for x in
                            (price, macaulay, modified, convexity)):
        raise ValueError("inputs exceed numerical range")
    return BondMetrics(price, macaulay, modified, convexity)


def write_scenarios(out: TextIO, coupon: float = 0.05,
                    ytm: float = 0.05, years: float = 5,
                    frequency: int = 2) -> None:
    """Write deterministic repricing results per 100 face value."""
    baseline = bond_metrics(100, coupon, ytm, years, frequency)
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(["shock_bps", "yield_pct", "price_per_100",
                     "exact_change_pct", "duration_approx_pct"])
    for bps in (-100, -50, 0, 50, 100):
        dy = bps / 10000
        price = bond_metrics(100, coupon, ytm + dy, years, frequency).price
        writer.writerow([bps, f"{(ytm + dy) * 100:.4f}", f"{price:.6f}",
                         f"{(price / baseline.price - 1) * 100:.6f}",
                         f"{-baseline.modified_duration * dy * 100:.6f}"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coupon", type=float, default=0.05, help="decimal annual coupon")
    parser.add_argument("--yield-rate", type=float, default=0.05, help="decimal annual YTM")
    parser.add_argument("--years", type=float, default=5)
    parser.add_argument("--frequency", type=int, default=2, choices=(1, 2, 4, 12))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        # Validate every scenario before opening or replacing an output file.
        for shock in (-0.01, -0.005, 0, 0.005, 0.01):
            bond_metrics(100, args.coupon, args.yield_rate + shock, args.years, args.frequency)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("w", encoding="utf-8", newline="") as out:
                write_scenarios(out, args.coupon, args.yield_rate, args.years, args.frequency)
        else:
            write_scenarios(sys.stdout, args.coupon, args.yield_rate, args.years, args.frequency)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
