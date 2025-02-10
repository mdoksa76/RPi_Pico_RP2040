import random
import math
import time
from machine import Pin, I2C
import ssd1306

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Define the square and circle parameters
square_size = 62
circle_radius = square_size // 2
center_x = oled_width // 2
center_y = oled_height // 2

# Draw the square
oled.rect(center_x - circle_radius, center_y - circle_radius, square_size, square_size, 1)

# Draw the circle
for angle in range(0, 360):
    x = int(circle_radius * math.cos(math.radians(angle)))
    y = int(circle_radius * math.sin(math.radians(angle)))
    oled.pixel(center_x + x, center_y + y, 1)

print("Pi calculation by Monte Carlo method")

def calculate_pi(num_points):
    inside_circle = 0
    outside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-circle_radius, circle_radius)
        y = random.uniform(-circle_radius, circle_radius)
        distance = math.sqrt(x**2 + y**2)
        if distance <= circle_radius:
            inside_circle += 1
            oled.pixel(center_x + int(x), center_y + int(y), 1)
        else:
            outside_circle += 1
            oled.pixel(center_x + int(x), center_y + int(y), 1)  # Change to 1 to make points visible
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate, inside_circle, outside_circle

# Number of points to use for the visualization
num_points = 1000

# Measure the time taken for the calculation
start_time = time.time()

# Calculate pi
pi_estimate, inside_circle, outside_circle = calculate_pi(num_points)

end_time = time.time()
elapsed_time = end_time - start_time

# Display the image
oled.show()

print(f"Estimated value of π: {pi_estimate}")
print(f"Number of points inside the circle: {inside_circle}")
print(f"Number of points outside the circle: {outside_circle}")
print(f"Time taken: {elapsed_time:.6f} seconds")
