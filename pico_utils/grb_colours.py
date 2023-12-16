from typing import List, Tuple

GRB = Tuple[int, int, int]

# set up some tuples for Green Red Blue colours
white: GRB = (240, 140, 255)  # White-ish!
red: GRB = (0, 255, 0)
green: GRB = (255, 0, 0)
blue: GRB = (0, 0, 255)
yellow: GRB = (255, 175, 150)
orange: GRB = (238, 223, 105)
pink: GRB = (150, 150, 200)
purple: GRB = (40, 100, 255)
ice_blue: GRB = (150, 25, 200)
unicorn: GRB = (175, 150, 255)
bogey: GRB = (215, 100, 0)

light_off: GRB = (0, 0, 0)

# list of all colours
colours: List[GRB] = [
    white,
    red,
    green,
    blue,
    yellow,
    orange,
    pink,
    purple,
    ice_blue,
    unicorn,
    bogey,
]


def next_colour(colour: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Return the next colour in the list of colours

    :param colour: tuple of 3 ints 0-255
    """
    return colours[(colours.index(colour) + 1) % len(colours)]
