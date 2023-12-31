import asyncio

from machine import Pin
from neopixel import NeoPixel

from pico_utils import faders as fade
from pico_utils import rgb_colours as rgb
from pico_utils.rgb_colours import RGB


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
        self._colour = rgb.red
        # background task state
        self._running = False
        self._task = None

        #### public members to set directly ####################################
        # period of background task
        self.period_ms = 200
        self.brightness: int = 20

    def set_colour(self, colour: tuple[int, int, int]) -> None:
        """
        Set the colour of the RGB LED
        """
        self._colour = colour
        self._neo.fill(colour)
        self._neo.write()

    def off(self) -> None:
        """
        Turn off the RGB LED
        """
        self.set_colour(rgb.light_off)

    def colours(
        self,
        count: int = 0,
        colour: RGB = rgb.red,
    ) -> None:
        """
        Rotate through all RGB colours
        """
        self._running = True
        self._task = asyncio.create_task(self._colours(colour, count))

    async def _colours(self, colour: RGB, count: int) -> None:
        counter = 0
        self._running = True

        while self._running:
            counter += 1
            self.set_colour(fade.brightness(colour, self.brightness))
            if counter == count:
                break
            await asyncio.sleep(self.period_ms * 0.001)
            colour = rgb.next_colour(colour)

        self._running = False
        self._task = None

    def colour_fade(self, colour: RGB = rgb.red):
        """
        fade the LED through all colours, rotating through the pixels
        and gradually changing colour, leaving a trail of colour behind
        with each successive pixel slightly dimmer

        :param period_ms: the period of a single rotation in milliseconds
        :param colour: the starting colour
        """
        self.off()
        self._running = True
        self._colour = colour
        self._task = asyncio.create_task(self._colour_fade())

    def _render_fade(self, pixels: list[RGB], start) -> None:
        # dim all the pixels by 25% and then render them into the
        # NeoPixel list starting at the start index and wrapping around
        for i, pixel in enumerate(pixels):
            pixels[i] = fade.brightness(pixels[i], 0.75 * 255)
        for i in range(self._led_count):
            self._neo[i] = pixels[(i + start) % self._led_count]
        self._neo.write()

    async def _colour_fade(self):
        pixel = 0
        colour = self._colour
        pixels: list[RGB] = [rgb.light_off] * self._led_count

        while self._running:
            next_colour = rgb.next_colour(colour)
            diff = fade.colour_diff(next_colour, colour)
            # fade between colours in steps of 10
            for i in range(10):
                # remove last pixel from the end and add a new one at the start
                pixels.pop(self._led_count - 1)
                this_pixel_colour = fade.colour_add(colour, diff, (i + 1) / 10)
                pixels.insert(0, fade.brightness(this_pixel_colour, self.brightness))
                self._render_fade(pixels, pixel)
                pixel = (pixel + 1) % self._led_count
                # 1 period is one time around the loop of all pixels
                await asyncio.sleep(self.period_ms * 0.001)
                if not self._running:
                    break
            colour = next_colour

    def stop(self):
        """stop the current task"""
        self._running = False
