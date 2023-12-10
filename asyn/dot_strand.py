# Imports
import time

from machine import Pin
from neopixel import NeoPixel

# LED details
GPIOnumber = 22
LEDcount = 15

# Colour variable
mycolour = 255, 0, 0

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# Turn off all LEDs before program start
strand.fill((0, 0, 0))
strand.write()
time.sleep(1)

while True:
    for i in range(LEDcount):
        strand[i] = mycolour
        strand.write()

        # Show the light for this long
        time.sleep(0.09)

        # Clear the strand at the end of each loop
        strand.fill((0, 0, 0))
        strand.write()

    for i in reversed(range(LEDcount)):
        strand[i] = mycolour
        strand.write()

        # Show the light for this long
        time.sleep(0.09)

        # Clear the strand at the end of each loop
        strand.fill((0, 0, 0))
        strand.write()
