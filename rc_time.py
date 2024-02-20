# Referenced from https://pimylifeup.com/raspberry-pi-light-sensor/

from machine import Pin
from utime import sleep

def RC_Time(rc_pin):
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

if __name__ == "__main__":
    try:
        while True:
            print(RC_Time(2))
    except KeyboardInterrupt:
        print("Stopped")









