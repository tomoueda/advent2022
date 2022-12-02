from args import example, actual

rounds = actual.split('\n')

scores = {'X': 1, 'Y': 2, 'Z': 3}
draw_scores = {'A': 1, 'B': 2, 'C': 3}
lose_scores = {'A': 3, 'B': 1, 'C': 2}
win_scores = {'A': 2, 'B': 3, 'C': 1}
win = {'C Z', 'A Z', 'B Z'}
draw = {'A Y', 'B Y', 'C Y'}
loss = {'B X', 'A X', 'C X'}
def calc(line):
    s = 0
    if line in win:
        s += 6
    if line in draw:
        s += 3
    if line in loss:
        s += 0
    if line[2] == 'Y':
        s += draw_scores[line[0]]
    if line[2] == 'X':
        s += lose_scores[line[0]] 
    if line[2] == 'Z':
        s += win_scores[line[0]]
    return s
print(sum(map(calc, rounds)))
