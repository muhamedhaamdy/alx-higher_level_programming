#!/usr/bin/python3
"""the begining of the file"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, 'w') as f:
        return f.write(text)
