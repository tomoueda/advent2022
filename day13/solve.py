from args import example, actual
from functools import cmp_to_key

pairs = actual.split('\n\n')

def is_int(item):
    return isinstance(item, int)

def is_in_order(left, right):
    for i in range(max(len(left), len(right))):
        l, r = None, None
        try:
            l = left[i]
            r = right[i]
        except:
            if l == None:
                return -1
            return 1 
        if l != r:
            if is_int(l) and is_int(r):
                if l < r:
                    return -1
                return 1 
            if is_int(l):
                l = [l]
            if is_int(r):
                r = [r]
            if l == r:
                continue
            elem = is_in_order(l, r)
            if elem is None:
                continue
            return elem

#idx = 1
#s = 0
#for pair in pairs:
#    if idx == 23:
#        print(pair)
#
#    line = pair.split('\n')
#    left = eval(line[0])
#    right = eval(line[1])
#    if is_in_order(left, right):
#        s += idx
#    idx += 1
#print(s)

objects = []
# part 2
for pair in pairs:
    for line in pair.split('\n'):
        objects.append(eval(line))
objects.append([[2]])
objects.append([[6]])

objects = sorted(objects, key=cmp_to_key(is_in_order))
print((objects.index([[2]]) + 1) * (objects.index([[6]]) + 1)) 