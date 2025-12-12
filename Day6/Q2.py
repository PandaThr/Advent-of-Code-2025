# Solution of Day 5 Q2
import math
with open("input.txt") as file:
    lines = file.readlines()
digit_len = len(lines) 
col_len = len(lines[-1])
print(digit_len,col_len)
agg_lines = []
op = []
save_op =""
for i in range(col_len):
    temp = ""
    for k in range(digit_len):
        ch = lines[k][i] # parse column-wise digits
        temp += ch 
    temp = temp.replace(" ", "")
    if temp != "":
        if temp[-1] == "+" or temp[-1] == "*":
            save_op = temp[-1]
            op.append(int(temp[:-1]))
        else:
            op.append(int(temp))
    else:
        op.append(save_op)
op.append(save_op) # Last operation does not have " ", this will cover the last one
res = 0
index = 0
op_count = 0
for i in range(len(op)):
    if op[i] == "+" or op[i] =="*":
        if op[i] == "+":
            res += sum(op[index:i])
            op_count+=1
        else:
            res += math.prod(op[index:i])
            op_count+=1
        index = i+1
print(f"Result: {res}")