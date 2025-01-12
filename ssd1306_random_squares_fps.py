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

def draw_random_squares(oled):
    oled.fill(0)
    for _ in range(10):  # Number of squares to draw
        x = random.randint(0, oled_width - 10)
        y = random.randint(0, oled_height - 10)
        size = random.randint(5, 10)
        oled.rect(x, y, size, size, 1)
    
    oled.show()

def main():
    frame_count = 0
    start_time = utime.ticks_ms()
    
    while True:
        draw_random_squares(oled)
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
        print("FPS: {:.2f}".format(fps))
        
        # Delay to control frame rate
        utime.sleep(0.1)

main()
