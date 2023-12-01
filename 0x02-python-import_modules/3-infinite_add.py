#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    summ = 0
    for i in (sys.argv - 1):
        summ += int(sys.argv[i + 1])
    print("{}".format(summ))
