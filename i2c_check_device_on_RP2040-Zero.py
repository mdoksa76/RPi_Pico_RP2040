from machine import Pin, I2C

# ANSI escape codes
BOLD = '\033[1m'
# Define the ANSI escape code for italic text
ITALIC = '\033[3m'
# Define the ANSI escape code to reset formatting
RESET = '\033[0m'

# Define I2C pin combinations
i2c0_pins = [(1, 0), (5, 4), (9, 8), (13, 12)]
i2c1_pins = [(3, 2), (7, 6), (11, 10), (15, 14), (27, 26)]

# Function to scan I2C devices
def scan_i2c(i2c_id, scl, sda):
    try:
        i2c = I2C(i2c_id, scl=Pin(scl), sda=Pin(sda))
        devices = i2c.scan()
        if devices:
            print(f"{BOLD}{ITALIC}I2C devices found on I2C{i2c_id} SCL={scl}, SDA={sda}: {devices}{RESET}")
        else:
            print(f"No I2C devices found on I2C{i2c_id} SCL={scl}, SDA={sda}")
    except OSError as e:
        print(f"Error on I2C{i2c_id} SCL={scl}, SDA={sda}: {e}")

# Scan all combinations for I2C0
print("Scanning I2C0 combinations:")
for scl, sda in i2c0_pins:
    scan_i2c(0, scl, sda)

# Scan all combinations for I2C1
print("Scanning I2C1 combinations:")
for scl, sda in i2c1_pins:
    scan_i2c(1, scl, sda)
