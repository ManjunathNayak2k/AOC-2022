import os

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

current_dir = None
directories = {}
sub_directories = {}

for line in lines:
    if line.startswith("$ cd"):
        c, cmd, *args = line.split()
        if args[0] == '/':
            current_dir = args[0]
        else:
            current_dir = os.path.normpath(os.path.join(current_dir, args[0]))

        if current_dir not in directories:
            directories[current_dir] = 0
            sub_directories[current_dir] = []

    if line.startswith("$") is False:
        sz, fname = line.split()
        if sz != 'dir':
            directories[current_dir] += int(sz)
        else:
            sub_directories[current_dir].append(os.path.normpath(os.path.join(current_dir, fname)))

dirsizes = {}

def dirsize(dir):
    dir_size = directories[dir]
    for i in sub_directories[dir]:
        if i in directories:
            dir_size += dirsize(i)
    return dir_size

# part 1
total_size = 0
for d in directories:
    dir_size = dirsize(d)
    if dir_size <= 100000:
        total_size += dir_size
print(total_size)

# part 2
current_mem = dirsize('/')
free_space = 70000000 - current_mem
min_size = 70000000
for d in directories:
    ds = dirsize(d)
    if free_space + ds >= 30000000:
        if min_size > ds:
            min_size = ds
print(min_size)