#!/usr/bin/python3
# 7-base_geometry.py
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a BaseGeometry object."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """An integer validation function."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
