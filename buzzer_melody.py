from machine import Pin, I2C, PWM
import time

# Initialize Buzzer
buzzer = PWM(Pin(0))  # Buzzer connected to GPIO 2

# Melody notes (frequencies in Hz)
melody = [262, 294, 330, 349, 392, 440, 494, 523]  # C4 to C5

# Function to play a melody
def play_melody():
    for note in melody:
        buzzer.freq(note)
        buzzer.duty_u16(32768)  # 50% duty cycle
        time.sleep(0.2)
        buzzer.duty_u16(0)  # Turn off buzzer
        time.sleep(0.05)

# Main loop
while True:
    play_melody()