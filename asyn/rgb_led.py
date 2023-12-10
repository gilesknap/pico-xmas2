import asyncio

from machine import Pin
from neopixel import NeoPixel

import pico_utils.grb_colours as grb
from pico_utils.faders import ascend, brightness, descend


class RgbLed:
    """
    A class to represent a NeoPixel LED attached to a GPIO on the Pico.

    This is the async version lets us blink or fade the LED without
    blocking the main thread.
    """

    def __init__(self, pin_num: int):
        # initialize the LED NeoPixel
        self._pin = NeoPixel(Pin(pin_num), 1)
        self._colour = grb.white
        self._on = False
        self.off()
        # background task state
        self.running = False
        self._task = None
        # period of background task
        self.period_ms = 500

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
        self._pin.fill(grb.light_off)
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
        self._task = asyncio.create_task(self._blink(period_ms, count))

    async def _blink(self, period_ms: int, count: int):
        counter = 0
        self.running = True
        self.period_ms = period_ms
        while self.running:
            counter += 1
            self.on()
            await asyncio.sleep(self.period_ms * 0.001)
            self.off()
            await asyncio.sleep(self.period_ms * 0.001)
            if counter == count:
                break
        self.running = False
        self._task = None

    def colour_fade(
        self, period_ms: int, direction=ascend, colour=grb.white, count: int = 0
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
        self.running = True
        self._task = asyncio.create_task(
            self._fader(period_ms, direction, colour, count)
        )

    async def _fader(self, period_ms: int, direction, colour, count: int):
        self.period_ms = period_ms
        counter = 0
        colour_num = grb.colours.index(colour)
        self.on()

        while self.running:
            counter += 1
            for factor in range(*direction):
                colour = brightness(grb.colours[colour_num], factor)
                self.set_colour(colour)
                # the ascent and decent are in steps of 10 in range 255
                # so we div by 25 to get approx period_ms per cycle
                await asyncio.sleep(self.period_ms * 0.001 / 25)

            if counter == count:
                break

            # use the direction tuples to flip the direction
            if direction == descend:
                direction = ascend
                colour_num = (colour_num + 1) % len(grb.colours)
            else:
                direction = descend
        self._task = None

    def stop(self):
        """stop the current task"""
        self.running = False

    def __repr__(self):
        """return a string representation of the LED"""
        return f"Led({self._pin}) value:{self._colour}"
