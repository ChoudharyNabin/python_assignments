"""
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included)
and the values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
"""


def print_dict():
    square_map = {}
    for i in range(1,4):
        square_map[i] = i ** 2
    return square_map


print(print_dict())

