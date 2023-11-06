#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    if len(my_list) == 0:
        return None
    j = 0
    for i in my_list:
        if i % 2 == 0:
            new_list[j] = True
        else:
            new_list[j] = False
        j += 1
    return new_list
