#!/usr/bin/python3
# 100-safe_print_integer_err.py
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
    except TypeError as te:
        print("Exception: {}".format(te), file=sys.stderr)

    return False
