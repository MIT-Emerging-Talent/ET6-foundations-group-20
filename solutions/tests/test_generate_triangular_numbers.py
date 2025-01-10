"""
Unit tests for the generate_triangular_numbers function.

This code tests the functionality of the generate_triangular_numbers function 
from the solutions.generate_triangular_numbers module. It verifies that the 
function correctly generates triangular numbers for valid inputs and raises 
appropriate exceptions for invalid inputs.

A triangular number is defined as the sum of the first n natural numbers, 
calculated using the formula: n * (n + 1) / 2.

Author: Nelson
Created on: 10 01 2025
"""


import unittest
from solutions.generate_triangular_numbers import generate_triangular_numbers


class TestGenerateTriangularNumbers(unittest.TestCase):
    """
    Unit test class for the generate_triangular_numbers function.

    This class contains tests to:
    - Check correct behavior for valid inputs.
    - Confirm proper error handling for invalid inputs.
    - Verify edge cases.
    """

    
    def test_valid_inputs(self):
        """
        Test the function with valid inputs.

        Ensures the function generates the correct list of triangular numbers
        for various valid inputs.
        """
        # Test case: Generate the first triangular number (n=1)
        self.assertEqual(generate_triangular_numbers(1), [1])

        # Test case: Generate the first 5 triangular numbers
        self.assertEqual(generate_triangular_numbers(5), [1, 3, 6, 10, 15])

        # Test case: Generate the first 10 triangular numbers
        self.assertEqual(
            generate_triangular_numbers(10),
            [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        )

    
    def test_invalid_inputs(self):
        """
        Test the function with invalid inputs.

        Ensures the function raises a ValueError for:
        - Non-positive integers (e.g., 0 or negative numbers).
        - Non-integer inputs (e.g., strings or floats).
        """
        # Test case: Input is zero
        with self.assertRaises(ValueError):
            generate_triangular_numbers(0)

        # Test case: Input is a negative integer
        with self.assertRaises(ValueError):
            generate_triangular_numbers(-5)

        # Test case: Input is a string
        with self.assertRaises(ValueError):
            generate_triangular_numbers("five")

        # Test case: Input is a float
        with self.assertRaises(ValueError):
            generate_triangular_numbers(3.5)

    
    def test_edge_cases(self):
        """
        Test edge cases for the function.

        Verifies that the function handles the smallest valid input correctly.
        """
        # Test case: Smallest valid input (n=1)
        self.assertEqual(generate_triangular_numbers(1), [1])


if __name__ == "__main__":
    """
    Run the test suite.

    When executed as a script, this block will run all the test cases in the 
    TestGenerateTriangularNumbers class.
    """
    unittest.main()