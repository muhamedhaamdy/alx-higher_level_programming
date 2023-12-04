#!/usr/bin/python3
"""begining of the file"""


class MyList(list):
    """my list class"""

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
