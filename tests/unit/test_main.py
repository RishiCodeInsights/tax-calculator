import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tax_calculator.main import build_parser, main


class TestMainModule(unittest.TestCase):
    """Unit tests for CLI parser and main entry behavior."""

    # Normal case: parser should read valid regime and income.
    def test_build_parser_parses_valid_args(self):
        parser = build_parser()
        args = parser.parse_args(["--regime", "new", "--income", "500000"])

        self.assertEqual(args.regime, "new")
        self.assertEqual(args.income, 500000.0)

    # Edge case: both CLI arguments are optional in parser definition.
    def test_build_parser_allows_missing_optional_args(self):
        parser = build_parser()
        args = parser.parse_args([])

        self.assertIsNone(args.regime)
        self.assertIsNone(args.income)

    # Expected failure path: invalid regime choice should exit.
    def test_build_parser_rejects_invalid_regime(self):
        parser = build_parser()

        with self.assertRaises(SystemExit):
            parser.parse_args(["--regime", "invalid"])

    # Expected failure path: main requires income for calculation.
    def test_main_returns_error_when_income_missing(self):
        output = io.StringIO()

        with patch("sys.argv", ["tax_calculator"]), redirect_stdout(output):
            exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertIn("Please provide --income to calculate tax.", output.getvalue())

    # Normal case: main prints computed tax and succeeds.
    def test_main_returns_success_for_valid_income(self):
        output = io.StringIO()

        with patch("sys.argv", ["tax_calculator", "--income", "750000"]), redirect_stdout(output):
            exit_code = main()

        self.assertEqual(exit_code, 0)
        self.assertIn("Calculated tax: 30000.0", output.getvalue())

    # Expected failure path: negative income bubbles up as ValueError.
    def test_main_raises_for_negative_income(self):
        with patch("sys.argv", ["tax_calculator", "--income", "-1"]):
            with self.assertRaises(ValueError):
                main()

    # Expected failure path: argparse exits on invalid float input.
    def test_main_exits_for_non_numeric_income(self):
        with patch("sys.argv", ["tax_calculator", "--income", "abc"]):
            with self.assertRaises(SystemExit):
                main()


if __name__ == "__main__":
    unittest.main()
