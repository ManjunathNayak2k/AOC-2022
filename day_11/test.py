with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

monkeys = {}


def divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def get_monkeys():
    cur = -1
    for line in lines:
        if line.startswith("Monkey"):
            cur += 1
            monkeys[cur] = {}

        elif line.startswith("  Starting items:"):
            monkeys[cur]['start_items'] = [int(x) for x in line[line.find(':')+1:].split(", ")]
        elif line.startswith("  Operation: "):
            monkeys[cur]['op'] = line[line.find('old')+4]
            monkeys[cur]['num'] = line[line.find('old')+6:]

        elif line.startswith("  Test: divisible by "):
            monkeys[cur]['test'] = int(line[line.find("by")+3:])
        elif line.startswith("    If true: "):
            monkeys[cur]['true'] = int(line[line.find("monkey")+7:])
        elif line.startswith("    If false: "):
            monkeys[cur]['false'] = int(line[line.find("monkey")+7:])

get_monkeys()
inspects=[0]*len(monkeys)

for i in range(20):
    for j in monkeys.keys():
        old_list = monkeys[j]['start_items']
        for k in monkeys[j]['start_items']:
            inspects[j]+=1
            og = k
            l = 1
            if monkeys[j]['num'] == 'old':
                l = int(k)
            else:
                l = int(monkeys[j]['num'])
            if monkeys[j]['op'] == '*':
                k*= l % 9699690
            elif monkeys[j]['op'] == '+':
                k+= l % 9699690
            k=k//3

            test = divisible(k, monkeys[j]['test'])

            if test:
                monkeys[monkeys[j]['true']]['start_items'].append(k)
            else:
                monkeys[monkeys[j]['false']]['start_items'].append(k)

        monkeys[j]['start_items'] = [x for x in monkeys[j]['start_items'] if x not in old_list]

inspects = sorted(inspects)
print(inspects[-1] * inspects[-2])

get_monkeys()
inspects=[0]*len(monkeys)

for i in range(10000):
    for j in monkeys.keys():
        old_list = monkeys[j]['start_items']
        for k in monkeys[j]['start_items']:
            inspects[j]+=1
            og = k
            l = 1
            if monkeys[j]['num'] == 'old':
                l = int(k)
            else:
                l = int(monkeys[j]['num'])
            if monkeys[j]['op'] == '*':
                k*= l % 9699690
            elif monkeys[j]['op'] == '+':
                k+= l % 9699690
            # k=k//3

            test = divisible(k, monkeys[j]['test'])

            if test:
                monkeys[monkeys[j]['true']]['start_items'].append(k)
            else:
                monkeys[monkeys[j]['false']]['start_items'].append(k)

        monkeys[j]['start_items'] = [x for x in monkeys[j]['start_items'] if x not in old_list]

inspects = sorted(inspects)
print(inspects[-1] * inspects[-2])