"""
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints: Use + to concatenate the strings
"""


def concat_str(str1, str2):
    """
    concatenates the strings
    :param str1: 1st string
    :param str2: 2nd string
    :return: the concatenated string
    """
    return str1 + str2


s1 = input("First string: ")
s2 = input("Second string: ")
print("Concatenated string:", concat_str(s1, s2))

