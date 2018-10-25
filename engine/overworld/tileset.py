import itertools
from ..resources import OverworldResources as R


class Tileset:
    tileset = []
    fps = 0

    @classmethod
    def init(cls, tileset, fps):
        cls.tileset = tileset
        cls.fps = fps

        # TODO: the animated tileset should ideally be created using a graphical tool
        add_animations_for_blue_tileset(cls.tileset)

    @classmethod
    def tile(cls, index, frame):
        if isinstance(cls.tileset[index], int):
            return R.tile(cls.tileset[index])
        else:
            return R.tile(cls.tileset[index][int(frame * len(cls.tileset[index]) / cls.fps)])


def add_animations_for_blue_tileset(tiles_list):
    tiles_list[11] = (25, 25, 26, 11)
    a = 38
    tiles_list[11+a] = (25+a, 25+a, 26+a, 11+a)

    for i in range(3):
        for j in range(3):
            a = 38*i + j
            tiles_list[8+a] = (8+a, 27+a, 30+a, 33+a, 30+a, 27+a)
