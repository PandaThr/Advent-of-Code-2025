with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

def find_splitter(line):
    res = []
    for i in range(len(line)):
        if line[i] == "^":
            res.append(i)
    return res
# print(lines)
index = lines[0].find("S")
col = set()
col.add(index)
res = 0
for i in range(1,len(lines)):
    oc = find_splitter(line=lines[i]) 
    if len(oc) != 0:
        # print(f"splitter: {oc}")
        temp = set()
        for c in col:
            if c in oc:
                temp.add(c-1)
                temp.add(c+1)
                res +=1
            else:
                temp.add(c)
        col = temp
print(f"Result: {res}")