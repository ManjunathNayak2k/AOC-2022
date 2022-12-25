with open("sample.txt", 'r', encoding="utf-8") as f:
    sample = f.read().strip().split('\n')

with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

sum = 0
for line in lines:
    power = 1
    string = list(line)
    num = 0
    while string:
        c = string.pop(-1)
        if c == '=':
            c = -2
        elif c == '-':
            c = -1
        else:
            c = int(c)
        num += power * c
        
        power *= 5
    print(num)
    sum += num

snafu = ''

while sum > 0:
    mod = sum % 5
    if mod == 3:
        snafu = '=' + snafu
        sum = (sum + 2) // 5
    elif mod == 4:
        snafu = '-' + snafu
        sum = (sum + 1) // 5
    else:
        snafu = str(mod) + snafu
        sum = (sum - mod) // 5


print(snafu)