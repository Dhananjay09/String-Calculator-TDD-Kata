"""
Name : Dhananjay Singh
Date : 06/08/2025
"""
"""String Calculator implementation using TDD principles."""

from typing import List
import re


class StringCalculator:
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string input.
        
        Args:
            numbers: String containing numbers separated by delimiters
            
        Returns:
            Sum of all numbers in the string
            
        Raises:
            ValueError: If negative numbers are found
        """
        if not numbers:
            return 0
        
        # Handle custom delimiter
        if numbers.startswith("//"):
            delimiter_end = numbers.find("\n")
            if delimiter_end != -1:
                delimiter = numbers[2:delimiter_end]
                numbers = numbers[delimiter_end + 1:]
                number_list = [int(num) for num in numbers.split(delimiter)]
            else:
                return 0
        else:
            # Handle single number
            if "," not in numbers and "\n" not in numbers:
                number_list = [int(numbers)]
            else:
                # Handle multiple numbers with mixed delimiters
                # Replace newlines with commas, then split by comma
                normalized_numbers = numbers.replace("\n", ",")
                number_list = [int(num) for num in normalized_numbers.split(",")]
        
        # Check for negative numbers
        negative_numbers = [num for num in number_list if num < 0]
        if negative_numbers:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negative_numbers))}")
        
        return sum(number_list)
