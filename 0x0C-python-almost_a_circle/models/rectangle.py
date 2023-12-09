#!/usr/bin/python3
"""The rectangle file"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if isinstance(width, int):
            if width > 0:
                self.__widht = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")
        
        if isinstance(x, int):
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x  must be >= 0")
        else:
            raise TyepError("x must be an integer")
        
        if isinstance(y, int):
            if y >= 0:
                self.__x = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TyepError("y must be an integer")


    def area(self):
        """return the arrea of the rectangle"""
        return self.__widht * self.__height

    def display(self):
        """display the rectangel with the character #"""
        for i in range(0, self.__height):
            print('#' * self.__widht)

    @property
    def width(self):
        """The width property."""
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
             raise ValueError("width  must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height  must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """The x property."""
        return self.__x
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x  must be > 0")
        self.__x = value

    @property
    def y(self):
        """The y property."""
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y  must be > 0")
        self.__y = value


