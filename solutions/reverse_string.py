"""
This module provides a function to reverse an inputed string.

Function:
    reverse_string(s: str) -> str:
        Reverses the input string and returns the reversed one.

Features:
- Simple and efficient string reversal.
- Built-in error handling for invalid inputs.

Raises:
        TypeError: If the input `s` is not a string.
        ValueError: If the input `s` is an empty string.
Example:
    >>> reverse_string("Deadline")
    enildaeD
"""


def reverse_string(s: str) -> str:
    """
    Reverses the given string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.

    Example:
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("12345")
        '54321'
    """
    # Defensive assertion: Ensure the input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Defensive assertion: Ensure the string is not empty
    if not s:
        raise ValueError("Input string cannot be empty")
    return s[::-1]  # Return the reversed string using slicing
