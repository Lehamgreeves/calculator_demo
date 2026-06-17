"""
advanced.py

This module contains advanced calculator operations.
"""

import math


def power(base, exponent):
    """
    Raise a number to a power.

    Args:
        base (float): Base number.
        exponent (float): Exponent.

    Returns:
        float: base raised to exponent.
    """
    return base ** exponent


def square_root(number):
    """
    Calculate the square root of a number.

    Args:
        number (float): Input number.

    Returns:
        float: Square root of number.

    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def factorial(number):
    """
    Calculate the factorial of a whole number.

    Args:
        number (int): Input number.

    Returns:
        int: Factorial result.

    Raises:
        ValueError: If number is negative or not an integer.
    """
    if not isinstance(number, int):
        raise ValueError("Factorial only accepts integers.")
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(number)


def percentage(value, percent):
    """
    Calculate a percentage of a value.

    Args:
        value (float): Original value.
        percent (float): Percentage to calculate.

    Returns:
        float: Percentage result.
    """
    return (value * percent) / 100


def sine(angle_degrees):
    """
    Calculate sine of an angle in degrees.

    Args:
        angle_degrees (float): Angle in degrees.

    Returns:
        float: Sine value.
    """
    radians = math.radians(angle_degrees)
    return math.sin(radians)


def cosine(angle_degrees):
    """
    Calculate cosine of an angle in degrees.

    Args:
        angle_degrees (float): Angle in degrees.

    Returns:
        float: Cosine value.
    """
    radians = math.radians(angle_degrees)
    return math.cos(radians)


def tangent(angle_degrees):
    """
    Calculate tangent of an angle in degrees.

    Args:
        angle_degrees (float): Angle in degrees.

    Returns:
        float: Tangent value.
    """
    radians = math.radians(angle_degrees)
    return math.tan(radians)