"""
Hardware outputs for the PiHut Advent Calendar 2023

Note the wiring is for giles' modifications so check the
[wiring diagram](README.md) before using this code.
"""

from asyn.led import Led
from asyn.rgb_led import RgbLed
from asyn.segmented import Segmented

# day 1 LED
onboard_led = Led(25)

# day 2 LED
big_red_led = Led(14)

# day 4 segmented display
seg1_led = Led(13)
seg2_led = Led(12)
seg3_led = Led(11)
seg4_led = Led(10)
seg5_led = Led(9)
led_segments = [seg1_led, seg2_led, seg3_led, seg4_led, seg5_led]
segmented = Segmented(led_segments)

# day 5 colour LEDs
rgb_led1 = RgbLed(28)
rgb_led2 = RgbLed(27)

# day 6 RGB LED Ring
