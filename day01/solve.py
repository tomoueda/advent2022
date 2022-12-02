
from inp import inp 

# part 1

m = 0
t = 0
for line in inp.split('\n'):
    if line == '':
        if t > m:
            m = t
        t = 0
    else:
        t += int(line)
print(m)

# part 2

t = 0
cals = []
for line in inp.split('\n'):
    if line == '':
        cals.append(t)
        t = 0
    else:
        t += int(line)
cals.sort(reverse=True)
print(sum(cals[:3]))
