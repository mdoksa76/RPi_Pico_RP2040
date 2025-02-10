from machine import Pin, Timer
import time
from neopixel import Neopixel
import urandom

# Configuration
timer = Timer()
pixels = Neopixel(1, 0, 16, "RGB")

def random_color():
    return urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)

def fireflies(p, wait):
    r, g, b = random_color()
    p.set_pixel(0, (r, g, b))
    p.show()
    time.sleep(wait)

pixels.brightness(50)

try:
    while True:
        fireflies(pixels, urandom.uniform(0.1, 1.0))
except KeyboardInterrupt:
    print("Script interrupted by user")
    pixels.set_pixel(0, (0, 0, 0))  # Turn off the LED
    pixels.show()
