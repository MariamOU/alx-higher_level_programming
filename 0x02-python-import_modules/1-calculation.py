#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the addition, sub, mult and div of a and b"""
from calculator_1 import add, mul, sub, div
a = 10
b = 5
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
