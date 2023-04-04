#!/usr/bin/python3
# 2-matrix_divided
"""Defines a matrix dividing function."""


def matrix_divided(matrix, div):
    """Divides the elements of matrix using div as divisor.

    Args:
        matrix (list): List containing elements to be divided.
        div (int): The divisor.

    Return:
        A new matrix - new_matrix
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or \
       not all(isinstance(ele, list) for ele in matrix) or \
       not all(all(isinstance(x, int) or isinstance(x, float) for x in ele)
               for ele in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if all(len(ele) == len(matrix[0]) for ele in matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x/div, 2), ele)) for ele in matrix])
