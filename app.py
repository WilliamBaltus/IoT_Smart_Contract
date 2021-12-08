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
import json


app = Flask(__name__)

deployed = os.environ.get('IS_HEROKU')
print(deployed)
if not firebase_admin._apps:
    if( int(deployed) < 1):
        print("RUNNING LOCAL, NOT HEROKU")
        cred = credentials.Certificate(r"iot_smart_contract.json")
    else:
        #create dictioanry containing environmental variables from heroku config vars

        private_key = str(os.environ['private_key'])
        #string is used for private key because json dumps would convert one backslash to two backslashes, making an invalid key.
        #thus this is used to remove extra '\' that is added by json.dumps function... soemhow this worked...
        stringDict = """{'private_key': """ + "'"+ private_key + "'" + "}"""
        stringDict = eval(stringDict)
        credentialsDict = { "type": os.environ['type'],
                            "project_id":os.environ['project_id'],
                            "private_key_id":os.environ['private_key_id'],
                            "private_key":os.environ['private_key'],
                            "client_email":os.environ['client_email'],
                            "client_id": os.environ['client_id'],
                            "auth_uri":os.environ['auth_uri'],
                            "token_uri":os.environ['token_uri'],
                            "auth_provider_x509_cert_url":os.environ['auth_provider_x509_cert_url'],
                            "client_x509_cert_url":os.environ['client_x509_cert_url']}
       
        #combine heroku environment variable dictionary with private key dictionary
        finalDict = {**credentialsDict,**stringDict}
        #convert to json string and write to file
        jsonDict = json.dumps(finalDict, indent = 2)
        #print(jsonDict)
        #create and write to json file
        with open("sample.json", "w") as outfile:
            outfile.write(jsonDict)

        #use json file as certificate to establish connection to firebase
        cred = credentials.Certificate(r"sample.json")

    
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