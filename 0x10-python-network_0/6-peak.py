#!/usr/bin/python3
"""
    Finds a peak in a list of unsorted integers.
"""


def find_peak(arr):
    """Finds a peak in the given array"""
    size = len(arr)
    if size == 0:
        return None
    for i in range(len(arr)):
        if (i >= 0 and arr[i] > arr[i - 1] and
                i + 1 < size and arr[i] > arr[i + 1]):
            break

    return arr[i]
