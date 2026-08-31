import unittest
from dataclasses import FrozenInstanceError

from tax_calculator.input.losses import LossCarryForwardInput, create_loss_carry_forward_input


class TestCreateLossCarryForwardInput(unittest.TestCase):
    # Normal case: explicit loss carry-forward fields are captured.
    def test_create_loss_carry_forward_input_with_values(self):
        result = create_loss_carry_forward_input(
            brought_forward_house_property_loss=50000,
            brought_forward_business_loss=25000,
            brought_forward_capital_loss_st=15000,
            brought_forward_capital_loss_lt=7000,
            unabsorbed_depreciation=8000,
        )

        self.assertEqual(result.brought_forward_business_loss, 25000)
        self.assertEqual(result.unabsorbed_depreciation, 8000)

    # Edge case: defaults should all be zero.
    def test_create_loss_carry_forward_input_defaults(self):
        result = create_loss_carry_forward_input()

        self.assertEqual(result, LossCarryForwardInput())

    # Expected behavior: immutable model.
    def test_loss_carry_forward_input_is_immutable(self):
        result = create_loss_carry_forward_input()

        with self.assertRaises(FrozenInstanceError):
            result.brought_forward_capital_loss_st = 1

    # Expected failure: unknown argument should raise TypeError.
    def test_losses_unexpected_arg_fails(self):
        with self.assertRaises(TypeError):
            create_loss_carry_forward_input(invalid=1)


if __name__ == "__main__":
    unittest.main()
