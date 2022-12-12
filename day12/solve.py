from args import example, actual
from collections import defaultdict
import heapq

def eligible(curr, next):
#    if next == 'E' and curr != 'z':
#        return False
    if curr == 'z' and next == 'E':
        return True
    if curr == 'S' and next == 'a':
        return True
    if ord(curr) + 1 >= ord(next):
        return True
    return False 

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
    steps, coor = heapq.heappop(heap)
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
                heapq.heappush(heap, (steps + 1, next_coor))

