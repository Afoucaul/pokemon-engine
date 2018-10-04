import pygame
from .screen import Screen
from .camera import Camera
from .resources import OverworldResources as R
from .world import World


class Overworld:
    window = None
    fps = 0
    screen_width = 0
    screen_height = 0
    screen_columns = 0
    screen_rows = 0

    @classmethod
    def init(cls, window, fps, width=160, height=144, columns=10, rows=9):
        cls.fps = fps
        cls.window = window
        cls.screen_width = width
        cls.screen_height = height
        cls.screen_columns = columns
        cls.screen_rows = rows

    def __init__(self, world: World, x0=0, y0=0):
        cls = type(self)

        x_unit = cls.screen_width // cls.screen_columns
        y_unit = cls.screen_height // cls.screen_rows

        self.world = world
        self.screen = Screen(
            None,
            (cls.screen_columns+2) * x_unit, 
            (cls.screen_rows+2) * y_unit,
            cls.screen_columns + 2,
            cls.screen_rows + 2
        )
        self.camera = Camera(
                cls.screen_width, 
                cls.screen_height, 
                self.screen, 
                x0=int(x_unit*(cls.screen_columns/2)),
                y0=int(y_unit*(cls.screen_rows/2)),
                )
        self.x = x0
        self.y = y0

    def run(self):
        cls = type(self)

        while True:
            frame_index, events = yield
            print(frame_index)

            self.process_input(events)

            # Draw screen
            self.draw_screen()

            # Update camera's position

            # Blit to the camera what's on screen
            self.camera.capture()

            # Scale camera onto window
            pygame.transform.scale(self.camera, cls.window.get_size(), cls.window)

            yield

    def draw_screen(self):
        cls = type(self)

        i0 = self.x - self.screen.columns // 2
        j0 = self.y - self.screen.rows // 2

        # Draw lower tile layer
        for i in range(self.screen.columns):
            for j in range(self.screen.rows):
                tile_index = self.world.lower_tiles[i0+i][j0+j]
                tile = R.tile(tile_index)
                self.screen.blit(tile, (i, j)) 

        for npc in self.world.npcs:
            # Draw NPCs at the right places
            pass

        # Draw upper tile layer
        for i in range(self.screen.columns):
            for j in range(self.screen.rows):
                tile_index = self.world.upper_tiles[i0+i][j0+j]
                tile = R.tile(tile_index)
                self.screen.blit(tile, (i, j)) 

    def process_input(self, events):
        for event in events:
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_k:
                    # UP
                    self.y -= 1

                elif event.key == pygame.locals.K_j:
                    # DOWN
                    self.y += 1

                elif event.key == pygame.locals.K_h:
                    # LEFT
                    self.x -= 1

                elif event.key == pygame.locals.K_l:
                    # RIGHT
                    self.x += 1
