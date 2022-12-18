
from args import example, actual
from collections import defaultdict
import re

lines = example.split('\n')
pattern = '(\d+)'

costs = {}
pressures = defaultdict(lambda: 0)
next_nodes = defaultdict(list)
for line in lines:
    inputs = line.split(' ')
    name = inputs[1]
    result = re.search(pattern, inputs[4])
    pressure = int(result.group(0))
    leads_to = list(map(lambda x: x.replace(',', ''), inputs[9:]))
    pressures[name] = pressure
    next_nodes[name] = leads_to 

def bfs(start):
    visited = set()
    queue = [(0, start)]
    while len(queue) != 0:
        cost, elem = queue.pop(0)
        if elem not in visited:
            visited.add(elem)
            if (pressures[elem] > 0 or elem == 'AA') and elem != start:
                costs[(start, elem)] = cost
            cost += 1
            for n in next_nodes[elem]:
                queue.append((cost, n))


nodes = set() 
# construct costs
for key in pressures.keys():
    if pressures[key] > 0 or key == 'AA':
        nodes.add(key)
        bfs(key)

paths = defaultdict(lambda: 0) 
memo = set() 
def get_key(valve = 'AA', min = 30, opened = set()):
    l = list(opened)
    l.sort()
    return (valve, min, ''.join(l))

# traverse everything keep all optimal values
def top(valve = 'AA', limit = 30, opened = set(), visited = set(), flow = 0):
    if paths[frozenset(visited)] < flow:
        paths[frozenset(visited)] = flow
    key = get_key(valve, limit, opened)
    if key in memo:
        return
    if limit == 0:
        return
    if len(nodes - opened) == 0:
        return

    # visit 
    pressure = pressures[valve]
    if valve not in opened and pressure > 0:
        top(valve, limit - 1, opened | {valve}, set(visited), pressure * (limit - 1) + flow)

    # travel
    rest = list(nodes - opened)
    rest.sort()
    for node in rest:
        if valve != node and node not in visited:
            new_visited = visited | {node}
            cost = costs[(valve, node)]
            n = limit - cost
            if n > 0:
                top(node, n, set(opened), new_visited, flow)
    memo.add(key)

top()
print(max(paths.values()))
# part 2
ans = []
for key, value in paths.items():
    for key2, value2 in paths.items():
        if not key & key2:
            ans.append(value + value2)
print(max(ans))


