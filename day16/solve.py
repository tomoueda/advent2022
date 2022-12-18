from args import example, actual
import heapq
import re
from collections import defaultdict 

lines = example.split('\n')
pattern = '(\d+)'



cost = {}
graph = {}
num_none_zero = 0
for line in lines:
    inputs = line.split(' ')
    name = inputs[1]
    result = re.search(pattern, inputs[4])
    pressure = int(result.group(0))
    leads_to = list(map(lambda x: x.replace(',', ''), inputs[9:]))
    graph[name] = {'pressure': pressure, 'leads_to': leads_to}
    if pressure != 0:
        num_none_zero += 1

nonzero = set()
nonzero.add('AA')
# find the shortest distance to the closest none zero node from each node. Keep AA as a starting node.
for key, val in graph.items():
    if val['pressure'] != 0:
        nonzero.add(key)
# print(nonzero)

potential = {}
real_graph = {}
def bfs(i = 'AA', visited = set()):
    if i not in visited:
        visited.add(i)
        s = 0
        if i in nonzero: 
            s += graph[i]['pressure']
        next_nodes = graph[i]['leads_to']
        for n in next_nodes:
            potential[n] = bfs(n, set(visited)) 
            s += potential[n]
        potential[i] = s
        return s
    return 0
bfs()

# print(real_graph)

memo = {}

def make_key(limit = 30, valve = 'AA', opened = []):
    opened.sort()
    return (limit, valve, ''.join(opened))

# part 1
def dp(limit = 30, valve = 'AA', opened = []):
    key = make_key(limit, valve, opened)
    if key in memo:
        return memo[key]

    if limit == 0:
        return 0
    m = 0
    pressure = graph[valve]['pressure']
    if valve not in opened and pressure != 0:
        # open the current valve
        left = limit - 1 
        new_opened = list(opened)
        new_opened.append(valve)
        m = max(m, pressure * left + dp(limit - 1, valve, new_opened))
    # or not
    next_valves = graph[valve]['leads_to']
    for n in next_valves:
        m = max(m, dp(limit - 1, n, list(opened)))

    memo[key] = m 
    return m
print(dp())

def make_key_2(limit, valves, opened):
    valves.sort()
    opened.sort()
    return (limit, ''.join(valves), ''.join(opened))


memo2 = defaultdict(lambda: 0)

def best_so_far(limit, opened):
    opened.sort()
    key = ''.join(opened) 
    return memo2[key] > limit


# part 2 
def dp2(limit = 26, valves = ['AA', 'AA'], opened = [], visited = set()):
    print(len(memo))
    key = make_key_2(limit, valves, opened)
    if key in memo:
        return memo[key]
    
    if len(opened) == num_none_zero:
        memo[key] = 0
        return 0

    if limit == 0:
        return 0
    m = 0
    valveA = valves[0]
    valveB = valves[1]
    pressure_A = graph[valves[0]]['pressure']
    pressure_B = graph[valves[1]]['pressure']
    leads_to_A = graph[valves[0]]['leads_to']
    leads_to_B = graph[valves[1]]['leads_to']


    left = limit - 1 
    # check the case where they are at the same valve.
    # first human will check either open or not.
    # second person will move to the next few valves.
    if valveA == valveB and valveA not in opened and pressure_A != 0:
        for n in leads_to_B:
            if n not in visited:
                new_visited = set(visited)
                new_visited.add(n)

                new_opened = list(opened)
                new_opened.append(valveA)
                m = max(m, pressure_A * left + dp2(left, [valveA, n], new_opened, new_visited))
    # check the case where both valves is not open
    # and valve A and valve B both should be opened
    elif valveA not in opened and pressure_A != 0 \
        and valveB not in opened and pressure_B != 0:
        # open the current valve
        new_opened = list(opened)
        new_opened.append(valveA)
        new_opened.append(valveB)
        m = max(m, (pressure_A * left) + (pressure_B * left) + dp2(left, [valveA, valveB], new_opened))
    elif valveA not in opened and pressure_A != 0:
        for n in leads_to_B:
            if n not in visited:
                new_visited = set(visited)
                new_visited.add(n)

                new_opened = list(opened)
                new_opened.append(valveA)
                m = max(m, pressure_A * left + dp2(left, [valveA, n], new_opened, new_visited))
    elif valveB not in opened and pressure_B != 0:
        for n in leads_to_A:
            if n not in visited:
                new_visited = set(visited)
                new_visited.add(n)

                new_opened = list(opened)
                new_opened.append(valveB)
                m = max(m, pressure_B * left + dp2(left, [n, valveB], new_opened, new_visited))

    # now just have both of them move
    for a in leads_to_A:
        for b in leads_to_B:
            if a not in visited or b not in visited:
                new_visited = set(visited)
                new_visited.add(a)
                new_visited.add(b)
                m = max(m, dp2(left, [a, b], list(opened), new_visited))
    memo[key] = m 
    return m
# print(dp2())
