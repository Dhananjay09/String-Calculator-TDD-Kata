"""
Name : Dhananjay Singh
Date : 06/08/2025
"""
"""String Calculator implementation using TDD principles."""

from typing import List
import re


class AddAllNumbers:
    def __init__(self, number_list):
        self.number_list = number_list

    @property
    def add_all_numbers(self) -> int:
        return sum(self.number_list)

class MultiplyAllNumbers:
    def __init__(self, number_list: list):
        self.number_list = number_list

    @property
    def multiply_all_numbers(self) -> int:
        answer = 1
        for number in self.number_list:
            answer *= number
        return answer

class HandleNegativeNumbers:
    def __init__(self, number_list: list):
        self.number_list = number_list

    def handle_negative_numbers(self):
        negative_numbers = [num for num in self.number_list if num < 0]
        if negative_numbers:
            raise ValueError(f"negative numbers not allowed "
                             f"{', '.join(map(str, negative_numbers))}")

class HandleNumbersWithDelimiter:
    def __init__(self, numbers_str):
        self.number_str = numbers_str

    def generate_numbers(self, delimiter_end:int) -> list:
        delimiter = self.number_str[2:delimiter_end]
        numbers = self.number_str[delimiter_end + 1:]
        return [int(num) for num in numbers.split(delimiter)]


class StringCalculator:

    def add_odd_numbers(self, number_list: list) -> int:
        odd_number_list = []
        for number in number_list:
            if number % 2 == 1:
                odd_number_list.append(number)
        return AddAllNumbers(odd_number_list).add_all_numbers
    
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
                number_list = HandleNumbersWithDelimiter(numbers).generate_numbers(delimiter_end)
                if delimiter == "@":
                    return MultiplyAllNumbers(number_list=number_list).multiply_all_numbers
                if delimiter == "o":
                    return self.add_odd_numbers(number_list=number_list)
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

        HandleNegativeNumbers(number_list=number_list).handle_negative_numbers()
        
        return AddAllNumbers(number_list).add_all_numbers
