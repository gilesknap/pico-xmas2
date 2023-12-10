# set up some tuples for Red Green Blue colours
red = (255, 0, 0)
orange = (255, 185, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)

light_off = (0, 0, 0)

# list of all colours
colours = [
    red,
    orange,
    yellow,
    green,
    cyan,
    blue,
    purple,
]


def next_colour(colour: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Return the next colour in the list of colours

    :param colour: tuple of 3 ints 0-255
    """
    return colours[(colours.index(colour) + 1) % len(colours)]
