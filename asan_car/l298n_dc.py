# Python Script

from ipaddress import summarize_address_range
import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23

in3 = 22
in4 = 27

ena = 25
enb = 17
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1=GPIO.PWM(ena,1000)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
p2=GPIO.PWM(enb,1000)


p1.start(25)
p2.start(25)
print("\n")
# print("The default speed & direction of motor is LOW & Forward.....")
print("INSTRUCTIONS\n\nstop-to stop\nw-forward\na-left\ns-backward\nd-right\n\nTo Change the Speed\nl-low\nm-medium\nh-high\n\nexit-to exit")
print("\n")    

while(1):

    x=input()
    
    if x=='run':
        print("asancar is running")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'

    if x=='stop':
        print("asancar has stopped")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='w':
        print("asancar is going forward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='a':
        print("asancar is going left")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='s':
        print("asan car is going backward")
        
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        x='z'

    elif x=='d':
        print("asancar is going right")
        
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='l':
        print("asancar's speed is low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("asancar's speed is medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("asancar's speed is high")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='exit':
        print("asancar is closed")
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")