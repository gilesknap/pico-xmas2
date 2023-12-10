import asyncio

import pico_utils.grb_colours as grb
import pico_utils.rgb_colours as rgb
from hardware.inputs import dips, environment, red_button, slider
from hardware.outputs import (
    big_red_led,
    rgb_led1,
    rgb_led2,
    rgb_ring,
    rgb_strand,
    segmented,
)
from pico_utils.faders import brightness, descend

running = True


def stop(_):
    global running
    running = False
    rgb_led1.stop()
    rgb_led2.stop()
    segmented.stop()


async def main():
    # use the global running variable to terminate the program
    global running

    # set the red button to stop the program
    red_button(callback=stop)

    # set up a heartbeat to show the code is running
    big_red_led.blink(500)
    # starting colour for the RBG LEDs
    colour = rgb.red
    # set up the RGB LEDs to fade through the colour spectrum
    rgb_led1.colour_fade(10)
    rgb_led2.colour_fade(10, descend, grb.pink)
    # set up the segmented display to count in binary
    segmented.start_count(period_ms=30)

    # validate some inputs
    environment.measurements()
    print("Dip switch value:", dips.value)

    while running:
        val = int(slider.value * 250)
        rgb_led1.period_ms = val
        rgb_led2.period_ms = val
        segmented.period_ms = val

        # use 1/10th brightness to avoid outshining the GRB LEDs
        pixel_val = brightness(colour, 25)
        rgb_strand.set_colour(pixel_val)
        rgb_ring.set_colour(pixel_val)

        colour = rgb.next_colour(colour)

        await asyncio.sleep(val / 255)


asyncio.run(main())
