import machine
import time

adc = machine.ADC(4)
temperature_value = adc.read_u16()
print(temperature_value)