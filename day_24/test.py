with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().strip().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

map = {}
walls = set()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        map[x,y] = []
        if c in ['^','<','>','v']:
            map[x,y].append(c)
        if c == '#':
            walls.add((x,y))

walls |= {(x,-1) for x in [-1,0,1]}
max_x = max([x for x,y in map.keys()])
max_y = max([y for x,y in map.keys()])

cur = set([(1,0)])
ends = [(max_x-1, max_y), (1,0), (max_x-1, max_y)]

moves = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]

def insert_val(new_map, key, val):    
    if val == '^':
        if key[1] == 1:
            new_map[(key[0],max_y-1)].append(val)
        else:
            new_map[(key[0],key[1]-1)].append(val)
    if val == '<':
        if key[0] == 1:
            new_map[(max_x-1,key[1])].append(val)
        else:
            new_map[(key[0]-1,key[1])].append(val)
    if val == '>':
        if key[0] == max_x-1:
            new_map[(1,key[1])].append(val)
        else:
            new_map[(key[0]+1,key[1])].append(val)
    if val == 'v':
        if key[1] == max_y-1:
            new_map[(key[0],1)].append(val)
        else:
            new_map[(key[0],key[1]+1)].append(val)

def print_map():
    global map

    for y in range(max_y+1):
        for x in range(max_x+1):
            key = (x,y)
            values = map[key]
            if key in [(1,0), (max_x-1, max_y)]:
                print('.', end='')
            elif key in walls:
                print('#', end='')
            elif len(values) > 1:
                print(len(values), end='')
            elif len(values) == 0:
                print('.', end='')
            else:
                print(values[0], end='')
        print()

time = 0
while len(ends) > 0:
    time += 1

    new_map = dict([(key,[]) for key in map.keys()])
    for key, values in map.items():
        if len(values) != 0:
            for val in values:
                insert_val(new_map, key, val)
    
    for key, values in new_map.items():
        map[key] += values
    map = new_map
    
    blizzards = set(x for x in map.keys() if len(map[x])>0)
    new_moves = {(x+dx,y+dy) for dx,dy in moves for x,y in cur}
    cur = new_moves - blizzards - walls
    if ends[0] in cur:
        print(time)
        cur = set([ends[0]])
        ends.pop(0)

    # print_map()


