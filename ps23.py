"""
Question: Write a method which can calculate square value of number
Hints: Using the ** operator
"""


def calc_square(number):
    """
       Calculates the square of a number
       :param number: integer value for which the square value is to be calculated
       :return: returns the square of a number
    """
    square = number ** 2
    return square


num = int(input("Enter the number: "))
print(calc_square(num))

