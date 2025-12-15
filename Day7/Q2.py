with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
total_row = len(lines)
def find_splitter(line):
    res = []
    for i in range(len(line)):
        if line[i] == "^":
            res.append(i)
    return res
startIndex = lines[0].find("S") # Fixed starting
'''
    Split every time if the ray touches the splitter. If it touches it creates tow path, follow until reaching total_row-1 . I just want to do it with recursion
'''
splitter_positions = []
for line in lines:
    splitter_positions.append(find_splitter(line))
print(splitter_positions)
state = {}
def follow_rays(colIndex:int,rowIndex:int):
    if (colIndex,rowIndex) in state: # This is basically required since the input data row size is > 50
        return state[(colIndex,rowIndex)]
    splitterPositions = splitter_positions[rowIndex]
    print(f"Row: {rowIndex,colIndex}, Splitter: {splitterPositions}")
    if rowIndex < total_row-1:
        if colIndex in splitterPositions:
             state[(colIndex,rowIndex)] = follow_rays(colIndex+1,rowIndex+1) + follow_rays(colIndex-1,rowIndex+1) # This relies on the input data structure that in the col=0 and col= end, we do not have splitters.
             return state[(colIndex,rowIndex)]
        else:
            state[(colIndex,rowIndex)] = follow_rays(colIndex,rowIndex+1)
            return state[(colIndex,rowIndex)]
    else:
        return 1
print(follow_rays(startIndex,0))