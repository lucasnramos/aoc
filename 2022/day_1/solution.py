#!/bin/env/python3

import os

# part 1
def getInput():
    dir = os.path.dirname(__file__)
    return open(os.path.join(dir, "./input.txt"), "r")
    
lines = getInput().readlines()
current_sum = 0
elves = list()
t1, t2, t3 = 0, 0, 0

for el in lines:
    if el != '\n':
        current_sum += int(el)
    else:
        elves.append(current_sum)
        if current_sum > t3:
            if current_sum < t2:
                t3 = current_sum
            elif current_sum < t1:
                t2, t3 = current_sum, t2
            else:
                t1, t2, t3 = current_sum, t1, t2
        current_sum = 0

new_sum = t1 + t2 + t3
for line in lines:
    if line == "" or line == "\n":
        current_sum = 0
    else:
        current_sum += int(line)

elves.sort()
print(elves.pop()) # part one solution
print(new_sum) # part two solution
