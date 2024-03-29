#!/usr/bin/python3
# 2-square.py
"""Defines a class Square."""


class Square:
    """Represents a Square object."""
    def __init__(self, size=0):
        """Initializes a class object

        Args:
            size (int): Size of the new Square object.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
