#!/usr/bin/python3
# 6-square.py
"""Defines a class Square."""


class Square:
    """Represents a Square object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square object.

        Args:
            size (int): size of the new object.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns/set the current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns/sets the current square position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple or \
           not all(type(n) is int for n in value) or \
           len(value) != 2 or \
           not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square using the # character."""
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                print(self.__size * "#")

    def __str__(self):
        """Returns the string representation of a square."""
        if self.__size == 0:
            return ""
        else:
            string = "".join(["\n" for i in range(self.__position[1])])
            for i in range(self.__size):
                string += "".join([" " for i in range(self.__position[0])])
                string += "".join(["#" for i in range(self.__size)])
                if i != self.__size - 1:
                    string += "\n"
            return (string)
