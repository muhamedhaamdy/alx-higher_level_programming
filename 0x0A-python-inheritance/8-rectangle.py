#!/usr/bin/python3
"""the begining of the file"""


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
