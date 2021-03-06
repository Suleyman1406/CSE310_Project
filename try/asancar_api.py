import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time
from l9119_engine import forward, backward, left, stop, right
from hcsr04 import calculate_right_distance, calculate_left_distance
from obstacle_avoiding import obstacle_avoidence
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
@app.route("/")
def index():
    return 'Engine has started'
    
@app.route("/<deviceName>/<action>", methods=['GET'])
def action(deviceName, action):
    if deviceName == 'manual':
        if action == 'forward':
                    forward()
        elif action == 'backward':
                    backward()
        elif action == 'right':
                    right()
        elif action == 'left':
                    left()
        elif action == 'stop':
                    stop()
    elif deviceName == 'auto':
        myFile = open("myFile1.txt", "w")
        myFile.write(action)
        myFile.close()
        obstacle_avoidence()
    else:
        return 'is Confused'
    return 'everything is AWESOME!'
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)