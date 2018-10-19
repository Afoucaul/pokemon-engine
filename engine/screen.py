import pygame


class Screen(pygame.Surface):
    def __init__(self, window, width, height, columns, rows):
        x_unit = width // columns
        y_unit = height // rows
        assert not x_unit % 2
        assert not y_unit % 2

        real_width = x_unit * columns
        real_height = y_unit * rows

        super().__init__((real_width, real_height), pygame.SRCALPHA)

        self.window = window
        self.width = real_width
        self.height = real_height
        self.columns = columns
        self.rows = rows
        self.x_unit = x_unit
        self.y_unit = y_unit

    def blit(self, image, origin, *, delta_x=0, delta_y=0):
        """origin: pair within the (columns, rows) range"""
        i, j = origin
        x = i * self.x_unit + delta_x
        y = j * self.y_unit + delta_y

        if delta_x or delta_y:
            print("Blitting on screen at ({}, {})".format(x, y))

        super().blit(image, (x, y))
        if self.window is not None:
            pygame.transform.scale(self, self.window.get_size(), self.window)
