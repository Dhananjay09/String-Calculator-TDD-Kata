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
