from args import example, actual

rounds = actual.split('\n')
result = {'Z': 6, 'Y': 3, 'X': 0}
shape = {'C': {'Y': 3, 'X': 2, 'Z': 1}, 'B': {'Z': 3, 'Y': 2, 'X': 1}, 'A': {'X': 3, 'Z': 2, 'Y': 1}}
print(sum(map(lambda x: result[x[2]] + shape[x[0]][x[2]], rounds)))