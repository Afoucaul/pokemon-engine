from .utils import translation
from ..resources import OverworldResources as R


class OverworldObject:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.translation = None
        self.sprite = R.sprite(self.name, 'down-neutral')

    def translate(self, x, y):
        self.translation = translation(x, y, after=lambda: self._finish_translation(x, y))

    def update(self):
        if self.translation is not None:
            x, y = next(self.translation)
            self.x += x
            self.y += y

    def _finish_translation(self, x, y):
        self.translation = None
        self.x += x
        self.y += y
