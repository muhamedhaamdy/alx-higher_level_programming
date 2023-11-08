#!/usr/bin/python3
def weight_average(my_list=[]):
    summation = 0
    dev = 0
    for i in my_list:
        summation += i[0] * i[1]
        dev += i[1]
    return summation / dev
