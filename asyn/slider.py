import asyncio
from typing import Callable

from machine import ADC, Pin


class Slider:
    """
    A class to represent a sliding pot attached to an ADC on the Pico.

    Some async methods are provided to monitor the slider state without
    blocking the main thread.
    """

    def __init__(self, pin_num: int, name: str):
        self.adc = ADC(Pin(26))
        self.num = pin_num

        self.pressed = 0
        self.name = name

    @property
    def value(self):
        """return the current value of the slider"""
        value = self.adc.read_u16() / 65535
        if value < 0.02:
            # get around MicroPython issue with rounding
            return 0
        return round(value, 2)

    async def less_than(self, value: int, hook: Callable):
        """
        async monitoring value until it is less than the argument value
        """
        while not self.value < value:
            await asyncio.sleep(0.05)
        hook(self)

    async def greater_than_hook(self, value: int, hook):
        """
        async monitoring of button state
        """
        while not self.value > value:
            await asyncio.sleep(0.05)
        hook(self)

    @staticmethod
    def print_state(slider: "Slider"):
        """print the state of the slider"""
        print(slider)

    def __repr__(self):
        """return a string representation of the slider"""
        return f"slider:{self.name}, value:{self.value}"
