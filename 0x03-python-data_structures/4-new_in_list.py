#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = list(my_list)
    x = 0
    for i in newlist:
        if x + 1 == idx:
            newlist[i] = element
        x += 1
    return newlist
