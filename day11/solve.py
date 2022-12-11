from functools import reduce
from args import example, actual
from collections import defaultdict
import re

monkey_lines = actual.split('\n\n')
monkey_count = defaultdict(lambda: 0)
monkeys = []

def add(x, y):
    return x + y

def mult(x, y):
    return x * y

class Monkey:
    def __init__(self, lines):
        self.num = self._parse_num(lines[0])
        self.items = self._parse_items(lines[1])
        self.func, self.object = self._parse_operator(lines[2])
        self.divisible_by = self._parse_divisible_by(lines[3])
        self.true_cond = int(lines[4].split(' ')[-1])
        self.false_cond = int(lines[5].split(' ')[-1])
    
    def operate(self, item, crt):
        if self.object == 'old':
            return self.func(item, item) % crt # part 1 //3
        return self.func(item, int(self.object)) % crt # part 1 // 3
    
    def test(self, new_item):
        if new_item % self.divisible_by == 0:
            return self.true_cond
        return self.false_cond

    def _parse_num(self, line):
        pattern = "Monkey (\d+):"
        match = re.search(pattern, line)
        return match.group(1)
    
    def _parse_items(self, line):
        return list(map(int, line.split(': ')[1].split(', ')))
    
    def _parse_operator(self, line):
        operator_str = line.split(' ')
        operator = add if operator_str[-2] == '+' else mult
        return (operator, operator_str[-1])
    
    def _parse_divisible_by(self, line):
        return int(line.split(' ')[-1])
    
    def __str__(self):
        return str(self.items)

for monkey_paragraph in monkey_lines:
    monkey_lines = monkey_paragraph.split('\n')
    monkeys.append(Monkey(monkey_lines))

crt = reduce(mult, [monkey.divisible_by for monkey in monkeys], 1)
print(crt)

rounds = 1 
num_rounds = 10001

while rounds < num_rounds:
    for monkey in monkeys:
        while len(monkey.items) != 0:
            item = monkey.items.pop(0)
            monkey_count[monkey.num] += 1
            new_item = monkey.operate(item, crt)
            to_monkey = monkey.test(new_item)
            monkeys[to_monkey].items.append(new_item)

    #print('-------', rounds, '-------')
    #for monkey in monkeys:
    #    print(monkey.num, monkey.items)
    #print('---------------')
    rounds += 1
ans = []
for key, val in monkey_count.items():
    ans.append((val, key))
ans.sort()
print(ans[-1][0] * ans[-2][0])

