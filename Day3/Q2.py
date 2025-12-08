# Solution of Day 3 Q2
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
jolt_max = 0
for line in lines:
    dict_count = {}
    print(line)
    idx_lst = [d for d in range(len(line)-12,len(line),1)]
    idx = -1
    k = 0
    jolt = ""
    # O(n)
    for k in range(12): 
        temp = min(len(line)-1,idx_lst[k]+1)
        for i in range(min(len(line)-1,idx_lst[k]),idx,-1):
            if int(line[i]) >= int(line[idx_lst[k]]):
                idx_lst[k] = i
        idx = idx_lst[k]
        
    print(idx_lst)
    for i in idx_lst:
        jolt += line[i]
    print(jolt)
    print("="*100)
    jolt_max += int(jolt) 
print(f"Result: {jolt_max}")
    