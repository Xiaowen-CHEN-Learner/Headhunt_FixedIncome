"""Independent identities and numerical checks, not market-data validation."""
import csv
import io
import math
import unittest
from pathlib import Path
from bond_demo import bond_metrics, write_scenarios


class BondTests(unittest.TestCase):
    def test_par_bond(self):
        self.assertAlmostEqual(bond_metrics(100, .05, .05, 5).price, 100)

    def test_zero_coupon(self):
        self.assertAlmostEqual(bond_metrics(100, 0, .04, 5).price, 100 / 1.02 ** 10)

    def test_zero_yield(self):
        self.assertAlmostEqual(bond_metrics(100, .05, 0, 5).price, 125)

    def test_price_decreases_with_yield(self):
        self.assertGreater(bond_metrics(100, .05, .04, 5).price,
                           bond_metrics(100, .05, .06, 5).price)

    def test_face_value_scaling(self):
        a, b = bond_metrics(100, .05, .04, 5), bond_metrics(1000, .05, .04, 5)
        self.assertAlmostEqual(b.price, 10 * a.price)
        self.assertAlmostEqual(a.modified_duration, b.modified_duration)

    def test_zero_coupon_duration(self):
        m = bond_metrics(100, 0, .04, 5)
        self.assertAlmostEqual(m.macaulay_duration, 5)
        self.assertAlmostEqual(m.modified_duration, 5 / 1.02)

    def test_duration_matches_price_derivative(self):
        m, h = bond_metrics(100, .05, .05, 5), 1e-5
        p0 = bond_metrics(100, .05, .05 - h, 5).price
        p1 = bond_metrics(100, .05, .05 + h, 5).price
        self.assertAlmostEqual(m.modified_duration, -(p1 - p0) / (2 * h * m.price), places=6)

    def test_convexity_matches_second_derivative(self):
        m, h = bond_metrics(100, .05, .05, 5), 1e-4
        p0 = bond_metrics(100, .05, .05 - h, 5).price
        p1 = bond_metrics(100, .05, .05 + h, 5).price
        self.assertAlmostEqual(m.convexity, (p1 - 2 * m.price + p0) / (h * h * m.price), places=4)

    def test_negative_yield_supported(self):
        self.assertGreater(bond_metrics(100, 0, -.01, 5).price, 100)

    def test_bad_frequency(self):
        for frequency in (0, 3, True, 2.0):
            with self.subTest(frequency=frequency), self.assertRaises(ValueError):
                bond_metrics(100, .05, .05, 5, frequency)

    def test_off_coupon_date_rejected(self):
        with self.assertRaises(ValueError):
            bond_metrics(100, .05, .05, 5.1)

    def test_bad_financial_inputs(self):
        for inputs in ((0, .05, .05, 5), (100, -.01, .05, 5),
                       (100, .05, -2, 5), (100, .05, .05, 0)):
            with self.subTest(inputs=inputs), self.assertRaises(ValueError):
                bond_metrics(*inputs)

    def test_nonfinite_inputs(self):
        for val in (math.nan, math.inf, -math.inf):
            with self.subTest(val=val), self.assertRaises(ValueError):
                bond_metrics(100, .05, val, 5)

    def test_expected_csv(self):
        out = io.StringIO()
        write_scenarios(out)
        expected = Path(__file__).resolve().parents[1] / "examples" / "expected_scenarios.csv"
        self.assertEqual(out.getvalue(), expected.read_text(encoding="utf-8"))

    def test_scenario_baseline(self):
        out = io.StringIO()
        write_scenarios(out)
        rows = list(csv.DictReader(io.StringIO(out.getvalue())))
        self.assertEqual(len(rows), 5)
        self.assertEqual(float(rows[2]["exact_change_pct"]), 0)
        self.assertEqual(float(rows[2]["price_per_100"]), 100)


if __name__ == "__main__":
    unittest.main()
