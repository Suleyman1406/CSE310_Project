import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

R_TRIG = 8
R_ECHO = 7

L_TRIG = 26
L_ECHO = 19

print("HC-SR04 distance measurement in progress")

GPIO.setup(R_TRIG,GPIO.OUT)
GPIO.setup(R_ECHO,GPIO.IN)

GPIO.setup(L_TRIG,GPIO.OUT)
GPIO.setup(L_ECHO,GPIO.IN)

while True:

    # Right sensor begin
    GPIO.output(R_TRIG, False)
    print("Olculuyor...")
    time.sleep(1)

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
    
    if right_distance > 2 and right_distance < 400:
        print("RIGHT -- Mesafe:",right_distance - 0.5,"cm")
    else:
        print("RIGHT -- Menzil asildi")

    # Rigth sensor end
    # Left sensor start 

    GPIO.output(L_TRIG, False)
    print("Olculuyor...")
    time.sleep(1)

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

    if left_distance > 2 and left_distance < 400:
        print("LEFT -- Mesafe:",left_distance - 0.5,"cm")
    else:
        print("LEFT -- Menzil asildi")
    
    # Left sensor end