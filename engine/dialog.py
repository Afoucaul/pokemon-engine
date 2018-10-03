import pygame
from pygame.locals import QUIT
from .screen import Screen 
from .resources import DialogResources as R
from .application import Application


def split_text(text, width):
    """Split text into lines of max width"""
    return [text]


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
        y0 = y1 - 6
    
        cls.draw_frame(x0, y0, x1, y1)
        while True:
            frame, events = yield
            print("Event: {}".format(events))
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
            print("Blitting W at ({}, {})".format(x0, y))
            target.blit(R.frame('e'), (x1, y))
    
        for x in range(x0+1, x1):
            for y in range(y0+1, y1):
                target.blit(R.background(), (x, y))

    @classmethod
    def draw_char(cls, x, y, char):
        cls.screen.blit(R.font(char), (x, y))


def dialog_box(text):
    Application.push_frame(Dialog.dialog_box(text))
