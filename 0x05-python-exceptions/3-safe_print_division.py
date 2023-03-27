#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): Dividend.
        b (int): Divisor.

    Return:
        Return the result of the division - res:
        Otherwise - None.
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
