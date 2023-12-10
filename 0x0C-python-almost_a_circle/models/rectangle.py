#!/usr/bin/python3
"""The rectangle file"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """return the arrea of the rectangle"""
        return self.__widht * self.__height

    def display(self):
        """display the rectangel with the character #"""
        for i in range (0, self.__y):
            print()
        for i in range(0, self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """returns the string representation of an object."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
        """update the rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']
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
