import unittest

from tax_calculator.engine.calculator import calculate_tax


class TestCalculateTax(unittest.TestCase):
    """Unit tests for slab-based tax computation."""

    # Normal case: zero income should produce zero tax.
    def test_zero_income(self):
        self.assertEqual(calculate_tax(0), 0.0)

    # Edge case: boundary of first slab remains untaxed.
    def test_first_slab_upper_boundary(self):
        self.assertEqual(calculate_tax(300000), 0.0)

    # Edge case: smallest taxable amount in second slab.
    def test_just_above_first_slab(self):
        self.assertEqual(calculate_tax(300001), 0.05)

    # Normal case: income spanning multiple slabs.
    def test_mid_bracket_income(self):
        self.assertEqual(calculate_tax(750000), 30000.0)

    # Edge case: exact upper boundary before 30% slab.
    def test_upper_standard_slab_boundary(self):
        self.assertEqual(calculate_tax(1500000), 150000.0)

    # Normal case: amount spilling into top slab.
    def test_above_highest_slab(self):
        self.assertEqual(calculate_tax(1600000), 180000.0)

    # Edge case: decimal income should still compute correctly.
    def test_fractional_income(self):
        self.assertAlmostEqual(calculate_tax(300000.5), 0.025)

    # Expected failure path: negative income is rejected.
    def test_negative_income_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_tax(-1)

    # Expected failure path: non-numeric values are invalid.
    def test_non_numeric_income_raises_type_error(self):
        with self.assertRaises(TypeError):
            calculate_tax("500000")


if __name__ == "__main__":
    unittest.main()
