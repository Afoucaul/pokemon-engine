import itertools


DIRECTIONS = {
    'up':       (0, -1),
    'down':     (0, 1),
    'left':     (-1, 0),
    'right':    (1, 0)
}


def vector_to_direction(x, y):
    for direction, (i, j) in DIRECTIONS.items():
        if (i, j) == (x, y):
            return direction


def translation(x, y, x_pixels_per_frame=1, y_pixels_per_frame=0, after=None):
    if not y_pixels_per_frame:
        y_pixels_per_frame = x_pixels_per_frame

    x_unit = 1 if not x else x_pixels_per_frame * x // abs(x)
    y_unit = 1 if not y else y_pixels_per_frame * y // abs(y)

    yield from itertools.zip_longest(
            (x_unit for _ in range(abs(x))),
            (y_unit for _ in range(abs(y))),
            fillvalue=0)
    if after:
        after()


def world_to_screen(overworld, x, y):
    return (
        x - overworld.x + overworld.screen.columns // 2 - 1,
        y - overworld.y + overworld.screen.rows // 2 - 1
    )
