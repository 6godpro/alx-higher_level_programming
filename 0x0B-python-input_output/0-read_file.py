#!/usr/bin/python3
# 0-read_file.py
"""This module contains a function that reads a text file."""


def read_file(filename=''):
    """Reads a text file and prints to stdout.

    Args:
        filename (str): The name of the file to read from.
    """
    with open(filename, encoding="utf-8") as my_file:
        content = my_file.read()
    print(content, end='')
