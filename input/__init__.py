from tax_calculator.input.capital_gains import CapitalGainsInput, create_capital_gains_input
from tax_calculator.input.deductions import DeductionsInput, create_deductions_input
from tax_calculator.input.house_property import HousePropertyInput, create_house_property_input
from tax_calculator.input.losses import LossCarryForwardInput, create_loss_carry_forward_input
from tax_calculator.input.other_sources import OtherSourcesInput, create_other_sources_input
from tax_calculator.input.salary import SalaryInput, create_salary_input
from tax_calculator.input.tax_credits import TaxCreditsInput, create_tax_credits_input
from tax_calculator.input.top_level import TopLevelInput, create_top_level_input
from tax_calculator.input.unified_request import UnifiedTaxInput, create_unified_tax_input

__all__ = [
    "TopLevelInput",
    "create_top_level_input",
    "SalaryInput",
    "create_salary_input",
    "HousePropertyInput",
    "create_house_property_input",
    "CapitalGainsInput",
    "create_capital_gains_input",
    "OtherSourcesInput",
    "create_other_sources_input",
    "DeductionsInput",
    "create_deductions_input",
    "TaxCreditsInput",
    "create_tax_credits_input",
    "LossCarryForwardInput",
    "create_loss_carry_forward_input",
    "UnifiedTaxInput",
    "create_unified_tax_input",
]
