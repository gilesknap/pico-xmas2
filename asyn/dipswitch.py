from machine import Pin


class DipSwitch:
    """
    A class to represent a dip switch attached to a set of pins on the Pico.

    An arbitrary number of pins can be used, but they should be in order from
    least significant to most significant.

    Readouts from this class are then in the form of an integer representing
    the binary value of the switches.

    Asynchronous monitoring of changes of state are supported. (TODO)
    """

    def __init__(self, pin_nums: list[int]):
        self._pin_nums = pin_nums
        self._dips = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in pin_nums]

    @property
    def value(self) -> int:
        """
        Return the integer represented by the binary value of the dip switches
        """
        value = 0
        for i, pin in enumerate(self._dips):
            if pin.value():
                value += 2**i
        return value
