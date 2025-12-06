with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

def rotation(rot:str, point):
    direction = rot[0]
    number = int(rot[1:])
    full_rot = 0
    if direction == "R":
        res = (point + number) % 100
        full_rot = (point + number) // 100
        return res, full_rot
    else:
        res = (point - number) % 100
        full_rot = number // 100
        if point != 0:
             full_rot += (point <= number % 100)
        return res, full_rot

point = 50
pswd = 0 
for line in lines:
    old_point, old_pswd = point, pswd
    point,full_rot = rotation(line,point)
    pswd += full_rot
print(pswd)