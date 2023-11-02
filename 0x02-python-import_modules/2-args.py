#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    print("{} arguments:".format(size-1))
    for i in range(size - 1):
        print("{}: {}".format(i + 1, argv[i]))
