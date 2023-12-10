"""
Utilities for fading between colours
"""


def brightness(colour: tuple[int, int, int], factor) -> tuple[int, int, int]:
    """
    Return a new colour tuple with brightness factor applied

    :param colour: tuple of 3 ints 0-255
    :param factor: int 0-255
    """
    return tuple([int(c * factor / 255) for c in colour])  # type: ignore


def colour_diff(
    colour1: tuple[int, int, int], colour2: tuple[int, int, int]
) -> tuple[int, int, int]:
    """
    Return the difference between two colours

    :param colour1: tuple of 3 ints 0-255
    :param colour2: tuple of 3 ints 0-255
    """
    return tuple([c1 - c2 for c1, c2 in zip(colour1, colour2)])  # type: ignore


def colour_add(
    colour1: tuple[int, int, int], colour2: tuple[int, int, int], factor: float = 1.0
) -> tuple[int, int, int]:
    """
    Return the sum of two colours

    :param colour1: tuple of 3 ints 0-255
    :param colour2: tuple of 3 ints 0-255
    """
    return tuple([c1 + int(c2 * factor) for c1, c2 in zip(colour1, colour2)])  # type: ignore


# tuples for making ascending and descending ranges for 0-255 with no overlaps
ascend = (0, 255, 10)
descend = (255, 0, -10)
