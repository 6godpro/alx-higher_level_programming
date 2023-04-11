#!/usr/bin/python3
# 7-base_geometry.py
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a BaseGeometry object."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """An integer validation function.

        Args:
            name (str): The name of the argument.
            value (int): The argument to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
