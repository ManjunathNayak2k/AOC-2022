with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

x = 1
clock = 0
sum = 0
for line in lines:
    clock+=1
    if (clock-20) % 40 == 0:
        sum += clock * x
    if line.startswith("addx"):
        clock+=1
        if (clock-20) % 40 == 0:
            sum += clock * x
        _, z = line.split(' ')
        x+= int(z)

print(sum)

arr = [["." for _ in range(40)] for _ in range(6)]
clock = 0
x = 1
sum = 0

for line in lines:
    cmd, *sz = line.split(' ')

    sprite_pos = x
    cur = clock % 40
    if sprite_pos in [cur, cur-1, cur+1]:
        arr[clock // 40][cur % 40] = "#"
    clock += 1

    if line.startswith("addx"):
        sprite_pos = x
        cur = clock % 40
        if sprite_pos in [cur, cur-1, cur+1]:
            arr[clock // 40][cur % 40] = "#"
        clock += 1
        x += int(sz[0])

image = ""
for row in arr:
    image += ''.join(row)
    image += "\n"

print(image.strip())