import machine
import time

# Definiranje pinova
led_pin = machine.Pin(25, machine.Pin.OUT)
button_pin = machine.Pin(24, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    button_state = button_pin.value()
    print("Stanje gumba:", button_state)  # Debug: ispis stanja gumba

    if button_state == 0:  # Promijenjeno na 0 za PULL_UP
        led_pin.value(1)  # Upali LED
        print("LED je upaljen")  # Debug: ispis stanja LED-a
    else:
        led_pin.value(0)  # Ugasi LED
        print("LED je ugašen")  # Debug: ispis stanja LED-a

    time.sleep(0.1)  # Kratka pauza za smanjenje opterećenja procesora
