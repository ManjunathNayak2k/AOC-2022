with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

grid = {}
max_height = 0

for line in lines:
    line = line.split('->')

    x,y = map(int, line[0].split(','))
    grid[x,y] = '#'

    for coord in line[1:]:
        x1,y1 = map(int, coord.split(','))
        while x1!=x or y1!=y:
            dx = (x1>x) - (x>x1)
            dy = (y1>y) - (y>y1)
            x += dx
            y += dy
            grid[x,y] = '#'

            max_height = max(max_height,y)

for i in range(-1000, 1000):
    grid[i, max_height+2] = '#'

done1 = done2 = False
x,y = 500,0
count1 = count2 = 0

while not done2:
    if y>=max_height:
        done1 = True
    if (x,y+1) not in grid:
        y = y+1
    elif (x-1,y+1) not in grid:
        x = x-1
        y = y+1
    elif (x+1,y+1) not in grid:
        x = x+1
        y = y+1
    else:
        if not done1:
            count1 += 1
        count2 += 1
        grid[x,y]='o'
        if (x, y) == (500, 0):
            done2 = True
        x,y = 500,0


print(count1)
print(count2)
