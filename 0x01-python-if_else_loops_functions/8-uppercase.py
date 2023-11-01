#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        char = str[i]
        if str[i] >= 'a' and str[i] <= 'z':
            char = chr(ord(str[i]) - 32)
        if i == len(str) - 1 or char == '':
            print(char)
        else:
            print("{}".format(char), end="")
