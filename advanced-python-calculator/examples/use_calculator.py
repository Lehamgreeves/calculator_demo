"""
use_calculator.py

This file shows how to import and use the calculator package.
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
    sine,
    cosine,
    tangent,
    mean,
    median,
    mode,
    minimum,
    maximum,
    data_range,
    CalculatorHistory,
)


def main():
    history = CalculatorHistory()

    result = add(10, 5)
    print("Addition:", result)
    history.add_record("10 + 5", result)

    result = subtract(10, 5)
    print("Subtraction:", result)
    history.add_record("10 - 5", result)

    result = multiply(10, 5)
    print("Multiplication:", result)
    history.add_record("10 * 5", result)

    result = divide(10, 5)
    print("Division:", result)
    history.add_record("10 / 5", result)

    result = modulus(10, 3)
    print("Modulus:", result)
    history.add_record("10 % 3", result)

    result = floor_divide(10, 3)
    print("Floor Division:", result)
    history.add_record("10 // 3", result)

    result = power(2, 3)
    print("Power:", result)
    history.add_record("2 ** 3", result)

    result = square_root(25)
    print("Square Root:", result)
    history.add_record("sqrt(25)", result)

    result = factorial(5)
    print("Factorial:", result)
    history.add_record("5!", result)

    result = percentage(200, 15)
    print("Percentage:", result)
    history.add_record("15% of 200", result)

    print("Sine 30:", sine(30))
    print("Cosine 60:", cosine(60))
    print("Tangent 45:", tangent(45))

    numbers = [10, 20, 20, 30, 40, 50]

    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Minimum:", minimum(numbers))
    print("Maximum:", maximum(numbers))
    print("Range:", data_range(numbers))

    print("\\nCalculation History:")
    for record in history.get_history():
        print(record)


if __name__ == "__main__":
    main()