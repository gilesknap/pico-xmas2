import asyncio

from machine import Pin
from neopixel import NeoPixel

from pico_utils import faders as fade
from pico_utils import rgb_colours as rgb


class RgbMulti:
    """
    A class to represent a multiple LED NeoPixel attached to a GPIO on the Pico.

    This is an async version lets us blink or fade the LEDs without
    blocking the main thread.
    """

    def __init__(self, gpio: int, led_count: int) -> None:
        self._gpio = gpio
        self._led_count = led_count
        self._neo = NeoPixel(Pin(self._gpio), self._led_count)
        # background task state
        self.running = False
        self._task = None
        # period of background task
        self.period_ms = 500

    def set_colour(self, colour: tuple[int, int, int]) -> None:
        """
        Set the colour of the RGB LED
        """
        self._neo.fill(colour)
        self._neo.write()

    def off(self) -> None:
        """
        Turn off the RGB LED
        """
        self.set_colour(rgb.light_off)

    def colours(
        self,
        period_ms: int = 1000,
        count: int = 0,
        colour: tuple[int, int, int] = rgb.red,
        brightness: int = 20,  # 10% brightness is a good default!
    ) -> None:
        """
        Rotate through all RGB colours
        """
        self.running = True
        self._task = asyncio.create_task(
            self._colours(period_ms, colour, count, brightness)
        )
        self.set_colour(colour)

    async def _colours(
        self, period_ms: int, colour: tuple[int, int, int], count: int, brightness: int
    ) -> None:
        counter = 0
        self.running = True
        self.period_ms = period_ms

        while self.running:
            counter += 1
            self.set_colour(fade.brightness(colour, brightness))
            if counter == count:
                break
            await asyncio.sleep(self.period_ms * 0.001)
            colour = rgb.next_colour(colour)

        self.running = False
        self._task = None

    def stop(self):
        """stop the current task"""
        self.running = False
