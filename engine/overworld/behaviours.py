import random


def random_direction():
    """Pick a random unit vector along one axis"""
    return random.choice(((0, 1), (0, -1), (1, 0), (-1, 0)))


def behaviour_random_walk(instance, frame):
    """Make random steps, at random instants"""
    if frame == 0 and random.randint(0, 10) < 5:
        x, y = random_direction()
        if instance.can_move_to(instance.x + x, instance.y + y):
            instance.translate(x, y)
