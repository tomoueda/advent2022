from collections import defaultdict
from args import example, actual

highest = -10000000000 
graph = defaultdict(lambda: None)
lines = actual.split('\n')
for line in lines:
    pivots = line.split(' -> ')
    start = tuple(map(int, pivots[0].split(',')))
    highest = max(highest, start[1])
    for i in range(1, len(pivots)):
        end = tuple(map(int, pivots[i].split(',')))
        idx = 1 if start[0] == end[0] else 0
        to, fro = (start[idx], end[idx]) if start[idx] < end[idx] else (end[idx], start[idx])
        for i in range(to, fro + 1):
            if start[0] == end[0]:
                graph[start[0], i] = 'x'
            else:
                graph[i, start[1]] = 'x'
        start = end 
        highest = max(highest, start[1])

DOWN = (0, 1)
LEFT = (-1, 1)
RIGHT = (1, 1)


def lookup(curr):
    if curr in graph:
        return True
    if curr[1] == highest + 2:
        return True
    return False

num_ston = 0
def next_sand_place():
    curr = (500, 0) 
    """
    should terminate
    """
    while True:
        down = (curr[0] + DOWN[0], curr[1] + DOWN[1])
        if not lookup(down):
            curr = down
            continue
        left = (curr[0] + LEFT[0], curr[1] + LEFT[1])
        if not lookup(left):
            curr = left 
            continue
        right = (curr[0] + RIGHT[0], curr[1] + RIGHT[1])
        if not lookup(right):
            curr = right 
            continue
        return (curr)


while True:
    stone_pos = next_sand_place()
    if stone_pos == 'terminate' or stone_pos == (500, 0):
        num_ston += 1
        break
    graph[stone_pos] = 'o'
    num_ston += 1
print(num_ston)

s = ''
for j in range(0, 300):
    for i in range(400, 600):
        if (i, j) in graph:
            s += graph[i,j]
        else:
            s += '.'
    s += '\n'
print(s)