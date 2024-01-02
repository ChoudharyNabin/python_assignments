"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also, please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""


class String:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter the string: ")

    def print_string(self):
        print(self.s.upper())


string = String()
string.get_string()
string.print_string()
