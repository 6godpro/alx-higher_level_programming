#!/usr/bin/python3
# 5-square.py
"""Defines a class Square."""


class Square:
    """Represents a Square object."""
    def __init__(self, size=0):
        """Initializes a Square object.

        Args:
            size (int): size of the new object.
        """
        self.size = size

    @property
    def size(self):
        """Returns/sets the current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * "#")
