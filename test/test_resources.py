import os
import pytest
import pygame

from engine import resources

RESOURCES_PATH = "resources"


@pytest.fixture(scope="session", autouse=True)
def start_pygame(request):
    pygame.init()
    pygame.display.set_mode((640, 480))


def test_dialog_loading():
    resources.DialogResources.load_frame_from_directory(os.path.join(RESOURCES_PATH, "frame"))
    for side in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'bg']:
        assert side in resources.DialogResources.frame_elements
        assert isinstance(resources.DialogResources.frame_elements[side], pygame.Surface)

    resources.DialogResources.load_font_from_directory(os.path.join(RESOURCES_PATH, "font"))
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,.'":
        assert char in resources.DialogResources.characters
        assert isinstance(resources.DialogResources.characters[char], pygame.Surface)
