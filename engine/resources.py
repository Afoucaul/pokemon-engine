import os
import pygame
import pickle


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
    sprites = {}
    world = None
    sprites_directory = ""

    @classmethod
    def load_tileset(cls, path, width, height=None):
        if height is None:
            height = width

        source = pygame.image.load(path).convert_alpha()
        for j in range(source.get_height() // height):
            for i in range(source.get_width() // width):
                tile = pygame.Surface((width, height), pygame.SRCALPHA)
                tile.blit(source, (0, 0), (i*width, j*height, (i+1)*width, (j+1)*height))
                cls.tileset.append(tile)

    @classmethod
    def load_sprites(cls, paths, name):
        cls.sprites[name] = {
            direction: pygame.image.load(path).convert_alpha()
            for (direction, path) in paths.items()
        }

    @classmethod
    def load_sprites_from_directory(cls, directory, name):
        cls.sprites_directory = directory
        cls.load_sprites({
            "{}-{}".format(direction, stance): 
            os.path.join(directory, "{}_{}_{}.png".format(name, direction, stance))
            for direction in ['down', 'left', 'right', 'up']
            for stance in ['neutral', 'walking']
        }, name)

    @classmethod
    def load_world(cls, path):
        with open(path, 'rb') as source:
            cls.world = pickle.load(source)

    @classmethod
    def tile(cls, index):
        return cls.tileset[index]

    @classmethod
    def sprite(cls, name, direction):
        if name not in cls.sprites:
            cls.load_sprites_from_directory(cls.sprites_directory, name)
        return cls.sprites[name][direction]
