import machine
import time

# Definiranje pinova
led_pin = machine.Pin(25, machine.Pin.OUT)
button_pin = machine.Pin(24, machine.Pin.IN, machine.Pin.PULL_UP)

# Varijabla za praćenje stanja LED-a
led_state = False

while True:
    button_state = button_pin.value()
    if button_state == 0:  # Gumb je pritisnut
        time.sleep(0.1)  # Debounce vrijeme
        if button_pin.value() == 0:  # Provjera je li gumb još uvijek pritisnut
            led_state = not led_state  # Promjena stanja LED-a
            led_pin.value(led_state)  # Postavljanje stanja LED-a
            print("LED stanje promijenjeno:", led_state)  # Debug: ispis stanja LED-a
            while button_pin.value() == 0:
                time.sleep(0.1)  # Čekanje dok se gumb ne otpusti

    time.sleep(0.1)  # Kratka pauza za smanjenje opterećenja procesora
