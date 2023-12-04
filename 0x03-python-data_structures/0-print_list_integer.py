#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function that prints all integers of a list"""
    for i in range(len(my_list)):
        if int(my_list[i]) == i:
            print("{:d}".format(my_list[i]))
