#!/usr/bin/python3
"""The rectangle file"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__widht = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = super().__init__(id)
