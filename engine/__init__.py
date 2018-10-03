from importlib import import_module

application = import_module(".application", __name__)
dialog = import_module(".dialog", __name__)
screen = import_module(".screen", __name__)
resources = import_module(".resources", __name__)
