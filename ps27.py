"""
Define a function that can convert a integer into a string and print it in console.

Hints: Use str() to convert a number to string.
"""


def convert_to_string(int_value):
    """
    Converts the integer value into string
    :param int_value: the value to be converted to string
    :return: string of the integer value
    """
    return str(int_value)


value = int(input("The number: "))
print("The string of the integer is", convert_to_string(value))
