from functools import reduce
from args import example, actual
from collections import defaultdict 

print(2673432 * 4000000 + 3308112)

import re

pattern = 'Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)'
pattern = re.compile('(-?\d+)+')

steps = defaultdict(list)
limit = 4000000

class Sensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_beacon(self, x, y):
        self.bx = x
        self.by = y 
        self.dist = abs(self.x - self.bx) + abs(self.y - self.by)

    def formulate(self):
        top = self.y - self.dist
        bottom = self.y + self.dist

        for i in range(self.dist + 1):
            if top + i >= 0:
                step = steps[top + i]
                spread = [max(0, self.x - i), min(self.x + i, limit)]
                step.append(spread)

        for i in range(self.dist + 1):
            if bottom - i <= limit:
                step = steps[bottom - i]
                spread = [max(0, self.x - i), min(self.x + i, limit)]
                step.append(spread)

    def get(self):
        return (self.x, self.y)

    def get_beacon(self):
        return (self.bx, self.by)

lines = actual.split('\n')
sensors = []
for line in lines:
    i = pattern.finditer(line)
    x = int(next(i).group(0))
    y = int(next(i).group(0))
    sensor = Sensor(x, y)
    bx = int(next(i).group(0))
    by = int(next(i).group(0))
    sensor.set_beacon(bx, by)
    sensors.append(sensor)

for sensor in sensors:
    sensor.formulate()

def reduce_spreads(spreads):
    if len(spreads) <= 1:
        return spreads
    prev = len(spreads)
    new_spread = []
    while prev != len(new_spread) and len(spreads) > 1:
        prev = len(new_spread)
        new_spread = []
        alpha = spreads[0]
        for i in range(1, len(spreads)):
            beta = spreads[i]
            if (alpha[0] >= beta[0] and alpha[0] <= beta[1]) or (beta[0] >= alpha[0] and beta[0] <= alpha[1]) \
                or (abs(alpha[1] - beta[0]) == 1) or (abs(alpha[0] - beta[1]) == 1):
                merged = [min(alpha[0], beta[0]), max(alpha[1], beta[1])]
                alpha = merged 
                if i == len(spreads) - 1:
                    new_spread.append(alpha)
            else:
                if i == len(spreads) - 1:
                    new_spread.append(alpha)
                    new_spread.append(beta)
                else:
                    new_spread.append(alpha)
                alpha = beta
        spreads = new_spread
    return spreads 

sample = [[2256537, 2522023], [1509263, 2256537], [3067557, 4000000], [1393067, 1998869], [1123973, 1240927], [0, 329183], [2523969, 3607247], [2650115, 2730745], [1998869, 2755919], [1938067, 1998869], [0, 1585167]]
sample.sort()
print(reduce_spreads(sample))

for key, spreads in steps.items():

    spreads.sort()
    reduced = reduce_spreads(spreads)
    if (len(reduced) > 1):
        print(key, reduced)
