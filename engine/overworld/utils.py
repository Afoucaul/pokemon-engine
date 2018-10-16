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
