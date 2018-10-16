from importlib import import_module

Overworld = import_module(".scene", __name__).Overworld
OverworldObject = import_module(".objects", __name__).OverworldObject
