#!/usr/bin/python3

def max_integer(my_list=[]):
    """function that finds the biggest integer of a list"""
    
    if len(my_list) == 0:
        return None
    
    _max = 0
    for x in range(len(my_list)):
        if my_list[x] > _max:
            _max = my_list[x]
        return _max
