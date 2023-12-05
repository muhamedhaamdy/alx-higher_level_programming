#!/usr/bin/python3
"""the begining of the file"""


def append_write(filename="", text=""):
    """write to a file"""
    with open(filename, 'a') as f:
        return f.write(text)
