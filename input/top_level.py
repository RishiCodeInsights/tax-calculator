from dataclasses import dataclass
from typing import Literal


# Explicit literal types keep the profile contract constrained and self-documenting.
ResidentialStatus = Literal["resident", "non_resident"]
RegimeType = Literal["old", "new"]


@dataclass(frozen=True)
class TopLevelInput:
    """Typed top-level input fields for the tax calculator request."""

    tax_year: str
    age: int
    residential_status: ResidentialStatus
    regime: RegimeType


def create_top_level_input(
    tax_year: str,
    age: int,
    residential_status: ResidentialStatus,
    regime: RegimeType,
) -> TopLevelInput:
    """Build and return a typed top-level input object.

    Note: validation rules (range checks, supported years, etc.) are handled
    in the validation layer tasks.
    """

    return TopLevelInput(
        tax_year=tax_year,
        age=age,
        residential_status=residential_status,
        regime=regime,
    )
