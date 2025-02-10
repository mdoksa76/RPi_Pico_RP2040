from machine import Pin, Timer
from time import sleep
import time
from neopixel import Neopixel

led = Pin(25, Pin.OUT)
timer = Timer()
pixels = Neopixel(1, 0, 23, "RGB")

def blink(timer):
    led.toggle()

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(p, wait):
    for j in range(256):
        p.set_pixel(0, wheel(j))
        p.show()
        time.sleep(wait)

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

pixels.brightness(50)

try:
    while True:
        rainbow_cycle(pixels, 0.01)
except KeyboardInterrupt:
    print("Script interrupted by user")
    pixels.set_pixel(0, (0, 0, 0))  # Turn off the LED
    pixels.show()
