import requests
import json
import sys

# Data
with open('things.json') as json_data:
    thingsData = json.load(json_data)

with open('dataStreams.json') as json_data:
    dataStreamsData = json.load(json_data)


# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8084/52n-sos-webapp/service"

def insertProcedure(dataArray):
    # url = baseUrl + '/' + 'Things'
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

# def insertDatastream(dataArray):
#     # Create array with present observed properties
#     url = baseUrl + '/' + 'Datastreams'
#     datastreams = requests.get(url+ '?$select=name').json()
#     presentStreams = []
#     for stream in datastreams['value']:
#         presentStreams.append(stream['name'])
#     print("Datastreams present :", presentStreams)
#
#     for i in dataArray:
#         if i["name"] not in presentStreams:
#             try:
#                 req = requests.post(url, json = i)
#                 req.raise_for_status()
#                 print(req, "#### Datastream: ", i["name"], " inserted")
#             except:
#                 print(req, "####", "Could not insert ", i["name"] )
#
#
# insertThing(thingsData)
# insertDatastream(dataStreamsData)
