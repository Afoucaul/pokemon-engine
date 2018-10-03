import os
import pytest
import pygame

from engine import resources

RESOURCES_PATH = "resources"
WINDOW = None


@pytest.fixture(scope="session", autouse=True)
def start_pygame(request):
    global WINDOW
    pygame.init()
    WINDOW = pygame.display.set_mode((1280, 960))


def test_dialog_loading():
    resources.DialogResources.load_frame_from_directory(os.path.join(RESOURCES_PATH, "frame"))
    for side in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'bg']:
        assert side in resources.DialogResources.frame_elements
        assert isinstance(resources.DialogResources.frame_elements[side], pygame.Surface)

    resources.DialogResources.load_font_from_directory(os.path.join(RESOURCES_PATH, "font"))
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,.'":
        assert char in resources.DialogResources.characters
        assert isinstance(resources.DialogResources.characters[char], pygame.Surface)


def test_overworld_loading():
    resources.OverworldResources.load_tileset(os.path.join(RESOURCES_PATH, "tileset.png"), 16)
    assert len(resources.OverworldResources.tileset) == 38 * 41

    for i in range(38):
        for j in range(41):
            WINDOW.blit(resources.OverworldResources.tile(41*i + j), (i*16, j*16))
            pygame.display.flip()
            pygame.time.wait(60)

