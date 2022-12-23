with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().strip().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

COORDS = set()
DIRECTIONS = ['N','S','W','E']
MIN_X = MIN_Y = MAX_X = MAX_Y = 0

def print_board():
    global MAX_X,MAX_Y,MIN_Y,MIN_X
    MIN_Y = min([y for x,y in COORDS])
    MIN_X = min([x for x,y in COORDS])
    MAX_Y = max([y for x,y in COORDS])
    MAX_X = max([x for x,y in COORDS])

    # for y in range(MIN_Y, MAX_Y+1):
    #     for x in range(MIN_X, MAX_X+1):
    #         print('#' if (x,y) in COORDS else '.', end='')
    #     print()
    # print()

def check_if_move_necessary(x,y):
    global COORDS
    nearest_eight = [(x+dx, y+dy) 
                    for dx,dy 
                    in [(0,1),(1,1),(-1,1),(1,0),
                        (-1,0),(0,-1),(-1,-1),(1,-1)]]
    for (i,j) in nearest_eight:
        if (i,j) in COORDS:
            return True

    return False

def possible(x, y, dir):
    global COORDS
    checks = []

    if dir == 'N':
        checks = [(x+dx, y+dy) for dx,dy 
                in [(0,-1),(-1,-1),(1,-1)]]

    if dir == 'S':
        checks = [(x+dx, y+dy) for dx,dy 
                in [(0,1),(1,1),(-1,1)]]
    
    if dir == 'W':
        checks = [(x+dx, y+dy) for dx,dy 
                in [(-1,1),(-1,0),(-1,-1)]]

    if dir == 'E':
        checks = [(x+dx, y+dy) for dx,dy 
                in [(1,1),(1,0),(1,-1)]]

    for c in checks:
        if c in COORDS:
            return False
    return True
        
def get_move(x, dir):
    dx = dy = 0
    if dir == 'N':
        dy = -1

    if dir == 'S':
        dy = 1
    
    if dir == 'W':
        dx = -1

    if dir == 'E':
        dx = 1
    
    return (x[0]+dx, x[1]+dy)

def change_dirs():
    global DIRECTIONS

    DIRECTIONS.append(DIRECTIONS.pop(DIRECTIONS.index(DIRECTIONS[0])))

def solve(rounds):
    global COORDS, DIRECTIONS

    for round in range(rounds):
        to_move = set()

        for x in COORDS:
            if check_if_move_necessary(*x):
                to_move.add(x)

        if len(to_move) == 0:
            print(round+1)
            break
        moves = dict()
        for x in to_move:
            for dir in DIRECTIONS:
                if possible(*x,dir):
                    move = get_move(x, dir)
                    
                    if move in moves.keys():
                        moves[move] = moves[move] + [x]
                    else:
                        moves[move] = [x]
                    break
        
        for new, olds in moves.items():
            if len(olds) == 1:
                COORDS.remove(olds[0])
                COORDS.add(new)
        
        print_board()
        # print()
        change_dirs()

input = lines

for y, line in enumerate(input):
    for x, pos in enumerate(line):
        if pos == '#':
            COORDS.add((x,y))

solve(10)
print((MAX_X+1-MIN_X) * (MAX_Y+1-MIN_Y) - len(COORDS))

COORDS = set()
DIRECTIONS = ['N','S','W','E']
MIN_X = MIN_Y = MAX_X = MAX_Y = 0

for y, line in enumerate(input):
    for x, pos in enumerate(line):
        if pos == '#':
            COORDS.add((x,y))

solve(10000)