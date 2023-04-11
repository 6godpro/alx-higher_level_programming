#!/usr/bin/python3
# 11-square.py
"""Defines a class Square that inherits from BaseGeometry class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a rectangle."""

    def __init__(self, size):
        """Instantiates a Rectangle object.

        Args:
            size (int): Size of the new object.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the current rectangle."""
        return (self.__size ** 2)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
