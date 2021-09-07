import machine
from machine import Pin
import utime

LOG_FILE_PATH = "log/temperature.txt"
ONBOARD_LED_PIN = 25

led = Pin(ONBOARD_LED_PIN, Pin.OUT)
file = open(LOG_FILE_PATH, "w")


def get_timestamp():
    timestamp_format = "%d-%02d-%02d %02d:%02d:%02d"
    year, month, day, hour, minute, second, millis, _tzinfo = utime.gmtime()
    return timestamp_format % (year, month, day, hour, minute, second)


def get_temperature():
    sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
    conversion_factor = 3.3 / 65535
    reading = sensor_temp.read_u16() * conversion_factor
    return str(27 - (reading - 0.706) / 0.001721)


def wait_and_blink_led():
    led.low()
    utime.sleep(1)
    led.high()


while True:
    formatted_record = get_timestamp() + " -----> " + get_temperature()
    print(formatted_record)
    file.write(formatted_record + "\n")
    file.flush()
    wait_and_blink_led()
