from robot_car import RobotCar
from rc_time import RC_Time
from machine import Pin
from utime import sleep_us
from time import sleep
from thermistor import get_temp

# GPIO pins for logic input into DRV8833
LEFT_MOTOR_PIN1 = 12
LEFT_MOTOR_PIN2 = 13
RIGHT_MOTOR_PIN1 = 14
RIGHT_MOTOR_PIN2 = 15

# GPIO pins to read photoresistor values
LEFT_LIGHT_SENSOR = 1
RIGHT_LIGHT_SENSOR = 18

# GPIO pins to read thermistor values
LEFT_TEMP_SENSOR = 26
RIGHT_TEMP_SENSOR = 27

led = Pin("LED", Pin.OUT)

# parameters for changing speed
MAX_CHARGE_TIME = 7000
MAX_SPEED = 50
SLOW_MULTIPLIER = 1.2
MAX_TEMP = 75

MOTOR_PIN_ARRAY = [LEFT_MOTOR_PIN1, LEFT_MOTOR_PIN2, RIGHT_MOTOR_PIN1, RIGHT_MOTOR_PIN2]

# Create instance of RobotCar class
robot = RobotCar(MOTOR_PIN_ARRAY)
robot.change_speed(1.2* MAX_SPEED, 0.8 * MAX_SPEED)

# Main function
if __name__ == "__main__":
    try:
        new_left_speed = MAX_SPEED
        new_right_speed = MAX_SPEED
        temp_right_speed = 0
        temp_left_speed = 0
        while True:
            # turn led on
            led.high()

            # get charge values from light sensors (lower value -> more light)
            left_light = RC_Time(LEFT_LIGHT_SENSOR)
            right_light = RC_Time(RIGHT_LIGHT_SENSOR)
            # print(f"Left light: {left_light}, Right Light: {right_light}")

            # get temp values from thermistors (lower value -> colder)
            left_temp = get_temp(LEFT_TEMP_SENSOR)
            right_temp = get_temp(RIGHT_TEMP_SENSOR)
            temp_diff = left_temp - right_temp
            # print("temp diff: ", left_temp - right_temp)

            # Robot likes light -> will move toward light
            # if right sensor receives more input -> left wheel will turn faster -> turn right
            # if left sensor receives more input -> right wheel will turn faster -> turn left
            light_left_speed = right_light * MAX_SPEED / MAX_CHARGE_TIME
            light_right_speed = left_light * MAX_SPEED / MAX_CHARGE_TIME


            # Robot does not like heat -> will move away from heat
            # if right sensor receives more input -> right wheel will turn faster -> turn left
            # if left sensor receives more input -> left wheel will turn faster -> turn right
            if (temp_diff > 4):
                temp_left_speed = MAX_SPEED - (pow(temp_diff, 2) * MAX_SPEED / MAX_TEMP)

            elif (temp_diff < -4):
                temp_right_speed = MAX_SPEED - (pow(temp_diff, 2) * MAX_SPEED / MAX_TEMP)
            else:
                temp_left_speed = 0
                temp_right_speed = 0

            # print(f"Left temp: {temp_left_speed}, Right temp: {temp_right_speed}")

            new_left_speed = MAX_SPEED - light_left_speed + temp_left_speed
            new_right_speed = MAX_SPEED - light_right_speed + temp_right_speed
                
            # cap the speed at 0 and 100
            if (new_left_speed > 100):
                new_left_speed = 100

            if (new_right_speed > 100):
                new_right_speed = 100

            if (new_left_speed < 0):
                new_left_speed = 0

            if (new_right_speed < 0):
                new_right_speed = 0

            print(f"Left speed: {new_left_speed}, Right speed: {new_right_speed}")
            robot.change_speed(int(new_left_speed), int(new_right_speed))
            robot.move_forward()
            sleep_us(100)
            # sleep(2)
    except KeyboardInterrupt:
        robot.deinit()
    except ValueError:
        robot.deinit()