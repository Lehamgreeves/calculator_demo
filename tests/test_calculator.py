"""
test_calculator.py

Basic tests for the calculator package.
"""

from calculator_package import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    floor_divide,
    power,
    square_root,
    factorial,
    percentage,
    mean,
    median,
    mode,
    minimum,
    maximum,
    data_range,
)


def test_basic_operations():
    assert add(10, 5) == 15
    assert subtract(10, 5) == 5
    assert multiply(10, 5) == 50
    assert divide(10, 5) == 2
    assert modulus(10, 3) == 1
    assert floor_divide(10, 3) == 3


def test_advanced_operations():
    assert power(2, 3) == 8
    assert square_root(25) == 5
    assert factorial(5) == 120
    assert percentage(200, 15) == 30


def test_statistics_operations():
    numbers = [10, 20, 20, 30, 40, 50]

    assert mean(numbers) == 28.333333333333332
    assert median(numbers) == 25
    assert mode(numbers) == 20
    assert minimum(numbers) == 10
    assert maximum(numbers) == 50
    assert data_range(numbers) == 40