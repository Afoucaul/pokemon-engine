import numpy as np
from ..resources import OverworldResources as R


class Universe:
    def __init__(self, worlds, x0, y0):
        self.worlds = worlds
        self.x = x0
        self.y = y0

    @property
    def current(self):
        return self.worlds[self.x][self.y]

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.worlds = [[x if isinstance(x, str) else x.path for x in line] for line in self.worlds]
        if self.worlds[x][y] is None:
            raise ValueError("No world at {}".format((x, y)))

        self.load_at(x, y)
        self.load_at(x-1, y)
        self.load_at(x+1, y)
        self.load_at(x, y-1)
        self.load_at(x, y+1)

    def translate(self, x, y):
        self.move_to(self.x + x, self.y + y)
    
    def load_at(self, x, y):
        try:
            if isinstance(self.worlds[x][y], str):
                self.worlds[x][y] = R.load_world(self.worlds[x][y])
        except IndexError:
            pass
