from machine import Pin
import utime
led = Pin(25, Pin.OUT)

def signal_S():
    for i in range(3):
        utime.sleep(0.25)
        led.high()
        utime.sleep(0.25)
        led.low()

def signal_O():
    for i in range(3):
        utime.sleep(0.5)
        led.high()
        utime.sleep(0.5)
        led.low()

while True:
    signal_S()
    signal_O()
    signal_S()
    utime.sleep(1)