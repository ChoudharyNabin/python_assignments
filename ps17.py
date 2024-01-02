"""
Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program:
D 300 D 300 W 200 D 100
Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""


deposit_list = []
withdrawal_list = []
while True:
    tr_log = input("Enter the transaction logs: ")
    if len(tr_log) == 0:
        break
    if "D" in tr_log:
        deposit_list.append(int((tr_log.split(" "))[1]))
    elif "W" in tr_log:
        withdrawal_list.append(int((tr_log.split(" "))[1]))

print(sum(deposit_list) - sum(withdrawal_list))
