import asyncio

from asyn.led import Led


class Segmented:
    """
    A class to represent the 5 segment display from Advent Calendar 2023 day 4.

    It uses binary to represent the value of the display. The 5 segments can
    represent 0-31 (00000 to 11111 in binary).

    Background counting is supported.
    """

    def __init__(self, led_segments: list[Led]):
        self._led_segments = led_segments
        # prepare a list of tuples to represent binary 00000 to 11111
        self._bit_mask = []
        for i in range(32):
            digits = tuple(int(d) for d in f"{i:05b}")
            self._bit_mask.append(digits)
        self._start = 0
        self._stop = 31
        self._step = 1
        self._task = None
        # background task state
        self.running = False
        self._task = None
        # period of background task
        self.period_ms = 500
        # current value
        self.value = 0

    def set_value(self, value: int):
        """set the value of the display"""
        self.value = value
        self.display()

    def display(self):
        """display the current value"""
        # get the bit mask for the current value
        mask = self._bit_mask[self.value]
        # set each segment to the appropriate value
        for i in range(5):
            self._led_segments[i].enable(mask[i])

    async def _counter(self, repeats: int):
        count = 0
        self.running = True
        while self.running:
            count += 1
            for i in range(self._start, self._stop + 1, self._step):
                self.set_value(i)
                await asyncio.sleep(self.period_ms * 0.001)
                if not self.running:
                    break
            if count == repeats:
                break
        self.running = False

    async def wait_for_done(self):
        while self.running:
            await asyncio.sleep(0.1)

    def start_count(self, start=0, stop=31, step=1, period_ms=500, repeats=0):
        """
        count in binary from start to stop in steps of step with a period of
        period_ms milliseconds. If repeats is 0 then the count will continue
        forever.
        """
        self._start = start
        self._stop = stop
        self._step = step
        self.period_ms = period_ms
        self._task = asyncio.create_task(self._counter(repeats))

    def stop(self):
        self.running = False

    def __repr__(self):
        """return a string representation of the display"""
        return f"{self.value:05b})"
