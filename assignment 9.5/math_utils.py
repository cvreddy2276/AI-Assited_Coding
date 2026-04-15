"""
math_utils.py: Basic math utility functions.
"""

def square(n):
    """Return the square of a number.

    Args:
        n (int or float): The number to square.

    Returns:
        int or float: The square of n.
    """
    return n * n

def cube(n):
    """Return the cube of a number.

    Args:
        n (int or float): The number to cube.

    Returns:
        int or float: The cube of n.
    """
    return n * n * n

def factorial(n):
    """Return the factorial of a non-negative integer n.

    Args:
        n (int): The number to compute the factorial of. Must be non-negative.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
