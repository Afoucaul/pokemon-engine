import pygame
from .dialog import Dialog
from .overworld import Overworld
from .resources import DialogResources, OverworldResources
from .controller import Controller


class Application:
    width = 0
    height = 0
    fps = 0
    window = None
    frames = []
    clock = None
    controller = None

    @classmethod
    def init(cls, width, height, fps=60):
        cls.width = width
        cls.height = height
        cls.fps = fps

        pygame.init()
        cls.window = pygame.display.set_mode((width, height))

        cls.init_controller()
        cls.init_modules()

    @classmethod
    def init_modules(cls):
        DialogResources.load_frame_from_directory("resources/frame")
        DialogResources.load_font_from_directory("resources/font")
        Dialog.init(cls.window, cls.fps)

        OverworldResources.load_tileset("resources/tileset.png", 16, 16)
        OverworldResources.load_sprites_from_directory("resources/sprites", 'scientist')
        OverworldResources.load_sprites_from_directory("resources/sprites", 'red')
        Overworld.init(cls.window, cls.controller, cls.fps)

    @classmethod
    def init_controller(cls):
        cls.controller = Controller({
            'left':     pygame.locals.K_h, 
            'right':    pygame.locals.K_l, 
            'up':       pygame.locals.K_k, 
            'down':     pygame.locals.K_j, 
            'a':        pygame.locals.K_a, 
            'b':        pygame.locals.K_b, 
            'start':    pygame.locals.K_SPACE, 
            'select':   pygame.locals.K_RETURN
        })

    @classmethod
    def run(cls):
        cls.clock = pygame.time.Clock()
        leave = False
        frame_index = 0

        while True:
            cls.clock.tick(cls.fps)
            frame_index+= 1
            print(frame_index)

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    leave = True
                    break
                elif event.type in (pygame.locals.KEYDOWN, pygame.locals.KEYUP):
                    cls.controller.process(event)

            if leave or not cls.update_frame(frame_index):
                break

            pygame.display.flip()

    @classmethod
    def push_frame(cls, frame):
        """Push an execution frame on top of the application's stack

        The application runs frames, that are execution contexts, in a stack manner: only the top
        frame is executed, and when it ends, it is popped out, and the frame below is executed.

        A frame is a generator: events will be sent to it, and it will be invoked through the `next`
        function
        """
        next(frame)
        cls.frames.append(frame)

    @classmethod
    def pop_frame(cls):
        cls.frames.pop(-1)

    @classmethod
    def update_frame(cls, frame_index):
        try:
            cls.frames[-1].send(frame_index)
            next(cls.frames[-1])

        except StopIteration:
            cls.pop_frame()
            if cls.frames:
                cls.update_frame()
            else:
                return False

        return True
