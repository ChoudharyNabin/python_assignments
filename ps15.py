"""
Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a
Suppose the following input is supplied to the program: 9
Then, the output should be: 11106

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""

a = input("Enter the value of a: ")
a1 = int(a * 2)
a2 = a * 3
a3 = a * 4
print(int(a) + int(a1) + int(a2) + int(a3))
