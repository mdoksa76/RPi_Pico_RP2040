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
    
    # Get the current date and time
    current_time = utime.localtime()
    day = current_time[2]
    month = current_time[1]
    year = current_time[0]
    hours = current_time[3]
    minutes = current_time[4]
    seconds = current_time[5]
    
    # Format the date and time strings
    date_string = "{:02}-{:02}-{:04}".format(day, month, year)
    time_string = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    
    # Display the date and time
    oled.text(date_string, 0, 0)
    oled.text(time_string, 0, 16)
    
    # Update the display
    oled.show()
    
    # Wait for a second
    utime.sleep(1)
