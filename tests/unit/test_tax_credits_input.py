import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.tax_credits import TaxCreditsInput, create_tax_credits_input


class TestCreateTaxCreditsInput(unittest.TestCase):
    # Normal case: explicit tax paid/credit fields are preserved.
    def test_create_tax_credits_input_with_values(self):
        result = create_tax_credits_input(tds=12000, tcs=3000, advance_tax=10000, self_assessment_tax=5000)

        self.assertEqual(result.tds, 12000)
        self.assertEqual(result.self_assessment_tax, 5000)

    # Edge case: defaults represent no tax paid yet.
    def test_create_tax_credits_input_defaults(self):
        result = create_tax_credits_input()

        self.assertEqual(result, TaxCreditsInput())

    # Expected behavior: immutable model.
    def test_tax_credits_input_is_immutable(self):
        result = create_tax_credits_input()

        with self.assertRaises(FrozenInstanceError):
            result.tcs = 1

    # Expected failure: unknown argument should raise TypeError.
    def test_tax_credits_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_tax_credits_input(invalid=1)


if __name__ == "__main__":
    unittest.main()
