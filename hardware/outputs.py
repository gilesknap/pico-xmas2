"""
Hardware outputs for the PiHut Advent Calendar 2023

Note the wiring is for giles' modifications so check the
[wiring diagram](README.md) before using this code.
"""

from asyn.buzzer import Buzzer
from asyn.display import Display
from asyn.grb_led import RgbLed
from asyn.led import Led
from asyn.rgb_multi import RgbMulti
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

rgb_strand = RgbMulti(22, 15)

# day 10 RGB Dot Strand
rgb_ring = RgbMulti(15, 12)

# Extra item from the 2022 calendar
buzzer = Buzzer(7)

# Display from day #12
display = Display(16, 17, 0, 0x27, 2, 16)
