# Solution of Day 4 Q1

def print_matrix(matrix):
    for m in matrix:
        print(m)
matrix = []
with open("input.txt") as file:
    matrix = ["." + line.rstrip() + "." for line in file]
matrix = ["." * (len(matrix)+2)] + matrix + ["." * (len(matrix)+2)]
n = len(matrix)
print_matrix(matrix=matrix)
count = 0
for i in range(1,n-1):
    for j in range(1,n-1):
        temp = 0
        if matrix[i][j] == "@":
            temp = int(matrix[i][j-1] == "@") + int(matrix[i][j+1] == "@") + \
            int(matrix[i-1][j-1] == "@") + int(matrix[i-1][j+1] == "@") +\
            int(matrix[i+1][j-1] == "@") + int(matrix[i+1][j+1] == "@") +\
            int(matrix[i-1][j] == "@") + int(matrix[i+1][j] == "@")
            if temp < 4:
                count +=1
                print(f"i:{i},j:{j}, temp: {temp}, count: {count}")
print(f"Result: {count}")
