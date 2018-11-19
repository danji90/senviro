import requests
import json
import sys

# Data
sensorData = [{"description":"Photon WeatherShield Atmospheric Sensors","name":"PhotonWeatherShield", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"},{"description":"Measures wind speed and direction","name":"Anemometer", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"},{"description":"Measures soil moisture","name":"SoilMoistureSensor", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"},{"description":"Measures soil temperature","name":"DS18B20", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"}, {"description":"Measures rainfall","name":"Pluviometer", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"}, {"description":"Battery Readings","name":"Battery", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"}]


# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8082/FROST-Server/v1.0"

def insertSensors(dataArray):
    # Create array with present sensors
    sensors = requests.get(baseUrl + '/' + 'Sensors').json()
    sens = []
    for sen in sensors['value']:
        sens.append(sen['name'])
    print("Sensors present :", sens)

    # Insert sensors if they are not already present
    for i in sensorData:
        if i["name"] not in sens:
            a = requests.post(baseUrl + '/' + 'Sensors', json = i)
            print(i["name"], " inserted")

insertSensors(sensorData)
