from machine import Pin, I2C
import ssd1306
import utime
import random
import math

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Bitmap slika loga Raspberry Pi (jednostavna crno-bijela slika)
raspberry_pi_logo = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def loading_animation():
    oled.fill(0)
    loading_text = "LOADING"
    for i in range(len(loading_text)):
        oled.text(loading_text[:i+1], 32, 50)
        oled.fill_rect(i * 16, 20, 8, 10, 1)  # Popunjava dva kvadrata odjednom
        oled.show()
        utime.sleep(0.5)
    
    # Dodavanje završnog kvadrata
    oled.fill_rect(len(loading_text) * 16, 20, 8, 10, 1)
    oled.show()
    utime.sleep(0.5)
    
    # Blinkanje teksta "LOADING"
    for _ in range(3):
        oled.fill_rect(32, 50, 64, 10, 0)  # Brisanje teksta
        oled.show()
        utime.sleep(0.3)
        oled.text(loading_text, 32, 50)  # Ponovno ispisivanje teksta
        oled.show()
        utime.sleep(0.3)
        
def loading_dots_animation(oled, duration=4, speed=0.05):
    oled.fill(0)
    center_x = oled_width // 2
    center_y = oled_height // 2 + 8
    radius = 15
    num_dots = 12
    angle_step = 2 * math.pi / num_dots
    start_time = utime.time()

    while utime.time() - start_time < duration:
        oled.fill(0)
        for i in range(num_dots - 4):  # Exclude some dots
            angle = i * angle_step + (utime.time() - start_time) * 2 * math.pi / duration
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            oled.pixel(x, y, 1)
        oled.show()
        utime.sleep(speed)

def display_logo():
    oled.fill(0)
    # Prikazivanje loga
    for y in range(len(raspberry_pi_logo)):
        for x in range(len(raspberry_pi_logo[y])):
            if raspberry_pi_logo[y][x] == 1:
                oled.pixel(x + 32, y, 1)
    oled.show()
    utime.sleep(2)

    # Inverting the logo
    for y in range(len(raspberry_pi_logo)):
        for x in range(len(raspberry_pi_logo[y])):
            if raspberry_pi_logo[y][x] == 1:
                oled.pixel(x + 32, y, 0)
            else:
                oled.pixel(x + 32, y, 1)
    oled.show()
    utime.sleep(5)
    
def animate_flip(oled, pixel_matrix):
    #import utime

    def display_image(pixel_matrix):
        oled.fill(0)
        for y in range(len(pixel_matrix)):
            for x in range(len(pixel_matrix[y])):
                if pixel_matrix[y][x] == 1:
                    oled.pixel(x + 32, y, 1)
        oled.show()

    def horizontal_flip(pixel_matrix):
        flipped_matrix = []
        for row in pixel_matrix:
            flipped_row = row[::-1]  # Reverse the order of pixels in the row
            flipped_matrix.append(flipped_row)
        return flipped_matrix

    for _ in range(5):  # Perform 5 flips
        pixel_matrix = horizontal_flip(pixel_matrix)
        display_image(pixel_matrix)
        utime.sleep(1)  # Adjust the delay as needed

def atom_animation(oled, num_iterations=100):
    import utime
    import math

    center_x = 64
    center_y = 32
    radius = 20
    angle_step = 10

    def draw_circle(oled, x0, y0, r):
        x = r
        y = 0
        err = 0

        while x >= y:
            oled.pixel(x0 + x, y0 + y, 1)
            oled.pixel(x0 + y, y0 + x, 1)
            oled.pixel(x0 - y, y0 + x, 1)
            oled.pixel(x0 - x, y0 + y, 1)
            oled.pixel(x0 - x, y0 - y, 1)
            oled.pixel(x0 - y, y0 - x, 1)
            oled.pixel(x0 + y, y0 - x, 1)
            oled.pixel(x0 + x, y0 - y, 1)
            y += 1
            if err <= 0:
                err += 2 * y + 1
            if err > 0:
                x -= 1
                err -= 2 * x + 1

    for _ in range(num_iterations):
        oled.fill(0)
        
        # Draw the nucleus
        draw_circle(oled, center_x, center_y, 2)  # Small circle with radius 2
        
        # Draw the electrons
        for i in range(4):
            angle = (i * 90 + angle_step) % 360
            rad = math.radians(angle)
            x = int(center_x + radius * math.cos(rad))
            y = int(center_y + radius * math.sin(rad))
            oled.pixel(x, y, 1)
        
        oled.show()
        angle_step += 10
        utime.sleep(0.1)

def draw_random_squares():
    oled.fill(0)
    for _ in range(10):  # Number of squares to draw
        x = random.randint(0, oled_width - 10)
        y = random.randint(0, oled_height - 10)
        size = random.randint(5, 10)
        oled.rect(x, y, size, size, 1)
    oled.show()
    
def play_random_squares():
    for i in range(100):
        draw_random_squares()
        
def draw_circle(oled, x0, y0, radius):
    x = radius
    y = 0
    err = 0

    while x >= y:
        oled.pixel(x0 + x, y0 + y, 1)
        oled.pixel(x0 + y, y0 + x, 1)
        oled.pixel(x0 - y, y0 + x, 1)
        oled.pixel(x0 - x, y0 + y, 1)
        oled.pixel(x0 - x, y0 - y, 1)
        oled.pixel(x0 - y, y0 - x, 1)
        oled.pixel(x0 + y, y0 - x, 1)
        oled.pixel(x0 + x, y0 - y, 1)
        y += 1
        if err <= 0:
            err += 2 * y + 1
        if err > 0:
            x -= 1
            err -= 2 * x + 1

def draw_random_circles(oled):
    oled.fill(0)
    for _ in range(5):  # Number of circles to draw
        x = random.randint(10, oled_width - 10)
        y = random.randint(10, oled_height - 10)
        radius = random.randint(3, 10)
        draw_circle(oled, x, y, radius)
    oled.show()

def play_random_circles():
    for i in range(100):
        draw_random_circles(oled)

def draw_random_shapes(oled):
    oled.fill(0)
    for _ in range(15):  # Number of shapes to draw
        shape_type = random.choice(['circle', 'rectangle'])
        x = random.randint(10, oled_width - 10)
        y = random.randint(10, oled_height - 10)
        size = random.randint(3, 10)
        
        if shape_type == 'circle':
            draw_circle(oled, x, y, size)
        else:
            width = random.randint(5, 15)
            height = random.randint(5, 15)
            oled.rect(x, y, width, height, 1)
    oled.show()

def play_random_shapes():
    for i in range(100):
        draw_random_shapes(oled)

def draw_random_diagonal_lines(oled, x0, y0):
    for _ in range(10): # Number of lines to draw
        x_end = random.choice([0, oled_width])
        y_end = random.choice([0, oled_height])
        oled.line(x0, y0, x_end, y_end, 1)

def lines_animation(oled, duration=8, speed=0.05):
    oled.fill(0)
    start_time = utime.time()
    max_lines = 20

    while utime.time() - start_time < duration:
        oled.fill(0)
        for _ in range(max_lines):
            x_start = random.randint(0, oled_width)
            y_start = random.randint(0, oled_height)
            length = random.randint(10, 30)
            direction = random.choice([-1, 1])
            if random.choice([True, False]):
                x_end = x_start + length * direction
                y_end = y_start + length * direction
            else:
                x_end = x_start - length * direction
                y_end = y_start + length * direction
            oled.line(x_start, y_start, x_end, y_end, 1)
        oled.show()
        utime.sleep(speed)
        
def rain_animation(oled, num_iterations=100):
    import utime
    import random

    raindrops = [[random.randint(0, 127), random.randint(0, 63)] for _ in range(20)]

    for _ in range(num_iterations):
        oled.fill(0)
        for drop in raindrops:
            drop[1] += 1
            if drop[1] > 63:
                drop[1] = 0
                drop[0] = random.randint(0, 127)
            oled.pixel(drop[0], drop[1], 1)
        oled.show()
        utime.sleep(0.05)
        
def snowflakes_animation(oled, num_iterations=100):
    import utime
    import random

    snowflakes = [[random.randint(0, 127), random.randint(0, 63)] for _ in range(20)]

    for _ in range(num_iterations):
        oled.fill(0)
        for flake in snowflakes:
            flake[1] += random.randint(0, 1)
            flake[0] += random.choice([-1, 0, 1])
            if flake[1] > 63:
                flake[1] = 0
                flake[0] = random.randint(0, 127)
            if flake[0] < 0:
                flake[0] = 127
            elif flake[0] > 127:
                flake[0] = 0
            oled.pixel(flake[0], flake[1], 1)
        oled.show()
        utime.sleep(0.1)

def draw_matrix_char(oled, x, y, char):
    oled.text(char, x, y, 1)

def matrix_animation(oled):
    oled.fill(0)
    width = oled_width // 8
    height = oled_height // 8
    columns = [0] * width
    start_time = utime.time()

    while utime.time() - start_time < 10:  # Run for 10 seconds
        oled.fill(0)
        for i in range(width):
            if random.randint(0, 1):
                columns[i] = (columns[i] + 1) % height
            draw_matrix_char(oled, i * 8, columns[i] * 8, chr(random.randint(33, 126)))
        oled.show()
        utime.sleep(0.1)
        
def rotating_cube_animation(oled):
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]

    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    def rotate(vertices, angle_x, angle_y, angle_z):
        cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
        cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
        cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)

        rotated_vertices = []
        for x, y, z in vertices:
            # Rotate around X axis
            y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x
            # Rotate around Y axis
            x, z = x * cos_y - z * sin_y, x * sin_y + z * cos_y
            # Rotate around Z axis
            x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z
            rotated_vertices.append([x, y, z])
        return rotated_vertices

    def project(vertices, width, height, scale):
        projected_vertices = []
        for x, y, z in vertices:
            f = scale / (z + 3)
            x, y = x * f + width // 2, -y * f + height // 2
            projected_vertices.append([int(x), int(y)])
        return projected_vertices

    def draw_cube(oled, vertices, edges):
        for edge in edges:
            x1, y1 = vertices[edge[0]]
            x2, y2 = vertices[edge[1]]
            oled.line(x1, y1, x2, y2, 1)

    width, height = 60, 60  # Box size
    scale = 30  # Scale factor to fit within 30x30 area
    angle_x, angle_y, angle_z = 0, 0, 0

    for _ in range(100):  # Number of frames
        oled.fill(0)
        rotated_vertices = rotate(vertices, angle_x, angle_y, angle_z)
        projected_vertices = project(rotated_vertices, width, height, scale)
        
        # Center the cube in the middle of the screen
        for i in range(len(projected_vertices)):
            projected_vertices[i][0] += (oled_width - width) // 2
            projected_vertices[i][1] += (oled_height - height) // 2

        draw_cube(oled, projected_vertices, edges)
        oled.show()

        angle_x += 0.05
        angle_y += 0.05
        angle_z += 0.05

        utime.sleep(0.1)
        
def chaotic_lines_animation(oled, duration=8, speed=0.05):
    oled.fill(0)
    start_time = utime.time()
    max_lines = 20
    center_offset = 10  # Offset from the center

    while utime.time() - start_time < duration:
        oled.fill(0)
        for _ in range(max_lines):
            x_start = oled_width // 2 + random.randint(-center_offset, center_offset)
            y_start = oled_height // 2 + random.randint(-center_offset, center_offset)
            length = random.randint(10, 30)
            angle = random.uniform(0, 2 * math.pi)
            x_end = int(x_start + length * math.cos(angle))
            y_end = int(y_start + length * math.sin(angle))
            oled.line(x_start, y_start, x_end, y_end, 1)
        oled.show()
        utime.sleep(speed)

def earth_moon_simulation(oled):
    import utime
    import math

    # Simulation parameters
    G = 6.67430e-11  # Gravitational constant
    earth_mass = 5.972e24  # Mass of Earth in kg
    moon_mass = 7.348e22  # Mass of Moon in kg
    distance = 3844e5  # Average distance between Earth and Moon in meters
    time_step = 86400  # Time step in seconds (1 day)
    num_steps = 180  # Number of simulation steps

    # Initial positions and velocities
    earth_pos = [0, 0]
    moon_pos = [distance, 0]
    earth_vel = [0, 0]
    moon_vel = [0, 1022]  # Moon's average orbital speed in m/s

    def draw_text(oled, x, y, text):
        oled.text(text, x, y)

    center_x = oled.width // 2
    center_y = oled.height // 2

    for step in range(num_steps):
        oled.fill(0)
        
        # Calculate gravitational force
        dx = moon_pos[0] - earth_pos[0]
        dy = moon_pos[1] - earth_pos[1]
        distance = math.sqrt(dx**2 + dy**2)
        force = G * earth_mass * moon_mass / distance**2
        fx = force * dx / distance
        fy = force * dy / distance
        
        # Update velocities
        earth_vel[0] += fx / earth_mass * time_step
        earth_vel[1] += fy / earth_mass * time_step
        moon_vel[0] -= fx / moon_mass * time_step
        moon_vel[1] -= fy / moon_mass * time_step
        
        # Update positions
        earth_pos[0] += earth_vel[0] * time_step
        earth_pos[1] += earth_vel[1] * time_step
        moon_pos[0] += moon_vel[0] * time_step
        moon_pos[1] += moon_vel[1] * time_step
        
        # Scale positions to fit the display
        scale = 1.35e7  # Adjusted scale factor
        earth_x = center_x
        earth_y = center_y
        moon_x = int(center_x + (moon_pos[0] - earth_pos[0]) / scale)
        moon_y = int(center_y + (moon_pos[1] - earth_pos[1]) / scale)
        
        # Draw Earth and Moon
        draw_text(oled, earth_x, earth_y, 'o')
        draw_text(oled, moon_x, moon_y, '.')
        #oled.text(str(step + 1), 0, 2)
        
        oled.show()
        utime.sleep(0.05)
        
def star_wars_text(oled, text, speed=0.05):
    oled.fill(0)
    lines = text.split('\n')
    start_y = oled_height

    while start_y > -len(lines) * 8:
        oled.fill(0)
        for i, line in enumerate(lines):
            y = start_y + i * 8
            if 0 <= y < oled_height:
                oled.text(line, (oled_width - len(line) * 8) // 2, y)
        oled.show()
        utime.sleep(speed)
        start_y -= 1

def end_animation():
    text = """RP2040 demo

Coded by Copilot
----------------
Inspired by

demo scene
----------------
Uploaded by

MD76
----------------
https://github
.com/mdoksa76/
RPi_Pico_RP2040


Thank you
for watching!"""
    star_wars_text(oled, text)

def main():
    loading_animation()
    display_logo()
    animate_flip(oled, raspberry_pi_logo)
    loading_dots_animation(oled)
    atom_animation(oled)
    loading_dots_animation(oled)
    play_random_squares()
    loading_dots_animation(oled)
    play_random_circles()
    loading_dots_animation(oled)
    play_random_shapes()
    loading_dots_animation(oled)
    lines_animation(oled)
    loading_dots_animation(oled)
    rain_animation(oled)
    snowflakes_animation(oled)
    loading_dots_animation(oled)
    matrix_animation(oled)
    loading_dots_animation(oled)
    rotating_cube_animation(oled)
    loading_dots_animation(oled)
    chaotic_lines_animation(oled)
    loading_dots_animation(oled)
    earth_moon_simulation(oled)
    end_animation()
    display_logo()

main()
