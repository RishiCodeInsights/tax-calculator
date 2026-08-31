from dataclasses import dataclass


@dataclass(frozen=True)
class OtherSourcesInput:
    """Income from other sources input buckets."""

    interest_savings: float = 0.0
    interest_deposits: float = 0.0
    dividend_income: float = 0.0
    lottery_income: float = 0.0
    other_income: float = 0.0


def create_other_sources_input(
    interest_savings: float = 0.0,
    interest_deposits: float = 0.0,
    dividend_income: float = 0.0,
    lottery_income: float = 0.0,
    other_income: float = 0.0,
) -> OtherSourcesInput:
    """Build and return typed other-sources input data."""

    return OtherSourcesInput(
        interest_savings=interest_savings,
        interest_deposits=interest_deposits,
        dividend_income=dividend_income,
        lottery_income=lottery_income,
        other_income=other_income,
    )
