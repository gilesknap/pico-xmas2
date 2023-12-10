import asyncio

from machine import PWM, Pin


class Led:
    """
    A class to represent an LED attached to a GPIO on the Pico.

    This is the async version of the Led class from utils/led.py
    """

    def __init__(self, pin_num: int):
        # initialize the LED to off and full brightness
        self._task = None
        self._pin = Pin(pin_num, Pin.OUT)
        self._pwm = PWM(self._pin)
        self._pwm.freq(1000)
        # full brightness
        self._power = 65535
        # turn the LED off
        self._pwm.duty_u16(0)
        # background task state
        self.running = False
        self._task = None
        # period of background task
        self.period_ms = 500

    def on(self):
        """turn on the LED at the current brightness"""
        self._pwm.duty_u16(self._power)

    def off(self):
        """turn off the LED"""
        self._pwm.duty_u16(0)

    def enable(self, value: bool):
        """set the LED on or off based on argument value"""
        if value:
            self.on()
        else:
            self.off()

    def brightness(self, value=65535):
        """set the brightness of the LED"""
        self._power = value
        # if the LED is already on then change the brightness
        if self._pwm.duty_u16() > 0:
            self.on()

    def blink(self, period_ms: int):
        self._task = asyncio.create_task(self._blink(period_ms))

    async def _blink(self, period_ms: int):
        self.running = True
        self.period_ms = period_ms
        while self.running:
            self.on()
            await asyncio.sleep(self.period_ms * 0.001)

            if not self.running:
                break

            self.off()
            await asyncio.sleep(self.period_ms * 0.001)

    def stop(self):
        """stop the current task"""
        self.running = False

    def __repr__(self):
        """return a string representation of the LED"""
        return f"Led({self._pin}) brightness:{self._pwm.duty_u16()}"
