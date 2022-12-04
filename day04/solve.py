
from args import example, actual

lines = actual.split('\n')
num = 0
overlaps = 0
for line in lines:
    ranges = line.split(',')
    first = ranges[0].split('-')
    second = ranges[1].split('-')
    a, b = int(first[0]), int(first[1])
    c, d= int(second[0]), int(second[1])
# part 1
#    if a >= c and b <= d:
#        num += 1
#        continue
#    if c >= a and d <= b:
#        num += 1

# part 2
    if len(set(range(a, b + 1)).intersection(range(c, d + 1))) != 0:
        num += 1

print(num)
