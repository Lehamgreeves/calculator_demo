"""
test_calculator.py

Basic tests for the calculator package using the new class-based architecture.
"""

from calculator_package import (
    BasicCalculator,
    AdvancedCalculator,
    StatisticsCalculator,
)


def test_basic_operations():
    calc = BasicCalculator()
    
    assert calc.calculate("add", 10, 5) == 15
    assert calc.calculate("subtract", 10, 5) == 5
    assert calc.calculate("multiply", 10, 5) == 50
    assert calc.calculate("Divide", 10, 5) == 2  # Matches your original "Divide" casing
    assert calc.calculate("modulus", 10, 3) == 1
    assert calc.calculate("floor_divide", 10, 3) == 3


def test_advanced_operations():
    calc = AdvancedCalculator()
    
    # Assuming AdvancedCalculator implements a similar .calculate() method.
    # For single-argument operations (like square_root), the second value can be 0 or ignored.
    assert calc.calculate("power", 2, 3) == 8
    assert calc.calculate("square_root", 25, 0) == 5
    assert calc.calculate("factorial", 5, 0) == 120
    assert calc.calculate("percentage", 200, 15) == 30


def test_statistics_operations():
    calc = StatisticsCalculator()
    numbers = [10, 20, 20, 30, 40, 50]

    # Since statistics operations take a list instead of two separate floats (a, b),
    # they are typically implemented as direct instance methods:
    assert calc.mean(numbers) == 28.333333333333332
    assert calc.median(numbers) == 25
    assert calc.mode(numbers) == 20
    assert calc.minimum(numbers) == 10
    assert calc.maximum(numbers) == 50
    assert calc.data_range(numbers) == 40