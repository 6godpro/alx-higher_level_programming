#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplying function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the matrix multiplication of the two arguments.

    Args:
        m_a (list): The first argument.
        m_A (list): The first argument.

    Return:
        The matrix multiplication of both matrices m_a and m_b.
    """

    return (np.matmul(m_a, m_b))
