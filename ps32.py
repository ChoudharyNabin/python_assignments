"""
Define a function that can accept an integer number as input and print the "It is an even number"
if the number is even, otherwise print "It is an odd number".

Hints: Use % operator to check if a number is even or odd.
"""


def is_odd_or_even(num):
    """
    checks if the number is odd or even
    :param num: number to be checked
    :return: "It is an odd number" if the number is odd
             "It is an even number" if the number is even
    """
    if num % 2 == 0:
        return "It is an even number"
    else:
        return "It is an odd number"


number = int(input("Enter the number: "))
print(is_odd_or_even(number))

