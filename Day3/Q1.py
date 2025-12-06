# Solution of Day 3 Q1
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
jolt_max = 0
for line in lines:
    idx_1, idx_2,mem = 0, 0, 0
    # Two pointer, O(n) for each line
    while idx_2 < len(line)-1:
        if int(line[idx_2 +1])>int(line[idx_1]) and idx_2 + 1  < len(line)-1:
            idx_1 = idx_2+1
            mem = 0
        else:
            if int(line[idx_2 + 1])>mem:
                mem = int(line[idx_2 + 1])
        idx_2+=1
    print(int(line[idx_1])*10+mem)
    jolt_max += int(line[idx_1])*10+mem
print(f"Result: {jolt_max}")
    