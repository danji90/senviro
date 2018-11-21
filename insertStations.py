import requests
import json
import sys

# Data
with open('things.json') as json_data:
    thingsData = json.load(json_data)

with open('test.json') as json_data:
    dataStreamsData = json.load(json_data)


# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8082/FROST-Server/v1.0"

def insertThing(dataArray):
    url = baseUrl + '/' + 'Things'
    # Create array with present sensors
    things = requests.get(url).json()
    presentThings = []
    for thing in things['value']:
        presentThings.append(thing['name'])
    print("Things present :", presentThings)

    # Insert sensors if they are not already present
    for i in dataArray:
        if i["name"] not in presentThings:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Thing: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )

    # While loop attempt (still gives list index out of range error, but works)
    # i = 0
    # while (dataArray[i]["name"] not in sens) and (i < len(dataArray)):
    #     print(i)
    #     print(dataArray[i])
    #     try:
    #         req = requests.post(url, json = dataArray[i])
    #         req.raise_for_status()
    #         print(req, "#### Sensor: ", dataArray[i]["name"], " inserted")
    #     except:
    #         print(req, "####", "Could not insert ", dataArray[i]["name"] )
    #     i += 1

def insertDatastream(dataArray):
    # Create array with present observed properties
    url = baseUrl + '/' + 'Datastreams'
    datastreams = requests.get(url).json()
    presentStreams = []
    for stream in datastreams['value']:
        presentStreams.append(stream['name'])
    print("Datastreams present :", presentStreams)

    for i in dataArray:
        if i["name"] not in presentStreams:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Datastream: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )


insertDatastream(dataStreamsData)
