import pico_utils.grb_colours as grb
from hardware.outputs import (
    rgb_led1,
    rgb_led2,
    rgb_ring,
    rgb_strand,
    segmented,
)
from pico_utils.faders import descend

description = "Colour Fade"


def go():
    # setup this mode - called once at start up
    print("Starting mode 1 Colour Fade ...")

    # set up the RGB LEDs to fade through the colour spectrum
    # with one LED fading up and the other fading down and with
    # different colours
    rgb_led1.colour_fade()
    rgb_led2.colour_fade(direction=descend, colour=grb.pink)

    # set up the segmented display to count in binary
    segmented.start_count()

    # set up the RGB ring and strand to fade through the colour spectrum
    # in a loop around the ring / strand
    rgb_ring.colour_fade()
    rgb_strand.brightness = 60
    rgb_strand.colour_fade()
