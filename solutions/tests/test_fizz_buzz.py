"""
Unit tests for the fizz_buzz function from the solutions.fizz_buzz module.

This class uses the unittest framework to validate the behavior of the fizz_buzz function
across various input values, ensuring it produces the correct output lists. Tests include
cases for n = 1, 3, 5, 15, and additional edge cases to comprehensively test the function.
"""

import unittest
from solutions.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """Test cases for the fizz_buzz function.

    This class contains unit tests for the fizz_buzz function to ensure
    that it produces the expected output for various input values.
    """

    def test_fizzbuzz_15(self):
        """Test FizzBuzz for n = 15."""
        expected = [
            1,
            2,
            "Fizz",
            4,
            "Buzz",
            "Fizz",
            7,
            8,
            "Fizz",
            "Buzz",
            11,
            "Fizz",
            13,
            14,
            "FizzBuzz",
        ]
        self.assertEqual(fizz_buzz(15), expected)

    def test_fizzbuzz_3(self):
        """Test FizzBuzz for n = 3."""
        expected = [1, 2, "Fizz"]
        self.assertEqual(fizz_buzz(3), expected)

    def test_fizzbuzz_5(self):
        """Test FizzBuzz for n = 5."""
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(fizz_buzz(5), expected)

    def test_fizzbuzz_1(self):
        """Test FizzBuzz for n = 1."""
        expected = [1]
        self.assertEqual(fizz_buzz(1), expected)

    def test_fizzbuzz_zero(self):
        """Test FizzBuzz for n = 0."""
        with self.assertRaises(ValueError):
            fizz_buzz(0)

    def test_fizzbuzz_negative(self):
        """Test FizzBuzz for negative n."""
        with self.assertRaises(ValueError):
            fizz_buzz(-5)

    def test_fizzbuzz_non_integer(self):
        """Test FizzBuzz for non-integer n."""
        non_integers = [3.5, "string", None, [], {}, (), 2.0]
        for value in non_integers:
            with self.assertRaises(TypeError):
                fizz_buzz(value)

    def test_fizzbuzz_large_number(self):
        """Test FizzBuzz for a larger number n = 30."""
        expected = [
            1,
            2,
            "Fizz",
            4,
            "Buzz",
            "Fizz",
            7,
            8,
            "Fizz",
            "Buzz",
            11,
            "Fizz",
            13,
            14,
            "FizzBuzz",
            16,
            17,
            "Fizz",
            19,
            "Buzz",
            "Fizz",
            22,
            23,
            "Fizz",
            "Buzz",
            26,
            "Fizz",
            28,
            29,
            "FizzBuzz",
        ]
        self.assertEqual(fizz_buzz(30), expected)

    def test_fizzbuzz_edge_case(self):
        """Test FizzBuzz for n = 2."""
        expected = [1, 2]
        self.assertEqual(fizz_buzz(2), expected)


if __name__ == "__main__":
    unittest.main()
