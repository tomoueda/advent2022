
from args import example, actual

segs = actual.split('\n\n')
lines = segs[0].split('\n')
lines = lines[1:]
buckets_num = ((len(lines[0]) + 1) // 4)
buckets = []
for i in range(buckets_num):
    buckets.append(list())

print(lines)
def construct_buckets(lines):
    for line in lines:
        idx = 0
        for i in range(0, len(line), 4):
            linear = line[i:i+4]
            letter = linear[1]
            if letter == '1':
                return
            elif letter != ' ':
                buckets[idx].insert(0, letter)
            idx += 1
    
construct_buckets(lines)
print(buckets)

instructions = segs[1]
for instr in instructions.split('\n'):
    raw = instr.split(' ')
    how_many = int(raw[1])
    from_ = int(raw[3]) - 1
    to_ = int(raw[5]) - 1
    print(how_many, from_, to_)
    for i in range(how_many):
        # part 1 letter = buckets[from_].pop()
        letter = buckets[from_].pop(-how_many + i)
        buckets[to_].append(letter)

for bucket in buckets:
    print(bucket.pop())