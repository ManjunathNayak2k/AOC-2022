with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split()

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split()


coords = set()
cur_max = 0
for line in lines:
    x,y,z = [int(x) for x in line.split(',')]
    coords.add((x,y,z))

def surrounds(x,y,z):
    return [
        (x-1,y,z),(x+1,y,z),
        (x,y-1,z),(x,y+1,z),
        (x,y,z-1),(x,y,z+1)
    ]

ans = 0
for coord in coords:
    for neighbour in surrounds(*coord):
        if neighbour not in coords:
            ans += 1

print(ans)

x_min = min(x for x,y,z in coords)
x_max = max(x for x,y,z in coords)
y_min = min(y for x,y,z in coords)
y_max = max(y for x,y,z in coords)
z_min = min(z for x,y,z in coords)
z_max = max(z for x,y,z in coords)

def check(x,y,z):
    visited = set()
    to_check = [(x,y,z)]
    reaches_out = False

    while True:
        if len(to_check) == 0:
            break
        cur = to_check.pop()
        while cur in visited:
            if len(to_check) == 0:
                break
            cur = to_check.pop()
        visited.add(cur)
        (x,y,z) = cur
        if (x,y,z) in coords:
            continue
        if x<x_min or x>x_max or y<y_min or y>y_max or z<z_min or z>z_max:
            reaches_out = True
            break

        to_check = to_check + surrounds(*cur)

    return reaches_out

limit = 25

for z in range(limit):
    for y in range(limit):
        for x in range(limit):
            if not check(x,y,z) and (x,y,z) not in coords:
                coords.add((x,y,z))

ans = 0
for coord in coords:
    for neighbour in surrounds(*coord):
        if neighbour not in coords:
            ans += 1

print(ans)
