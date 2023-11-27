#!/usr/bin/python3
"""Hello with the start of the file"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """inittial function"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def __str__(self):
        """represernt a string"""
        s = ""
        if not self.__height or not self.__width:
            return ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                s += ("#")
            if i != self.__height - 1:
                s += ("\n")
        return s

    def __repr__(self):
        """represernt a string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete the isinstance"""
        print("Bye rectangle...")

    def area(self):
        """calculate the area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter"""
        if not self.__width or not self.height:
            return 0
        return 2 * (self.__width + self.__height)
