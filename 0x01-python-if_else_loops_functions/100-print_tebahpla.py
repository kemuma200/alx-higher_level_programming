#!/usr/bin/python3
f = 0
for c in range(122, 96, -1):
    print("{}".format(chr(c - f)), end="")
    if f == 0:
        f = 32
    else:
        f = 0
