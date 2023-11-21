#!/usr/bin/python3
""" Square """


class Square:
    """ square class """
    def __init__(self, size=0):
        """ initial function """
        self.__size = size

    @property
    def size(self):
        """ Getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter """
        if type(size) is int and size >= 0:
            self.__size = size
        elif type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ calulate the area """
        return self.__size * self.__size

    def my_print(self):
        """ print the square """
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if not self.__size:
            print()
