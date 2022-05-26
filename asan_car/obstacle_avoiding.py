import RPi.GPIO as GPIO  
import time
from l9119_engine import forward, backward, left, stop, right
from hcsr04 import calculate_right_distance, calculate_left_distance

GPIO.setmode(GPIO.BCM)                   
GPIO.setwarnings(False)

def obstacle_avoidence(number_of_lives):
    going_forward = False
    already_measured_left = False

    for x in range(number_of_lives):
        if already_measured_left:
            distance = calculate_right_distance()
            obstacle = 'on right'
        else:
            distance = calculate_left_distance()
            obstacle = 'on left'
        already_measured_left = not already_measured_left
        print("distance "+obstacle+" is "+str(distance))
        if distance < 25:
            stop()
            time.sleep(1)
            backward()
            time.sleep(1.5)
            if obstacle == 'on right':
                left()
            else:
                right()
            time.sleep(1)
            going_forward = False
        if going_forward is False:
            forward()
            going_forward = True

if __name__ == "__main__":
    while True:
        obstacle_avoidence(1)

