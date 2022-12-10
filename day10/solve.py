
from args import example, actual

lines = actual.split('\n')

cycle = 0
cycle_val = {'addx': 2, 'noop': 1}
x = 1 

s = 0
signal_num = 0
for line in lines:
    instr = line.split(' ')
    ins = instr[0]
    val = cycle_val[ins]
    while val > 0:
        val -= 1
        cycle += 1
        if cycle % 40 == 20:
            s += x * cycle
            signal_num += 1
        if val == 0 and ins == 'addx':
            x += int(instr[1])
print(s)

# part 2
ans = ''


cycle = 0
cycle_val = {'addx': 2, 'noop': 1}
x = 1 

s = 0
signal_num = 0
row = 0
for line in lines:
    instr = line.split(' ')
    ins = instr[0]
    val = cycle_val[ins]
    while val > 0:
        val -= 1
        cycle += 1
        if cycle % 40 == 0:
            ans += '\n'
        if row % 40 in  [x - 1, x, x + 1]:
            ans += '#'
        else:
            ans += '.'
        row += 1
        if val == 0 and ins == 'addx':
            x += int(instr[1])
print(ans)