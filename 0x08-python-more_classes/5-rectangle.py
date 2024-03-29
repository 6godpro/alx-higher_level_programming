#!/usr/bin/python3
# 3-rectangle.py
"""Defines a Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiates a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets the width of the current triangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets the height of the current triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the current rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the current rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string representation of an rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        string = ""
        for i in range(self.__height):
            string += "".join(["#" for i in range(self.__width)])
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        """Displays a message after an instance is deleted"""
        print("Bye rectangle...")
