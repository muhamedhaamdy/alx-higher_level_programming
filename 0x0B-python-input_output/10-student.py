#!/usr/bin/python3
"""the begining of the file"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {item: getattr(self, item)
                    for item in attrs if hasattr(self, item)}
        return self.__dict__
