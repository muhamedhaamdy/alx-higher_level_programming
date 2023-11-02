#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    print("{} arguments:".format(size-1))
    for i in range (1, size):
        print("{}: {}".format(i, argv[i]))
