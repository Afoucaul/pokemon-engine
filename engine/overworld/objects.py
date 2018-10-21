from .utils import translation, vector_to_direction
from ..resources import OverworldResources as R
from .scene import Overworld


class OverworldObject:
    def __init__(self, world, name):
        self.world = world
        self.name = name
        self.x = 0
        self.y = 0
        self.delta_x = 0
        self.delta_y = 0
        self.translation = None
        self.translation_frame = 0
        self.direction = 'down'
        self.stance = 'neutral'
        self.behaviour = None

    def translate(self, x, y):
        self.translation = translation(
            x * Overworld.tile_width, 
            y * Overworld.tile_height, 
            after=lambda: self._finish_translation(x, y)
        )
        self.translation_threshold = Overworld.tile_width if x else Overworld.tile_height

    def update(self, frame):
        if self.translation is not None:
            self.translation_frame += 1
            try:
                x, y = next(self.translation)
                self.delta_x += x
                self.delta_y += y

                # Update sprite
                self.direction = vector_to_direction(x, y)
                if self.translation_frame < self.translation_threshold:
                    self.stance = "walking"
                else:
                    self.stance = "neutral"

            except StopIteration:
                self.translation = None
                self.delta_x = 0
                self.delta_y = 0
                self.stance = "neutral"

        elif self.behaviour is not None:
            self.behaviour(self, frame)

    def _finish_translation(self, x, y):
        self.translation = None
        self.translation_frame = 0
        self.x += x
        self.y += y

    @property
    def sprite(self):
        return R.sprite(self.name, "{}-{}".format(self.direction, self.stance))

    def can_move_to(self, x, y):
        """Tells if the object can move to a given tile"""
        # TODO: compare with current state
        return self.world.collisions[x-1, y-1] == 0

    def __repr__(self):
        return "OverworldObject({}) at ({}, {})".format(self.name, self.x, self.y)
