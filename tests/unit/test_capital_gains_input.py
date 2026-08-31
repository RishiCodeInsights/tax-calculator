import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.capital_gains import CapitalGainsInput, create_capital_gains_input


class TestCreateCapitalGainsInput(unittest.TestCase):
    # Normal case: accepts explicit capital gains buckets.
    def test_create_capital_gains_input_with_values(self):
        result = create_capital_gains_input(10000, 20000, 30000, 40000)

        self.assertEqual(result.stcg_111a, 10000)
        self.assertEqual(result.ltcg_112, 40000)

    # Edge case: all values default to zero.
    def test_create_capital_gains_input_defaults(self):
        result = create_capital_gains_input()

        self.assertEqual(result, CapitalGainsInput())

    # Expected behavior: immutable model.
    def test_capital_gains_input_is_immutable(self):
        result = create_capital_gains_input()

        with self.assertRaises(FrozenInstanceError):
            result.stcg_other = 1

    # Expected failure: unknown argument should raise TypeError.
    def test_capital_gains_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_capital_gains_input(invalid=1)


if __name__ == "__main__":
    unittest.main()
