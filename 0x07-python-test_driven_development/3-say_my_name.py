#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name printing function."""


def say_my_name(first_name, last_name=""):
    """Prints the string My name is <first name> <last name>

    Args:
        first_name: The first argument.
        last_name: The second argument.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
