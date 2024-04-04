from machine import Pin, I2C
from utime import sleep

from dht20 import DHT20

left_sda = Pin(8)
left_scl = Pin(9)
right_sda = Pin(16)
right_scl = Pin(17)
left_i2c = I2C(0, sda=left_sda, scl=left_scl)
right_i2c = I2C(0, sda=right_sda, scl=right_scl)

left_dht20 = DHT20(0x38, left_i2c)
# right_dht20 = DHT20(0x38, right_i2c)

while True:
    right_measurements = left_dht20.measurements
    print(f"Temperature: {right_measurements['t']} °C, humidity: {right_measurements['rh']} %RH")
    sleep(1)