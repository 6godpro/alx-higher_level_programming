#!/usr/bin/python3
# 1-write_file.py
"""This module contains a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and return the number of
       characters written.

    Args:
        filename (str): The text file to write to.
        text (str): The string to be written to the text file.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        bytes = my_file.write(text)

    return bytes
