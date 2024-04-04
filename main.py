from robot_car import RobotCar
from rc_time import RC_Time
from machine import Pin
from utime import sleep_us

# GPIO Pins for logic input into DRV8833
LEFT_MOTOR_PIN1 = 12
LEFT_MOTOR_PIN2 = 13
RIGHT_MOTOR_PIN1 = 14
RIGHT_MOTOR_PIN2 = 15
LEFT_LIGHT_SENSOR = 1
RIGHT_LIGHT_SENSOR = 18
led = Pin("LED", Pin.OUT)

# parameters for changing speed
MAX_CHARGE_TIME = 7000
MAX_SPEED = 75
SLOW_MULTIPLIER = 1.2

MOTOR_PIN_ARRAY = [LEFT_MOTOR_PIN1, LEFT_MOTOR_PIN2, RIGHT_MOTOR_PIN1, RIGHT_MOTOR_PIN2]

# Create instance of RobotCar class
robot = RobotCar(MOTOR_PIN_ARRAY)

# currently working on vehicle 2a
if __name__ == "__main__":
    try:
        while True:
            # turn led on
            led.high()

            # # get charge values from light sensors
            # left_light = RC_Time(LEFT_LIGHT_SENSOR)
            # right_light = RC_Time(RIGHT_LIGHT_SENSOR)
            # print("left:", left_light)
            # print("right:", right_light)

            # # calculate speeds for each motor depending on light sensor value
            # new_left_speed = (MAX_SPEED * SLOW_MULTIPLIER) - (right_light * (MAX_SPEED * SLOW_MULTIPLIER) / MAX_CHARGE_TIME)
            # new_right_speed = MAX_SPEED - (left_light * MAX_SPEED / MAX_CHARGE_TIME)
            # print("left:", new_left_speed)
            # print("right:", new_right_speed)
            # robot.change_speed(int(new_left_speed), int(new_right_speed))
            # robot.move_forward()
            # sleep_us(100)
            robot.move_forward()
    except KeyboardInterrupt:
        robot.deinit()