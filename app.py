#Created: 11/17/21
#Updated: 12/5/21
#Author:  William Baltus
#This script is a very basic API. It connects to a raspberry pi, pulls temperature sensor data,
#which is collected separately and stored in a firebase database
#Populates dictionary, jsonify's string, and returns string. 
#Route is programmed to handle GET requests


from flask import Flask, jsonify
from time import sleep
import firebase_admin
from firebase_admin import credentials, firestore


app = Flask(__name__)

if not firebase_admin._apps:
    cred = credentials.Certificate(r"iot_smart_contract.json")
    firebase_admin.initialize_app(cred)

firebase= firestore.client()

@app.route('/', methods=['GET'])
def hello_world():
    data_ref = firebase.collection('12-05-21').document('08:00:08AM')
    dataDict = data_ref.get().to_dict()
    temp = dataDict['Temperature']
    return jsonify({'Device': 'Raspberry Pi',
                    'Temperature': temp })

if __name__ == '__main__':  
    app.run() 