#!/usr/bin/python3
# 3-square.py
"""Defines a class Square."""


class Square:
    """Represents a Square object."""
    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): Size of the current square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)
