import machine
import utime

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / 65535

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706) / 0.001721
    print(temp)
    utime.sleep(0.5)
