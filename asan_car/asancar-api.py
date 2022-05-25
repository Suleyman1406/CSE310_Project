from struct import calcsize
import RPi.GPIO as GPIO
import logging
from flask import Flask, render_template, request
from flask_restful import Api
import time
from obstacle_avoiding import calculate_right_distance, calculate_left_distance

# Initialize Logging
logging.basicConfig(level=logging.WARNING)  # Global logging configuration
logger = logging.getLogger('main')  # Logger for this module
logger.setLevel(logging.INFO) # Debugging for this file.

# Flask & Flask-RESTful instance variables
app = Flask(__name__)
api = Api(app)

#Global variables
R_TRIG = 8
R_ECHO = 7
L_TRIG = 26
L_ECHO = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(R_TRIG,GPIO.OUT)                  
GPIO.setup(R_ECHO,GPIO.IN)                   
GPIO.setup(L_TRIG,GPIO.OUT)              
GPIO.setup(L_ECHO,GPIO.IN) 

@app.route("/")
def index():
	# Read Sensors Status
	right_distance = calculate_right_distance()
	left_distance = calculate_left_distance()
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : right_distance,
              'ledYlw'  : left_distance,
        }
	return render_template('index.html', **templateData)
		

@app.route("/<deviceName>")
def action(deviceName):
	if deviceName == 'right':
		right_distance = calculate_right_distance()
	if deviceName == 'left':
		left_distance = calculate_left_distance()
   
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : right_distance,
              'ledYlw'  : left_distance,
        }
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)