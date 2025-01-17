"""
Unit tests for the generate_triangular_numbers function
in the solutions.generate_triangular_numbers module.

This module contains a set of test cases to ensure the correctness of the
generate_triangular_numbers function, which generates triangular numbers for given inputs.
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

    def test_valid_inputs(self) -> None:
        """
        Test the function with valid inputs.

        Ensures the function generates the correct list of triangular numbers
        for various valid inputs.
        """
        self.assertEqual(generate_triangular_numbers(1), [1])
        self.assertEqual(generate_triangular_numbers(5), [1, 3, 6, 10, 15])
        self.assertEqual(
            generate_triangular_numbers(10),
            [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],
        )

    def test_invalid_inputs(self) -> None:
        """
        Test the function with invalid inputs.

        Ensures the function raises a ValueError for:
        - Non-positive integers (e.g., 0 or negative numbers).
        - Non-integer inputs (e.g., strings or floats).
        """
        with self.assertRaises(ValueError):
            generate_triangular_numbers(0)
        with self.assertRaises(ValueError):
            generate_triangular_numbers(-5)
        with self.assertRaises(ValueError):
            generate_triangular_numbers("five")
        with self.assertRaises(ValueError):
            generate_triangular_numbers(3.5)

    def test_edge_cases(self) -> None:
        """
        Test edge cases for the function.

        Verifies that the function handles the smallest valid input correctly.
        """
        self.assertEqual(generate_triangular_numbers(1), [1])


if __name__ == "__main__":
    unittest.main()
