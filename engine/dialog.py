import pygame
from pygame.locals import QUIT
from .screen import Screen 
from .resources import DialogResources as R
from . import application


def split_text(text, width):
    """Split text into lines of max width; returns a generator"""
    words = text.split(" ")
    line = ""
    for word in words:
        l = line + (" " if line else "") + word
        if len(l) > width:
            print("Yielding line", line)
            yield line
            line = word
        else:
            line = l

    print("Yielding line", line)
    yield line


class Dialog:
    screen = None
    fps = 0

    @classmethod
    def init(cls, window, fps, width=160, height=144, columns=20, rows=18):
        cls.fps = fps
        cls.screen = Screen(window, width, height, columns, rows)

    @classmethod
    def dialog_box(cls, text):
        """Display a dialog box on two lines at the bottom of the screen"""
        target = cls.screen

        x1 = target.columns - 1
        y1 = target.rows - 1
        x0 = 0
        y0 = y1 - 5

        cls.draw_frame(x0, y0, x1, y1)
        lines = split_text(text, x1 - x0 - 3)
        line = iter(next(lines))
        row = 0
        column = 1
        waiting = False
        finished = False

        while True:
            print("Row:", row)
            frame, events = yield

            if not waiting:
                char = next(line, None)
                if char is None:
                    if row == 1:
                        waiting = True
                    try:
                        line = iter(next(lines))
                        row = 1 - row
                        column = 1

                    except StopIteration:
                        finished = True
                        waiting = True

                else:
                    cls.draw_char(char, column, y0 + 2*row + 2)
                    print("Drawing char at", char, column, y0 + 2*row + 2)
                    column += 1

            else:
                if events:
                    if finished:
                        break
                    waiting = False
                    row = 0
                    column = 1
                    cls.draw_frame(x0, y0, x1, y1)

                if finished or frame >= cls.fps / 2: 
                    cls.draw_char(" ", x1-1, y1-1)
                else:
                    cls.draw_char("v", x1-1, y1-1)

            yield
    
    @classmethod
    def simple_menu(options, target=None):
        pass
    
    @classmethod
    def callback_menu(cls, options):
        pass
    
    @classmethod
    def draw_frame(cls, x0, y0, x1, y1):
        """Draw a frame for a dialog box on the target screen"""
        target = cls.screen

        target.blit(R.frame('nw'), (x0, y0))
        target.blit(R.frame('sw'), (x0, y1))
        target.blit(R.frame('ne'), (x1, y0))
        target.blit(R.frame('se'), (x1, y1))
    
        for x in range(x0+1, x1):
            target.blit(R.frame('n'), (x, y0))
            target.blit(R.frame('s'), (x, y1))
    
        for y in range(y0+1, y1):
            target.blit(R.frame('w'), (x0, y))
            target.blit(R.frame('e'), (x1, y))
    
        for x in range(x0+1, x1):
            for y in range(y0+1, y1):
                target.blit(R.background(), (x, y))

    @classmethod
    def draw_char(cls, char, x, y):
        cls.screen.blit(R.font(char), (x, y))


def dialog_box(text):
    application.Application.push_frame(Dialog.dialog_box(text))
