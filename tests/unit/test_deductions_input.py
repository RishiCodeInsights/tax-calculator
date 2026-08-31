import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.deductions import DeductionsInput, create_deductions_input


class TestCreateDeductionsInput(unittest.TestCase):
    # Normal case: maps deduction values correctly.
    def test_create_deductions_input_with_values(self):
        result = create_deductions_input(
            deduction_80c=150000,
            deduction_80ccd_1b=50000,
            deduction_80d_self_family=25000,
            deduction_80d_parents=50000,
            deduction_80e=10000,
            deduction_80g=15000,
            deduction_80tta=10000,
            deduction_80ttb=0,
            deduction_24b_self_occupied_interest=200000,
            family_pension_deduction=15000,
        )

        self.assertEqual(result.deduction_80c, 150000)
        self.assertEqual(result.deduction_24b_self_occupied_interest, 200000)

    # Edge case: omitted inputs fall back to zeros.
    def test_create_deductions_input_defaults(self):
        result = create_deductions_input()

        self.assertEqual(result, DeductionsInput())

    # Expected behavior: immutable model.
    def test_deductions_input_is_immutable(self):
        result = create_deductions_input()

        with self.assertRaises(FrozenInstanceError):
            result.deduction_80g = 1

    # Expected failure: unknown argument should raise TypeError.
    def test_deductions_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_deductions_input(invalid=1)


if __name__ == "__main__":
    unittest.main()
