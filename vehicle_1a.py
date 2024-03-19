from robot_car import RobotCar
from rc_time import RC_Time
from machine import Pin

# GPIO Pins for logic input into DRV8833
LEFT_MOTOR_PIN1 = 12
LEFT_MOTOR_PIN2 = 13
RIGHT_MOTOR_PIN1 = 14
RIGHT_MOTOR_PIN2 = 15
led = Pin("LED", Pin.OUT)

MOTOR_PIN_ARRAY = [LEFT_MOTOR_PIN1, LEFT_MOTOR_PIN2, RIGHT_MOTOR_PIN1, RIGHT_MOTOR_PIN2]

# Create instance of RobotCar class
robot = RobotCar(MOTOR_PIN_ARRAY)

if __name__ == "__main__":
    try:
        while True:
            time = RC_Time(1)
            if (time < 300 and time > 60):
                led.high()
                robot.move_forward()
            else:
                led.low()
                robot.stop()
    except KeyboardInterrupt:
        robot.deinit()