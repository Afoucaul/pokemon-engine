from importlib import import_module

dialog = import_module(".dialog", __name__)
screen = import_module(".screen", __name__)
resources = import_module(".resources", __name__)
