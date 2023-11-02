#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summation = 0
    for i in range(1, len(argv)):
        summation += int(argv[i])
    print(summation)
