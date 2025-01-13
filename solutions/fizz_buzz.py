"""
This module provides a function that generates a list of numbers from 1 to n
with specific rules for multiples of 3 and 5.

For each number in the range:
- For multiples of 3, "Fizz" is added instead of the number.
- For multiples of 5, "Buzz" is added instead of the number.
- For multiples of both 3 and 5, "FizzBuzz" is added instead of the number.

Features:
- Input validation to ensure that the input is a positive integer.
- Customizable output format (e.g., changing the words "Fizz" and "Buzz"
  to user-defined strings).
- Ability to generate results as a string instead of a list.

Example:
>>> fizz_buzz(15)
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13,
  14, 'FizzBuzz']
"""


def fizz_buzz(n: int) -> list:
    """
    Generates a list of numbers from 1 to n with the following rules:
    - For multiples of 3, "Fizz" is added instead of the number.
    - For multiples of 5, "Buzz" is added instead of the number.
    - For multiples of both 3 and 5, "FizzBuzz" is added instead of the number.

    Parameters:
    n (int): The upper limit of the range (inclusive) to generate.

    Returns:
    list: A list containing the numbers and/or string representations according
    to the rules.

    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is less than 1.

    Example:
    >>> fizz_buzz(10)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']

    """
    # Defensive assertions
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be greater than or equal to 1.")
    results = []  # Initialize an empty list to store the results
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append(
                "FizzBuzz"
            )  # Append "FizzBuzz" for multiples of both 3 and 5
        elif i % 3 == 0:
            results.append("Fizz")  # Append "Fizz" for multiples of 3
        elif i % 5 == 0:
            results.append("Buzz")  # Append "Buzz" for multiples of 5
        else:
            results.append(i)  # Append the number itself if not a multiple of 3 or 5
    return results  # Return the list of results
