from robot_car import RobotCar
from utime import sleep
from rc_time import RC_Time

# GPIO Pins for logic input into DRV8833
LEFT_MOTOR_PIN1 = 12
LEFT_MOTOR_PIN2 = 13
RIGHT_MOTOR_PIN1 = 14
RIGHT_MOTOR_PIN2 = 15

MOTOR_PIN_ARRAY = [LEFT_MOTOR_PIN1, LEFT_MOTOR_PIN2, RIGHT_MOTOR_PIN1, RIGHT_MOTOR_PIN2]

# Create instance of RobotCar class
robot = RobotCar(MOTOR_PIN_ARRAY)

if __name__ == "__main__":
    try:
        while True:
            time = RC_Time(2)
            print(time)
            if (time < 300 and time > 10):
                robot.move_forward()
            else:
                robot.stop()
    except KeyboardInterrupt:
        robot.deinit()
