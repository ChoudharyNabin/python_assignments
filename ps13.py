"""
Question: Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program: hello world! 123
Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""


sentence = input("Enter the sentence: ")
letter_count = 0
digit_count = 0
for item in sentence:
    if item.isdigit():
        digit_count += 1
    if item.isalpha():
        letter_count += 1

print("LETTERS " + str(letter_count) + " DIGITS " + str(digit_count))

