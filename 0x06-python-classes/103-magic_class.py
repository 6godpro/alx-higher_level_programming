#!/usr/bin/python3
# 103-magic_class.py
"""Define a MagicClass class that does exactly the same as a provided \
bytecode"""


import math


class MagicClass:
    """Represents a MagicClass object."""
    def __init__(self, radius=0):
        """Initializes an object.

        Args:
            radius (int or float): The radius of the new object.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the current MagicClass area."""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Returns the current MagicClass circumference."""
        return (2 * math.pi * self.__radius)
