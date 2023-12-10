Asyn Classes
============

Each module in this sub-package implements a class with code for
one of the input or output device types supplied with the
2023 Advent Calendar.

Note that the LED ring and RGB dot strand are both arrays of addressable
RGB LEDs. Thus they are both handled by the class RgbMulti.

All of these classes use asyncio to implement some background functionality.
This is why we are able to blink all of the LEDs at the same time while
still responding to button presses and slider changes.
