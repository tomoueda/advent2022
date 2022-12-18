from args import example, actual
from collections import defaultdict
from multiprocessing import Pool, cpu_count

grid = set()

class V:
    def __init__(self, x, y):
        self.coor = (x, y) 
    def __add__(self, o):
        return V(self[0] + o[0], self[1] + o[1])
    def __radd__(self, o):
        return V(self[0] + o[0], self[1] + o[1])
    def __rmul__(self, o):
        return V(self[0] * o, self[1] * o)
    def __getitem__(self, key):
        return self.coor[key]
    def __hash__(self):
        return hash(self.coor)
    def __eq__(self, o):
        if isinstance(o, tuple):
            return self.coor == o
        return self.coor == o.coor
    def __str__(self):
        return str(self.coor)
    def __repr__(self):
        return str(self.coor)


down = V(0, -1)
right = V(1, 0)
left = V(-1, 0)
up = V(0, 1)
noop = V(0, 0)
all_dirs = {down, right, left, up}
move_map = {'>': right, '<': left}

left_wall = -1 
right_wall = 7 

"""
0 -> 
####
left-most is pivot

1 ->
.#.
###
.#.
center is pivot

2 -> 
..#
..#
###
lower-right is pivot

3 -> 
#
#
#
#
top if pivot

4 -> 
##
##
top-left is pivot
"""

rocks = [
    [i * right for i in range(4)],
    all_dirs | {noop},
    {up, left, 2 * up, 2 * left, noop},
    [i * down for i in range(4)],
    {right, down, noop, right + down}
]

pivots = [ 
    V(2, 4),
    V(3, 5),
    V(4, 4),
    V(2, 7),
    V(2, 5)
]


def get_rock(rock, pivot):
    return {pivot + dir for dir in rocks[rock]}

def spawn(rock, highest):
    pivot = pivots[rock] + (0, highest)
    return get_rock(rock, pivot)

def collided(node):
    x = node[0]
    y = node[1]
    return (x == -1 
        or y == 0 
        or x == right_wall 
        or node in grid)

def move_possible(rock, next_rock):
    """ Just do the operation and check that they're all not collided 
    """
    for node in next_rock:
        if node in rock:
           continue 
        if collided(node):
            return False
    return True

def move_dir(rock, dir):
    next_rock = {x + dir for x in rock}
    if move_possible(rock, next_rock):
        return next_rock 
    return rock

def print_grid(grid, highest):
    s = ''
    for j in range(highest + 10, max(0, highest - 64), -1):
        for i in range(0, 7, 1):
            if (i, j) in grid:
                s += '@'
            else:
                s += '.'
        s += '\n'
    print(s)

# part 1
def sim(movement, limit):
    t = 0
    highest = 0
    num_rocks = 0
    rock_type = 0
    move = 0
    while num_rocks < limit:
        rock = None 
        next_rock = spawn(rock_type, highest)
        while rock != next_rock:
            rock = next_rock
            dir = move_map[movement[move]]
            move = (move + 1) % len(movement)
            rock = move_dir(rock, dir)
            next_rock = move_dir(rock, down)
        [grid.add(node) for node in rock]
        highest = max({x[1] for x in rock} | {highest})
        rock_type = (rock_type + 1) % 5
        num_rocks += 1
    return highest
# print(sim(example))

grid = set()
limit = 1000000000000 

def comp_row(t, h):
    row = list(filter(lambda node: node[1] == t, grid))
    row2 = list(filter(lambda node: node[1] == h, grid))

    diff = {node[0] for node in row} ^ {node[0] for node in row2}
    return len(diff) == 0

def get_top(highest):
    filtered = filter(lambda x : x[1] > highest - 64, grid)
    m = map(lambda x: (x[0], (x[1] - highest) + 64), filtered)
    m = list(m)
    m.sort()
    return tuple(m)

#part 2  
def part2(movement):
    highest = 0
    num_rocks = 0
    rock_type = 0
    move = 0
    memo = {}
    while num_rocks < 10000000000:
        rock = None 
        next_rock = spawn(rock_type, highest)
        while rock != next_rock:
            rock = next_rock
            dir = move_map[movement[move]]
            move = (move + 1) % len(movement) 
            rock = move_dir(rock, dir)
            next_rock = move_dir(rock, down)
        [grid.add(node) for node in rock]
        highest = max({x[1] for x in rock} | {highest})
        # find repeats
        if (num_rocks > 100):
            top = get_top(highest)
            if (top in memo):
                last_rock, last_highest = memo[top]
                return (num_rocks - last_rock, highest - last_highest)
            memo[top] = (num_rocks, highest)
        rock_type = (rock_type + 1) % 5
        num_rocks += 1
    return highest
cycle_len, height_diff = part2(actual)
print(cycle_len, height_diff)
bulk = ((10**12) // cycle_len) * height_diff
grid = set() 
left = sim(actual, 10**12 % cycle_len)
print(left + bulk)
# print(1514285714288 - (left + bulk))