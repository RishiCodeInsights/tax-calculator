import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.top_level import TopLevelInput, create_top_level_input


class TestCreateTopLevelInput(unittest.TestCase):
    """Unit tests for top-level input object creation."""

    # Normal case: valid resident profile under new regime.
    def test_create_top_level_input_normal_case(self):
        result = create_top_level_input(
            tax_year="2024-25",
            age=30,
            residential_status="resident",
            regime="new",
        )

        self.assertIsInstance(result, TopLevelInput)
        self.assertEqual(result.tax_year, "2024-25")
        self.assertEqual(result.age, 30)
        self.assertEqual(result.residential_status, "resident")
        self.assertEqual(result.regime, "new")

    # Normal case: accepts another valid combination.
    def test_create_top_level_input_old_regime_non_resident(self):
        result = create_top_level_input(
            tax_year="2025-26",
            age=45,
            residential_status="non_resident",
            regime="old",
        )

        self.assertEqual(
            result,
            TopLevelInput(
                tax_year="2025-26",
                age=45,
                residential_status="non_resident",
                regime="old",
            ),
        )

    # Edge case: zero age currently passes through (validation is separate layer).
    def test_create_top_level_input_edge_zero_age(self):
        result = create_top_level_input(
            tax_year="2024-25",
            age=0,
            residential_status="resident",
            regime="new",
        )

        self.assertEqual(result.age, 0)

    # Edge case: empty tax year currently passes through (validation is separate layer).
    def test_create_top_level_input_edge_empty_tax_year(self):
        result = create_top_level_input(
            tax_year="",
            age=25,
            residential_status="resident",
            regime="new",
        )

        self.assertEqual(result.tax_year, "")

    # Expected behavior check: model is frozen and cannot be mutated.
    def test_created_model_is_immutable(self):
        result = create_top_level_input(
            tax_year="2024-25",
            age=28,
            residential_status="resident",
            regime="new",
        )

        with self.assertRaises(FrozenInstanceError):
            result.age = 29

    # Expected failure: required argument omission should raise TypeError.
    def test_missing_required_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            create_top_level_input(
                tax_year="2024-25",
                age=30,
                residential_status="resident",
            )

    # Expected failure: unexpected keyword should raise TypeError.
    def test_unexpected_keyword_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            create_top_level_input(
                tax_year="2024-25",
                age=30,
                residential_status="resident",
                regime="new",
                invalid_field=True,
            )


if __name__ == "__main__":
    unittest.main()
