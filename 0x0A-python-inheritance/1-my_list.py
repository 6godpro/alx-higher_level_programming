#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MyClass that inherits from the class list."""


class MyList(list):
    """Represents a MyList object."""
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
