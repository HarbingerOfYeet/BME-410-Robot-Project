import utime
from machine import Pin, PWM

motor1A = Pin(14, Pin.OUT)
motor2A = Pin(15, Pin.OUT)

def forward():
    motor1A.high()
    motor2A.low()

def backward():
    motor1A.low()
    motor2A.high()

def stop():
    motor1A.low()
    motor2A.low()

if __name__ == "__main__":
    # print("Forward")
    # forward()
    # utime.sleep(2)
    # print("Backward")
    # backward()
    # utime.sleep(2)
    # print("Stop")
    # stop()
    print("on")
    motor1A.high()
    utime.sleep(2)
    print("off")
    motor1A.low()
    utime.sleep(2)
    print("on")
    motor1A.high()
    utime.sleep(2)
    print("off")
    motor1A.low()