from args import example
import re

sensors = []

pattern = re.compile('(-?\d+)+')
lines = example.split('\n')
for line in lines:
    results = map(int, pattern.findall(line))
    sx = next(results)
    sy = next(results)
    bx = next(results)
    by = next(results)
    print(sx, sy, bx, by)
    dist = abs(sx - bx) + abs(sy - by)
    sensors.append({'sensor': (sx, sy), 'dist': dist})

def boundaries(sensors):
    for i in range(sensors['dist'] + 1):
        sensors


