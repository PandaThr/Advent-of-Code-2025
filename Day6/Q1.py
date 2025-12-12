# Solution of Day 5 Q1
import math
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

lines = [ra.split(" ") for ra in lines]
agg_lines = []
for line in lines:
    temp = []
    for l in line:
        if l != "":
            temp.append(l)
    agg_lines.append(temp)
res = 0
for index in range(len(agg_lines[-1])):
    temp = []
    for k in range(len(agg_lines)-1):
        temp.append(int(agg_lines[k][index]))
    if agg_lines[-1][index] == "+":
        res += sum(temp)
    else:
        res += math.prod(temp)
print(f"Result: {res}")
