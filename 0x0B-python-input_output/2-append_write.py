#!/usr/bin/python3
# 2-append_write.py
"""This module contains a function that appends to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a text file and return the number of
       characters added.

    Args:
        filename (str): The text file to append to.
        text (str): The string to be appended to the text file.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        bytes = my_file.write(text)

    return bytes
