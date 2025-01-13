"""
Unit tests for the `reverse_string` function.

This module tests the `reverse_string` function, which reverses an input string.
It includes various test cases to ensure that the function handles:
- Normal strings
- Strings containing numbers
- Strings with special characters
- Single characters
- Palindromes
- Strings with spaces
- Extremely long strings
It also checks that a ValueError is raised for empty strings and that a TypeError is raised for non-string inputs.
"""

import unittest
from solutions.reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    """Test cases for the reverse_string function.

    This class contains unit tests for the reverse_string function to ensure
    that it correctly reverses strings under various scenarios.
    """

    def test_reverse_normal(self):
        """Test reversing a normal string."""
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_single_character(self):
        """Test reversing a single character string."""
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_palindrome(self):
        """Test reversing a palindrome."""
        self.assertEqual(reverse_string("madam"), "madam")

    def test_reverse_spaces(self):
        """Test reversing a string with spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_numbers_in_string(self):
        """Test reversing a string containing numbers."""
        self.assertEqual(reverse_string("12345"), "54321")

    def test_special_characters(self):
        """Test reversing a string with special characters."""
        self.assertEqual(reverse_string("!@#$"), "$#@!")

    def test_long_string(self):
        """Test reversing an extremely long string."""
        long_string = "a" * 10000
        self.assertEqual(reverse_string(long_string), long_string[::-1])

    def test_reverse_empty(self):
        """Test that an empty string raises a ValueError."""
        with self.assertRaises(ValueError):
            reverse_string("")  # This input should raise a ValueError

    def test_integer_input(self):
        """Test that an integer input raises a TypeError."""
        with self.assertRaises(TypeError):
            reverse_string(12345)  # Non-string input: integer

    def test_none_input(self):
        """Test that a None input raises a TypeError."""
        with self.assertRaises(TypeError):
            reverse_string(None)  # Non-string input: NoneType

    def test_list_input(self):
        """Test that a list input raises a TypeError."""
        with self.assertRaises(TypeError):
            reverse_string(["a", "b", "c"])  # Non-string input: list


if __name__ == "__main__":
    unittest.main()
