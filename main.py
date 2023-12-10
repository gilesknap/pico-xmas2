import asyncio

from hardware.inputs import slider
from hardware.outputs import big_red_led, rgb_led1, rgb_led2
from pico_utils.rgb_colours import descend, pink


async def main():
    big_red_led.blink(500)
    rgb_led1.colour_fade(10)
    rgb_led2.colour_fade(10, descend, pink)

    while True:
        await asyncio.sleep(1)


asyncio.run(main())
