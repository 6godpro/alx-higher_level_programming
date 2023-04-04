#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """"""
    def test_zero_arg(self):
        self.assertEqual(max_integer(), None)

    def test_one_arg(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_more_than_one_arg(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_neg_val(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_neg_with_pos_val(self):
        self.assertEqual(max_integer([-4, 2, -1, 3]), 3)

    def test_float_val(self):
        self.assertEqual(max_integer([1.0, -4.1, 3.4, -1.4]), 3.4)

    def test_float_with_int_val(self):
        self.assertEqual(max_integer([-1, 7.5, 3, 4]), 7.5)

    def test_tuple_arg(self):
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_char_args(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_string_args(self):
        self.assertEqual(max_integer(["Hello", "there"]), "there")

    """Testing non-iterable arguments."""

    def test_None_arg(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_arg(self):
        with self.assertRaises(TypeError):
             max_integer(12)

    def test_non_iter_int_arg(self):
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3)

    """Testing with non-indexable iterable."""

    def test_set_arg(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4})

    """Testing with a list containing int/float values with strings"""
    def test_int_float_with_str_arg(self):
        with self.assertRaises(TypeError):
            max_integer(["Hello", 2, 'Betty', 98])
