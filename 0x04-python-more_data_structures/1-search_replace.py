#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for x in new_list:
        if x == search:
            x = replace
    return (new_list)
