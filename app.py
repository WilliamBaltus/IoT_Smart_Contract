#Created: 11/17/21
#Updated: 12/5/21
#Author:  William Baltus
#This script is a very basic API. It connects to a raspberry pi, pulls temperature sensor data,
#which is collected separately and stored in a firebase database
#Populates dictionary, jsonify's string, and returns string. 
#Route is programmed to handle GET requests


from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from os import environ
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)

deployed = environ.get('IS_HEROKU')
print(deployed)
if not firebase_admin._apps:
    if( int(deployed) < 1):
        print("RUNNING LOCAL, NOT HEROKU")
        cred = credentials.Certificate(r"iot_smart_contract.json")
        firebase_admin.initialize_app(cred)
    else:
        #create dictioanry containing environmental variables from heroku config vars
        print("RUNNING HEROKU, NOT LOCAL")
        credentialsDict = { "type": environ['FIREBASE_TYPE'],
                            "project_id":environ['FIREBASE_PROJECT_ID'],
                            "private_key_id":environ['FIREBASE_PRIVATE_KEY_ID'],
                            "private_key":environ['FIREBASE_PRIVATE_KEY'].replace("\\n", "\n"),
                            "client_email":environ['FIREBASE_CLIENT_ID'],
                            "client_id": environ['FIREBASE_CLIENT_ID'],
                            "auth_uri":environ['FIREBASE_AUTH_URI'],
                            "token_uri":environ['FIREBASE_TOKEN_URI'],
                            "auth_provider_x509_cert_url":environ['FIREBASE_AUTH_PROVIDER_X509_CERT_URL'],
                            "client_x509_cert_url":environ['FIREBASE_CLIENT_X509_CERT_URL']}
                            
        #print("ENV KEYS:", credentialsDict)

        CREDENTIALS = credentials.Certificate(credentialsDict)
        firebase_admin.initialize_app(CREDENTIALS)
        

firebase= firestore.client()

@app.route('/', methods=['GET'])
def hello_world():
    data_ref = firebase.collection('12-05-21').document('08:00:08AM')
    dataDict = data_ref.get().to_dict()
    temp = dataDict['Temperature']
    temp = float(temp)
    return jsonify({'Device': 'Raspberry Pi',
                    'Temperature': temp })

if __name__ == '__main__':  
    app.run() 