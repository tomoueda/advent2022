from args import example, example2, actual

lines = actual.split('\n')

UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

dirs = {'R': RIGHT, 'L': LEFT, 'U': UP, 'D': DOWN}

head_curr = (0, 0)
prev_curr = (0, 0)
tail_curr = (0, 0)
tail_visited = set((0, 0))
for line in lines:
    dir_let = line[0]
    num = int(line[2:])
    for i in range(num):
        dir = dirs[dir_let]
        prev_curr = head_curr 
        head_curr = (head_curr[0] + dir[0], head_curr[1] + dir[1])
        if abs(tail_curr[0] - head_curr[0]) > 1 or abs(tail_curr[1] - head_curr[1]) > 1:
            tail_curr = prev_curr
            tail_visited.add(tail_curr)
# print(len(tail_visited))


# part 2


currs = [(0, 0)] * 10 
prev = (0, 0)
tail_visited = set()

def print_board():
    s = '' 
    for i in range(-15, 20):
        for j in range(-15, 20):
            if i == 0 and j == 0:
                s += 's'
            elif (i, j) in currs:
                s += str(currs.index((i, j))) 
            else:
                s += '•'
        s += '\n'
    print(s)

for line in lines:
    dir_let = line[0]
    num = int(line[2:])
    print(dir_let, num)
    for i in range(num):
        dir = dirs[dir_let]
        currs[0] = (currs[0][0] + dir[0], currs[0][1] + dir[1])
        for i in range(1, len(currs)):
            prev = currs[i - 1]
            curr = currs[i]
            if prev[0] - curr[0] > 1 and prev[1] != curr[1]: 
                move = 1 if prev[1] - curr[1] > 0 else -1
                currs[i] = (curr[0] + 1, curr[1] + move) 
            elif prev[0] - curr[0] < -1 and prev[1] != curr[1]: 
                move = 1 if prev[1] - curr[1] > 0 else -1
                currs[i] = (curr[0] - 1, curr[1] + move) 
            elif prev[0] != curr[0] and prev[1] - curr[1] > 1: 
                move = 1 if prev[0] - curr[0] > 0 else -1
                currs[i] = (curr[0] + move, curr[1] + 1) 
            elif prev[0] != curr[0] and prev[1] - curr[1] < -1: 
                move = 1 if prev[0] - curr[0] > 0 else -1
                currs[i] = (curr[0] + move, curr[1] - 1) 
            elif abs(prev[0] - curr[0]) > 1 or abs(prev[1] - curr[1]) > 1: 
                move_x, move_y = 0, 0
                if prev[0] != curr[0]:
                    move_x = 1 if prev[0] - curr[0] > 0 else -1
                if prev[1] != curr[1]:
                    move_y = 1 if prev[1] - curr[1] > 0 else -1
                currs[i] = (curr[0] + move_x, curr[1] + move_y)
            if i == 9:
                tail_visited.add(currs[i])
        if line == 'R 17':
            print_board()
        #print_board()
#        print('inter', currs) 
#    print('final', currs) 
#    print('final')
#    print_board()
print(tail_visited)
print(len(tail_visited))


            

