from machine import Pin, I2C
import ssd1306
import utime
import math

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Simulation parameters
G = 6.67430e-11  # Gravitational constant
earth_mass = 5.972e24  # Mass of Earth in kg
moon_mass = 7.348e22  # Mass of Moon in kg
distance = 3844e5  # Average distance between Earth and Moon in meters
time_step = 86400  # Time step in seconds (1 day)
num_steps = 1000  # Number of simulation steps

# Initial positions and velocities
earth_pos = [0, 0]
moon_pos = [distance, 0]
earth_vel = [0, 0]
moon_vel = [0, 1022]  # Moon's average orbital speed in m/s

def draw_text(oled, x, y, text):
    oled.text(text, x, y)

def earth_moon_simulation(oled):
    center_x = oled_width // 2
    center_y = oled_height // 2

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
        oled.text(str(step+1), 0, 2)
        
        oled.show()
        utime.sleep(0.05)
        
        # Print force, distance, and moon velocity
        moon_velocity = math.sqrt(moon_vel[0]**2 + moon_vel[1]**2)
        print(f"Step: {step}, Force: {force:.2e} N, Distance: {distance:.2e} m, Moon Velocity: {moon_velocity:.2f} m/s")

def main():
    earth_moon_simulation(oled)

main()
