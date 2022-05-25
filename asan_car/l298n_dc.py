from ipaddress import summarize_address_range
import RPi.GPIO as GPIO          
from time import sleep

m1_a = 24
m1_b = 23

m2_a = 22
m2_b = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(m1_a,GPIO.OUT)
GPIO.setup(m1_b,GPIO.OUT)
GPIO.output(m1_a,GPIO.LOW)
GPIO.output(m1_b,GPIO.LOW)

GPIO.setup(m2_a,GPIO.OUT)
GPIO.setup(m2_b,GPIO.OUT)
GPIO.output(m2_b,GPIO.LOW)
GPIO.output(m2_a,GPIO.LOW)


# print("The default speed & direction of motor is LOW & Forward.....")
print("INSTRUCTIONS\n\nst-to stop\nw-forward\na-left\ns-backward\nd-right\n\ne - to exit")
print("\n")    

while(True):
    x=input()

    if x=='st':
        print("asancar has stopped")
        GPIO.output(m1_a,GPIO.LOW)
        GPIO.output(m1_b,GPIO.LOW)
        GPIO.output(m2_a,GPIO.LOW)
        GPIO.output(m2_b,GPIO.LOW)
        x='z'

    elif x=='w':
        print("asancar is going forward")
        GPIO.output(m1_a,GPIO.LOW)
        GPIO.output(m1_b,GPIO.HIGH)
        GPIO.output(m2_a,GPIO.LOW)
        GPIO.output(m2_b,GPIO.HIGH)
        temp1=1
        x='z'

    elif x=='a':
        print("asancar is going left")
        GPIO.output(m1_a,GPIO.LOW)
        GPIO.output(m1_b,GPIO.HIGH)
        GPIO.output(m2_a,GPIO.HIGH)
        GPIO.output(m2_b,GPIO.LOW)
        x='z'

    elif x=='s':
        print("asan car is going backward")
        GPIO.output(m1_a,GPIO.HIGH)
        GPIO.output(m1_b,GPIO.LOW)
        GPIO.output(m2_a,GPIO.HIGH)
        GPIO.output(m2_b,GPIO.LOW)
        temp1=0
        x='z'

    elif x=='d':
        print("asancar is going right")
        GPIO.output(m1_a,GPIO.HIGH)
        GPIO.output(m1_b,GPIO.LOW)
        GPIO.output(m2_a,GPIO.LOW)
        GPIO.output(m2_b,GPIO.HIGH)
        x='z'
     
    elif x=='e':
        print("asancar is closed")
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")