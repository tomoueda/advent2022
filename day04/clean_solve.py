from args import actual, example

lines = actual.split('\n')
s = 0
for line in lines:
    elves = line.split(',')
    a, b = map(int, elves[0].split('-'))
    c, d = map(int, elves[1].split('-'))
    if (a >= c and a <= d) or (c >= a and c <= b):
        s += 1
print(s)