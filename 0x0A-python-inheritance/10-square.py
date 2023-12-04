#!/usr/bin/python3
"""the begining of the file"""
Rectangle = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return super().__str__
