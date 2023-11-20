#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_of_int = 1
    for i in range(0, x):
        try:
            num =  int(my_list[i])
            print("{:d}".format(num), end="")
            num_of_int += 1
        except (ValueError, TypeError):
            continue
    print()
    return num_of_int - 1
