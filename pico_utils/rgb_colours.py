from typing import List, Tuple

RGB = Tuple[int, int, int]

# set up some tuples for Red Green Blue colours
red: RGB = (255, 0, 0)
orange: RGB = (255, 185, 0)
yellow: RGB = (255, 255, 0)
green: RGB = (0, 255, 0)
cyan: RGB = (0, 255, 255)
blue: RGB = (0, 0, 255)
purple: RGB = (255, 0, 255)

light_off = (0, 0, 0)

# list of all colours
colours: List[RGB] = [
    red,
    orange,
    yellow,
    green,
    cyan,
    blue,
    purple,
]


def next_colour(colour: RGB) -> RGB:
    """
    Return the next colour in the list of colours

    :param colour: tuple of 3 ints 0-255
    """
    return colours[(colours.index(colour) + 1) % len(colours)]
