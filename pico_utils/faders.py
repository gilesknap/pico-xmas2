"""
Utilities for fading between colours
"""


def brightness(colour, factor):
    """
    Return a new colour tuple with brightness factor applied
    """
    return tuple(int(factor / 255 * colour[i]) for i in range(3))


# tuples for making ascending and descending ranges for 0-255 with no overlaps
ascend = (0, 255, 10)
descend = (255, 0, -10)
