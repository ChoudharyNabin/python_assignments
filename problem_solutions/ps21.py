"""
Question: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN,
LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 .
The numbers after the direction are steps. Please write a program to compute the distance from current position after
a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2
Then, the output of the program should be: 2

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""


import math

curr_pos = [0, 0]
final_pos = [0, 0]
while True:
    move = input("Enter the movement: ")
    if len(move) == 0:
        break
    direction, steps = move.split(" ")
    if direction == "UP":
        final_pos[1] += int(steps)
    elif direction == "DOWN":
        final_pos[1] -= int(steps)
    elif direction == "LEFT":
        final_pos[0] -= int(steps)
    elif direction == "RIGHT":
        final_pos[0] += int(steps)

distance = round(math.sqrt((final_pos[0] - curr_pos[0]) ** 2 + (final_pos[1] - curr_pos[1]) ** 2))
print(distance)
