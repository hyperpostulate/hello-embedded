import machine
import utime

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / 65535
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    year, month, day, hour, minute, second, millis, _tzinfo = utime.gmtime()
    timestamp = "%d-%02d-%02d %02d:%02d:%02d" % (year, month, day, hour, minute, second)
    formatted_record = timestamp + " -----> " + str(temperature)
    print(formatted_record)
    utime.sleep(1)
