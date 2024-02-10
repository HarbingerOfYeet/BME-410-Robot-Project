from robot_car import RobotCar
from utime import sleep

# GPIO Pins for logic input into DRV8833
LEFT_MOTOR_PIN1 = 2
LEFT_MOTOR_PIN2 = 3
RIGHT_MOTOR_PIN1 = 14
RIGHT_MOTOR_PIN2 = 15

MOTOR_PIN_ARRAY = [LEFT_MOTOR_PIN1, LEFT_MOTOR_PIN2, RIGHT_MOTOR_PIN1, RIGHT_MOTOR_PIN2]

# Create instance of RobotCar class
robot = RobotCar(MOTOR_PIN_ARRAY)

if __name__ == "__main__":
    robot.move_forward()
    sleep(2)
    robot.move_backward()
    sleep(2)
