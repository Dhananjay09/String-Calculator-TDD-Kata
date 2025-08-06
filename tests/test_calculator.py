"""Test cases for StringCalculator using TDD principles."""

import pytest
from src.string_calculator import StringCalculator


class TestStringCalculator:
    def test_add_empty_string_returns_zero(self, calculator):
        """Test that an empty string returns 0."""
        assert calculator.add("") == 0

    def test_add_single_number_returns_number(self, calculator):
        """Test that a single number returns that number."""
        assert calculator.add("1") == 1
        assert calculator.add("42") == 42

    def test_add_two_numbers_returns_sum(self, calculator):
        """Test that two comma-separated numbers return their sum."""
        assert calculator.add("1,2") == 3
        assert calculator.add("10,20") == 30

    def test_add_multiple_numbers_returns_sum(self, calculator):
        """Test that multiple comma-separated numbers return their sum."""
        assert calculator.add("1,2,3") == 6
        assert calculator.add("1,2,3,4,5") == 15

    def test_add_numbers_with_newlines_returns_sum(self, calculator):
        """Test that numbers separated by newlines return their sum."""
        assert calculator.add("1\n2,3") == 6
        assert calculator.add("1\n2\n3") == 6

    def test_add_with_custom_delimiter_returns_sum(self, calculator):
        """Test that custom delimiters work correctly."""
        assert calculator.add("//;\n1;2") == 3
        assert calculator.add("//|\n1|2|3") == 6

    def test_add_custom_delimiter_without_newline_returns_zero(
            self, calculator):
        """Test that custom delimiter without newline returns 0."""
        assert calculator.add("//;") == 0
        assert calculator.add("//|") == 0

    def test_add_negative_number_throws_exception(
            self, calculator):
        """Test that negative numbers throw an exception."""
        with pytest.raises(ValueError, match="negative numbers not allowed"):
            calculator.add("-1,2")

    def test_add_multiple_negative_numbers_throws_exception_with_all_negatives(
        self, calculator
    ):
        """Test that multiple negative numbers show all in exception message."""
        with pytest.raises(
            ValueError, match="negative numbers not allowed -1, -3"
        ):
            calculator.add("-1,2,-3")

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("", 0),
            ("1", 1),
            ("1,2", 3),
            ("1,2,3", 6),
            ("1\n2,3", 6),
            ("//;\n1;2", 3),
        ],
    )
    def test_add_various_inputs(self, calculator, input_str, expected):
        """Parametrized test for various valid inputs."""
        assert calculator.add(input_str) == expected

    @pytest.mark.parametrize(
        "input_str,expected_error",
        [
            ("-1", "negative numbers not allowed -1"),
            ("-1,2,-3", "negative numbers not allowed -1, -3"),
            ("1,-2,3,-4", "negative numbers not allowed -2, -4"),
        ],
    )
    def test_add_negative_numbers_exceptions(
        self, calculator, input_str, expected_error
    ):
        """Parametrized test for negative number exceptions."""
        with pytest.raises(ValueError, match=expected_error):
            calculator.add(input_str) 