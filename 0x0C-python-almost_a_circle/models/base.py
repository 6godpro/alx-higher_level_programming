#!/usr/bin/python3
# base.py
"""Defines a class Base."""

import csv
import json


class Base:
    """Represents a Base object."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates a Base object

        Args:
            id (int): The id of the object.

        The goal of this class is to manage the id attribute of
        all other classes in thid project.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list):"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'

        if type(list_dictionaries) is list and \
           all(type(item) is dict for item in list_dictionaries):
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): This is a string representing a list of
                                dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): This is a list of objects that inherit
                              (directly or indirectly) from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write(json.dumps([]))
            else:
                if type(list_objs) is list and \
                   all(isinstance(obj, Base) for obj in list_objs):
                    obj_dict_list = [o.to_dictionary() for o in list_objs]
                    f.write(Base.to_json_string(obj_dict_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename) as f:
                content = f.read()
                list_dict = Base.from_json_string(content)
                if type(list_dict) is list and \
                   all(isinstance(d, dict) for d in list_dict):
                    return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV representation of list_objs to a file.

        Args:
            list_objs (list): This is a list of objects that inherit
                              (directly or indirectly) from Base.
        """
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if type(list_objs) is list and \
                   all(isinstance(obj, Base) for obj in list_objs):
                    obj_dict_list = [o.to_dictionary() for o in list_objs]
                    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
                    csvwriter.writeheader()
                    csvwriter.writerows(obj_dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename) as csvfile:
                csvreader = csv.DictReader(csvfile)
                list_dict = [{k: int(v) for k, v in d.items()}
                             for d in csvreader]
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
