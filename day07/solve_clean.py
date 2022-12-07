from args import example, actual 

class Tree:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.total = 0 
        self.sub_directory = []
    
    def add(self, size):
        self.total += size

    def sum(self):
        return self.total + sum([x.sum() for x in self.sub_directory])

    def get_tree(self, name):
        for sub in self.sub_directory:
            if sub.name == name:
                return sub
        return None

lines = actual.split('\n')
curr = Tree('/', None)
head = curr

for line in lines:
    elems = line.split(' ')
    if elems[0] == '$':
        if elems[1] == 'cd':
            dir = elems[2]
            if dir == '/':
                curr = head
            elif dir == '..':
                curr = curr.parent
            else:
                tree = curr.get_tree(dir)
                if not tree:
                    tree = Tree(dir, curr)
                    curr.sub_directory.append(tree)
                curr = tree
    elif elems[0] == 'dir':
        continue
    else:
        curr.add(int(elems[0]))

        
s = 0
total = 70000000
diff = 30000000
taken_up = head.sum()
this_is = (diff - (total - taken_up))

to_delete = 100000000000000000
q = [head]
while len(q) != 0:
    temp = q.pop()
    t_s = temp.sum()
    if t_s > this_is:
        to_delete = min(to_delete, t_s)
#    if t_s < 100000: part1
#        s += t_s
    for dir in temp.sub_directory:
        q.append(dir)
# print(s)
print(to_delete)

