"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the values only.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary.
Also we can use item() to get key/value pairs.
"""


def print_dict():
    square_map = {}
    for i in range(1, 21):
        square_map[i] = i ** 2
    square_values = []
    for key, value in square_map.items():
        square_values.append(str(value))
    return ",".join(square_values)


print(print_dict())


