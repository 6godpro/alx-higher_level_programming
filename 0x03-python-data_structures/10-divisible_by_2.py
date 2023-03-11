#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""
    bool_list = [True if num % 2 == 0 else False for num in my_list]
    return bool_list
