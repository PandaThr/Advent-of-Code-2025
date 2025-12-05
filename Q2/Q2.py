# Solution of Day 2 Q2
# Parsing the ranges
with open("input.txt") as file:
    lines = file.read()

ranges = lines.split(",")
boundaries = [ra.split("-") for ra in ranges]

def find_invalid_sum(start:str,end:str):
    invalid = 0
    for number in range(int(start),int(end)+1):
        number_str = str(number)
        i = 1
        rep_bool = False
        # One could do this with recursion, 
        # but given input this is good enough
        while len(number_str) > i and not(rep_bool):
            sub_str = number_str[:i]
            temp = sub_str
            while len(temp)<=len(number_str):
                if temp == number_str:
                    print(number)
                    invalid += number
                    rep_bool = True
                temp += sub_str
            i += 1
        
    return invalid

sum_invalid_IDs = 0
for bo in boundaries:
    start, end = bo
    sum_invalid_IDs += find_invalid_sum(start,end)
    print(start,end,sum_invalid_IDs)
print(f"Result: {sum_invalid_IDs}")