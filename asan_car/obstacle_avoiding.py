from enum import Flag
from turtle import backward
import RPi.GPIO as GPIO                    #Import GPIO library
import time

#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

in1=24
in2=23
in3=22
in4=27

ena = 25
enb = 17

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
p1=GPIO.PWM(ena,1000)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
p2=GPIO.PWM(enb,1000)

def stop():
    print("stop")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def forward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print("Forward")

def back():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    print("back")

def left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    print("left")

def right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("right")

R_TRIG = 8
R_ECHO = 7
L_TRIG = 26
L_ECHO = 19

GPIO.setup(R_TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(R_ECHO,GPIO.IN)                   # initialize GPIO Pin as input
GPIO.setup(L_TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(L_ECHO,GPIO.IN)                   # initialize GPIO Pin as input

def calculate_right_distance():
    GPIO.output(R_TRIG, False)
    print("Olculuyor...")
    time.sleep(0.5)

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
    return right_distance - 0.5
                  
def calculate_left_distance():
    GPIO.output(L_TRIG, False)
    print("Olculuyor...")
    time.sleep(0.5)

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
    return left_distance - 0.5

p1.start(75)
p2.start(75)

stop()
time.sleep(2)

danger_in_left = False
danger_in_right = False
going_forward = False

while True:

    if calculate_left_distance() < 25:
        back()
        time.sleep(0.5)
        right()
        time.sleep(0.3)
        going_forward=False
    if calculate_right_distance() < 25:
        back()
        time.sleep(0.5)
        left()
        time.sleep(0.3)
        going_forward=False
    if going_forward is False:
        forward()

