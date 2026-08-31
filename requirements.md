# Python Tax Calculator — Requirements (MVP)

## 1) Scope

- Build a Python CLI tax calculator for resident individual taxpayers.
- Support one selected tax year (config-driven), with slab rates and cess.
- Compute tax for salary, house property, business, and other income.
- Show full calculation breakdown and final payable/refundable amount.
- Exclude ITR filing workflows, document upload, and legal advice.

## 2) Functional Requirements

- Accept user financial and profile inputs.
- Validate inputs and reject invalid or inconsistent values with clear messages.
- Compute:
  - Gross Total Income
  - Set-off and carry-forward effects (within declared MVP scope)
  - Deductions (as per selected regime constraints)
  - Taxable Income
  - Slab-wise base tax and special-rate tax components
  - Rebate, surcharge, and cess
  - TDS/TCS and advance/self-assessment tax adjustments
  - Net tax payable or refund
- Return both summary and itemized breakdown.
- Load tax rules from config file (`JSON`/`YAML`) rather than hardcoding.

## 3) Inputs (Suggested)

### 3.1 Profile & Regime

- `tax_year` (example: `2026-27`)
- `age` (integer)
- `residential_status` (`resident` / `non_resident`) — keep optional in MVP only if resident-only scope is enforced
- `regime` (`old` / `new`)
- `is_senior_citizen` (derived from `age` if needed by rule engine)
- `is_super_senior_citizen` (derived from `age` if needed by rule engine)

### 3.2 Income Fields

#### A) Salary Breakup

- `salary_gross`
- `salary_exempt_allowances_total` (or detailed allowances as separate fields)
- `professional_tax`
- `hra_received`
- `rent_paid`
- `is_metro_city` (for HRA logic)
- `employer_nps_contribution` (for eligible deduction)

#### B) House Property

- `house_property_type` (`self_occupied` / `let_out`)
- `gross_annual_value` (for let-out)
- `municipal_taxes_paid`
- `interest_on_housing_loan`
- `unrealized_rent` (optional)
- `arrears_of_rent` (optional)

#### C) Business / Profession

- `business_income`

#### D) Capital Gains (Special Rate Buckets)

- `stcg_111a`
- `stcg_other`
- `ltcg_112a`
- `ltcg_112`

#### E) Other Sources

- `interest_savings`
- `interest_deposits`
- `dividend_income`
- `lottery_income` (special rate)
- `other_income`

#### F) Loss Set-Off / Carry Forward (Optional MVP+)

- `brought_forward_house_property_loss`
- `brought_forward_business_loss`
- `brought_forward_capital_loss_st`
- `brought_forward_capital_loss_lt`
- `unabsorbed_depreciation`

### 3.3 Deductions

Note: `standard_deduction` should be computed from tax-rule config based on year + regime, not manually entered by user.

#### Old Regime Candidate Deductions (subject to rule eligibility/caps)

- `deduction_80c`
- `deduction_80ccd_1b`
- `deduction_80d_self_family`
- `deduction_80d_parents`
- `deduction_80e`
- `deduction_80g`
- `deduction_80tta`
- `deduction_80ttb`
- `deduction_24b_self_occupied_interest` (if modeled separately)

#### New Regime Allowed Deductions (as per selected year rules)

- `employer_nps_contribution` (if allowed)
- `family_pension_deduction` (if applicable)
- Any additional deduction explicitly marked as allowed in rule config for that year

### 3.4 Taxes Already Paid / Credits

- `tds`
- `tcs`
- `advance_tax`
- `self_assessment_tax`

### 3.5 Optional Meta Inputs (Useful for Traceability)

- `rounding_preference` (if configurable)
- `computation_notes` (user-entered notes, non-numeric)

## 4) Outputs (Suggested)

- `input_echo_normalized` (normalized/derived values used by engine)
- `gross_total_income`
- `setoff_adjustments_total`
- `special_rate_income_tax`
- `total_deductions_allowed`
- `taxable_income`
- `income_tax_normal_rate`
- `income_tax_before_cess` (normal + special-rate tax)
- `rebate_amount`
- `surcharge_amount`
- `marginal_relief_amount` (if applicable)
- `cess_amount`
- `total_tax_liability`
- `tax_paid_total`
- `net_tax_payable` or `refund_amount`
- `breakdown` (step-by-step line items)
- `warnings` (assumptions/caps applied)

## 5) Validation Rules

- All monetary fields must be numeric; missing optional values default to `0`.
- No negative values for fields that cannot be negative.
- Enforce deduction caps from rule config.
- Enforce regime-based deduction eligibility.
- Enforce section-level conditions (example: 80TTA vs 80TTB mutual applicability by age/type).
- Enforce income-type-specific treatment for special-rate buckets.
- Enforce set-off restrictions (for example, house property loss set-off cap under applicable rules).
- Apply consistent rounding policy (for example, nearest rupee) at defined stages.
- Reject unknown tax year or regime with actionable errors.
- Reject conflicting or partial dependency inputs (example: `hra_received` without `rent_paid`).

## 6) Edge Cases

- Zero income.
- Taxable income exactly on slab boundaries.
- Very high income crossing surcharge thresholds.
- Rebate eligibility boundary behavior.
- Deductions entered above statutory caps.
- Negative house property income with set-off limits.
- Tax paid greater than liability (refund case).
- Floating-point precision issues (use `Decimal`).
- Missing or partial inputs.
- Conflicting inputs (for example, disallowed deduction under selected regime).
- Special-rate income present with low/zero normal taxable income.
- Surcharge and marginal relief boundary behavior.
- Senior/super-senior eligibility transitions at age boundaries.

## 7) Constraints

- Externalize tax rules; do not bury constants in application logic.
- Deterministic results for same input plus same rule version.
- Ensure auditability: every computed value must be traceable in `breakdown`.
- CLI-first MVP; no web UI dependency.
- Support only declared scope and fail fast outside scope.
- Add disclaimer that this tool is estimation-only and not legal advice.
- Keep computation year-aware: no hard-coded section caps or slab constants.

## 8) Non-Functional Requirements

- Performance target: `<100ms` per local calculation.
- Accuracy target: match known benchmark cases for selected year and regime.
- Test coverage target:
  - Unit tests for slab calculations
  - Unit tests for rebate/surcharge/marginal relief/cess
  - Unit tests for special-rate incomes
  - Unit tests for set-off behavior and deduction eligibility by regime
  - Unit tests for validation and caps
- Maintainability target: separate modules for `input`, `validation`, `rules`, `engine`, and `output`.
