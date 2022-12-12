from args import example, actual
from collections import defaultdict

def val(a):
    if a == 'S':
        return ord('a') 
    if a == 'E':
        return ord('z')
    return ord(a)
    

def eligible(curr, next):
    return val(curr) + 1 >= val(next)

heap = []
dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
lines = example.split('\n')
graph = defaultdict(lambda: None) 
for j in range(len(lines)):
    for i in range(len(lines[0])):
        graph[i, j] = lines[j][i]
        if graph[i, j] in {'S', 'a'}:
            heap.append((0, (i, j)))


visited = set()

while len(heap) != 0:
    steps, coor = heap.pop(0)
    curr = graph[coor]
    if curr == 'E':
        print(steps)
        break
    if coor not in visited:
        visited.add(coor)
        for next_coor in map(lambda x: (coor[0] + x[0], coor[1] + x[1]), dirs):
            next_elem = graph[next_coor]
            if next_elem is None:
                continue
            if eligible(curr, next_elem):
                heap.append((steps + 1, next_coor))

