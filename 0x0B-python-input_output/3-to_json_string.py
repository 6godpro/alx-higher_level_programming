#!/usr/bin/python3
# 3-to_json_string.py
"""This module contains a function that serializes an object."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj (any): The object to be serialized.
    """
    return json.dumps(my_obj)
