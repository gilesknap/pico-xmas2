import pico_utils.grb_colours as grb
from hardware.outputs import (
    rgb_led1,
    rgb_led2,
    rgb_ring,
    rgb_strand,
    segmented,
)
from pico_utils.faders import descend


def go():
    # setup this mode - called once at start up
    print("Starting mode 1 Colour Cycle ...")

    # set up the RGB LEDs to fade through the colour spectrum
    rgb_led1.colour_fade(10)
    rgb_led2.colour_fade(10, descend, grb.pink)
    # set up the segmented display to count in binary
    segmented.start_count(period_ms=30)

    rgb_ring.colours()
    rgb_strand.colours()


def tick():
    # execute one step of this mode
    pass
    # most modes require no code here because the background tasks
    # take care of everything
