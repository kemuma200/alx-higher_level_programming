#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase form"""
    for c in str:
        if ord(c) >= 97 and ord() <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
