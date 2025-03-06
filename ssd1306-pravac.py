from machine import Pin, I2C
import ssd1306
import utime

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Center coordinates
center_x = oled_width // 2
center_y = oled_height // 2

def pravac(oled,a,b):
    oled.fill(0)
    oled.hline(0, center_y, oled_width, 1)
    oled.vline(center_x, 0, oled_height, 1)
    oled.rect(0, 0, oled_width, oled_height, 1)
    oled.text('x', oled_width-10, center_y+2, 1)
    oled.text('y', center_x+2, 0, 1)
    for x in [-60, -45, -30, -15, 15, 30, 45, 60]:
        screen_x = center_x + x
        oled.vline(screen_x, center_y - 2, 4, 1)
    for y in [-30, -15, 15, 30]:
        screen_y = center_y - y
        oled.hline(center_x - 2, screen_y, 4, 1)
    
    tocke = [(center_x + x, center_y - int(a * x + b)) for x in [-center_x, center_x]]
    oled.line(tocke[0][0], tocke[0][1], tocke[1][0], tocke[1][1], 1)
    oled.show()
    utime.sleep(5)
    
pravac(oled,0.5,5)
pravac(oled,2.5,-5)
pravac(oled,0.25,20)
pravac(oled,-1,-10)
