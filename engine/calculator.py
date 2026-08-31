def calculate_tax(income):
    """Calculate slab-wise income tax for FY 2024-25 (India, new regime)."""

    # Input guard: this implementation expects a non-negative numeric income.
    if income < 0:
        raise ValueError("Income cannot be negative")

    # Progressive slab definition (upper_limit, rate).
    # Rates follow FY 2024-25 new regime (Section 115BAC).
    slabs = [
        (300000, 0.00),   # Up to 3,00,000 taxed at 0%
        (600000, 0.05),   # 3,00,001 to 6,00,000 taxed at 5%
        (900000, 0.10),   # 6,00,001 to 9,00,000 taxed at 10%
        (1200000, 0.15),  # 9,00,001 to 12,00,000 taxed at 15%
        (1500000, 0.20),  # 12,00,001 to 15,00,000 taxed at 20%
        (float("inf"), 0.30),  # Above 15,00,000 taxed at 30%
    ]

    tax = 0.0
    previous_limit = 0.0

    # Apply tax slice-by-slice.
    # Only income inside the current slab is taxed at the slab rate.
    for upper_limit, rate in slabs:
        if income <= previous_limit:
            break

        taxable_slice = min(income, upper_limit) - previous_limit
        tax += taxable_slice * rate
        previous_limit = upper_limit

    return tax
