import pygame

class Screen(pygame.Surface):
    def __init__(self, width, height, columns, rows):
        x_unit = width // columns
        y_unit = height // rows

        real_width = x_unit * columns
        real_height = y_unit * rows

        super(real_width, real_height)

        self.width = real_width
        self.height = real_height
        self.columns = columns
        self.rows = rows
        self.x_unit = x_unit
        self.y_unit = y_unit

    def blit(self, image, origin):
        """origin: pair within the (columns, rows) range"""
        i, j = origin
        x = i * self.x_unit
        y = j * self.y_unit

        super().blit(image, (x, y))
