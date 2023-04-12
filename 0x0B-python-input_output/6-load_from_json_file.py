#!/usr/bin/python3
# 6-load_from_json_file.py
"""This module contains a function that creates an Object
from a JSON string."""

import json


def load_from_json_file(filename):
    """Creates Object from JSON string."""
    with open(filename, encoding="utf-8") as my_file:
        return (json.loads(my_file.read()))
