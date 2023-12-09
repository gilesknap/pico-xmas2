"""
ASYNC Configuration for interfacing with the Hardware supplied
in the PiHut Advent Calendar 2023
"""
from asyn.button import Button


# day 3 buttons
def red_button(callback=None):
    return Button(pin_num=0, name="Red", handler=callback)


def green_button(callback=None):
    return Button(pin_num=1, name="Green", handler=callback)
