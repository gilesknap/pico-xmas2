import pico_utils.grb_colours as grb
from hardware.outputs import (
    rgb_led1,
    rgb_led2,
    rgb_ring,
    rgb_strand,
    segmented,
)

description = "Flash"


def go():
    # set up the RGB LEDs to fade through the colour spectrum
    rgb_led1.colours()
    rgb_led2.colours(colour=grb.pink)
    # set up the segmented display to count in binary
    segmented.start_count(period_ms=30)

    rgb_ring.colours()
    rgb_strand.colours()
