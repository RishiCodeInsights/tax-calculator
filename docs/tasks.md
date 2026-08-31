# Python Tax Calculator � Atomic Task Backlog

Each item is intentionally small: **one task = one prompt**.

## 0) Project Setup

### T001 - Initialize package structure [Done]
**Prompt:** Create Python package folders `tax_calculator/input`, `tax_calculator/validation`, `tax_calculator/rules`, `tax_calculator/engine`, `tax_calculator/output`, and add `__init__.py` in each.
**Status:** Completed

### T002 - Create app entry point [Done]
**Prompt:** Add CLI entry file `tax_calculator/main.py` with a `main()` function and argument parsing placeholder.
**Status:** Completed

### T003 - Add dependency and tool config [Done]
**Prompt:** Add project dependencies and tooling config (for example `pyproject.toml`) including `pytest` and any YAML parser needed.
**Status:** Completed  added `pyproject.toml` and updated `requirements.txt` with `pytest` + `PyYAML`.

### T004 - Add base README disclaimer [Done]
**Prompt:** Add estimation-only disclaimer and project scope summary to `README.md`.
**Status:** Completed added disclaimer and scope sections in `README.md`.

## 1) Input Contract

### T005 - Define top-level input schema model
**Prompt:** Create a typed input model (dataclass or Pydantic) for top-level fields: `tax_year`, `age`, `residential_status`, `regime`.

### T006 - Add salary input model
**Prompt:** Add salary input fields model: `salary_gross`, `salary_exempt_allowances_total`, `professional_tax`, `hra_received`, `rent_paid`, `is_metro_city`, `employer_nps_contribution`.

### T007 - Add house property input model
**Prompt:** Add house property input fields model: `house_property_type`, `gross_annual_value`, `municipal_taxes_paid`, `interest_on_housing_loan`, `unrealized_rent`, `arrears_of_rent`.

### T008 - Add capital gains input model
**Prompt:** Add capital gains input fields model: `stcg_111a`, `stcg_other`, `ltcg_112a`, `ltcg_112`.

### T009 - Add other sources input model
**Prompt:** Add other sources model: `interest_savings`, `interest_deposits`, `dividend_income`, `lottery_income`, `other_income`.

### T010 - Add deductions input model
**Prompt:** Add deductions model with fields: `deduction_80c`, `deduction_80ccd_1b`, `deduction_80d_self_family`, `deduction_80d_parents`, `deduction_80e`, `deduction_80g`, `deduction_80tta`, `deduction_80ttb`, `deduction_24b_self_occupied_interest`, `family_pension_deduction`.

### T011 - Add tax credits input model
**Prompt:** Add tax paid/credit fields model: `tds`, `tcs`, `advance_tax`, `self_assessment_tax`.

### T012 - Add loss carry-forward model
**Prompt:** Add optional loss fields model: `brought_forward_house_property_loss`, `brought_forward_business_loss`, `brought_forward_capital_loss_st`, `brought_forward_capital_loss_lt`, `unabsorbed_depreciation`.

### T013 - Compose unified request object
**Prompt:** Combine all sub-models into one unified calculator input object and provide defaults of `0` for optional numeric fields.

## 2) Rules Config Layer

### T014 - Define rules file format
**Prompt:** Create a versioned rule file format (`JSON`/`YAML`) containing slabs, cess rate, rebate rules, surcharge thresholds, and deduction caps.

### T015 - Implement rule loader
**Prompt:** Implement `rules/loader.py` to load tax rules by `tax_year` and return typed rule objects.

### T016 - Implement regime eligibility map
**Prompt:** Add regime-wise deduction eligibility map in rules so each deduction clearly declares allowed/disallowed per regime.

### T017 - Add standard deduction rule
**Prompt:** Move `standard_deduction` into rule config and remove it from user-entered deduction inputs.

### T018 - Add special-rate tax rule tables
**Prompt:** Add rules for special-rate categories (`stcg_111a`, `ltcg_112a`, `ltcg_112`, `lottery_income`) in config.

## 3) Validation Layer

### T019 - Build numeric field validator
**Prompt:** Implement validator that ensures all money fields are numeric and non-null values default to `0` when optional.

### T020 - Build non-negative constraints
**Prompt:** Implement field-level non-negative checks for all fields that cannot legally be negative.

### T021 - Validate regime enum and tax year
**Prompt:** Validate that `regime` and `tax_year` exist in supported config; raise actionable errors otherwise.

### T022 - Validate dependency inputs
**Prompt:** Add cross-field validation rules (example: if `hra_received` > 0 then `rent_paid` must be provided).

### T023 - Validate deduction caps
**Prompt:** Enforce deduction caps from config and capture capped values as warnings.

### T024 - Validate regime deduction eligibility
**Prompt:** Reject or zero-out disallowed deductions based on selected regime and configured policy.

### T025 - Validate section mutual conditions
**Prompt:** Implement mutual applicability checks such as 80TTA vs 80TTB eligibility by age/type.

### T026 - Validate set-off eligibility
**Prompt:** Validate set-off related fields and enforce configured set-off limits.

## 4) Computation Engine

### T027 - Implement salary income computation
**Prompt:** Build salary computation function that derives taxable salary from salary breakup and allowed exemptions/deductions as per rules.

### T028 - Implement house property computation
**Prompt:** Build house property computation for self-occupied and let-out cases, including interest and municipal tax logic.

### T029 - Implement other heads aggregation
**Prompt:** Build aggregation functions for business income, other sources income, and normal-rate capital gains portions.

### T030 - Implement set-off engine
**Prompt:** Implement current-year set-off and optional brought-forward adjustment logic within configured limits.

### T031 - Implement gross total income step
**Prompt:** Implement function to calculate `gross_total_income` after applying valid set-off logic.

### T032 - Implement deduction engine
**Prompt:** Implement deduction computation that applies regime eligibility and cap rules and returns detailed deduction breakdown.

### T033 - Implement taxable income step
**Prompt:** Implement function to derive `taxable_income` from gross total income minus allowed deductions.

### T034 - Implement slab tax calculator
**Prompt:** Implement slab-wise normal income tax calculator using configured slabs and return slab-line breakdown.

### T035 - Implement special-rate tax calculator
**Prompt:** Implement tax calculation for special-rate income buckets and return separate `special_rate_income_tax`.

### T036 - Implement rebate calculation
**Prompt:** Implement rebate calculation (for example section 87A behavior) fully driven by year/regime rules.

### T037 - Implement surcharge and marginal relief
**Prompt:** Implement surcharge logic across thresholds plus marginal relief calculation from config.

### T038 - Implement cess calculation
**Prompt:** Implement cess calculation on post-rebate/post-surcharge tax as per configured rate.

### T039 - Implement rounding policy
**Prompt:** Implement deterministic rounding stages (intermediate vs final) using `Decimal` and configured policy.

### T040 - Implement final payable/refund step
**Prompt:** Implement final tax settlement by adjusting liability against `tds + tcs + advance_tax + self_assessment_tax` and output payable/refund.

## 5) Output Layer

### T041 - Define output contract
**Prompt:** Create typed output model including `gross_total_income`, `taxable_income`, `income_tax_before_cess`, `cess_amount`, `total_tax_liability`, `tax_paid_total`, `net_tax_payable/refund_amount`, and warnings.

### T042 - Build detailed breakdown formatter
**Prompt:** Implement step-by-step itemized breakdown output showing each intermediate value and rule reference key.

### T043 - Build CLI summary renderer
**Prompt:** Add CLI renderer that prints concise summary + detailed breakdown in readable table/text format.

## 6) Application Wiring

### T044 - Build orchestrator flow
**Prompt:** Wire `input -> validation -> rule loading -> computation -> output` into one orchestrator function.

### T045 - Add CLI input ingestion
**Prompt:** Add CLI input ingestion from JSON file path argument and map payload to input contract.

### T046 - Add structured error handling
**Prompt:** Add friendly error responses for validation errors and unknown tax rule issues.

## 7) Testing

### T047 - Add slab calculation unit tests
**Prompt:** Write unit tests for slab boundaries and bracket transitions for both regimes.

### T048 - Add special-rate tax tests
**Prompt:** Write unit tests for `stcg_111a`, `ltcg_112a`, `ltcg_112`, and lottery tax handling.

### T049 - Add rebate/surcharge/cess tests
**Prompt:** Write unit tests for rebate boundaries, surcharge thresholds, marginal relief, and cess.

### T050 - Add deduction eligibility tests
**Prompt:** Write unit tests for old/new regime deduction eligibility and cap enforcement.

### T051 - Add validation failure tests
**Prompt:** Write unit tests for invalid types, unknown year/regime, negative values, and conflicting dependent inputs.

### T052 - Add integration golden cases
**Prompt:** Add 3-5 end-to-end benchmark scenarios with expected outputs for regression safety.

## 8) Frontend/UX (CLI-Facing)

### T053 - Improve prompt/input helper text
**Prompt:** Add clear CLI help text explaining each major input group and required vs optional fields.

### T054 - Add assumptions/warnings display
**Prompt:** Ensure CLI clearly prints assumptions, capped deductions, and regime-based disallowed entries.

### T055 - Add output export option
**Prompt:** Add optional `--output-json` flag to save full calculation response as JSON.

## 9) Hardening

### T056 - Add deterministic precision safeguards
**Prompt:** Ensure all monetary arithmetic uses `Decimal` end-to-end and never falls back to float.

### T057 - Add audit trace IDs per step
**Prompt:** Add stable step identifiers in breakdown output so each computed value is traceable.

### T058 - Add version stamp in output
**Prompt:** Include rule version and calculator version metadata in final output.

### T059 - Final README usage examples
**Prompt:** Add sample commands and example input/output snippets for both old and new regimes.

### T060 - Pre-release checklist
**Prompt:** Add a release checklist covering tests, rule review, and disclaimer verification.


