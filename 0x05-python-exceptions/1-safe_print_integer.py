#!/usr/bin/python3
def safe_print_integer(value):
    b = True
    try:
        num = int(value)
        print("{:d}".format(num))
    except ValueError:
         b = False
    finally:
        return b
