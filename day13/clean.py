from args import example, actual
from functools import cmp_to_key
from itertools import zip_longest

pairs = actual.split('\n\n')

def is_int(item):
    return isinstance(item, int)

def is_in_order(left, right):
    for l, r in zip_longest(left, right, fillvalue='@'):
        if l == '@':
            return -1
        if r == '@':
            return 1
        if l != r:
            if is_int(l) and is_int(r):
                return l - r
            if is_int(l):
                l = [l]
            if is_int(r):
                r = [r]
            elem = is_in_order(l, r)
            if elem != 0:
                return elem
    return 0

idx = 1
s = 0
for pair in pairs:
    line = pair.split('\n')
    left = eval(line[0])
    right = eval(line[1])
    if is_in_order(left, right) < 0:
        s += idx
    idx += 1
print(s)

objects = []
# part 2
for pair in pairs:
    for line in pair.split('\n'):
        objects.append(eval(line))
objects.append([[2]])
objects.append([[6]])

objects = sorted(objects, key=cmp_to_key(is_in_order))
print((objects.index([[2]]) + 1) * (objects.index([[6]]) + 1)) 