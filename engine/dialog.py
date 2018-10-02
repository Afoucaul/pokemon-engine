from .screen import Screen 
from .resources import Dialog as R


def dialog_box(text, target=None):
    pass


def simple_menu(options, target=None):
    pass


def callback_menu(options, target=None):
    pass


def draw_frame(x0, y0, x1, y1, target=None):
    """Draw a frame for a dialog box on the target screen"""
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
