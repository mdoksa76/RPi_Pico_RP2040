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

def draw_triangle(oled, x0, y0, x1, y1, x2, y2):
    oled.line(x0, y0, x1, y1, 1)
    oled.line(x1, y1, x2, y2, 1)
    oled.line(x2, y2, x0, y0, 1)

def draw_random_triangles(oled):
    oled.fill(0)
    for _ in range(5):  # Number of triangles to draw
        x0 = random.randint(0, oled_width - 1)
        y0 = random.randint(0, oled_height - 1)
        x1 = random.randint(0, oled_width - 1)
        y1 = random.randint(0, oled_height - 1)
        x2 = random.randint(0, oled_width - 1)
        y2 = random.randint(0, oled_height - 1)
        draw_triangle(oled, x0, y0, x1, y1, x2, y2)
    
    oled.show()

def main():
    frame_count = 0
    start_time = utime.ticks_ms()
    
    while True:
        draw_random_triangles(oled)
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
