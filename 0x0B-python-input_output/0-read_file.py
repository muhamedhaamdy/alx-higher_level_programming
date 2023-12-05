#!/usr/bin/python3
"""the begining of the file"""


def read_file(filename=""):
    """read a file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
