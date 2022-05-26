import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

R_TRIG = 8
R_ECHO = 7
L_TRIG = 26
L_ECHO = 19

GPIO.setup(R_TRIG,GPIO.OUT)
GPIO.setup(R_ECHO,GPIO.IN)
GPIO.setup(L_TRIG,GPIO.OUT)
GPIO.setup(L_ECHO,GPIO.IN)

def calculate_right_distance():
    GPIO.output(R_TRIG, False)
    time.sleep(0.1)

    GPIO.output(R_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(R_TRIG, False)

    while GPIO.input(R_ECHO)==0:
        right_pulse_start = time.time()

    while GPIO.input(R_ECHO)==1:
        right_pulse_end = time.time()

    right_pulse_duration = right_pulse_end - right_pulse_start
    
    right_distance = right_pulse_duration * 17150
    right_distance = round(right_distance, 2)
    return right_distance - 0.5
                  
def calculate_left_distance():
    GPIO.output(L_TRIG, False)
    time.sleep(0.1)

    GPIO.output(L_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(L_TRIG, False)

    while GPIO.input(L_ECHO)==0:
        left_pulse_start = time.time()

    while GPIO.input(L_ECHO)==1:
        left_pulse_end = time.time()

    left_pulse_duration = left_pulse_end - left_pulse_start
    
    left_distance = left_pulse_duration * 17150
    left_distance = round(left_distance, 2)
    return left_distance - 0.5

def main():
    already_measured_left = False
    while True:
        
        if already_measured_left:
            distance = calculate_right_distance()
            str = 'right'
            already_measured_left = False
            
        else:
            distance = calculate_left_distance()
            str = 'left'
            already_measured_left = True
            
        if distance > 2 and distance < 400:
            print(str+" -- Mesafe:",distance - 0.5,"cm")
        else:
            print(str+" -- Menzil asildi")
        time.sleep(0.5)

if __name__ == "__main__":
    main()