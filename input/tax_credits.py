from dataclasses import dataclass


@dataclass(frozen=True)
class TaxCreditsInput:
    """Tax paid/credit fields used in final payable/refund settlement."""

    tds: float = 0.0
    tcs: float = 0.0
    advance_tax: float = 0.0
    self_assessment_tax: float = 0.0


def create_tax_credits_input(
    tds: float = 0.0,
    tcs: float = 0.0,
    advance_tax: float = 0.0,
    self_assessment_tax: float = 0.0,
) -> TaxCreditsInput:
    """Build and return typed tax-credits input data."""

    return TaxCreditsInput(
        tds=tds,
        tcs=tcs,
        advance_tax=advance_tax,
        self_assessment_tax=self_assessment_tax,
    )
