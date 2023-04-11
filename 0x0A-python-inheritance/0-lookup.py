#!/usr/bin/python3
# 0-lookup.py
"""Defines a function that returns the properties of an object."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return (dir(obj))
