from dataclasses import dataclass


@dataclass(frozen=True)
class LossCarryForwardInput:
    """Optional brought-forward loss fields for set-off flow."""

    brought_forward_house_property_loss: float = 0.0
    brought_forward_business_loss: float = 0.0
    brought_forward_capital_loss_st: float = 0.0
    brought_forward_capital_loss_lt: float = 0.0
    unabsorbed_depreciation: float = 0.0


def create_loss_carry_forward_input(
    brought_forward_house_property_loss: float = 0.0,
    brought_forward_business_loss: float = 0.0,
    brought_forward_capital_loss_st: float = 0.0,
    brought_forward_capital_loss_lt: float = 0.0,
    unabsorbed_depreciation: float = 0.0,
) -> LossCarryForwardInput:
    """Build and return typed loss carry-forward input data."""

    return LossCarryForwardInput(
        brought_forward_house_property_loss=brought_forward_house_property_loss,
        brought_forward_business_loss=brought_forward_business_loss,
        brought_forward_capital_loss_st=brought_forward_capital_loss_st,
        brought_forward_capital_loss_lt=brought_forward_capital_loss_lt,
        unabsorbed_depreciation=unabsorbed_depreciation,
    )
