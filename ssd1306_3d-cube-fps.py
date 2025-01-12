from machine import Pin, I2C
import ssd1306
import utime
import math

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Initialize OLED display
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Define the vertices of the cube
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

# Define the edges of the cube
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

def main():
    width, height = 30, 30  # Box size
    scale = 15  # Scale factor to fit within 30x30 area
    viewer_distance = 4
    angle_x, angle_y, angle_z = 0, 0, 0
    frame_count = 0
    start_time = utime.ticks_ms()

    while True:
        oled.fill(0)
        rotated_vertices = rotate(vertices, angle_x, angle_y, angle_z)
        projected_vertices = project(rotated_vertices, width, height, scale)
        
        # Center the cube in the middle of the screen
        for i in range(len(projected_vertices)):
            projected_vertices[i][0] += (oled_width - width) // 2
            projected_vertices[i][1] += (oled_height - height) // 2

        draw_cube(oled, projected_vertices, edges)
        
        # Calculate FPS
        frame_count += 1
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time) / 1000
        if elapsed_time > 0:
            fps = frame_count / elapsed_time
        else:
            fps = 0
        
        # Display FPS
        oled.fill_rect(0, 0, oled_width, 8, 0)  # Clear the top line
        oled.text("FPS: ", 0, 0)
        oled.text("{:.2f}".format(fps), 0, 10)
        print("FPS: {:.2f}".format(fps))
        oled.show()

        angle_x += 0.05
        angle_y += 0.05
        angle_z += 0.05

        utime.sleep(0.1)

main()
