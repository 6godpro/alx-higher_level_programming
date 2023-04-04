#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplying function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: The first matrix.
        m_b (list): The second matrix.

    Return:
        The muliplication of the two matrices.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or not all(len(ele) > 0 for ele in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or not all(len(ele) > 0 for ele in m_b):
        raise ValueError("m_b can't be empty")

    if not all(all(isinstance(x, int) or isinstance(x, float)
                   for x in ele) for ele in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if not all(all(isinstance(x, int) or isinstance(x, float)
                   for x in ele) for ele in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(ele) == len(m_a[0]) for ele in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(ele) == len(m_b[0]) for ele in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for r_a in range(len(m_a)):
        tmp = []
        for r_b in range(len(m_b[0])):
            n = 0
            for c in range(len(m_a[0])):
                n += m_a[r_a][c] * m_b[c][r_b]
            tmp.append(round(n, 2))
        m_c.append(tmp)

    return m_c
