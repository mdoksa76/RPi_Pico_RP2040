from machine import Pin, I2C

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Scan for I2C devices
devices = i2c.scan()

if devices:
    for device in devices:
        print("I2C device found at address:", hex(device))
else:
    print("No I2C devices found")
