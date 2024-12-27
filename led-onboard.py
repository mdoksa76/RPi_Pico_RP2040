import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

start_time = utime.ticks_ms()

while True:
    current_time = utime.ticks_ms()
    elapsed_time = utime.ticks_diff(current_time, start_time)
    led_onboard.value(1)
    print(f"on - time: {elapsed_time} ms")
    utime.sleep_ms(1000)
    
    current_time = utime.ticks_ms()
    elapsed_time = utime.ticks_diff(current_time, start_time)
    led_onboard.value(0)
    print(f"off - time: {elapsed_time} ms")
    utime.sleep_ms(1000)
