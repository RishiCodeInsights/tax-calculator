from dataclasses import dataclass
from typing import Optional

from tax_calculator.input.capital_gains import CapitalGainsInput, create_capital_gains_input
from tax_calculator.input.deductions import DeductionsInput, create_deductions_input
from tax_calculator.input.house_property import HousePropertyInput, create_house_property_input
from tax_calculator.input.losses import LossCarryForwardInput, create_loss_carry_forward_input
from tax_calculator.input.other_sources import OtherSourcesInput, create_other_sources_input
from tax_calculator.input.salary import SalaryInput, create_salary_input
from tax_calculator.input.tax_credits import TaxCreditsInput, create_tax_credits_input
from tax_calculator.input.top_level import TopLevelInput


@dataclass(frozen=True)
class UnifiedTaxInput:
    """Single request object combining all input sections."""

    top_level: TopLevelInput
    salary: SalaryInput
    house_property: HousePropertyInput
    capital_gains: CapitalGainsInput
    other_sources: OtherSourcesInput
    deductions: DeductionsInput
    tax_credits: TaxCreditsInput
    losses: LossCarryForwardInput


def create_unified_tax_input(
    top_level: TopLevelInput,
    salary: Optional[SalaryInput] = None,
    house_property: Optional[HousePropertyInput] = None,
    capital_gains: Optional[CapitalGainsInput] = None,
    other_sources: Optional[OtherSourcesInput] = None,
    deductions: Optional[DeductionsInput] = None,
    tax_credits: Optional[TaxCreditsInput] = None,
    losses: Optional[LossCarryForwardInput] = None,
) -> UnifiedTaxInput:
    """Build unified request object with zero-default sections when omitted."""

    return UnifiedTaxInput(
        top_level=top_level,
        salary=salary or create_salary_input(),
        house_property=house_property or create_house_property_input(),
        capital_gains=capital_gains or create_capital_gains_input(),
        other_sources=other_sources or create_other_sources_input(),
        deductions=deductions or create_deductions_input(),
        tax_credits=tax_credits or create_tax_credits_input(),
        losses=losses or create_loss_carry_forward_input(),
    )
