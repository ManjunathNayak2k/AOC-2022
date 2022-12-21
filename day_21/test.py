from sympy.solvers import solve
from sympy import Symbol

with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().strip().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

dict_of_ops = {}
for line in sample:
    # print(line)
    if len(line) < 12:
        dict_of_ops[line[0:4]] = int(line[6:])
    else:    
        dict_of_ops[line[0:4]] = [line[6:10], line[11], line[13:]]
    # print(len(line))

x= Symbol('x')

def calculate(node, part):
    item = dict_of_ops[node]
    if type(item) == int:
        if part == 2 and node=='humn':
            return x 
        return item
        
    else:
        item1 = calculate(dict_of_ops[node][0], part)
        item2 = calculate(dict_of_ops[node][2], part)
        if part == 2 and node == 'root':
            return solve(item1-item2, x)
        op = dict_of_ops[node][1]
        if op == '+':
            return item1+item2
        if op == '*':
            return item1*item2
        if op == '/':
            return item1/item2
        if op == '-':
            return item1-item2

print(calculate('root',1))
print(calculate('root',2))


