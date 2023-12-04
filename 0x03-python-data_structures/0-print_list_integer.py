#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function that prints all integers of a list"""
    i = 0
    for i in len(my_list):
        if int(my_list[i]) == i:
            print(str.format(my_list[i]))
