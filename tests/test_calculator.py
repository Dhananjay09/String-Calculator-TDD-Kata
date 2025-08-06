"""Test cases for StringCalculator using TDD principles."""

import pytest
from src.string_calculator import StringCalculator


class TestStringCalculator:
    def test_add_empty_string_returns_zero(self, calculator):
        """Test that an empty string returns 0."""
        assert calculator.add("") == 0
