from robot_car import RobotCar
from rc_time import RC_Time
from machine import Pin

# GPIO Pins for logic input into DRV8833
LEFT_MOTOR_PIN1 = 12
LEFT_MOTOR_PIN2 = 13
RIGHT_MOTOR_PIN1 = 14
RIGHT_MOTOR_PIN2 = 15
LEFT_LIGHT_SENSOR = 1
RIGHT_LIGHT_SENSOR = 2
led = Pin("LED", Pin.OUT)

MOTOR_PIN_ARRAY = [LEFT_MOTOR_PIN1, LEFT_MOTOR_PIN2, RIGHT_MOTOR_PIN1, RIGHT_MOTOR_PIN2]

# Create instance of RobotCar class
robot = RobotCar(MOTOR_PIN_ARRAY)

# currently working on vehicle 2a
if __name__ == "__main__":
    try:
        while True:
            left_light = RC_Time(LEFT_LIGHT_SENSOR)
            right_light = RC_Time(RIGHT_LIGHT_SENSOR)
            print("left_light:", left_light)
            print("right_light:", right_light)

            # change the speed of each wheel depending on what the current value of the sensor is

            if (left_light < 300 and left_light > 60):
                led.high()
                robot.move_forward()
            else:
                led.low()
                robot.stop()
    except KeyboardInterrupt:
        robot.deinit()