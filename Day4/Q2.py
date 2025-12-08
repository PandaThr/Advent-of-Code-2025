# Solution of Day 4 Q1

def print_matrix(matrix):
    for m in matrix:
        str_l=""
        for l in m:
            str_l+=str(l)
        print(str_l)

matrix = []
with open("input.txt") as file:
    for line in file.readlines():
        ls = [0]
        for char in line:
            if char == "@":
                ls.append(1)
            if char == ".":
                ls.append(0)
        ls = ls + [0]
        
        matrix.append(ls)
matrix = [[0] * (len(matrix)+2)] + matrix + [[0] * (len(matrix)+2)]
print_matrix(matrix)
n = len(matrix)
count = 0
mark = []
stage_mark = 1
while stage_mark >0:
    stage_mark = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            temp = 0
            if matrix[i][j] == 1:
                temp = int(matrix[i][j-1] == 1) + int(matrix[i][j+1] == 1) + \
                int(matrix[i-1][j-1] == 1) + int(matrix[i-1][j+1] == 1) +\
                int(matrix[i+1][j-1] == 1) + int(matrix[i+1][j+1] == 1) +\
                int(matrix[i-1][j] == 1) + int(matrix[i+1][j] == 1)
                if temp < 4:
                    mark.append([i,j])
                    stage_mark+=1
                    # print(f"i:{i},j:{j}, temp: {temp}, count: {count}")
    for m in mark:
        matrix[m[0]][m[1]] = 0
    count += stage_mark
    print("="*25)
    print_matrix(matrix)
    print(f"Removed items in this stage: {stage_mark}")
print(f"Result: {count}")
