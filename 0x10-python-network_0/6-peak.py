#!/usr/bin/python3
"""Technical interview preparation"""


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers'''

    if not len(list_of_integers):
        return None
    for i in range(0, len(list_of_integers) - 1):
        if not i and list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
        elif i and list_of_integers[i] > list_of_integers[i-1]\
                and list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
    return list_of_integers[len(list_of_integers) - 1]
