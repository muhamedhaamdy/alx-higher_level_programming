#!/usr/bin/python3
"""the begining of the file"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            rasie ValueError("<name> must be greater than 0")