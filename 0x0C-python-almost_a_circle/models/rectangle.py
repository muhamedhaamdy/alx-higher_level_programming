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


