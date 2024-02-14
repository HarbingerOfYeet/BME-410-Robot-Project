# Referenced from https://pimylifeup.com/raspberry-pi-light-sensor/

from machine import Pin
from utime import sleep

def rc_time(rc_pin):
    count = 0

    # Output on the pin for 0.1 s
    rc_pin = Pin(2, Pin.OUT)
    rc_pin.low()
    sleep(0.1)

    # Change the pin back to input
    rc_pin.init(rc_pin.IN)

    # Count until the pin reaches high
    while (rc_pin.value() == 0):
        count += 1

    return count

try:
    while True:
        print(rc_time(2))
except KeyboardInterrupt:
    print("Stopped")









