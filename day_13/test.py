from functools import cmp_to_key
with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

del lines[2::3]
del sample[2::3]

to_check = sample # change to lines for puzzle input

correct_count = 0

def compare(l1, l2):
    if type(l1) == int and type(l2) == int:
        if l1 < l2:
            return -1
        elif l1 > l2:
            return 1
        else:
            return 0

    if type(l1) == int:
        l1 = [l1]
    elif type(l2) == int:
        l2 = [l2]

    for i in range(min(len(l1), len(l2))):
        check = compare(l1[i], l2[i])
        if check != 0:
            return check

    if len(l1) < len(l2):
        return -1
    elif len(l1) > len(l2):
        return 1
    else:
        return 0

packets = []

for i in range(0,len(to_check),2):

    var1 = eval(to_check[i])
    var2 = eval(to_check[i+1])

    packets.append(var1)
    packets.append(var2)

    if compare(var1, var2) < 0:
        correct_count+=(i+2)/2

packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(compare))
print(correct_count)
print((packets.index([[2]])+1) * (packets.index([[6]])+1))