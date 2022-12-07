with open("input.txt", 'r', encoding="utf-8") as f:
    line = f.read()

# part 1
for i in range(len(line) - 4):
    if (len(set(line[i:i+4])) == 4):
        print(i+4)
        break

#part 2
for i in range(len(line) - 14):
    if (len(set(line[i:i+14])) == 14):
        print(i+14)
        break