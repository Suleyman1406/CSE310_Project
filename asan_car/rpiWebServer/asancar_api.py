import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
@app.route("/")
def index():
    return 'Engine has started'
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'manual':
        if action == 'forward':
                    actuator = 'going forward'
        elif action == 'backward':
                    actuator = 'going backward'
        elif action == 'right':
                    actuator = 'going right'
        elif action == 'left':
                    actuator = 'going left'
    elif deviceName == 'auto':
        actuator = 'Obstacle avoiding'
    else:
        actuator = 'is confused'
    return actuator
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)