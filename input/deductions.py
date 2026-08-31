from dataclasses import dataclass


@dataclass(frozen=True)
class DeductionsInput:
    """Deduction fields captured as input before eligibility/cap validation."""

    deduction_80c: float = 0.0
    deduction_80ccd_1b: float = 0.0
    deduction_80d_self_family: float = 0.0
    deduction_80d_parents: float = 0.0
    deduction_80e: float = 0.0
    deduction_80g: float = 0.0
    deduction_80tta: float = 0.0
    deduction_80ttb: float = 0.0
    deduction_24b_self_occupied_interest: float = 0.0
    family_pension_deduction: float = 0.0


def create_deductions_input(
    deduction_80c: float = 0.0,
    deduction_80ccd_1b: float = 0.0,
    deduction_80d_self_family: float = 0.0,
    deduction_80d_parents: float = 0.0,
    deduction_80e: float = 0.0,
    deduction_80g: float = 0.0,
    deduction_80tta: float = 0.0,
    deduction_80ttb: float = 0.0,
    deduction_24b_self_occupied_interest: float = 0.0,
    family_pension_deduction: float = 0.0,
) -> DeductionsInput:
    """Build and return typed deductions input data."""

    return DeductionsInput(
        deduction_80c=deduction_80c,
        deduction_80ccd_1b=deduction_80ccd_1b,
        deduction_80d_self_family=deduction_80d_self_family,
        deduction_80d_parents=deduction_80d_parents,
        deduction_80e=deduction_80e,
        deduction_80g=deduction_80g,
        deduction_80tta=deduction_80tta,
        deduction_80ttb=deduction_80ttb,
        deduction_24b_self_occupied_interest=deduction_24b_self_occupied_interest,
        family_pension_deduction=family_pension_deduction,
    )
