#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers from 0 to 100"""
    """Multipkes of both 3 and 5 produce fizzbuzz output"""
    """Multiples of 3 get Fizz"""
    """Multiples of 5 get Buzz"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif i % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
