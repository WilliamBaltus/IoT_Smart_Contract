#Created: 11/17/21
#Updated: 12/5/21
#Author:  William Baltus
#This script is a very basic API. It connects to a raspberry pi, generates random number in place of sensor data
#Also shines LED to indicate functionality.
#Populates dictionary, jsonify's string, and returns string. 
#Route is programmed to handle GET requests


from flask import Flask, jsonify
app = Flask(__name__)
from gpiozero import LED
import random
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

#------------------GPIO AND DEVICE INITIALIZATION--------------------
#connect to Pi IP ADDRESS
factory = PiGPIOFactory(host = '155.246.137.109')
ledPin = 16
led = LED(ledPin, pin_factory= factory, initial_value=False)
#---------------------------------------------------------------------

@app.route('/', methods=['GET'])
def hello_world():
    led.blink()
    temp = random.randint(1,100)
    return jsonify({'Device': 'Raspberry Pi',
                    'Temperature': temp })

if __name__ == '__main__':
    app.run()
    sleep(1)
    led.close()