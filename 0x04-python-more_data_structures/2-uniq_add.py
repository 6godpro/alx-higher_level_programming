#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    sum = 0
    for num in set(my_list):
        sum += num
    return sum
