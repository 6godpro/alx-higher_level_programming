#!/usr/bin/python3
# 8-class_to_json.py
"""Defines a function that returns a dictionary representation of
an object."""


def class_to_json(obj):
    """Returns the dictionary representation fo JSON serialization
       of an object."""
    return obj.__dict__
