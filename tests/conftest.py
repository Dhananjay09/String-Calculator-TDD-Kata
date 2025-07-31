"""Pytest configuration and shared fixtures."""

import pytest
from src.string_calculator import StringCalculator


@pytest.fixture
def calculator():
    """Provide a StringCalculator instance for tests."""
    return StringCalculator()


@pytest.fixture
def sample_numbers():
    """Provide sample number strings for testing."""
    return {
        "empty": "",
        "single": "1",
        "two_numbers": "1,2",
        "multiple": "1,2,3,4,5",
        "with_newlines": "1\n2,3",
        "custom_delimiter": "//;\n1;2",
        "negative": "-1,2,-3",
    } 