"""
Utilities for fading between colours
"""


def brightness(colour: tuple[int, int, int], factor) -> tuple[int, int, int]:
    """
    Return a new colour tuple with brightness factor applied

    :param colour: tuple of 3 ints 0-255
    :param factor: int 0-255
    """

    # this long winded form instead of list comprehension required to
    # avoid the type checker complaining about the return type
    a, b, c = colour
    return (int(factor / 255 * a), int(factor / 255 * b), int(factor / 255 * c))


# tuples for making ascending and descending ranges for 0-255 with no overlaps
ascend = (0, 255, 10)
descend = (255, 0, -10)
