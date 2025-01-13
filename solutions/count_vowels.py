"""
This module provides a function to count the number of vowels in a given text.
The vowels here are a,e,i,o,u,A,E,I,O,U.

Function:
- count_vowels: Counts vowels in a provided string.

Raises:
        TypeError: If the input `s` is not a string.
        ValueError: If the input `s` is an empty string.

Example:
    >>> vowel_counter("Deadline")
    4
"""


def count_vowels(s) -> int:
    """
    Counts the number of vowels in the given string.

    Parameters:
    s (str): The string in which to count vowels.

    The vowels are "a,e,i,o,u,A,E,I,O,U"

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> count_vowels("hello")
    2
    >>> count_vowels("Nelsona")
    3
    >>> count_vowels("This is amazing.")
    5
    """
    # Defensive assertion: Ensure the input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Defensive assertion: Ensure the string is not empty
    if not s:
        raise ValueError("Input string cannot be empty")

    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    return sum(1 for char in s if char in vowels)
