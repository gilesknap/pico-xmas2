# set up some tuples for Green Red Blue colours
white = 240, 140, 255  # White-ish!
red = 0, 255, 0
green = 255, 0, 0
blue = 0, 0, 255
yellow = 255, 175, 150
orange = 238, 223, 105
pink = 150, 150, 200
purple = 40, 100, 255
ice_blue = 150, 25, 200
unicorn = 175, 150, 255
bogey = 215, 100, 0
light_off = 0, 0, 0

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


def brightness(colour, factor):
    """
    Return a new colour tuple with brightness factor applied
    """
    return tuple(int(factor / 255 * colour[i]) for i in range(3))


# tuples for making ascending and descending ranges for 0-255 with no overlaps
ascend = (0, 255, 10)
descend = (255, 0, -10)
