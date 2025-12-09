# Solution of Day 5 Q2
with open("input.txt") as file:
    lines = file.read()

ranges = lines.split("\n")
boundaries = [ra.split("-") for ra in ranges[:177]]
boundaries = [[int(a),int(b)] for a,b in boundaries]

def merge(intervals): # LeetCode Challenge #56 
        intervals.sort(key=lambda x: x[0])
        new_interval = [intervals[0]]
        for i in range(1,len(intervals)):
            if new_interval[-1][1] < intervals[i][0]:
                new_interval.append(intervals[i])
            else:
                if new_interval[-1][1] < intervals[i][1]:
                    new_interval[-1][1] = intervals[i][1]
        return new_interval


merged_array = merge(boundaries)
print(merged_array)
res = 0
for m in merged_array:
    a,b = m
    res += b-a+1


print(f"Result: {res}")