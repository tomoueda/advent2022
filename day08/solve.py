from args import example, actual

grid = []
lines = actual.split('\n')
for line in lines:
    grid.append([int(i) for i in line])
print(grid)
ans = 2 * len(grid[0]) + (len(grid) - 2) * 2

def scenic_score(height, i, j):
    # check top
    def check_top():
        t = i - 1
        s = 0
        while t >= 0:
            s += 1
            if height <= grid[t][j]:
                return s
            t -= 1
        return s

    def check_bottom():
        t = i + 1
        s = 0
        while t < len(grid):
            s += 1
            if height <= grid[t][j]:
                return s
            t += 1
        return s


    def check_left():
        t = j - 1
        s = 0
        while t >= 0:
            s += 1
            if height <= grid[i][t]:
                return s
            t -= 1
        return s

    def check_right():
        t = j + 1
        s = 0
        while t < len(grid[0]):
            s += 1
            if height <= grid[i][t]:
                return s
            t += 1
        return s
    return check_top() * check_bottom() * check_right() * check_left()


m = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) -1):
        is_vis = scenic_score(grid[i][j], i, j)
        m = max(is_vis, m)

print(m)