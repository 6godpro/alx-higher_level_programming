#!/usr/bin/python3
# 4-from_json_string.py
"""This module contains a function that deserializes a JSON string."""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The string to be deserialized.
    """
    return (json.loads(my_str))
