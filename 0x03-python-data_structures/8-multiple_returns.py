#!/usr/bin/python3
def multiple_returns(sentence):
    """ function that returns a tuple with the length of a string and its first character"""
    if len(sentence) == 0:
        return ("{}, {}".format(0, None)
    return ("{}, {}".format(len(sentence), sentence[0]))
