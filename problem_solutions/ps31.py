"""
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.

Hints: Use len() function to get the length of a string
"""


def max_len(str1, str2):
    """
    prints the string with maximum length
    :param str1: 1st string
    :param str2: 2nd string
    :return: string with the maximum length
    """
    if len(str1) > len(str2):
        return str1
    elif len(str1) == len(str2):
        return str1, str2
    else:
        return str2


s1 = input("First string: ")
s2 = input("Second string: ")
print(max_len(s1, s2))

