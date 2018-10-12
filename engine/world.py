import numpy as np


class World:
    def __init__(self, *, width=0, height=0):
        self.lower_tiles = np.random.randint(100, size=(width, height), dtype=np.int16)
        self.upper_tiles = np.random.randint(100, size=(width, height), dtype=np.int16)
        self.collisions = np.zeros((width, height), dtype=np.int16)
        self.events = np.zeros((width, height), dtype=np.int16)
        self.npcs = []
