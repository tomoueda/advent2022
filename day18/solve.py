from args import example, actual

dirs = [(0, 1, 0), (1, 0, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

class V:
    def __init__(self, x, y, z):
        self.coor = (x, y, z) 
    def __add__(self, o):
        return V(self[0] + o[0], self[1] + o[1], self[2] + o[2])
    def __radd__(self, o):
        return V(self[0] + o[0], self[1] + o[1], self[2] + o[2])
    def __rmul__(self, o):
        return V(self[0] * o, self[1] * o, self[1] * o)
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


cubes = set()
lines = actual.split('\n')
s = 0
for line in lines:
    cube = V(*map(int, line.split(',')))
    cubes.add(cube)

for cube in cubes:
    l = 6
    for dir in dirs:
        if cube + dir in cubes:
            l -= 1
    s += l
# print(s)


# part 2
# bounding box of solution
max_points = [-1000000, -1000000, -10000000]
min_points = [100000000, 10000000, 10000000]

cubes = set()
lines = actual.split('\n')
s = 0
for line in lines:
    cube = V(*map(int, line.split(',')))
    for i in range(3):
        max_points[i] = max(cube[i], max_points[i])
        min_points[i] = min(cube[i], min_points[i])
    cubes.add(cube)

trapped = set()
free = set()
def outside_bb(n):
    for i in range(3):
        if max_points[i] < n[i]:
            return True
        if min_points[i] > n[i]:
            return True
    return False

def is_trapped(n):
    if n in trapped:
        return True
    if n in free:
        return False 
    # keep bfsing until you hit a bounding box if it's not inside then all visited coordinates has access to water.
    # if you run out all visited coordiinates are trapped.
    visited = set() 
    queue = [n]
    while len(queue) != 0:
        node = queue.pop()
        if node not in visited:
            visited.add(node)
            for neigh in [node + dir for dir in dirs]:
                if outside_bb(neigh):
                    # this means everyone is free
                    free.update(visited)
                    return False
                if neigh not in cubes:
                    queue.append(neigh)
    # uh oh ran out travel space and never visited outside the
    # the bounding box, must be trapped and all visited coordinates
    trapped.update(visited)
    return True

for cube in cubes:
    l = 6
    # consider each side
    for dir in dirs:
        n = cube + dir
        # if it's blocked it's easy substract that surface.
        if n in cubes:
            l -= 1
        elif is_trapped(n):
            l -= 1
    s += l
print(s)


