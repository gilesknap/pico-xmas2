import asyncio
from typing import Callable

from machine import PWM, Pin


class Buzzer:
    """
    A class to play tunes on a piezoelectric buzzer.

    Uses asyncio to play a tune without blocking the main thread.
    """

    # Create our library of tone variables
    A = 440
    As = 466
    B = 494
    C = 523
    Cs = 554
    D = 587
    Ds = 622
    E = 659
    F = 698
    Fs = 740
    G = 784
    Gs = 830

    def __init__(self, pin_num: int):
        """setup the buzzer"""
        self.pin_num = pin_num
        self.buzzer = PWM(Pin(pin_num))
        self.running = False
        self._print = print

    def set_print(self, print: Callable):
        self._print = print

    def play_tune(self, tune: list, volume: int = 1000, lyrics=True, repeat: int = 0):
        """setup a Tune object with a list of notes and a volume"""
        self.tune = tune
        self.volume = volume
        self.lyrics = lyrics
        self.task = asyncio.create_task(self.repeat_tune(repeat))

    async def play_tone(self, note: int, length: int, gap: int):
        """play a tone for a given length of time and pause afterwards"""
        self.buzzer.duty_u16(self.volume)
        self.buzzer.freq(note)
        await asyncio.sleep(length)
        self.buzzer.duty_u16(0)
        await asyncio.sleep(gap)

    async def play_tune_once(self):
        """play a tune"""
        for element in self.tune:
            if isinstance(element, str) and self.lyrics:
                self._print(element)
            elif isinstance(element, tuple):
                note, length, gap = element
                await self.play_tone(note, length, gap)
            if not self.running:
                break

        # buzzer off
        self.buzzer.duty_u16(0)

    async def repeat_tune(self, repeat: int):
        """play a tune a given number of times (0 for forever)"""
        count = 0
        self.running = True
        while self.running:
            count += 1
            await self.play_tune_once()
            if count == repeat:
                break
        self.running = False

    def stop(self):
        """stop playing the tune"""
        self.running = False
