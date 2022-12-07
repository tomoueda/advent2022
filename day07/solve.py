from args import example, actual 

class Tree:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.sub_directory = []
    
    def append(self, line):
        output = line.split(' ')
        if output[0] == 'dir':
            return 
        self.files.append(int(output[0]))

    def sum(self):
        s = sum(self.files)
        s += sum([x.sum() for x in self.sub_directory])
        return s

    def get_tree(self, name):
        for sub in self.sub_directory:
            if sub.name == name:
                return sub
        return None

out = actual.split('\n')
curr = Tree('/', None)
head = curr

def linesiter():
    for line in out:
        yield line
    yield None

lines = linesiter()

output = next(lines)
while output != None:
    elems = output.split(' ')
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
            output = next(lines)
        if elems[1] == 'ls':
            output = next(lines)
            while output and output[0] != '$':
                curr.append(output)
                output = next(lines)

        
s = 0
total = 70000000
diff = 30000000
target = 4000000
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

