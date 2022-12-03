from args import example, actual

def find_collison(line):
    half = int(len(line) / 2)
    first, second = line[:half], line[half:]
    first_set = set()
    second_set = set()
    for a in first:
        first_set.add(a)
    for b in second:
        second_set.add(b)
    inter = first_set.intersection(second_set)
    for a in inter:
        return a
    

# s = 0
# for line in actual.split('\n'):
#     let = find_collison(line)
#     ord_val = ord(let) 
#     if ord_val <= 122 and ord_val >= 97:
#         s += ord_val - 96
#     else:
#         s += ord_val - 38 
# print(s)

# part 2
s = 0
lines = actual.split('\n')
for i in range(0, len(lines), 3):
    inter = set(lines[i]).intersection(set(lines[i + 1])).intersection(set(lines[i+2]))
    for a in inter:
        ord_val = ord(a) 
        if ord_val <= 122 and ord_val >= 97:
            s += ord_val - 96
        else:
            s += ord_val - 38 

print(s)