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
GPIO.setup(m2_a,GPIO.OUT)
GPIO.setup(m2_b,GPIO.OUT)

GPIO.output(m1_a,GPIO.LOW)
GPIO.output(m1_b,GPIO.LOW)
GPIO.output(m2_b,GPIO.LOW)
GPIO.output(m2_a,GPIO.LOW)

def stop():
    print("stop")
    GPIO.output(m1_a,GPIO.LOW)
    GPIO.output(m1_b,GPIO.LOW)
    GPIO.output(m2_a,GPIO.LOW)
    GPIO.output(m2_b,GPIO.LOW)

def forward():
    GPIO.output(m1_a,GPIO.LOW)
    GPIO.output(m1_b,GPIO.HIGH)
    GPIO.output(m2_a,GPIO.LOW)
    GPIO.output(m2_b,GPIO.HIGH)
    print("Forward")

def backward():
    GPIO.output(m1_a,GPIO.HIGH)
    GPIO.output(m1_b,GPIO.LOW)
    GPIO.output(m2_a,GPIO.HIGH)
    GPIO.output(m2_b,GPIO.LOW)
    print("back")

def left():
    GPIO.output(m1_a,GPIO.LOW)
    GPIO.output(m1_b,GPIO.HIGH)
    GPIO.output(m2_a,GPIO.HIGH)
    GPIO.output(m2_b,GPIO.LOW)
    print("left")

def right():
    GPIO.output(m1_a,GPIO.HIGH)
    GPIO.output(m1_b,GPIO.LOW)
    GPIO.output(m2_a,GPIO.LOW)
    GPIO.output(m2_b,GPIO.HIGH)
    print("right")

def main():
    print("INSTRUCTIONS\n\nst-to stop\nw-forward\na-left\ns-backward\nd-right\n\ne - to exit\n")

    while(True):
        x=input()

        if x=='st':
            stop()
            x='z'

        elif x=='w':
            forward()
            temp1=1
            x='z'

        elif x=='a':
            left()
            x='z'

        elif x=='s':
            backward()
            temp1=0
            x='z'

        elif x=='d':
            right()
            x='z'
        
        elif x=='e':
            print("asancar is closed")
            GPIO.cleanup()
            print("GPIO Clean up")
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")

if __name__ == "__main__":
    main()