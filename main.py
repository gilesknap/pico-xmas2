import asyncio

from hardware.inputs import red_button, slider
from hardware.outputs import big_red_led, rgb_led1, rgb_led2, segmented
from pico_utils.rgb_colours import descend, pink

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
    rgb_led2.colour_fade(10, descend, pink)
    segmented.start_count(period_ms=30)

    red_button(callback=stop)

    while running:
        val = int(slider.value * 250)
        rgb_led1.period_ms = val
        rgb_led2.period_ms = val
        segmented.period_ms = val

        await asyncio.sleep(1)


asyncio.run(main())
