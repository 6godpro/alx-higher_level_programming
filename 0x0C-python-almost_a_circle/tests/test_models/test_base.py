#!/usr/bin/python3
# test_base.py
"""Defines test cases for the Base class."""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase_Instantiation(unittest.TestCase):
    """Unittests for instantiation of Base objects."""

    def test_nb_objects_private(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_object)

    def test_two_base_with_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - b1.id, 1)

    def test_three_bases_with_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b3.id, b2.id + 1)

    def test_three_bases_with_unique_id_in_between(self):
        b1 = Base(None)
        b2 = Base(89)
        b3 = Base(None)
        self.assertEqual(b1.id, b3.id - 1)

    def test_unique_id(self):
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_loop_to_set_id(self):
        for i in range(5):
            b = Base()
        self.assertEqual(b.id, 5)

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    # Test public attribute `id` with other data types
    def test_string_arg(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_arg(self):
        self.assertEqual(2.3, Base(2.3).id)

    def test_bool_arg(self):
        self.assertEqual(True, Base(True).id)

    def test_list_arg(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_arg(self):
        self.assertEqual({'a': 1, 'b': 2}, Base({'a': 1, 'b': 2}).id)

    def test_tuple_arg(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_arg(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_inf_arg(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_nan_arg(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_bytes_arg(self):
        self.assertEqual(b'hello', Base(b'hello').id)

    def test_frozenset_arg(self):
        self.assertEqual(frozenset([1, 2, 3]), Base(frozenset([1, 2, 3])).id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittest for testing the dictionary to json string representation."""
    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string("l_1", "l_2")

    def test_to_json_string_none_arg(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty_list_arg(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_set_arg(self):
        self.assertEqual(Base.to_json_string({1, 2, 3}), None)

    def test_to_json_string_str_arg(self):
        self.assertEqual(Base.to_json_string("invalid"), None)

    def test_to_json_string_bool_arg(self):
        self.assertEqual(Base.to_json_string(True), None)

    def test_to_json_string_tuple_arg(self):
        self.assertEqual(Base.to_json_string((1, 2, 3)), None)

    def test_to_json_string_not_list_of_dict_arg(self):
        self.assertEqual(Base.to_json_string([1, 2, 3]), None)

    def test_to_json_string_dict_arg(self):
        self.assertEqual(Base.to_json_string({'a': 1, 'b': 2, 'c': 3}), None)

    def test_to_json_string_frozenset_arg(self):
        self.assertEqual(Base.to_json_string(frozenset([1, 2, 3])), None)

    def test_to_json_string_bytes_arg(self):
        self.assertEqual(Base.to_json_string(b'betty'), None)

    def test_to_json_string_inf_arg(self):
        self.assertEqual(Base.to_json_string(float('inf')), None)

    def test_to_json_string_inf_arg(self):
        self.assertEqual(Base.to_json_string(float('nan')), None)

    def test_to_json_string_mixed_list(self):
        l_1 = [{'a': 1, 'b': 2}, 3, 4.0]
        self.assertEqual(Base.to_json_string(l_1), None)

    def test_to_json_string_list_of_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(res, json_dictionary)

    def test_to_json_string_list_of_more_than_one_dict(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 2, 1, 9, 89)
        d_1 = r1.to_dictionary()
        d_2 = r2.to_dictionary()
        json_dictionary = Base.to_json_string([d_1, d_2])
        res = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 89, "width": 10, "height": 2, "x": 1, "y": 9}]'
        self.assertEqual(res, json_dictionary)

    def test_to_json_string_return_type(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)


class TestBase_from_json_string(unittest.TestCase):
    """Unittest for testing the representation of json string as
    Python object."""
    def test_from_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string("[]", "[]")

    def test_from_json_string_none_arg(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list_arg(self):
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_from_json_string_set_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string({1, 2, 3})

    def test_from_json_string_bool_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(True)

    def test_from_json_string_tuple_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string((1, 2, 3))

    def test_from_json_string_not_list_of_dict_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([1, 2, 3])

    def test_from_json_string_dict_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string({'a': 1, 'b': 2, 'c': 3})

    def test_from_json_string_frozenset_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(frozenset([1, 2, 3]))

    def test_from_json_string_invalid_bytes_arg(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string(b'betty')

    def test_from_json_invalid_string_str_arg(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string("invalid")

    def test_from_json_string_inf_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(float('inf'))

    def test_from_json_string_inf_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(float('nan'))

    def test_from_json_string_list_of_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        list_dict = Base.from_json_string(json_dictionary)
        res = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(res, list_dict)

    def test_from_json_string_list_of_more_than_one_dict(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 2, 1, 9, 89)
        d_1 = r1.to_dictionary()
        d_2 = r2.to_dictionary()
        json_dictionary = Base.to_json_string([d_1, d_2])
        list_dict = Base.from_json_string(json_dictionary)
        res = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
               {"id": 89, "width": 10, "height": 2, "x": 1, "y": 9}]
        self.assertEqual(res, list_dict)

    def test_from_json_string_return_type(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        list_dict = Base.from_json_string(json_string)
        self.assertIsInstance(list_dict, list)
