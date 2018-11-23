import requests
import json
import sys

# Data
with open('sensors.json') as json_data:
    sensorData = json.load(json_data)

with open('observedProperties.json') as json_data:
    obsPropData = json.load(json_data)

# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8082/FROST-Server/v1.0"

def insertSensor(dataArray):
    url = baseUrl + '/' + 'Sensors'
    # Create array with present sensors
    sensors = requests.get(url+ '?$select=name').json()
    presentSensors = []
    for sen in sensors['value']:
        presentSensors.append(sen['name'])
    print("Sensors present :", presentSensors)

    # Insert sensors if they are not already present
    for i in dataArray:
        if i["name"] not in presentSensors:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Sensor: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )


def insertObsProp(dataArray):
    # Create array with present observed properties
    url = baseUrl + '/' + 'ObservedProperties'
    obsProp = requests.get(url + '?$select=name').json()
    presentProps = []
    for prop in obsProp['value']:
        presentProps.append(prop['name'])
    print("Observed properties present :", presentProps)

    for i in dataArray:
        if i["name"] not in presentProps:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Observed Properties: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )


insertSensor(sensorData)
insertObsProp(obsPropData)
