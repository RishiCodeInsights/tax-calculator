from dataclasses import dataclass


@dataclass(frozen=True)
class CapitalGainsInput:
    """Capital gains buckets required for special/normal tax handling."""

    stcg_111a: float = 0.0
    stcg_other: float = 0.0
    ltcg_112a: float = 0.0
    ltcg_112: float = 0.0


def create_capital_gains_input(
    stcg_111a: float = 0.0,
    stcg_other: float = 0.0,
    ltcg_112a: float = 0.0,
    ltcg_112: float = 0.0,
) -> CapitalGainsInput:
    """Build and return typed capital-gains input data."""

    return CapitalGainsInput(
        stcg_111a=stcg_111a,
        stcg_other=stcg_other,
        ltcg_112a=ltcg_112a,
        ltcg_112=ltcg_112,
    )
