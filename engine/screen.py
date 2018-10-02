import pygame

class Screen(pygame.Surface):
    def __init__(self, width, height, columns, rows):
        super(width, height)

        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows

    def blit(self, image, origin):
        super().blit(image, origin)
