from machine import Pin, I2C
import ssd1306
import utime

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # Clear the display
    oled.fill(0)
    
    # Get the current time
    current_time = utime.localtime()
    hours = current_time[3]
    minutes = current_time[4]
    seconds = current_time[5]
    
    # Format the time string
    time_string = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    
    # Display the time
    oled.text(time_string, 0, 0)
    
    # Update the display
    oled.show()
    
    # Wait for a second
    utime.sleep(1)
