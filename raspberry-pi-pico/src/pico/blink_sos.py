from machine import Pin
import utime

ONBOARD_LED_PIN = 25

led = Pin(ONBOARD_LED_PIN, Pin.OUT)


def signal_short():
    utime.sleep_ms(250)
    led.high()
    utime.sleep_ms(250)
    led.low()


def signal_long():
    utime.sleep_ms(500)
    led.high()
    utime.sleep_ms(500)
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
    utime.sleep_ms(1000)
