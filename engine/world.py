import numpy as np


class World:
    def __init__(self, *, width=0, height=0):
        self.lower_tiles = np.random.randint(100, size=(height, width), dtype=np.int16)
        self.upper_tiles = -1*np.ones((height, width), dtype=np.int16)
        self.collisions = np.zeros((height, width), dtype=np.int16)
        self.events = np.zeros((height, width), dtype=np.int16)
        self.npcs = []
        self.path = ""

    def set_layer(self, layer_name, layer):
        print("Setting layer {} for world of size {}; new layer is of size {}".format(
            layer_name, self.lower_tiles.shape, (len(layer), len(layer[0]))))
        getattr(self, layer_name)[:] = layer

    @property
    def width(self):
        return self.lower_tiles.shape[0]

    @property
    def height(self):
        return self.lower_tiles.shape[1]
