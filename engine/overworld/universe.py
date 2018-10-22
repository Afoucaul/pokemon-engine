import numpy as np
from ..resources import OverworldResources as R


def catch_as_None(f):
    def g(*a, **k):
        try:
            return f(*a, **k)
        except Exception:
            return None
    return g


class Universe:
    def __init__(self, worlds, i0, j0):
        self.worlds = worlds
        self.i = i0
        self.j = j0

        self.move_to(i0, j0)

    @property
    def current(self):
        return self.worlds[self.i][self.j]

    @property
    @catch_as_None
    def upper(self):
        return self.worlds[self.i-1][self.j]

    @property
    @catch_as_None
    def lower(self):
        return self.worlds[self.i+1][self.j]

    @property
    @catch_as_None
    def left(self):
        return self.worlds[self.i][self.j-1]

    @property
    @catch_as_None
    def right(self):
        return self.worlds[self.i][self.j+1]

    def move_to(self, i, j):
        self.i = i
        self.j = j
        self.worlds = [[i if isinstance(i, str) else i.path for i in line] for line in self.worlds]
        if self.worlds[i][j] is None:
            raise ValueError("No world at {}".format((i, j)))

        self.load_at(i, j)
        self.load_at(i-1, j)
        self.load_at(i+1, j)
        self.load_at(i, j-1)
        self.load_at(i, j+1)

    def translate(self, i, j):
        self.move_to(self.i + i, self.j + j)
    
    def load_at(self, i, j):
        try:
            if isinstance(self.worlds[i][j], str):
                self.worlds[i][j] = R.load_world(self.worlds[i][j])
        except IndexError:
            pass
