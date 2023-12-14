import asyncio
import re
import time

from machine import Pin

from typings.stdlib.typing import Callable, Optional

pin_regex = re.compile(r"GPIO(\d+)")


class Button:
    """
    A class to represent a button attached to a GPIO on the Pico.

    This is an async implementation that allows us to monitor multiple
    buttons at the same time.
    """

    def __init__(
        self,
        pin_num: int,
        name: str,
        handler: Optional[Callable] = None,
        debounce_ms: int = 30,
    ):
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)
        self.num = pin_num
        self.irq = self.pin.irq(
            handler=self._callback, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING
        )

        self.debounce_ms = debounce_ms
        self.last_state_change = time.ticks_ms()

        self.pressed = 0  # 0 = released, 1 = pressed
        self.handler = handler or self.print_state  # default handler prints state
        self.name = name

    def _callback(self, _):
        """
        The callback function that is called when the button is pressed.
        """
        value = self.pin.value()

        # only interested in transitions of button state
        if value != self.pressed:
            # debounce the button
            now = time.ticks_ms()
            diff = now - self.last_state_change
            if diff > self.debounce_ms:
                self.last_state_change = now
                self.pressed = value
                self.handler(self)

    async def wait_for_press(self):
        """
        async monitoring of button state
        """
        while not self.pressed:
            await asyncio.sleep(0.05)

    async def wait_for_release(self):
        """
        async monitoring of button state
        """
        while self.pressed:
            await asyncio.sleep(0.05)

    @staticmethod
    def print_state(button):
        """print the state of the button"""
        print(button)

    def __repr__(self):
        """return a string representation of the button"""
        return f"{self.name} " + f"{'pressed' if self.pressed else 'released'}"
