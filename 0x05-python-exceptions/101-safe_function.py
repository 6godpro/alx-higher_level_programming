#!/usr/bin/python3
# 101-safe_function.py
import sys


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: A pointer to a function to be executed.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of fct call.
    """
    try:
        res = fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        res = None
    return res
