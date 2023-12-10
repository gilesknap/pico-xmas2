"""
Hardware inputs for the PiHut Advent Calendar 2023

Note the wiring is for giles' modifications so check the
[wiring diagram](README.md) before using this code.
"""

from asyn.button import Button
from asyn.dipswitch import DipSwitch
from asyn.slider import Slider
from asyn.temp_mon import TempMon


# day 3 buttons
def red_button(callback=None):
    return Button(pin_num=0, name="Red", handler=callback)


def green_button(callback=None):
    return Button(pin_num=1, name="Green", handler=callback)


# day 5 dip switches
dips = DipSwitch([2, 3, 4, 5, 6])

# day 7 slider
slider = Slider(pin_num=26, name="Slider")

# day 9 Temperature and Humidity sensor
environment = TempMon(18, 19)
