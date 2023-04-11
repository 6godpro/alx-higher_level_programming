#!/usr/bin/python3
# 100-my_int.py
"""Defines a class MyInt that inherits from the class int."""


class MyInt(int):
    """Represents a MyInt object."""
    def __eq__(self, other):
        """Inverts the __eq__ method inherited from the class int"""
        return (self.numerator != other.numerator)

    def __ne__(self, other):
        """Inverts the __ne__ method inherited from the class int"""
        return (self.numerator == other.numerator)
