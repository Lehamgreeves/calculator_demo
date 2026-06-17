"""
basic.py

This module contains basic calculator operations.
"""


def add(a, b):
    """
    Add two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: Sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: Difference between a and b.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: Product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: Result of division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    """
    Return the remainder after division.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: Remainder.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot calculate modulus by zero.")
    return a % b


def floor_divide(a, b):
    """
    Return the floor division result.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: Floor division result.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot floor divide by zero.")
    return a // b