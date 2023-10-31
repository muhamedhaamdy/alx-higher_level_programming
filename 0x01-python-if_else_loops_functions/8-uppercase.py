#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if i == len(str):
            print(str[i])
        else:
            print("{}".format(str[i] - 32), end="")
