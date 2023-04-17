#!/usr/bin/python3
# square.py
"""Defines a class Square."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square.

        Args:
            size (int): The size of the new square.
            x (int): The x position of the new square.
            y (int): The y position of the new square.
            id (int): The id of the new square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the current Square."""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.size))

    @property
    def size(self):
        """Gets/Sets the size attribute of the currrent Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square instance with new attributes."""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
