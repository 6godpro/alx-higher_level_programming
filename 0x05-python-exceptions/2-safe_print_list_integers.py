#!/usr/bin/python3
# 2-safe_print_list_integers.py


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.

    Args:
        my_list (int): Contains the integer elements to print.
        x (int): Number of elements to print.

    Return:
        The number of elements - size.
    """
    size = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            size += 1
        except (ValueError, TypeError):
            continue
    print("")
    return size
