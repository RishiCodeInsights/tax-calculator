import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.salary import SalaryInput, create_salary_input


class TestCreateSalaryInput(unittest.TestCase):
    # Normal case: all explicit values are accepted and mapped.
    def test_create_salary_input_with_values(self):
        result = create_salary_input(
            salary_gross=1200000,
            salary_exempt_allowances_total=150000,
            professional_tax=2400,
            hra_received=180000,
            rent_paid=240000,
            is_metro_city=True,
            employer_nps_contribution=50000,
        )

        self.assertEqual(result.salary_gross, 1200000)
        self.assertEqual(result.rent_paid, 240000)
        self.assertTrue(result.is_metro_city)

    # Edge case: defaults should be zero/False when omitted.
    def test_create_salary_input_defaults(self):
        result = create_salary_input()

        self.assertEqual(result, SalaryInput())

    # Expected behavior: frozen dataclass blocks mutation.
    def test_salary_input_is_immutable(self):
        result = create_salary_input(salary_gross=1)

        with self.assertRaises(FrozenInstanceError):
            result.salary_gross = 2

    # Expected failure: unknown argument should raise TypeError.
    def test_salary_input_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_salary_input(unknown_field=1)


if __name__ == "__main__":
    unittest.main()
