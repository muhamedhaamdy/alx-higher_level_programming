#!/usr/bin/python3
def element_at(my_list, idx):
    ans = None
    for i in range(len(my_list)):
        if i == idx:
            ans = my_list[i]
    return (ans)
