"""
Define a function which can generate and print a list where the values are square of numbers
between 1 and 20 (both included).

Hints: Use ** operator to get power of a number. Use range() for loops.
Use list.append() to add values into a list.
"""


def square_values_in_list():
    square_values = []
    for i in range(1, 21):
        square_values.append(str(i ** 2))

    return ",".join(square_values)


print(square_values_in_list())


