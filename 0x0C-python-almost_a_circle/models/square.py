#!/usr/bin/python3
"""the squre file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size property."""
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns the string representation of an object."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):
        """Update the square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

