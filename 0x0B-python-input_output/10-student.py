#!/usr/bin/python3
# 10-student.py
"""Defines a class Student."""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the dictionary representation of a Student.

        Args:
            attrs (list): (optional) Contains a list of attributes
            to be retrieved.

        If attrs is a list of strings, retrieve only attribute
        names contained in this list.
        """
        if type(attrs) is list and all(isinstance(ele, str)
                                       for ele in attrs):
            return {k: self.__dict__[k] for k in sorted(attrs)
                    if hasattr(self, k)}
        return {k: self.__dict__[k] for k in sorted(self.__dict__)}
