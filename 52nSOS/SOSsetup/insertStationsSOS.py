import requests
import json
import sys
import ast

# Data
with open('sensorsSOS.json') as json_data:
    sensors = json.load(json_data)


# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8084/52n-sos-webapp/service"

def insertSensor(dataArray):
    # Insert sensors if they are not already present
    for i in dataArray:
        try:
            req = requests.post(baseUrl, json = i)
            msg = ast.literal_eval(req.content.decode('utf-8'))
            req.raise_for_status()
            print(req, "#### Thing inserted: ", msg)
        except:
            err = ast.literal_eval(req.content.decode('utf-8'))
            print(req, "####", "Could not insert thing! Error: ", err)

insertSensor(sensors)
