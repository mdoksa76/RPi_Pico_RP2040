from machine import Pin, I2C
import ssd1306
import utime

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Center coordinates
center_x = oled_width // 2
center_y = oled_height // 2

def draw_small_text(oled, text, x, y):
    for i, char in enumerate(text):
        oled.text(char, x + i * 4, y)

def plot_linear_function(oled, m, b):
    oled.fill(0)
    
    #Draw rectangle around screen
    oled.hline(1,1,127,1)
    oled.vline(127,0,127,63)
    oled.hline(1,63,127,63)
    oled.vline(0,1,63,1)
    
    # Draw x and y axes
    oled.hline(0, center_y, oled_width, 1)
    oled.vline(center_x, 0, oled_height, 1)
    
    # Add labels for x and y axes
    oled.text("x", oled_width - 10, center_y - 10)
    oled.text("y", center_x + 2, 0)
    
    # Add ticks and numbers on the x-axis
    for x in [-60, -30, 0, 30]:
        screen_x = center_x + x
        oled.vline(screen_x, center_y - 2, 4, 1)
        if x != 0:
            draw_small_text(oled, str(x), screen_x - 6, center_y + 5)
    
    # Add ticks and numbers on the y-axis
    for y in [-30, -15, 15]:
        screen_y = center_y - y
        oled.hline(center_x - 2, screen_y, 4, 1)
        draw_small_text(oled, str(y), center_x + 5, screen_y - 4)
    
    # Plot the linear function y = mx + b
    for x in range(-center_x, center_x):
        y = int(m * x + b)
        screen_x = center_x + x
        screen_y = center_y - y
        if 0 <= screen_x < oled_width and 0 <= screen_y < oled_height:
            oled.pixel(screen_x, screen_y, 1)
        if m>0:
            oled.text(f"{m},{b}", 2, 4)
        elif m<0:
            oled.text(f"{m},{b}", 2, 52)
    
    oled.show()

# Example: Plot y = 0.5x + 0
plot_linear_function(oled, -0.76, 0)
