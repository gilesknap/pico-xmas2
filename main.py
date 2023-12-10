import asyncio

import pico_utils.faders as faders
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

running = True


def stop(_):
    global running
    running = False
    rgb_led1.stop()
    rgb_led2.stop()
    segmented.stop()


async def main():
    global running
    big_red_led.blink(500)
    rgb_led1.colour_fade(10)
    rgb_led2.colour_fade(10, faders.descend, grb.pink)
    segmented.start_count(period_ms=30)
    for colour in rgb.colours:
        rgb_strand.set_colour(colour)
        rgb_ring.set_colour(colour)
        await asyncio.sleep(0.5)
    rgb_strand.off()
    rgb_ring.off()

    red_button(callback=stop)

    environment.measurements()
    print("Dip switch value:", dips.value)

    while running:
        val = int(slider.value * 250)
        rgb_led1.period_ms = val
        rgb_led2.period_ms = val
        segmented.period_ms = val

        await asyncio.sleep(1)


asyncio.run(main())
