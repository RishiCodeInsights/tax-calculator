import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.house_property import HousePropertyInput, create_house_property_input


class TestCreateHousePropertyInput(unittest.TestCase):
    # Normal case: explicit house-property values are captured.
    def test_create_house_property_input_with_values(self):
        result = create_house_property_input(
            house_property_type="let_out",
            gross_annual_value=500000,
            municipal_taxes_paid=10000,
            interest_on_housing_loan=200000,
            unrealized_rent=5000,
            arrears_of_rent=3000,
        )

        self.assertEqual(result.house_property_type, "let_out")
        self.assertEqual(result.gross_annual_value, 500000)

    # Edge case: defaults represent zeroed optional fields.
    def test_create_house_property_input_defaults(self):
        result = create_house_property_input()

        self.assertEqual(result, HousePropertyInput())

    # Expected behavior: instance is immutable.
    def test_house_property_input_is_immutable(self):
        result = create_house_property_input()

        with self.assertRaises(FrozenInstanceError):
            result.gross_annual_value = 1

    # Expected failure: unknown argument should raise TypeError.
    def test_house_property_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_house_property_input(unexpected=1)


if __name__ == "__main__":
    unittest.main()
