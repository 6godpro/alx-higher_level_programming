#!/usr/bin/python3
# 4-square.py
"""Defines a class Square."""


class Square:
    """Represents a Square object."""

    def __init__(self, size=0):
        """Initializes a Square object.

        Args:
            size (int): size of the new square object.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the current object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of the current object>

        Args:
            value (int): Size to set to the object to.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the current object."""
        return (self.__size * self.__size)
