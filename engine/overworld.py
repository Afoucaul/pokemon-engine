from .screen import Screen


class Overworld:
    screen = None
    fps = 0

    def init(cls, window, fps, width=160, height=144, columns=10, rows=9):
        cls.fps = fps
        cls.screen = Screen(window, width, height, columns, rows)

    def __init__(self):
        pass

    def run(self, world):
        while True:
            frame_index, events = yield

            yield
