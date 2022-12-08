from args import actual, example
from collections import defaultdict
from functools import reduce

# part 1
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
grid = defaultdict(lambda: None)
lines = actual.split('\n')
for i in range(len(lines[0])):
    for j in range(len(lines)):
        grid[(i, j)] = int(lines[i][j])
ans = 2 * len(lines[0]) + (len(lines) - 2) * 2

def is_visible(height, i, j):
    def helper(dir):
        k, l = i + dir[0], j + dir[1]
        while grid[k, l] is not None:
            if height <= grid[k, l]:
                return False 
            k, l = k + dir[0], l + dir[1]
        return True
    return reduce(lambda x, y: x or y, [helper(dir) for dir in dirs])

for i in range(1, len(lines[0]) - 1):
    for j in range(1, len(lines) - 1):
        if is_visible(grid[i, j], i, j):
            ans += 1
print(ans)
        
# part 2

def score(height, i, j):
    def helper(dir):
        s = 0 
        k, l = i + dir[0], j + dir[1]
        while grid[k, l] is not None:
            s += 1
            if height <= grid[k, l]:
                break
            k, l = k + dir[0], l + dir[1]
        return s 
    return reduce(lambda x, y: x * y, [helper(dir) for dir in dirs])

m = 0
for i in range(1, len(lines[0]) - 1):
    for j in range(1, len(lines) - 1):
        m = max(m, score(grid[i, j], i, j))
print(m)
