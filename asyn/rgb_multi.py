# Imports
import time

from machine import Pin
from neopixel import NeoPixel

from pico_utils import rgb_colours as rgb


class RgbMulti:
    def __init__(self, gpio: int, led_count: int) -> None:
        self._gpio = gpio
        self._led_count = led_count
        self._neo = NeoPixel(Pin(self._gpio), self._led_count)

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

    def fade(self, period_ms: int = 1000) -> None:
        """
        Fade the RGB LED through the colour spectrum
        """
        for i in range(255):
            self.set_colour((i, 255 - i, 0))
            time.sleep_ms(period_ms // 255)

        for i in range(255):
            self.set_colour((255 - i, 0, i))
            time.sleep_ms(period_ms // 255)

        for i in range(255):
            self.set_colour((0, i, 255 - i))
            time.sleep_ms(period_ms // 255)
