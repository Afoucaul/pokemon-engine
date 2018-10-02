import os
import pygame


class Dialog:
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
    def character(cls, char):
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
    def load_frame_from_directory(cls, path):
        sides = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'bg']
        cls.load_frame({side: os.path.join(path, "{}.png".format(side)) for side in sides})
