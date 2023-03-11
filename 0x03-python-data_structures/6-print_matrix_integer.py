#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for ele in matrix:
        for i in range(len(ele)):
            print("{:d}".format(ele[i]), end='')
            if i != len(ele) - 1:
                print(' ', end='')
        print()
