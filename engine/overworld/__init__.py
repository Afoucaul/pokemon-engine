from importlib import import_module

objects = import_module(".objects", __name__)

Overworld = import_module(".scene", __name__).Overworld
OverworldObject = objects.OverworldObject
behaviours = import_module(".behaviours", __name__)
scene = import_module(".scene", __name__)
