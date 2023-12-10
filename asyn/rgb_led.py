import asyncio

from machine import Pin
from neopixel import NeoPixel

from pico_utils.rgb_colours import (
    ascend,
    brightness,
    colours,
    descend,
    light_off,
    white,
)


class RgbLed:
    """
    A class to represent an LED attached to a GPIO on the Pico.

    This is the async version of the Led class from utils/led.py
    """

    def __init__(self, pin_num: int):
        # initialize the LED NeoPixel
        self._pin = NeoPixel(Pin(pin_num), 1)
        self._colour = white
        self._on = False
        self.off()

    def set_colour(self, colour: tuple):
        """set the colour of the LED"""
        self._colour = colour
        self.on()

    def on(self):
        """turn on the LED at the current colour"""
        self._pin.fill(self._colour)
        self._pin.write()

    def off(self):
        """turn off the LED"""
        self._pin.fill(light_off)
        self._pin.write()

    def enable(self, value: bool):
        """set the LED on or off based on argument value"""
        if value:
            self.on()
        else:
            self.off()

    def blink(self, period_ms: int, count: int = 0):
        """
        blink the LED at the current colour

        arguments:
        period_ms: the period of the blink in milliseconds
        count: the number of blinks, 0 means blink forever
        """
        self.task = asyncio.create_task(self._blink(period_ms, count))

    async def _blink(self, period_ms: int, count: int):
        counter = 0
        while True:
            counter += 1
            self.on()
            await asyncio.sleep(period_ms * 0.001)
            self.off()
            await asyncio.sleep(period_ms * 0.001)
            if counter == count:
                break

    def colour_fade(
        self, period_ms: int, direction=ascend, colour=white, count: int = 0
    ):
        """
        fade the LED in out through the colours, switching colours at
        the minimum brightness.

        arguments:
        period_ms: the period of the each fade sequence in milliseconds
        count: the number of chases, 0 means chase forever
        direction: the direction of the first fade
        colour: the colour to start at
        """
        self.task = asyncio.create_task(
            self._fader(period_ms, direction, colour, count)
        )

    async def _fader(self, period_ms: int, direction, colour, count: int):
        counter = 0
        colour_num = colours.index(colour)
        self.on()

        while True:
            counter += 1
            for factor in range(*direction):
                colour = brightness(colours[colour_num], factor)
                self.set_colour(colour)
                await asyncio.sleep(period_ms * 0.001 / 255)

            if counter == count:
                break

            # use the direction tuples to flip the direction
            if direction == descend:
                direction = ascend
                colour_num = (colour_num + 1) % len(colours)
            else:
                direction = descend

    def stop(self):
        if self.task:
            self.task.cancel()
        self.task = None

    def __repr__(self):
        """return a string representation of the LED"""
        return f"Led({self._pin}) value:{self._colour}"