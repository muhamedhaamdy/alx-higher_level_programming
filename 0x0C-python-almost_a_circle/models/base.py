#!/usr/bin/python3
"""The base file"""
import json


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init func"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation of
            list_objs to a file"""
        json_string = []
        if list_objs:
            for obj in list_objs:
                json_string.append(obj.to_dictionary())
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w') as f:
            f.write(cls.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        if not json_string or not len(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        elif cls.__name == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy
