from machine import Pin, Timer

ONBOARD_LED_PIN = 25
BLINKS_PER_SECOND = 10

led = Pin(ONBOARD_LED_PIN, Pin.OUT)
timer = Timer()


def blink(timer):
    led.toggle()


timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=blink)
