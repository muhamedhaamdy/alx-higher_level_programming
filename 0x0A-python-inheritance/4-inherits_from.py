#!/usr/bin/python3
"""begining of the file"""


def inherits_from(obj, a_class):
    """is same class"""

    return isinstance(obj, a_class) and not type(obj) is a_class
