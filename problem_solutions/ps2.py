"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def factorial(number):
    fact = 1
    while number != 0:
        fact = number * fact
        number -= 1
    return fact


nums = input("Enter the numbers: ")
nums_list = nums.split(",")
fact_res = []
for num in nums_list:
    fact_res.append(str(factorial(int(num))))
print(",".join(fact_res))

