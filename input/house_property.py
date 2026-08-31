from dataclasses import dataclass
from typing import Literal


HousePropertyType = Literal["self_occupied", "let_out"]


@dataclass(frozen=True)
class HousePropertyInput:
    """House property related fields for tax calculation."""

    house_property_type: HousePropertyType = "self_occupied"
    gross_annual_value: float = 0.0
    municipal_taxes_paid: float = 0.0
    interest_on_housing_loan: float = 0.0
    unrealized_rent: float = 0.0
    arrears_of_rent: float = 0.0


def create_house_property_input(
    house_property_type: HousePropertyType = "self_occupied",
    gross_annual_value: float = 0.0,
    municipal_taxes_paid: float = 0.0,
    interest_on_housing_loan: float = 0.0,
    unrealized_rent: float = 0.0,
    arrears_of_rent: float = 0.0,
) -> HousePropertyInput:
    """Build and return typed house-property input data."""

    return HousePropertyInput(
        house_property_type=house_property_type,
        gross_annual_value=gross_annual_value,
        municipal_taxes_paid=municipal_taxes_paid,
        interest_on_housing_loan=interest_on_housing_loan,
        unrealized_rent=unrealized_rent,
        arrears_of_rent=arrears_of_rent,
    )
