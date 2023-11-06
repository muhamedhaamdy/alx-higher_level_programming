#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = -10000000
    for i in my_list:
        if mx < i:
            mx = i
    return mx
