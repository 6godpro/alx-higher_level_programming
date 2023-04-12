#!/usr/bin/python3
# 5-save_to_json_file.py
"""This module contains a function that writes an Object to a text file."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
