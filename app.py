#Created: 11/17/21
#Updated: 12/5/21
#Author:  William Baltus
#This script is a very basic API. It connects to a raspberry pi, pulls temperature sensor data,
#which is collected separately and stored in a firebase database
#Populates dictionary, jsonify's string, and returns string. 
#Route is programmed to handle GET requests


from flask import Flask, render_template
from functions.firebaseHelper import pullFirebase
import time
from turbo_flask import Turbo
import threading
import sys

app = Flask(__name__)
turbo = Turbo(app)

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

@app.context_processor
def inject_load():
    
    latestData = pullFirebase()
    temp = str(latestData['Temperature']) + " F"
    humidity = str(latestData['Humidity']) + "%"
    pressure = str(latestData['Pressure']) + "HPa"
    return {
        'Temperature': temp,
        'Humidity': humidity,
        'Pressure': pressure,
        'Date': time.strftime("%m/%d/%y"),
        'Timestamp': time.strftime("at %I:%M:%S%p"),
        }

def update_load():
    with app.app_context():
        while True:
            time.sleep(10)
            turbo.push(turbo.replace(render_template('latestData.html'), 'latestData'))

@app.route('/', methods = ['POST', 'GET'])
def index():
    #get data from firebase to load onto index page
    latestData = pullFirebase()
    temp = str(latestData['Temperature']) + " F"
    humidity = str(latestData['Humidity']) + "%"
    pressure = str(latestData['Pressure']) + "HPa"
    templateData = {
                    'Temperature': temp,
                    'Humidity': humidity,
                    'Pressure': pressure,
                    'Date': time.strftime("%m/%d/%y"),
                    'Timestamp': time.strftime("at %I:%M:%S%p"),
                    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':  
    app.run() 
