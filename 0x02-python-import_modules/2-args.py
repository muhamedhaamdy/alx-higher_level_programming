#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    if size == 1:
        print("0 arguments.")
    elif size == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(size-1))
        for i in range(1, size):
            print("{}: {}".format(i, argv[i]))
