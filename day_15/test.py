import re

with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

dict_of_dists = {}
Y_MAX = 2000000
MAX_VAL = 4000000

beacons = set()

for line in lines:
    x1, y1, x2, y2 = [int(s) for s in re.findall(r"-?\d+", line)]

    dict_of_dists[x1,y1] = abs(x2-x1)+ abs(y2-y1)
    beacons.add((x2,y2))

count = 0
no_beacons = set()

for x1,y1 in dict_of_dists:
    for dx in [1,-1]:
        x = x1
        dist = abs(y1 - Y_MAX)
        x = x1
        while dist <= dict_of_dists[x1,y1]:
            if(x,Y_MAX) not in beacons:
                no_beacons.add((x, Y_MAX))
            x += dx
            dist += 1

print(len(no_beacons))

got_ans = False
for y in range(0, MAX_VAL):
    ranges = []

    for x1,y1 in dict_of_dists:
        dis_left = dict_of_dists[x1,y1] - abs(y1-y)
        if dis_left > 0:
            start_range = max(0, x1-dis_left)
            end_range = min(MAX_VAL, x1+dis_left)
            ranges.append((start_range,end_range))

    cur_min = 0

    for (start,end) in sorted(ranges):
        # print(start,end)
        if cur_min >= start:
            cur_min = max(cur_min, end)
        else:
            print(cur_min*4000000 + y)
            got_ans = True
            break

    if got_ans:
        break