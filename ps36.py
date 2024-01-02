"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the keys only.

Hints: Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number.
Use range() for loops. Use keys() to iterate keys in the dictionary.
Also we can use item() to get key/value pairs.
"""


def print_dict():
    square_map = dict()
    for i in range(1,21):
        square_map[i] = i ** 2
    square_map_keys = []
    for key in square_map.keys():
        square_map_keys.append(str(key))

    return ",".join(square_map_keys)


print(print_dict())

