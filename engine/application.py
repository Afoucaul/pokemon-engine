import pygame
from .dialog import Dialog
from .resources import DialogResources


class Application:
    width = 0
    height = 0
    window = None
    frames = []
    clock = None

    @classmethod
    def init(cls, width, height):
        cls.width = width
        cls.height = height

        pygame.init()
        cls.window = pygame.display.set_mode((width, height))
        Dialog.init(cls.window)
        DialogResources.load_frame_from_directory("resources/frame")

    @classmethod
    def run(cls, fps=30):
        cls.clock = pygame.time.Clock()
        leave = False

        while True:
            cls.clock.tick(fps)

            events = []
            for event in pygame.event.get():
                if event.type == QUIT:
                    leave = True
                    break
                events.append(event)

            if leave:
                break

            # Dispatch events to the current component
            # Update the current component
            try:
                cls.frames[-1].send(events)
                next(cls.frames[-1])

            except StopIteration:
                cls.pop_frame()
                cls.frames[-1].send(events)
                next(cls.frames[-1])

    @classmethod
    def push_frame(cls, frame):
        next(frame)
        cls.frame.append(frame)

    @classmethod
    def pop_frame(cls):
        cls.frame.pop(-1)
