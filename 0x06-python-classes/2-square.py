#!/usr/bin/python3
""" Square """


class Square:
    """ square class """
    def __init__(self, size = 0):
        """ initial function """
        if type(size) == int and size >= 0:
            self.__size = size
        elif type(size) == int and size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
