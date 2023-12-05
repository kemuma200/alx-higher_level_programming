#!/usr/bn/python3
def no_c(my_string):
    """function that removes all characters c and C from a string"""
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] =="C":
            my_string[i] = ""
        return my_string
