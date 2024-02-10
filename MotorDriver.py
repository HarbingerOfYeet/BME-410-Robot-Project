from utime import sleep
from machine import Pin

motor_pin1 = Pin(14, Pin.OUT)
motor_pin2 = Pin(15, Pin.OUT)
motor_pin3 = Pin(2, Pin.OUT)
motor_pin4 = Pin(3, Pin.OUT)

def forward():
    motor_pin1.high()
    motor_pin2.low()
    motor_pin3.high()
    motor_pin4.low()

def backward():
    motor_pin1.low()
    motor_pin2.high()
    motor_pin3.high()
    motor_pin4.low()

def stop():
    motor_pin1.low()
    motor_pin2.low()
    motor_pin3.low()
    motor_pin4.low()

if __name__ == "__main__":
    print("Forward")
    forward()
    sleep(2)
    print("Backward")
    backward()
    sleep(2)
    print("Stop")
    stop()