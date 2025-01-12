from machine import Pin, I2C
import ssd1306
import utime
import random

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Initialize OLED display
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

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

def draw_random_shapes(oled):
    oled.fill(0)
    for _ in range(5):  # Number of shapes to draw
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

def main():
    frame_count = 0
    start_time = utime.ticks_ms()
    
    while True:
        draw_random_shapes(oled)
        frame_count += 1
        
        # Calculate FPS
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time) / 1000
        if elapsed_time > 0:
            fps = frame_count / elapsed_time
        else:
            fps = 0
        
        # Display FPS
        oled.fill_rect(0, 0, oled_width, 8, 0)  # Clear the top line
        oled.text("FPS: {:.2f}".format(fps), 0, 0)
        oled.show()
        
        # Delay to control frame rate
        utime.sleep(0.1)

main()
