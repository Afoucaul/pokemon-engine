import os
import pytest

import pygame
from pygame.locals import QUIT

from engine.overworld import Overworld, OverworldObject
from engine.overworld.behaviours import behaviour_random_walk
from engine.overworld import Universe
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


@pytest.mark.skip()
def test_pallet_town():
    universe = Universe([[os.path.join(RESOURCES_PATH, "worlds", "pallet_town.world")]], 0, 0)

    ow = Overworld(universe, 10, 10)
    application.Application.push_frame(ow.run())
    application.Application.run()


def test_pallet_town_and_neighbourhood():
    universe = Universe([
        [os.path.join(RESOURCES_PATH, "worlds", "viridian_city.world")],
        [os.path.join(RESOURCES_PATH, "worlds", "route1.world")],
        [os.path.join(RESOURCES_PATH, "worlds", "pallet_town.world")],
        [os.path.join(RESOURCES_PATH, "worlds", "route21.world")]
    ], 0, 0)

    ow = Overworld(universe, 20, 20)
    application.Application.push_frame(ow.run())
    application.Application.run()
