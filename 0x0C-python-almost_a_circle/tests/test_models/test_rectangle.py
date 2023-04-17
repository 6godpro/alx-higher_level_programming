#!/usr/bin/python3
# test_rectangle.py
"""This module contains test cases for the Rectangle class."""

import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Instantiation(unittest.TestCase):
    """Unittest for the instantiation of a rectangle."""
    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(12)

    def test_with_two_args(self):
        r1 = Rectangle(1, 3)
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, r1.id + 1)

    def test_with_three_args(self):
        r1 = Rectangle(1, 3, 5)
        r2 = Rectangle(2, 4, 6)
        self.assertEqual(r2.id, r1.id + 1)

    def test_with_four_args(self):
        r1 = Rectangle(1, 3, 5, 7)
        r2 = Rectangle(2, 4, 6, 8)
        r3 = Rectangle(3, 5, 7, 9)
        self.assertEqual(r3.id, r1.id + 2)

    def test_id_with_five_args(self):
        self.assertEqual(89, Rectangle(2, 4, 1, 3, 89).id)

    def test_with_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_rect_inherits_base(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

    # Test that all attributes are private
    def test_private_width_attr(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4).__width)

    def test_private_height_attr(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4).__height)

    def test_private_x_attr(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 4, 5, 6).__x)

    def test_private_y_attr(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 4, 5, 6).__y)

    # Test the getters and setters of the attributes
    def test_set_and_get_width_attr(self):
        r = Rectangle(2, 4, 0, 0)
        r.width = 89
        self.assertEqual(r.width, 89)

    def test_set_and_get_height_attr(self):
        r = Rectangle(1, 3, 1, 2)
        r.height = 98
        self.assertEqual(r.height, 98)

    def test_set_and_get_x_attr(self):
        r = Rectangle(2, 4)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_set_and_get_y_attr(self):
        r = Rectangle(2, 4, 1, 2)
        r.y = 6
        self.assertEqual(r.y, 6)


class TestRectangle_attr_type(unittest.TestCase):
    """Unittests for testing the type of the attributes."""
    def test_none_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_none_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_none_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None, 1)

    def test_none_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, None)

    def test_str_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_str_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_str_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "9", 1)

    def test_str_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "8")

    def test_float_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.2, 2)

    def test_float_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 11.5)

    def test_float_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 2.8, 1)

    def test_float_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, 5.3)

    def test_list_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_list_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1, 2, 3])

    def test_list_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1, 2, 3], 1)

    def test_list_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, [1, 2, 3])

    def test_tuple_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_tuple_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (1, 2, 3))

    def test_tuple_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (1, 2, 3), 1)

    def test_tuple_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, (1, 2, 3))

    def test_set_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_set_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {1, 2, 3})

    def test_set_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {1, 2, 3}, 1)

    def test_set_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, {1, 2, 3})

    def test_dict_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'a': 1, 'b': 2, 'c': 3}, 2)

    def test_dict_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {'a': 1, 'b': 2, 'c': 3})

    def test_dict_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {'a': 1, 'b': 2, 'c': 3}, 1)

    def test_dict_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, {'a': 1, 'b': 2, 'c': 3})

    def test_complex_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 2)

    def test_complex_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, complex(10))

    def test_complex_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, complex(1), 1)

    def test_complex_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, complex(0))

    def test_frozenset_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 2)

    def test_frozenset_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, frozenset({1, 2, 3}))

    def test_frozenset_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, frozenset({1, 2, 3}), 1)

    def test_frozenset_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, frozenset({1, 2, 3}))

    def test_nan_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_nan_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'))

    def test_nan_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float('nan'), 1)

    def test_nan_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, float('nan'))

    def test_inf_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_inf_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('inf'))

    def test_inf_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float('inf'), 1)

    def test_inf_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, float('inf'))

    def test_bytes_width_attr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'invalid', 2)

    def test_bytes_height_attr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, b'invalid')

    def test_bytes_x_attr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, b'invalid', 1)

    def test_bytes_y_attr(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, b'invalid')


class TestRectangle_attribute_value(unittest.TestCase):
    """Unittests for testing the values of the attributes."""
    def test_neg_width_attr(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width_attr(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_neg_height_attr(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_zero_height_attr(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    """If the value of width and height are not > 0, a TypeError is raised
    only for width"""
    def test_zero_width_and_height_attr(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 0)

    def test_neg_x_attr(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 20, -1, 4)

    def test_neg_y_attr(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 20, 2, -1)


class TestRectangle_instantiation_order(unittest.TestCase):
    """Unittest for testing the order of attribute instantiation."""
    def test_width_before_height(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, "not an integer")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("not an integer", 10, "invalid", 0)

    def test_width_before_y(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2, 0, "not an integer")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "invalid", "also an invalid", 2)

    def test_height_before_y(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -3, 2, "invalid")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "invalid", -2)


class TestRectangle_area(unittest.TestCase):
    """Unittest for testing the area of the Rectangle."""
    def test_small_values(self):
        self.assertEqual(81, Rectangle(9, 9, 2, 2).area())

    def test_set_before(self):
        r = Rectangle(20, 10)
        r.width = 11
        r.height = 392
        self.assertEqual(4312, r.area())


class TestRectangle_display(unittest.TestCase):
    """Unittest for testing the display of the rectangle."""
    @staticmethod
    def stdout_content(rect_obj):
        """Returns the stdout content after a program is run.

        Args:
            rect_obj (Rectangle object): A Rectangle object to test.
        """
        content = StringIO()
        sys.stdout = content

        rect_obj.display()

        sys.stdout = sys.__stdout__

        return content

    # test __str__ method
    def test_str_with_width_height(self):
        r = Rectangle(3, 2)
        res = "[Rectangle] ({}) 0/0 - 3/2".format(r.id)
        self.assertEqual(res, str(r))

    def test_str_with_width_height_x(self):
        r = Rectangle(1, 3, 5)
        res = "[Rectangle] ({}) 5/0 - 1/3".format(r.id)
        self.assertEqual(res, str(r))

    def test_str_with_width_height_x_y(self):
        r = Rectangle(3, 4, 12, 12)
        res = "[Rectangle] ({}) 12/12 - 3/4".format(r.id)
        self.assertEqual(res, str(r))

    def test_str_with_all_args(self):
        r = Rectangle(4, 6, 2, 1, 12)
        res = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(res, str(r))

    def test_str_with_one_arg(self):
        r = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # test display method
    def test_display_with_width_height(self):
        r = Rectangle(2, 2)
        content = TestRectangle_display.stdout_content(r)
        self.assertEqual("##\n##\n", content.getvalue())

    def test_display_with_width_height_x(self):
        r = Rectangle(1, 3, 5)
        content = TestRectangle_display.stdout_content(r)
        res = "     #\n     #\n     #\n"
        self.assertEqual(res, content.getvalue())

    def test_display_with_width_height_x_y(self):
        r = Rectangle(3, 4, 3, 2)
        content = TestRectangle_display.stdout_content(r)
        res = "\n\n   ###\n   ###\n   ###\n   ###\n"
        self.assertEqual(res, content.getvalue())

    def test_display_with_all_args(self):
        r = Rectangle(4, 4, 2, 2, 12)
        content = TestRectangle_display.stdout_content(r)
        res = "\n\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(res, content.getvalue())

    def test_display_with_one_arg(self):
        r = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_attributes(unittest.TestCase):
    """Unittest for testing the update attribute of the Rectangle."""
    def test_no_update(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        res = "[Rectangle] (10) 10/10 - 10/10"
        self.assertEqual(res, str(r))

    def test_update_none_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        res = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(res, str(r))

    def test_update_id_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        res = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(res, str(r))

    def test_update_id_width_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        res = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(res, str(r))

    def test_update_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        res = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(res, str(r))

    def test_update_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        res = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(res, str(r))

    def test_update_more_than_five_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        res = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(res, str(r))

    def test_update_more_than_once(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(20, 30, 40, 50, 60)
        res = "[Rectangle] (20) 50/60 - 30/40"
        self.assertEqual(res, str(r))

    def test_update_None_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 2, 3, 4, 5)
        res = "[Rectangle] ({}) 4/5 - 2/3".format(r.id)
        self.assertEqual(res, str(r))

    def test_update_non_int_width(self):
        r = Rectangle(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid arg", 3)

    def test_update_with_zero_width(self):
        r = Rectangle(89, 4, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0, 3)

    def test_update_with_neg_width(self):
        r = Rectangle(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(90, -3, 3)

    def test_update_non_int_height(self):
        r = Rectangle(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid arg")

    def test_update_with_zero_height(self):
        r = Rectangle(89, 4, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 3, 0)

    def test_update_with_neg_height(self):
        r = Rectangle(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(90, 3, -3)

    def test_update_non_int_x(self):
        r = Rectangle(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid arg")

    def test_update_with_neg_x(self):
        r = Rectangle(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(90, 2, 7, -3)

    def test_update_with_zero_x(self):
        r = Rectangle(90, 2, 7, 3, 4)
        r.update(90, 2, 7, 0, 4)
        res = "[Rectangle] (90) 0/4 - 2/7"
        self.assertEqual(res, str(r))

    def test_update_non_int_y(self):
        r = Rectangle(89, 2, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 0, "invalid arg")

    def test_update_with_neg_y(self):
        r = Rectangle(90, 2, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(90, 2, 7, 0, -3)

    def test_update_with_zero_y(self):
        r = Rectangle(90, 2, 7, 3, 4)
        r.update(90, 2, 7, 3, 0)
        res = "[Rectangle] (90) 3/0 - 2/7"
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=15)
        res = "[Rectangle] ({}) 10/10 - 15/10".format(r.id)
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=20, width=15)
        res = "[Rectangle] ({}) 10/10 - 15/20".format(r.id)
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_width_height_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=20, id=89, width=15)
        res = "[Rectangle] (89) 10/10 - 15/20"
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_width_height_id_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=20, id=89, width=15, x=5)
        res = "[Rectangle] (89) 5/10 - 15/20"
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_width_height_id_x_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=20, id=89, y=7, width=15, x=5)
        res = "[Rectangle] (89) 5/7 - 15/20"
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_twice_all(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=20, id=89, y=7, width=15, x=5)
        r.update(width=30, id=98, y=3, x=2, height=45)
        res = "[Rectangle] (98) 2/3 - 30/45"
        self.assertEqual(res, str(r))

    def test_update_with_kwargs_with_invalid_keys(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(h=20, w=10, a=5, b=7)
        res = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(res, str(r))

    def test_update_with_only_args_if_both(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 25, width=30, x=30, id=98)
        res = "[Rectangle] (89) 10/10 - 25/10"
        self.assertEqual(res, str(r))

    def test_update_with_args_and_then_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(20, 30, 40, 50, 60)
        r.update(height=50, id=None, width=20)
        res = "[Rectangle] ({}) 50/60 - 20/50".format(r.id)
        self.assertEqual(res, str(r))


class TestRectangle_update_order(unittest.TestCase):
    """Unittest for testing the order of updating the attributes."""
    def test_update_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "width", -3)

    def test_update_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -4, 5, "invalid")

    def test_update_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "invalid width", 5, 10, "not an integer")

    def test_update_height_before_x(self):
        r = Rectangle(89, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid height", -3)

    def test_update_height_before_y(self):
        r = Rectangle(89, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, -3, 4, "not an integer")

    def test_update_x_before_y(self):
        r = Rectangle(98, 10, 20, 30, 40)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(98, 10, 20, "invalid", -4)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing the dictionary representation of a Rectangle."""
    def test_to_dictionary_representation(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r_dictionary = r.to_dictionary()
        res = {'width': 2, 'height': 3, 'x': 4, 'y': 5, 'id': 6}
        self.assertEqual(res, r_dictionary)

    def test_to_dictionary_instances_not_eq(self):
        r1 = Rectangle(3, 6, 5, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_dict_eq(self):
        r1 = Rectangle(3, 6, 5, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__dict__, r2.__dict__)

    def test_to_dictionary_and_dict_values_eq(self):
        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        self.assertEqual(set(r_dict.values()), set(r.__dict__.values()))

    def test_to_dictionary_no_arg(self):
        r = Rectangle(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            r.to_dictionary(10)


if __name__ == "__main__":
    unittest.main()
