#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = False
    try:
        for i in range(0, x):
            print(my_list[i], end="")
    except IndexError:
        b = True
        break
    finally:
        print()
        return (i if b else i + 1)
