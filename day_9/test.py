with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')


headx = heady = tailx = taily = 0
coords = {(0, 0)}

commandsx = {"L": -1, 
            "R": 1, 
            "U": 0, 
            "D": 0}
commandsy = {"L": 0, 
            "R": 0, 
            "U": 1, 
            "D": -1}

for line in lines:
    direction, dist = line.split(' ')
    dx, dy = commandsx[direction], commandsy[direction]

    for _ in range(int(dist)):
        headx += dx
        heady += dy

        while max(abs(tailx - headx), abs(taily - heady)) > 1:
            if abs(tailx - headx) > 0:
                if headx > tailx:
                    tailx += 1
                else:
                    tailx += -1
            if abs(taily - heady) > 0:
                if heady > taily:
                    taily += 1
                else:
                    taily += -1
            coords.add((tailx, taily))

print(len(coords))

rope = [(0, 0)] * 10

coords = {(0,0)}

for line in lines:
    direction, dist = line.split(' ')
    dx, dy = commandsx[direction], commandsy[direction]

    for _ in range(int(dist)):
        rope[0] = (rope[0][0]+dx, rope[0][1]+dy)

        for i in range(1, 10):
            tailx = rope[i][0]
            taily = rope[i][1]
            headx = rope[i-1][0]
            heady = rope[i-1][1]

            while max(abs(tailx - headx), abs(taily - heady)) > 1:
                if abs(tailx - headx) > 0:
                    if headx > tailx:
                        tailx += 1
                    else:
                        tailx += -1
                if abs(taily - heady) > 0:
                    if heady > taily:
                        taily += 1
                    else:
                        taily += -1
            rope[i] = (tailx, taily)
        
        coords.add(rope[9])

print(len(coords))
