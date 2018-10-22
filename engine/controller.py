import pygame


KEYS = ('left', 'right', 'up', 'down', 'a', 'b', 'start', 'select')


class Controller:
    def __init__(self, mapping):
        validate_mapping(mapping)
        self.mapping = {v: k for k, v in mapping.items()}
        self.keys = {key: 0 for key in mapping}

    def process(self, event):
        print("==== EVENT ====")
        print(event.type)
        print(pygame.locals.KEYDOWN, pygame.locals.KEYUP)
        print()
        if event.type == pygame.locals.KEYDOWN:
            self.keys[self.mapping[event.key]] = 1

        elif event.type == pygame.locals.KEYUP:
            self.keys[self.mapping[event.key]] = 0

    def __getattr__(self, key):
        return self.keys[key]


def validate_mapping(mapping):
    for key in KEYS:
        mapping[key]
