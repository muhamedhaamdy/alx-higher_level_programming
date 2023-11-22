#!/usr/bin/python3
""" Square """


class Square:
    """ square class """
    def __init__(self, size=0, position=(0, 0)):
        """ initial function """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """The position property."""
        return self.__position

    @position.setter
    def position(self, value):
        """Getter"""
        if type(value) is tuple:
            if(type(value[0]) is int and value[0] >= 0 and type(value[1]) is int and value[1] >= 0):
                self.__position = Value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        """ calulate the area """
        return self.__size * self.__size

    def my_print(self):
        """ print the square """
        if not self.__size:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
        
