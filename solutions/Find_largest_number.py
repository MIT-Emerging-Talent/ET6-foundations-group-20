"""
This module contains a function `largest_num` that takes a list of numbers
and returns the largest number from that list.

The `largest_num` function checks if all elements in the input list are
numeric (either integers or floats). If the list is empty, it raises a
ValueError. The function returns the maximum number in the list using the
built-in `max()` function."""


def largest_num(numbers):
    """
    This function takes a list of numbers as input and returns the largest number.

    Parameters:
    A list of numbers.

    Returns:
        float: The largest number in the list.
    """

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements in the list must be numeric.")

    if not numbers:
        raise ValueError("The list is empty.")

    return max(numbers)
