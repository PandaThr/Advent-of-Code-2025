# Solution of Day 5 Q1

with open("input.txt") as file:
    lines = file.read()

ranges = lines.split("\n")
boundaries = [ra.split("-") for ra in ranges[:177]]
IDs = [ra.rstrip() for ra in ranges[178:]]
def check_in_range(number):
    for el in boundaries:
        start,end = el
        if int(start) <= number and int(end) >= number:
            return True
    return False
res = 0
for id_n in IDs:
    res += check_in_range(int(id_n))

print(f"Result: {res}")