import os
import pytest

import pygame
from pygame.locals import QUIT

from engine import dialog
from engine.screen import Screen
from engine.resources import Dialog


RESOURCES_PATH = "resources"
WINDOW = None


@pytest.fixture(scope="session", autouse=True)
def start_pygame():
    global WINDOW
    pygame.init()
    WINDOW = pygame.display.set_mode((640, 576))

    Dialog.load_frame_from_directory(os.path.join(RESOURCES_PATH, "frame"))
    print(Dialog.frame_elements)


def test_frame():
    screen = Screen(160, 144, 20, 18)
    dialog.draw_frame(0, 0, 4, 4, screen)
    pygame.transform.scale(screen, (640, 576), WINDOW)
    pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False



def test_dialog_box():
    pass
