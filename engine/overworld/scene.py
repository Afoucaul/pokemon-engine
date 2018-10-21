import pygame
from ..screen import Screen
from ..camera import Camera
from ..resources import OverworldResources as R
from ..world import World
from .utils import translation, world_to_screen
from . import objects

import time

class Overworld:
    window = None
    fps = 0
    screen_width = 0
    screen_height = 0
    screen_columns = 0
    screen_rows = 0
    tile_width = 0
    tile_height = 0

    @classmethod
    def init(cls, window, fps, width=160, height=144, columns=10, rows=9):
        cls.fps = fps
        cls.window = window
        cls.screen_width = width
        cls.screen_height = height
        cls.screen_columns = columns
        cls.screen_rows = rows
        cls.tile_width = width // columns
        cls.tile_height = height // rows

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
            x0=int(x_unit*(self.screen.columns/2)),
            y0=int(y_unit*(self.screen.rows/2)),
        )
        self.camera_movement = None

        self.main_character = objects.OverworldObject(self.world, 'red')
        self.main_character.x = x0
        self.main_character.y = y0
        self.world.npcs.append(self.main_character)

    @property
    def x(self):
        return self.main_character.x

    @property
    def y(self):
        return self.main_character.y

    @x.setter
    def x(self, value):
        self.main_character.x = value

    @y.setter
    def y(self, value):
        self.main_character.y = value

    def run(self):
        cls = type(self)
        reset_camera = False

        while True:
            frame_index, events = yield

            self.process_input(events)

            # Update objects
            for npc in self.world.npcs:
                npc.update(frame_index)

            # Update camera's position
            if self.camera_movement:
                try:
                    vector = next(self.camera_movement)
                    self.camera.translate(*vector)

                except StopIteration:
                    self.camera_movement = None
                    reset_camera = True

            # Draw screen
            self.draw_screen(frame_index)

            if reset_camera:
                self.camera.move_to_origin()
                reset_camera = False

            # Blit to the camera what's on screen
            self.camera.capture()

            # Scale camera onto window
            pygame.transform.scale(self.camera, cls.window.get_size(), cls.window)

            yield

    def draw_screen(self, frame):
        cls = type(self)

        i0 = self.x - self.screen.columns // 2
        j0 = self.y - self.screen.rows // 2

        # Draw lower tile layer
        for i in range(self.screen.columns):
            for j in range(self.screen.rows):
                tile_index = self.world.lower_tiles[i0+i, j0+j]
                tile = R.tile(tile_index)
                self.screen.blit(tile, (i, j)) 

        # Draw objects
        for npc in self.world.npcs:
            a, b = world_to_screen(self, npc.x, npc.y)
            self.screen.blit(
                npc.sprite, 
                (a, b),
                delta_x=npc.delta_x,
                delta_y=npc.delta_y
            )

        # Draw upper tile layer
        for i in range(self.screen.columns):
            for j in range(self.screen.rows):
                tile_index = self.world.upper_tiles[i0+i, j0+j]
                tile = R.tile(tile_index)
                self.screen.blit(tile, (i, j)) 

    def process_input(self, events):
        cls = type(self)

        for event in events:
            if event.type == pygame.locals.KEYDOWN:
                if not self.camera_movement:
                    x, y = 0, 0
                    if event.key == pygame.locals.K_k:
                        # UP
                        y = -1

                    elif event.key == pygame.locals.K_j:
                        # DOWN
                        y = 1

                    elif event.key == pygame.locals.K_h:
                        # LEFT
                        x = -1

                    elif event.key == pygame.locals.K_l:
                        # RIGHT
                        x = 1

                    if self.main_character.can_move_to(self.x + x, self.y + y):
                        self.camera_movement = translation(
                            x*cls.tile_width, 
                            y*cls.tile_height
                        )
                        self.main_character.translate(x, y)
