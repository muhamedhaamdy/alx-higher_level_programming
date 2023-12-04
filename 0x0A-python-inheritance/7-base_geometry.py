#!/usr/bin/python3
"""the begining of the file"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        """get the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value of the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            rasie ValueError("{} must be greater than 0".format(name))
