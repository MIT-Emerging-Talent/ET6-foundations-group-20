"""
Unit tests for the largest_num function in the Find_largest_number module.

This module contains a set of test cases to ensure the correctness of the
largest_num function, which identifies the largest number in a given list.
"""

import unittest

from solutions.find_largest_number import largest_num


class TestLargestNum(unittest.TestCase):
    """
    Unit tests for the largest_num() function, verifying its correctness
    across positive, negative, mixed, single-element, duplicate, and empty lists.
    """

    def test_positive_numbers(self):
        """Test case for a list of positive numbers."""
        self.assertEqual(largest_num([3, 9, 2, 3, 2]), 9)

    def test_negative_numbers(self):
        """Test case for a list of negative numbers."""
        self.assertEqual(largest_num([-3, -1, -2, -7, -8]), -1)

    def test_mixed_numbers(self):
        """Test case for a list of mixed positive and negative numbers."""
        self.assertEqual(largest_num([4, -9, 3, -8, 5]), 5)

    def test_single_element(self):
        """Test case for a list with a single element."""
        self.assertEqual(largest_num([100]), 100)

    def test_duplicates(self):
        """Test case for a list with duplicate numbers."""
        self.assertEqual(largest_num([1, 1, 1, 1]), 1)

    def test_empty_list(self):
        """Test case for an empty list (should raise ValueError)."""
        with self.assertRaises(ValueError):
            largest_num([])

    def test_non_numeric_input(self):
        """Test case for non-numeric input (should raise ValueError)."""
        with self.assertRaises(ValueError):
            largest_num(["a", "b", "c"])

    def test_large_numbers(self):
        """Test case for large numbers."""
        self.assertEqual(largest_num([1e10, 1e15, 1e11]), 1e15)


if __name__ == "__main__":
    unittest.main()
