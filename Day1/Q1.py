with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

def rotation(rot:str, point):
    direction = rot[0]
    number = int(rot[1:])
    if direction == "R":
        return (point + number) % 100
    else:
        return (point - number) % 100

point = 50
pswd = 0 
for line in lines:
    old_point = point
    point = rotation(line,point)
    print(old_point,line,point)
    if point == 0:
        pswd += 1
print(pswd)