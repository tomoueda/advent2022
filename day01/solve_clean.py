from inp import inp

elves = [map(int, x.split('\n')) for x in inp.split('')]
s = [sum(x) for x in elves]
s.sort()
print(s[-1])
print(sum(s[-3:]))