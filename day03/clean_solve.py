from functools import reduce
from args import actual

lines = actual.split('\n')
def score(c):
    return ord(c) - (96 if c.islower() else 38)

def part1():
    s = 0
    for line in lines:
        former, latter = line[:len(line)//2], line[len(line)//2:]
        c = next(iter(set(former).intersection(latter)))
        s += score(c)
    return s
print(part1())

def part2():
    s = 0
    for i in range(0, len(lines), 3):
        intersect = reduce(lambda a, b: set(a).intersection(b), lines[i:i+3])
        c = next(iter(intersect))
        s += score(c)
    return s
print(part2())



