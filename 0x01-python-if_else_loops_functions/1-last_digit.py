#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final = abs(number) % 10
greet = " "
if number < 0:
    final = -final
if (final > 5):
    greet = "and is greater than 5"
elif (final == 0):
    greet = "and is 0"
else:
    greet = "and is less than 6 and not 0"
print(f"Last digit of {number} is {final} {greet}")
