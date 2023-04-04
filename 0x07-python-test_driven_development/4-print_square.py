#!/usr/bin/python3
# 4-print_square.py
"""Defines a function that prints a square using the # character."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size length of the square to print.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for i in range(size)]
        print("")
