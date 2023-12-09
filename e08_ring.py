# Imports
import random
import time

from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(15), 12)

# Turn off all LEDs before program start
ring.fill((0, 0, 0))
ring.write()
time.sleep(1)

while True:
    # Select a random LED
    random_led = random.randint(0, 11)

    # Create random RGB values
    r = random.randint(0, 50)
    g = random.randint(0, 50)
    b = random.randint(0, 50)

    # Light the random LED in a random colour
    ring[random_led] = (r, g, b)
    ring.write()

    # Show the light for this long
    time.sleep(0.05)

    # Clear the ring at the end of each loop
    ring.fill((0, 0, 0))
    ring.write()
