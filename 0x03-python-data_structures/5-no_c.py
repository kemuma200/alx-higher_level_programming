#!/usr/bn/python3
def no_c(my_string):
    """function that removes all characters c and C from a string"""
    _cpy = [x for x in my_string if x != "c" and x != "C"]
    return ("".join(_cpy))
