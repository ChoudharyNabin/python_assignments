"""
Define a function which can compute the sum of two numbers.

Hints: Define a function with two numbers as arguments.
You can compute the sum in the function and return the value.
"""


def calc_sum(num1, num2):
    """
    Calculates the sum of two numbers
    :param num1: 1st number
    :param num2: 2nd number
    :return: total sum of two numbers
    """
    return num1 + num2


n1 = int(input("First number: "))
n2 = int(input("Second number: "))
print("Sum:", calc_sum(n1, n2))

