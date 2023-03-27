#!/usr/bin/python3
# 1-safe_print_integer.py


def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (int): The value to be printed

    Return:
        If a ValueError or TypeError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
