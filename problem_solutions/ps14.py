"""
Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world!
Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""


case_count_dict = {"UPPER CASE": 0, "LOWER CASE": 0}
sentence = input("Enter the sentence: ")
for char in sentence:
    if char.isupper():
        case_count_dict["UPPER CASE"] += 1
    elif char.islower():
        case_count_dict["LOWER CASE"] += 1
    else:
        pass

print("UPPER CASE " + str(case_count_dict["UPPER CASE"]) + " LOWER CASE " + str(case_count_dict["LOWER CASE"]))
