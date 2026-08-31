from dataclasses import dataclass


@dataclass(frozen=True)
class SalaryInput:
    """Salary-related input fields used in income computation."""

    salary_gross: float = 0.0
    salary_exempt_allowances_total: float = 0.0
    professional_tax: float = 0.0
    hra_received: float = 0.0
    rent_paid: float = 0.0
    is_metro_city: bool = False
    employer_nps_contribution: float = 0.0


def create_salary_input(
    salary_gross: float = 0.0,
    salary_exempt_allowances_total: float = 0.0,
    professional_tax: float = 0.0,
    hra_received: float = 0.0,
    rent_paid: float = 0.0,
    is_metro_city: bool = False,
    employer_nps_contribution: float = 0.0,
) -> SalaryInput:
    """Build and return typed salary input data."""

    return SalaryInput(
        salary_gross=salary_gross,
        salary_exempt_allowances_total=salary_exempt_allowances_total,
        professional_tax=professional_tax,
        hra_received=hra_received,
        rent_paid=rent_paid,
        is_metro_city=is_metro_city,
        employer_nps_contribution=employer_nps_contribution,
    )
