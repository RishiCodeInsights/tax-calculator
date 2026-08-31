# Tax Calculator (India)

## Disclaimer
This project provides **estimation-only** income tax calculations for learning and planning purposes.
It is **not** legal, financial, or tax-filing advice. Always verify results with official Income Tax Department utilities, a qualified Chartered Accountant (CA), or current government notifications before filing.

## About
This is a Python CLI project for Indian income tax estimation. The current implementation focuses on slab-based tax computation and is being expanded task-by-task with typed input contracts, validation rules, and detailed breakdown support.

## Current Scope
- Python CLI-first implementation.
- Resident-individual tax estimation workflow.
- FY/A.Y.-aware computation design (rules intended to be config-driven).
- Input contract models with unit tests.

## Out of Scope (Current Stage)
- ITR filing workflows.
- Document upload and reconciliation.
- Professional advisory replacement.

## How To Calculate Tax (CLI)
Run these commands from the repo root folder:

```bash
cd tax_calculator
python main.py --income 3700000 --regime new
```

Example output:

```text
Calculated tax: 810000.0
```

If income is missing:

```bash
python main.py
```

The app prints:

```text
Please provide --income to calculate tax.
```

## Developer Setup
Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Author
- Rishi Sinha
