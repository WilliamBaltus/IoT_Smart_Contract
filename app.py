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
import os


app = Flask(__name__)

if not firebase_admin._apps:
    credentialsDict = {"type": os.environ['type'],
                        "project_id":os.environ['project_id'],
                        "private_key_id":os.environ['private_key_id'],
                        "private_key":os.environ['private_key'],
                        "client_email":os.environ['client_email'],
                        "client_id": os.environ['client_id'],
                        "auth_uri":os.environ['auth_uri'],
                        "token_uri":os.environ['token_uri'],
                        "auth_provider_x509_cert_url":os.environ['auth_provider_x509_cert_url'],
                        "client_x509_cert_url":os.environ['client_x509_cert_url']
    }
    cred = credentials.Certificate(credentialsDict)
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