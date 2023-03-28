#!/usr/bin/python3
# 100-singly_linked_list.py
"""Defines a class Node."""


class Node:
    """Represents a Node class."""

    def __init__(self, data, next_node=None):
        """Initializes a Node object.

        Args:
            data (int): value to be assigned to the data attribute.
            next_node (Node): Node to """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns/sets the data of the current node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns/sets the next node of the cuurent node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a SinglyLinkedList object."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList."""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the string representation of a SinglyLinkedList"""
        tmp = self.__head
        while tmp is not None:
            print(tmp.data, end="")
            if tmp.next_node is not None:
                print("")
            tmp = tmp.next_node
        return ""
