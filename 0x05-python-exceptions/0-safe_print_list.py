#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    Args:
        my_list (list): Contains the elements to be printed.
        x (int): The number of elements to print.

    Return:
        The number of printed elements
    """
    size = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            size += 1
        except IndexError:
            break
    print("")
    return size
