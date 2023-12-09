#!/usr/bin/python3
"""The rectangle file"""
Base = __import__('base').Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__widht = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = super().id
