#!/usr/bin/python3
# 12-pascal_triangle.py
"""Computes the Pascal's triangle"""


def pascal_triangle(n):
    """Returns  a list of lists of integers representing the
       Pascal's triangle of n."""
    if n <= 0:
        return []

    tri = [[1]]
    for i in range(n - 1):
        tmp = [1]
        for j in range(len(tri[-1]) - 1):
            tmp.append(tri[-1][j] + tri[-1][j+1])
        tmp.append(1)
        tri.append(tmp)

    return tri
