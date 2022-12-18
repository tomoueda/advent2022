
class V:
    def __init__(self, *args):
        self.coor = tuple(args) 

    def __add__(self, o):
        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] + e[1] for e in zip(self.coor, o)])

    def __radd__(self, o):
        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] + e[1] for e in zip(self.coor, o)])

    def __rmul__(self, o):
        if isinstance(o, int):
            return V(*[o * e for e in self.coor])
        if len(self) != len(o):
            raise Exception('unequal lengths')
        return V(*[e[0] * e[1] for e in zip(self.coor, o)])

    def __getitem__(self, key):
        return self.coor[key]

    def __hash__(self):
        return hash(self.coor)

    def __eq__(self, o):
        if isinstance(o, tuple):
            return self.coor == o
        return self.coor == o.coor

    def __str__(self):
        return str(self.coor)

    def __repr__(self):
        return str(self.coor)

    def __len__(self):
        return len(self.coor)

def test():
    assert V(1, 2) + (3, 4) == (4, 6)
    assert 3 * V(1, 2) == (3, 6)
    assert (3, 4) * V(1, 2) == (3, 8)
    assert V(1, 2, 3) + (3, 4, 5) == (4, 6, 8)
test()