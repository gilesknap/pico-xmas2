# set up some tuples for Green Red Blue colours
white = (240, 140, 255)  # White-ish!
red = (0, 255, 0)
green = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 175, 150)
orange = (238, 223, 105)
pink = (150, 150, 200)
purple = (40, 100, 255)
ice_blue = (150, 25, 200)
unicorn = (175, 150, 255)
bogey = (215, 100, 0)

light_off = (0, 0, 0)

# list of all colours
colours = [
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
