"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.

Hints: Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""


def list_slicing_3():
    square_values = list()
    for i in range(1, 21):
        square_values.append(i ** 2)
    return square_values[5:]


print(list_slicing_3())



