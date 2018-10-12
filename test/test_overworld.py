import os
import pytest

import pygame
from pygame.locals import QUIT

from engine.overworld import Overworld
from engine.world import World
from engine import application
from engine.screen import Screen
from engine.resources import OverworldResources


RESOURCES_PATH = "resources"


@pytest.fixture(scope="session", autouse=True)
def start_pygame():
    application.Application.init(320, 288)


@pytest.mark.skip()
def test_overworld_drawing():
    world = World(height=40, width=40)
    ow = Overworld(world, 20, 20)
    application.Application.push_frame(ow.run())
    application.Application.run()


def test_pallet_town():
    OverworldResources.load_world(os.path.join(RESOURCES_PATH, "worlds", "pallet_town"))
    world = OverworldResources.world
    ow = Overworld(world, 10, 10)
    application.Application.push_frame(ow.run())
    application.Application.run()
