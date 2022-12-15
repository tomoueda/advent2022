from args import example, actual
from collections import defaultdict 

import re

pattern = 'Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)'
pattern = re.compile('(-?\d+)+')

steps = defaultdict(set)
class Sensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_beacon(self, x, y):
        self.bx = x
        self.by = y 

    def manhattan(self):
        return abs(self.x - self.bx) + abs(self.y - self.by)

    def black_out(self, horizon):
        ydist = abs(self.y - horizon)
        dist = self.manhattan()
        black_out = set()
        if ydist < dist:
            slack = (dist - ydist)
            black_out.add((self.x, horizon))
            for i in range(self.x - slack, slack + self.x + 1):
                black_out.add((i, horizon))
        return black_out
    
    def reverse_black_out(self, horizon, upper_limit):
        ydist = abs(self.y - horizon)
        dist = self.manhattan()
        poss = set()
        if ydist < dist:
            slack = (dist - ydist)
            for i in range(upper_limit):
                if i not in range(self.x - slack, slack + self.x + 1):
                    if (i, horizon) != self.get() and (i, horizon) != self.get_beacon():
                        poss.add((i, horizon))
        return poss 
    
    def total_reverse(self, upper_limit):
        for i in range(upper_limit):
            ydist = abs(self.y - i)
            dist = self.manhattan()
            if ydist < dist:
                if i not in steps:
                    steps[i] = self.reverse_black_out(i, upper_limit)
                else:
                    steps[i] = steps[i].intersection(self.reverse_black_out(i, upper_limit))

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

# horizon = 2000000  part 1
def part1(horizon):
    no_beacon = set()
    for sensor in sensors:
        no_beacon.update(sensor.black_out(horizon))

    for sensor in sensors:
        s = sensor.get()
        b = sensor.get_beacon()
        if s in no_beacon:
            no_beacon.remove(s)
        if b in no_beacon:
            no_beacon.remove(b)
    return no_beacon

# part 2
upper_limit = 4000000
for sensor in sensors:
    sensor.total_reverse(upper_limit)

for key, value in steps.items():
    if len(value) != 0:
        v = value.pop()
        print(v[0] * 4000000 + v[1])
