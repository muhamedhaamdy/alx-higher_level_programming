#!/usr/bin/python3
def safe_print_integer(value):
    b = True
    try:
        num = int(value)
        if float(value).is_integer():
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        return False
 
