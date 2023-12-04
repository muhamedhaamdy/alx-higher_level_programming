#!/usr/bin/python3
"""begining of the file"""


def is_same_class(obj, a_class):
    """is same class"""
    if type(obj) is type(a_class):
        return True
    else:
        return False
