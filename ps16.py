"""
Question: Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
Then, the output should be: 1,3,5,7,9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""


seq = input("Enter the sequence: ").split(",")
odd_num_list = [x for x in seq if int(x) % 2 != 0]
print(",".join(odd_num_list))

