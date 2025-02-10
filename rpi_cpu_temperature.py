import machine
import utime

# Initialize the ADC (Analog to Digital Converter) on pin 4
sensor_temp = machine.ADC(4)

# Conversion factor for temperature sensor
conversion_factor = 3.3 / (65535)

while True:
    # Read the raw ADC value
    adc_value = sensor_temp.read_u16()
    voltage = adc_value * conversion_factor
    
    # Convert the raw value to temperature in Celsius
    temperature = 27 - (voltage - 0.706) / 0.001721
    
    print(f"Temperature: {temperature:.2f}°C")
    print(f"ADC Value: {adc_value}")
    print(f"Voltage: {voltage:.4f}V")
    
    # Wait for a second before reading again
    utime.sleep(1)
