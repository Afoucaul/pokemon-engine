import os
import pytest

import pygame
from pygame.locals import QUIT

from engine import dialog
from engine import application
from engine.screen import Screen
from engine.resources import DialogResources


RESOURCES_PATH = "resources"


@pytest.fixture(scope="session", autouse=True)
def start_pygame():
    application.Application.init(320, 288)


@pytest.mark.skip()
def test_frame():
    dialog.Dialog.draw_frame(0, 0, 4, 4)
    dialog.Dialog.draw_frame(0, 13, 19, 17)
    pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

    dialog.Dialog.window.fill((0, 0, 0))
    dialog.Dialog.screen.fill((0, 0, 0))
    pygame.display.flip()


def test_dialog_box():
    dialog.dialog_box("hello world! my name is jean bon beurre and i love ham butter sandwiches")
    application.Application.run()
