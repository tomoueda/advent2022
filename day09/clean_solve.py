
from args import example, example2, actual

lines = example2.split('\n')

UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

KNOTS = 10 # part 1 KNOTS = 2 

def sign(n):
    return (n > 0) - (n < 0)

dirs = {'R': RIGHT, 'L': LEFT, 'U': UP, 'D': DOWN}
currs = [(0, 0)] * KNOTS

def print_board():
    s = '' 
    for y in range(20, -15, -1):
        for x in range(-15, 20):
            if x == 0 and y == 0:
                s += 's'
            elif (x, y) in currs:
                s += str(currs.index((x, y))) 
            else:
                s += '•'
        s += '\n'
    print(s)

visited = set()
for line in lines:
    dir, n = dirs[line[0]], int(line[2:])
    for _ in range(n):
        currs[0] = (currs[0][0] + dir[0], currs[0][1] + dir[1])
        for i in range(1, len(currs)):
            prev = currs[i - 1]
            curr = currs[i]
            hop = (prev[0] - curr[0], prev[1] - curr[1])
            if abs(hop[0]) > 1 or abs(hop[1]) > 1:
                currs[i] = (curr[0] + sign(hop[0]), curr[1] + sign(hop[1]))
        visited.add(currs[-1])
    print_board()
print(len(visited))
