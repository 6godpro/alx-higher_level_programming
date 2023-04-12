#!/usr/bin/python3
# 100-append_after.py
"""Defines a text insertion function."""

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing search_string.

    Args:
        filename (str): The file to be modified.
        search_string (str): The string to search for.
        new_string (str): The string to be inserted.
    """
    new = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            new += line
            if search_string in line:
                new += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new)
