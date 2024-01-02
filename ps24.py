"""
Question: Python has many built-in functions, and if you do not know how to use it,
you can read document online or find some books. But Python has a built-in document function for
every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(),
raw_input(). And add document for your own function

Hints: The built-in document method is doc
"""

print("-----abs() method documentation-----\n", abs.__doc__)
print("\n-----int() method documentation-----\n", int.__doc__)
print("\n-----input() method documentation-----\n", input.__doc__)


def calc_square(number):
    """
    Calculates the square of a number
    :param number: integer value for which the square value is to be calculated
    :return: returns the square of a number
    """
    square = number ** 2
    return square


print(calc_square(5))
print("\n-----calc_square() method documentation-----\n", calc_square.__doc__)
