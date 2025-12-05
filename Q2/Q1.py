# Parsing the ranges
with open("input.txt") as file:
    lines = file.read()

ranges = lines.split(",")
boundaries = [ra.split("-") for ra in ranges]

def find_invalid_sum(start:str,end:str):
    invalid = 0
    for number in range(int(start),int(end)+1):
        number_str = str(number)
        l = len(number_str) // 2
        if len(number_str) % 2 == 0:
            if number_str[:l] == number_str[l:]:
                print(number)
                invalid += number
    return invalid

sum_invalid_IDs = 0
for bo in boundaries:
    start, end = bo
    sum_invalid_IDs += find_invalid_sum(start,end)
    print(start,end,sum_invalid_IDs)
print(f"Result: {sum_invalid_IDs}")