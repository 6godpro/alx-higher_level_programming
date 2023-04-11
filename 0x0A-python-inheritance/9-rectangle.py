#!/usr/bin/python3
# 9-rectangle.py
"""Defines a class Rectangle that inherits from BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Instantiates a Rectangle object.

        Args:
            width (int): Width of the new object.
            height (int): Height of the new object.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the current rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
