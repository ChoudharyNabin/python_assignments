"""
Question: Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number. The numbers obtained should be printed in a
comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def are_all_digits_even(number):
    is_even = True
    while number != 0:
        digit = number % 10
        if digit % 2 != 0:
            is_even = False
            break
        number = number // 10
    return is_even


res = []
for num in range(2000, 3001):
    if are_all_digits_even(num):
        res.append(str(num))

print(",".join(res))
