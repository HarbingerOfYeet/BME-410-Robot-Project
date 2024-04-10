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
right_dht20 = DHT20(0x38, right_i2c)

while True:
    right_measurements = right_dht20.measurements
    left_measurements = left_dht20.measurements
    temp_diff = (right_dht20.measurements['t'] - left_dht20.measurements['t']) * 1000
    hum_diff = (right_dht20.measurements['rh'] - left_dht20.measurements['rh']) * 1000
    # print(f"Right Temp: {(right_measurements['t'] * 9/5) + 32} °F, Right Hum: {right_measurements['rh']} %RH")
    # print(f"Left Temp: {(left_measurements['t'] * 9/5) + 32} °F, Left Hum: {left_measurements['rh']} %RH")
    # print(f"Temp diff (right minus left): {temp_diff} °C (thousands)")
    print(f"Humidity diff: {hum_diff} %RH")
    sleep(1)