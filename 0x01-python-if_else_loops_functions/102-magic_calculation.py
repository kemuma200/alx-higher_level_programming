#!/usr/bin/python3
def magic_calculation(a, b, c):
    """function that does exactly the same as the following Python bytecode"""
    if a < b:
        return c
    if c > b:
        return (a + b)
    return (a*b - c)
