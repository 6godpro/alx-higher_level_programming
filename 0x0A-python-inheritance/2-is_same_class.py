#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class

    Args:
        obj (any): Object to determine it's class.
        a_class: Class to check if obj is an instance of.

    Return:
        If the object is exactly an instance of the specified class - True
        Otherwise - False
    """
    if type(obj) is not a_class:
        return False
    return True
