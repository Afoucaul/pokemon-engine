from importlib import import_module

behaviours = import_module(".behaviours", __name__)
objects = import_module(".objects", __name__)
scene = import_module(".scene", __name__)
tileset = import_module(".tileset", __name__)

Overworld = import_module(".scene", __name__).Overworld
OverworldObject = objects.OverworldObject
Universe = import_module(".universe", __name__).Universe
