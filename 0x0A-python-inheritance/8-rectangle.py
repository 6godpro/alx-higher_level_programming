#!/usr/bin/python3
# 8-rectangle.py
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
