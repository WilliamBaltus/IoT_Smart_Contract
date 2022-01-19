#!/usr/bin/env python3
#Written: 11/12/21
#Author: Grace Miguel + William Baltus
#Description:This code establishes connection with a firestore database.
#            and pushes freshly collected sensor data to the firebase database. 
#            This data is utilized in different scripts such as for data visualization.
#Updated: 12/4/21
#            Script now provides functions to pull latest data, get and update manual setting of greenhouse,
#            and get all documents within given collection. This will get updated!

import firebase_admin
from firebase_admin import credentials, firestore
from time import strftime
from os import environ
from dotenv import load_dotenv
#---------------------------------------------------------------------------------------------------------------------
load_dotenv()

tester = 123

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
#----------------------------------------------------------------------------------------------------------------------

#Connect's to firebase. Access's collection that contains date and time of latest data and retrieves
#Use that data (latest data), to access the collection which houses the latest data
def pullFirebase():
    dataDict = {}
    doc_ref = firebase.collection('latestData').document('JonCucciLikesMen')
    latestData = doc_ref.get().to_dict()
    date = latestData['date']
    timestamp = latestData['timestamp']
    data_ref = firebase.collection(date).document(timestamp)
    dataDict = data_ref.get().to_dict()

    #dictionary returns:  {'Pressure': 1028.6, 'Date and Time': '12/04/21 at 04:32:21PM', 'Humidity': 39.71, 'Temperature': 75.02}
    return dataDict

#used to get the latest data and whether or not user has set greenhouse to manual mode or not
def getManualMode():
    doc_ref = firebase.collection('latestData').document('JonCucciLikesMen')
    latestData = doc_ref.get().to_dict()
    manualMode= latestData['manualMode']
    return manualMode

#used to update manual mode setting
def updateManualMode(toggle):
    doc_ref = firebase.collection('latestData').document('JonCucciLikesMen')
    doc_ref.update({u'manualMode': toggle})
    return

#takes in date in the form of MM-DD-YY, returns all documents in given collection if exists
def getAllDocuments(date):
    doc_ref = firebase.collection(date)
    documents = doc_ref.stream()
    return documents

def testConnection():
    doc_ref = firebase.collection('Connection Test').document('test')
    currentValue = doc_ref.get().to_dict()
    print("Previous Value: " + str(currentValue['test']))
    newValue = currentValue['test'] + 1
    doc_ref.update({u'test': newValue})
    currentValue = doc_ref.get().to_dict()
    print("New Value: " + str(currentValue['test']))

if __name__ == "__main__":
    print("Testing connection...") 
    testConnection()
    print("Pulling latest data...")
    print(pullFirebase())
    
