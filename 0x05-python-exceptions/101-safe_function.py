#!/usr/bin/python3

def safe_function(fct, *args):
    """function that executes a function safely"""
    try:
        res = fct(*args)
        return res
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file= sys.stderr)
        return None
