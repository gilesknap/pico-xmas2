import asyncio

import machine
from machine import I2C

from lib.pico_i2c_lcd import I2cLcd


class Display:
    """
    A class to define a multi line LCD display

    Will accept print commands to each line and each line will asynchronously
    scroll if the text is longer than the display width.

    :param sda: the SDA pin number
    :param scl: the SCL pin number
    :param bus: the I2C bus number
    :param addr: the I2C address of the display
    :param rows: the number of rows on the display
    :param cols: the number of columns on the display
    """

    def __init__(self, sda: int, scl: int, bus: int, addr: int, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self.lines = ["" for _ in range(rows)]
        self._tasks = [None for _ in range(rows)]

        # Set up LCD I2C
        self._lcd_i2c = I2C(
            bus, sda=machine.Pin(sda), scl=machine.Pin(scl), freq=400000
        )
        self.lcd = I2cLcd(self._lcd_i2c, addr, rows, cols)

    def lcd_print(self, line: str, line_no: int = 0):
        """
        Show a string on one of the LCD's lines - scroll if necessary
        """
        if self._tasks[line_no] is not None:
            self._tasks[line_no].cancel()  # type: ignore

        self.lcd.move_to(0, line_no)
        if len(line) > self._cols:
            self._tasks[line_no] = asyncio.create_task(self._scroll(line, line_no))  # type: ignore
        else:
            self._tasks[line_no] = asyncio.create_task(  # type: ignore
                self.lcd.async_putstr(f"{line:16}", 0, line_no)
            )

    async def _scroll(self, line: str, line_no: int):
        """
        rotating scrolling text for text longer than display columns
        """
        ll = len(line)
        left_col = 0  # which character to start from in column 0
        while True:
            await self.lcd.async_putstr(
                f"{line[left_col:left_col+self._cols]}", 0, line_no
            )
            left_col = (left_col + 1) % ll
