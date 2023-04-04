#!/usr/bin/python3
# 0-add_integer.py
"""Adds two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int): first integer value.
        b (int): second integer value.

    Return:
        The total value of the two integers. - total
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    total = int(a) + int(b)
    return total
