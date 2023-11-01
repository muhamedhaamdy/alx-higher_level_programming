#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ans = 10 - (number % 10)
        if ans == 10:
            ans = 0
    else:
        ans = number % 10
    print(ans, end="")
    return ans
