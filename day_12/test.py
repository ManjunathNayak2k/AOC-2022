import string
import networkx

with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

grid = [list(line) for line in lines]

start = (0,0)
end = (0,0)

r = len(grid)
c = len(grid[0])

for y in range(r):
    for x in range(c):
        if grid[y][x] == 'S':
            start = (y,x)
            grid[y][x] = 'a'
        elif grid[y][x] == 'E':
            end = (y,x)
            grid[y][x] = 'z'

graph = networkx.DiGraph()

checks = [(0,1), (0,-1), (1,0), (-1,0)]
for y in range(r):
    for x in range(c):
        for check in checks:
            dx = check[0]
            dy = check[1]
            checkx = x + dx
            checky = y + dy

            if 0<=checkx<c and 0<=checky<r:
                first = string.ascii_lowercase.index(grid[y][x])
                second = string.ascii_lowercase.index(grid[checky][checkx])

                if first + 1 >= second:
                    graph.add_edge((y,x), (checky, checkx))

print(networkx.shortest_path_length(graph, start, end))

starts = []
for y in range(r):
    for x in range(c):
        if grid[y][x] == 'a':
            starts.append((y,x))

min = 1000

for new_start in starts:
    try:
        length = networkx.shortest_path_length(graph, new_start, end)
        if length < min:
            min = length
    except networkx.exception.NetworkXNoPath as e:
        pass

print(min)
