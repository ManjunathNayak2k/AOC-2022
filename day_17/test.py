with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read()

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read()
WIDTH = 7

ROCKS = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
    [(2, 0), (2, 1), (2, 2), (2, 3)],
    [(2, 0), (2, 1), (3, 0), (3, 1)],
]

num_rocks = 1000000000000
all_cycles = {}


def solve(jets, tower):

    jet_index= rock_index = 0
    y_add = top_y = 0

    while rock_index <= num_rocks:
        # print(rock_index)
        if rock_index == 2022:
            print(top_y)
        cur_rock = ROCKS[rock_index%len(ROCKS)]
        dy = max(y for x,y in tower) + 4
        cur_rock = [(x, y+dy) for x,y in cur_rock]

        while True:
            jet = jets[jet_index % len(jets)]
            jet_index += 1

            dx = -1 if jet=='<' else 1
            new_rock_x = [(x+dx, y) for x,y in cur_rock]

            if any(x<0 for x,y in new_rock_x):
                new_rock_x = cur_rock
            elif any(x>=WIDTH for x,y in new_rock_x):
                new_rock_x = cur_rock
            elif any(coord in tower for coord in new_rock_x):
                new_rock_x = cur_rock

            cur_rock = new_rock_x

            new_rock_y = [(x, y-1) for x,y in cur_rock]

            if any(coord in tower for coord in new_rock_y):
                tower.update(cur_rock)
                
                top_y = max(y for (x,y) in tower)
                recent_cycles = frozenset([(x,top_y-y) for (x,y) in tower if top_y-y<=30])

                cycle = (jet_index % len(jets), rock_index % len(ROCKS), recent_cycles)
                
                if cycle in all_cycles and rock_index >= 2022:
                    (old_rock, old_top) = all_cycles[cycle]
                    dy = top_y - old_top
                    drock = rock_index - old_rock
                    delta = (num_rocks-rock_index)//drock
                    y_add += delta*dy
                    rock_index += delta*drock
                    assert rock_index<=num_rocks
                all_cycles[cycle] = (rock_index, top_y)
                break
            
            cur_rock = new_rock_y

        rock_index += 1        
    print(top_y+y_add)
    return tower


tower = {(x, 0) for x in range(WIDTH)}
tower = solve(sample, tower)
