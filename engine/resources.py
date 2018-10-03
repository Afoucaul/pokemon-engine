import os
import pygame


class DialogResources:
    frame_elements = {}
    characters = {}

    @classmethod
    def load(cls):
        cls.load_frame(path)

    @classmethod
    def frame(cls, side):
        """side: either n, s, e, w, or a combination of those"""
        return cls.frame_elements[side]

    @classmethod
    def font(cls, char):
        """char: any letter defined in the charset"""
        return cls.characters[char]

    @classmethod
    def background(cls):
        return cls.frame_elements['bg']

    @classmethod
    def load_frame(cls, paths):
        for side, path in paths.items():
            cls.frame_elements[side] = pygame.image.load(path).convert()

    @classmethod
    def load_font(cls, paths):
        for char, path in paths.items():
            cls.characters[char] = pygame.image.load(path).convert()

    @classmethod
    def load_frame_from_directory(cls, path):
        sides = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'bg']
        cls.load_frame({side: os.path.join(path, "{}.png".format(side)) for side in sides})

    @classmethod
    def load_font_from_directory(cls, path):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,.'"
        cls.load_font({char: os.path.join(path, "{}.png".format(char)) for char in chars})


class OverworldResources:
    tileset = []

    @classmethod
    def load_tileset(cls, path, width, height=None):
        if height is None:
            height = width

        source = pygame.image.load(path).convert()
        for i in range(source.get_width() // width):
            for j in range(source.get_height() // height):
                tile = pygame.Surface((width, height))
                tile.blit(source, (0, 0), (i*width, j*height, (i+1)*width, (j+1)*height))
                cls.tileset.append(tile)

    @classmethod
    def tile(cls, index):
        return cls.tileset[index]
