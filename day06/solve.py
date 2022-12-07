from args import example, actual

lines = actual.split('\n')
for line in lines:
    for i in range(len(line) - 14):
        alpha4 = line[i:i+14]
        seen = set(alpha4)
        if len(seen) == 14:
            print(i + 14)
            break
