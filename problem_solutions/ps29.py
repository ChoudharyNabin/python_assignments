"""
Define a function that can receive two integral numbers in string form and compute their sum and
then print it in console.

Hints: Use int() to convert a string to integer.
"""


def calc_sum(s1, s2):
    """
    calculates the sum of two integral numbers in string form
    :param s1: first string integer
    :param s2: second string integer
    :return: the sum of the integers in string form
    """
    return int(s1) + int(s2)


n1 = input("1st string number: ")
n2 = input("2nd string number: ")
print("Sum:", calc_sum(n1, n2))

