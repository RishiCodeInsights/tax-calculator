import argparse

# Import path compatible with both layouts:
# 1) nested package layout: tax_calculator/engine/...
# 2) flat repo layout: engine/...
try:
    from tax_calculator.engine.calculator import calculate_tax
except ModuleNotFoundError:
    from engine.calculator import calculate_tax


def build_parser() -> argparse.ArgumentParser:
    """Create and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="tax_calculator",
        description="CLI entry point for Indian tax calculator.",
    )

    # Optional regime flag for future old/new-regime branching.
    parser.add_argument(
        "--regime",
        choices=["old", "new"],
        help="Tax regime to calculate against (placeholder).",
    )
    # Income used for slab tax computation.
    parser.add_argument(
        "--income",
        type=float,
        help="Annual taxable income in INR.",
    )

    return parser


def main() -> int:
    """Parse CLI args, execute tax calculation, and return exit code."""
    parser = build_parser()
    args = parser.parse_args()

    # Required-value check for current minimal CLI flow.
    if args.income is None:
        print("Please provide --income to calculate tax.")
        return 1

    # Core calculation call.
    tax = calculate_tax(args.income)
    print(f"Calculated tax: {tax}")
    return 0


# Enable direct execution: python main.py --income ...
if __name__ == "__main__":
    raise SystemExit(main())
