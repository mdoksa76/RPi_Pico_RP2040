import machine
import time

# Initialize PWM on GPIO pin 25
pwm = machine.PWM(machine.Pin(25))

# Set the PWM frequency to 1 kHz
pwm.freq(1000)

# Open a file to save the data
with open("pwm_data.txt", "w") as file:
    while True:
        # Gradually decrease the brightness
        for duty in range(65535, -1, -256):
            pwm.duty_u16(duty)
            voltage = (duty / 65535) * 3.3  # Assuming 3.3V as the reference voltage
            data = f"Decreasing: Duty = {duty}, Voltage = {voltage:.2f}V\n"
            file.write(data)
            print(data.strip())  # Print to terminal
            time.sleep(0.01)
        
        time.sleep(0.5)
        
        # Gradually increase the brightness
        for duty in range(0, 65536, 256):
            pwm.duty_u16(duty)
            voltage = (duty / 65535) * 3.3  # Assuming 3.3V as the reference voltage
            data = f"Increasing: Duty = {duty}, Voltage = {voltage:.2f}V\n"
            file.write(data)
            print(data.strip())  # Print to terminal
            time.sleep(0.01)
