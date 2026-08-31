import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.other_sources import OtherSourcesInput, create_other_sources_input


class TestCreateOtherSourcesInput(unittest.TestCase):
    # Normal case: accepts explicit other-source income fields.
    def test_create_other_sources_input_with_values(self):
        result = create_other_sources_input(5000, 10000, 2000, 0, 3000)

        self.assertEqual(result.interest_deposits, 10000)
        self.assertEqual(result.other_income, 3000)

    # Edge case: defaults should be zero.
    def test_create_other_sources_input_defaults(self):
        result = create_other_sources_input()

        self.assertEqual(result, OtherSourcesInput())

    # Expected behavior: immutable model.
    def test_other_sources_input_is_immutable(self):
        result = create_other_sources_input()

        with self.assertRaises(FrozenInstanceError):
            result.dividend_income = 1

    # Expected failure: unknown argument should raise TypeError.
    def test_other_sources_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_other_sources_input(invalid=1)


if __name__ == "__main__":
    unittest.main()
