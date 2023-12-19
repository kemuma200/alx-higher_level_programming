#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list"""
    _length = 0
    for i in range(x):
        try:
            print(my_list[x], end="")
            _length += 1
        except IndexError:
            break;
    print("")
    return _length
        
