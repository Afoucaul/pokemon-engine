from .utils import translation, vector_to_direction
from ..resources import OverworldResources as R


class OverworldObject:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.translation = None
        self.position = 'down-neutral'
        self.behaviour = None

    def translate(self, x, y):
        self.translation = translation(x, y, after=lambda: self._finish_translation(x, y))

    def update(self, frame):
        if self.translation is not None:
            try:
                x, y = next(self.translation)
                self.x += x
                self.y += y

                # Update sprite
                direction = vector_to_direction(x, y)
                self.position = "{}-neutral".format(direction)

            except StopIteration:
                self.translation = None

        elif self.behaviour is not None:
            self.behaviour(self, frame)

    def _finish_translation(self, x, y):
        self.translation = None
        self.x += x
        self.y += y

    @property
    def sprite(self):
        return R.sprite(self.name, self.position)

    def can_move_to(self, world, x, y):
        """Tells if the object can move to a given tile"""
        return True

    def __repr__(self):
        return "OverworldObject({}) at ({}, {})".format(self.name, self.x, self.y)


def behaviour_random_walk(instance, frame):
    if frame < 15:
        npr.choice(('n', 's', 'e', 'w'))
