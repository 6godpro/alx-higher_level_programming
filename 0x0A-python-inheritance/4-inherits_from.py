#!/usr/bin/python3
# 4-inherits_from.py
"""Defines a subclass checking function."""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass of a_class.

    Args:
        obj (any): Object to determine it's class.
        a_class (any): Class to check if obj is subclass of.

    Return:
        If obj is a subclass of the specified class - True
        Otherwise - False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
