import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input import (
    create_capital_gains_input,
    create_house_property_input,
    create_salary_input,
    create_top_level_input,
    create_unified_tax_input,
)
from tax_calculator.input.unified_request import UnifiedTaxInput


class TestCreateUnifiedTaxInput(unittest.TestCase):
    # Normal case: combines explicit section models into unified request.
    def test_create_unified_tax_input_with_explicit_sections(self):
        top_level = create_top_level_input("2024-25", 35, "resident", "new")
        salary = create_salary_input(salary_gross=1000000)
        house_property = create_house_property_input(gross_annual_value=300000)
        capital_gains = create_capital_gains_input(stcg_111a=20000)

        result = create_unified_tax_input(
            top_level=top_level,
            salary=salary,
            house_property=house_property,
            capital_gains=capital_gains,
        )

        self.assertIsInstance(result, UnifiedTaxInput)
        self.assertEqual(result.salary.salary_gross, 1000000)
        self.assertEqual(result.house_property.gross_annual_value, 300000)
        self.assertEqual(result.capital_gains.stcg_111a, 20000)

    # Edge case: missing optional sections should default to zeroed models.
    def test_create_unified_tax_input_defaults_optional_sections(self):
        top_level = create_top_level_input("2024-25", 30, "resident", "new")
        result = create_unified_tax_input(top_level=top_level)

        self.assertEqual(result.salary.salary_gross, 0.0)
        self.assertEqual(result.deductions.deduction_80c, 0.0)
        self.assertEqual(result.tax_credits.tds, 0.0)

    # Expected behavior: unified dataclass should be immutable.
    def test_unified_tax_input_is_immutable(self):
        top_level = create_top_level_input("2024-25", 30, "resident", "new")
        result = create_unified_tax_input(top_level=top_level)

        with self.assertRaises(FrozenInstanceError):
            result.salary = create_salary_input()

    # Expected failure: top-level section is required.
    def test_missing_top_level_raises_type_error(self):
        with self.assertRaises(TypeError):
            create_unified_tax_input()

    # Expected failure: unknown argument should raise TypeError.
    def test_unified_input_unexpected_arg_fails(self):
        top_level = create_top_level_input("2024-25", 30, "resident", "new")
        with self.assertRaises(TypeError):
            create_unified_tax_input(top_level=top_level, invalid=True)


if __name__ == "__main__":
    unittest.main()
