from machine import Pin
import utime

led = Pin(25, Pin.OUT)


def signal_short():
    utime.sleep(0.25)
    led.high()
    utime.sleep(0.25)
    led.low()


def signal_long():
    utime.sleep(0.5)
    led.high()
    utime.sleep(0.5)
    led.low()


def signal_s():
    for _ in range(3):
        signal_short()


def signal_o():
    for _ in range(3):
        signal_long()


while True:
    signal_s()
    signal_o()
    signal_s()
    utime.sleep(1)
