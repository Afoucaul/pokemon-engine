import pygame


class Camera(pygame.Surface):
    def __init__(self, width, height, source, *, x0=0, y0=0):
        super().__init__((width, height), pygame.SRCALPHA)

        self.width = width
        self.height = height
        self.source = source
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0

    def capture(self):
        """(x, y): camera's center coordinates relatively to its source"""
        x0 = self.get_width() // 2 - self.x
        y0 = self.get_height() // 2 - self.y
        self.blit(self.source, (x0, y0))

    def translate(self, x, y):
        self.x += x
        self.y += y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_to_origin(self):
        self.x = self.x0
        self.y = self.y0
