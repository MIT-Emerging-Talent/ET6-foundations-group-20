"""
This module contains unit tests for the count_vowels module.
It includes test cases for the following function:
- count_vowels: Test the function that counts vowels in a string.

Tests cover various cases including normal strings, empty strings, and case insensitivity.

Usage:
    Run tests using unittest framework:
    >>> python -m unittest test_vowel_counter.py
"""

import unittest

from solutions.count_vowels import count_vowels  # Import the count_vowels function


class TestCountVowels(unittest.TestCase):
    """Test cases for the count_vowels function.

    This class contains unit tests for the count_vowels function to ensure
    that it accurately counts the number of vowels in various input strings.
    """

    def test_count_vowels_normal(self):
        """Test counting vowels in a normal string.

        This test checks that the function correctly counts the vowels in a
        typical string with mixed characters.
        """
        self.assertEqual(count_vowels("Nagham"), 2)

    def test_count_vowels_no_vowels(self):
        """Test counting vowels in a string with no vowels.

        This test checks that the function returns 0 when there are no vowels
        in the input string.
        """
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_count_vowels_case_insensitive(self):
        """Test counting vowels in a case-insensitive manner.

        This test verifies that the function counts both uppercase and lowercase
        vowels correctly.
        """
        self.assertEqual(count_vowels("AbEcIdOfUg"), 5)

    def test_count_vowels_with_spaces(self):
        """Test counting vowels in a string with spaces.

        This test checks that the function correctly counts vowels in a string
        that contains spaces and punctuation.
        """
        self.assertEqual(count_vowels("Hello World!"), 3)

    # Defensive assertion tests
    def test_invalid_input_type_integer(self):
        """Test that the function raises a TypeError for non-string input (integer)."""
        with self.assertRaises(TypeError):
            count_vowels(12345)

    def test_invalid_input_type_list(self):
        """Test that the function raises a TypeError for non-string input (list)."""
        with self.assertRaises(TypeError):
            count_vowels(["a", "b", "c"])

    def test_empty_string(self):
        """Test that the function raises a ValueError for an empty string."""
        with self.assertRaises(ValueError):
            count_vowels("")


if __name__ == "__main__":
    unittest.main()
