import numpy as np


class World:
    def __init__(self, *, width=0, height=0):
        lower_tiles = np.zeros((width, height), type=np.int16)
        upper_tiles = np.zeros((width, height), type=np.int16)
        npcs = np.zeros((width, height), type=np.int16)
        events = np.zeros((width, height), type=np.int16)
        collisions = np.zeros((width, height), type=np.int16)
