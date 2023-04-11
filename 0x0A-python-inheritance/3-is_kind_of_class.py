#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines a class checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance(direct or inherited) of a_class.

    Args:
        obj (any): Object to determine it's class.
        a_class (any): Class to check if obj is an instance of.

    Return:
        If instance(direct or inherited) of the specified class - True
        Otherwise - False
    """
    if not isinstance(obj, a_class):
        return False
    return True
