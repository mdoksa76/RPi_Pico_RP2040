from machine import Pin
import time

# Initialize pins
red_led = Pin(12, Pin.OUT)
yellow_led = Pin(11, Pin.OUT)
green_led = Pin(10, Pin.OUT)

try:
    while True:
        # RED
        red_led.value(1)
        yellow_led.value(0)
        green_led.value(0)
        time.sleep(5)
        
        # RED + YELLOW
        red_led.value(1)
        yellow_led.value(1)
        green_led.value(0)
        time.sleep(1)
        
        # GREEN
        red_led.value(0)
        yellow_led.value(0)
        green_led.value(1)
        time.sleep(5)
        
        # YELLOW
        red_led.value(0)
        yellow_led.value(1)
        green_led.value(0)
        time.sleep(1)

except KeyboardInterrupt:
    red_led.value(0)
    yellow_led.value(0)
    green_led.value(0)
    print("Script interrupted by user")
