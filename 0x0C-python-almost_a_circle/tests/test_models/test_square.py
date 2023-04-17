#!/usr/bin/python3
# test_square.py
"""This module contains test cases for the Square class."""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_Instantiation(unittest.TestCase):
    """Unittest for testing the instantiation of a square."""
    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_with_one_args(self):
        s = Square(12)
        self.assertEqual(s.size, 12)

    def test_with_two_args(self):
        s1 = Square(1, 3)
        s2 = Square(2, 4)
        self.assertEqual(s2.id, s1.id + 1)

    def test_with_three_args(self):
        s1 = Square(1, 3, 5)
        s2 = Square(2, 4, 6)
        self.assertEqual(s2.id, s1.id + 1)

    def test_id_with_four_args(self):
        s = Square(1, 3, 5, 7)
        self.assertEqual(s.id, 7)

    def test_with_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_square_inherits_rect(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_square_inherits_base(self):
        self.assertIsInstance(Square(10), Base)

    # Test that all attributes are private
    def test_private_width(self):
        with self.assertRaises(AttributeError):
            Square(10).__width

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            Square(10).__height

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            Square(10).__x

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            Square(10).__y

    # Test that width, height and size are the same
    def test_width(self):
        s = Square(10, 1, 1)
        self.assertEqual(s.width, 10)

    def test_height(self):
        s = Square(10, 1, 1)
        self.assertEqual(s.height, 10)

    def test_size(self):
        s = Square(10, 1, 1)
        self.assertEqual(s.size, 10)

    # Test the getters and the setters of the attributes
    def test_set_and_get_width(self):
        s = Square(2, 0, 0)
        s.width = 89
        self.assertEqual(s.width, 89)

    def test_set_and_get_height(self):
        s = Square(2, 0, 0)
        s.height = 89
        self.assertEqual(s.height, 89)

    def test_set_and_get_x(self):
        s = Square(2, 4)
        s.x = 5
        self.assertEqual(s.x, 5)

    def test_set_and_get_y(self):
        s = Square(2, 4, 1, 2)
        s.y = 6
        self.assertEqual(s.y, 6)


class TestSquare_attribute_type(unittest.TestCase):
    """Unittests for testing the attribute types."""
    def test_none_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 0, 0)

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None, 1)

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10", 0)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "9", 1)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, "8")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(12.4)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 2.8, 1)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, 5.3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 0)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [1, 2, 3], 10)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, [1, 2, 3])

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, (1, 2, 3), 1)

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, (1, 2, 3))

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {1, 2, 3}, 1)

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, {1, 2, 3})

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'a': 1, 'b': 2, 'c': 3}, 2)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {'a': 1, 'b': 2, 'c': 3}, 1)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, {'a': 1, 'b': 2, 'c': 3})

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(2), 2)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, complex(1), 1)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, complex(0))

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3}), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, frozenset({1, 2, 3}), 10)

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, frozenset({1, 2, 3}))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('nan'), 1)

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, float('nan'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 2)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('inf'), 1)

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, float('inf'))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'invalid', 2)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, b'invalid', 1)

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, b'invalid')


class TestSquare_attribute_value(unittest.TestCase):
    """Unittests for testing the values of the attributes."""
    def test_neg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -1, 4)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -1)


class TestSquare_instantiation_order(unittest.TestCase):
    """Unittest for testing the order of attribute instantiation."""
    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", "also an invalid")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", 0, "also an invalid")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "invalid", "also an invalid")


class TestSquare_area(unittest.TestCase):
    """Unittest for testing the area of the Square."""
    def test_small_values(self):
        self.assertEqual(81, Square(9).area())

    def test_set_before(self):
        s = Square(20)
        s.size = 99999999
        self.assertEqual(9999999800000001, s.area())


class TestSquare_display(unittest.TestCase):
    """Unittest for testing the display of the Square."""
    @staticmethod
    def stdout_content(sq_obj):
        """Returns the stdout content after a program is run.

        Args:
            sq_obj (Square object): A Square object to test.
        """
        content = StringIO()
        sys.stdout = content

        sq_obj.display()

        sys.stdout = sys.__stdout__

        return content

    # test __str__ method
    def test_str_with_size(self):
        s = Square(3, 2, 0)
        res = "[Square] ({}) 2/0 - 3".format(s.id)
        self.assertEqual(res, str(s))

    def test_str_with_size_x(self):
        s = Square(1, 3, 5)
        res = "[Square] ({}) 3/5 - 1".format(s.id)
        self.assertEqual(res, str(s))

    def test_str_with_size_x_y(self):
        s = Square(3, 4, 8, 12)
        res = "[Square] (12) 4/8 - 3"
        self.assertEqual(res, str(s))

    def test_str_with_all_args(self):
        s = Square(4, 6, 2, 1)
        res = "[Square] (1) 6/2 - 4"
        self.assertEqual(res, str(s))

    def test_str_with_one_arg(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # test display method
    def test_display_with_size(self):
        s = Square(2)
        content = TestSquare_display.stdout_content(s)
        self.assertEqual("##\n##\n", content.getvalue())

    def test_display_with_size_x(self):
        s = Square(1, 3)
        content = TestSquare_display.stdout_content(s)
        res = "   #\n"
        self.assertEqual(res, content.getvalue())

    def test_display_with_size_x_y(self):
        s = Square(3, 4, 3)
        content = TestSquare_display.stdout_content(s)
        res = "\n\n\n    ###\n    ###\n    ###\n"
        self.assertEqual(res, content.getvalue())

    def test_display_with_all_args(self):
        s = Square(4, 2, 2, 12)
        content = TestSquare_display.stdout_content(s)
        res = "\n\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(res, content.getvalue())

    def test_display_with_one_arg(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_attributes(unittest.TestCase):
    """Unittest for testing the update attribute of the Square."""
    def test_no_update(self):
        s = Square(10, 10, 10, 10)
        s.update()
        res = "[Square] (10) 10/10 - 10"
        self.assertEqual(res, str(s))

    def test_update_none_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        res = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(res, str(s))

    def test_update_id_size(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        res = "[Square] (89) 10/10 - 2"
        self.assertEqual(res, str(s))

    def test_update_all(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        res = "[Square] (89) 3/4 - 2"
        self.assertEqual(res, str(s))

    def test_update_more_than_four_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        res = "[Square] (89) 3/4 - 2"
        self.assertEqual(res, str(s))

    def test_update_more_than_once(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(20, 30, 40, 50)
        res = "[Square] (20) 40/50 - 30"
        self.assertEqual(res, str(s))

    def test_update_None_id_size_x_y(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 2, 3, 4)
        res = "[Square] ({}) 3/4 - 2".format(s.id)
        self.assertEqual(res, str(s))

    def test_update_non_int_size(self):
        s = Square(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid arg", 3)

    def test_update_with_zero_size(self):
        s = Square(89, 4, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0, 3)

    def test_update_with_neg_size(self):
        s = Square(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(90, -3, 3)

    def test_update_non_int_x(self):
        s = Square(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 2, "invalid arg")

    def test_update_with_neg_x(self):
        s = Square(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(90, 2, -3)

    def test_update_with_zero_x(self):
        s = Square(90, 2, 3, 4)
        s.update(90, 2, 0, 4)
        res = "[Square] (90) 0/4 - 2"
        self.assertEqual(res, str(s))

    def test_update_non_int_y(self):
        s = Square(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 2, 3, "invalid arg")

    def test_update_with_neg_y(self):
        s = Square(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(90, 2, 7, -3)

    def test_update_with_zero_y(self):
        s = Square(90, 2, 7, 3)
        s.update(90, 2, 7, 0)
        res = "[Square] (90) 7/0 - 2"
        self.assertEqual(res, str(s))

    def test_update_with_kwargs_size(self):
        s = Square(10, 10, 10, 10)
        s.update(size=15)
        res = "[Square] (10) 10/10 - 15"
        self.assertEqual(res, str(s))

    def test_update_with_kwargs_size_id(self):
        s = Square(10, 10, 10, 10)
        s.update(size=20, id=89)
        res = "[Square] (89) 10/10 - 20"
        self.assertEqual(res, str(s))

    def test_update_with_kwargs_size_id_x(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=15, x=5)
        res = "[Square] (89) 5/10 - 15"
        self.assertEqual(res, str(s))

    def test_update_with_kwargs_all(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, y=7, size=15, x=5)
        res = "[Square] (89) 5/7 - 15"
        self.assertEqual(res, str(s))

    def test_update_with_kwargs_twice_all(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, y=7, size=15, x=5)
        s.update(id=98, y=3, x=2, size=45)
        res = "[Square] (98) 2/3 - 45"
        self.assertEqual(res, str(s))

    def test_update_with_kwargs_with_invalid_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(h=20, w=10, a=5, b=7)
        res = "[Square] (10) 10/10 - 10"
        self.assertEqual(res, str(s))

    def test_update_with_only_args_if_both(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 25, 35, size=30, x=30, id=98)
        res = "[Square] (89) 35/10 - 25"
        self.assertEqual(res, str(s))

    def test_update_with_args_and_then_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(20, 30, 40, 50)
        s.update(id=None, size=20)
        res = "[Square] ({}) 40/50 - 20".format(s.id)
        self.assertEqual(res, str(s))


class TestSquare_update_order(unittest.TestCase):
    """Unittest for testing the order of updating the attributes."""
    def test_update_size_before_x(self):
        s = Square(10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(10, -4, "invalid")

    def test_update_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(10, "invalid width", 5, "not an integer")

    def test_update_x_before_y(self):
        s = Square(98, 10, 20, 30)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(98, 10, "invalid", -4)


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing the dictionary representation of a Square."""
    def test_to_dictionary_representation(self):
        s = Square(2, 3, 4, 5)
        s_dictionary = s.to_dictionary()
        res = {'size': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertEqual(res, s_dictionary)

    def test_to_dictionary_instances_not_eq(self):
        s1 = Square(3, 6, 5, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_dict_eq(self):
        s1 = Square(3, 6, 5, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__dict__, s2.__dict__)

    def test_to_dictionary_and_dict_values_eq(self):
        s = Square(10, 2, 1, 9)
        s_dict = s.to_dictionary()
        self.assertEqual(set(s_dict.values()), set(s.__dict__.values()))

    def test_to_dictionary_no_arg(self):
        s = Square(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            s.to_dictionary(10)


if __name__ == "__main__":
    unittest.main()
