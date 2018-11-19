import requests
import json
import sys

# Data
sensorData = [{"description":"Photon WeatherShield Atmospheric Sensors","name":"PhotonWeatherShield", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"},{"description":"Measures wind speed and direction","name":"Anemometer", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"},{"description":"Measures soil moisture","name":"SoilMoistureSensor", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"},{"description":"Measures soil temperature","name":"DS18B20", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"}, {"description":"Measures rainfall","name":"Pluviometer", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"}, {"description":"Battery Readings","name":"Battery", "encodingType":"text/plan","metadata":"http://www.senviro.uji.es"}]

obsPropData = [{"name":"AirTemperature","definition":"http://www.senviro.uji.es","description":"Air temperature readings in °C"},{"name":"Humidity","definition":"http://www.senviro.uji.es","description":"Relative air humidity readings in %"},{"name":"AtmosphericPressure","definition":"http://www.senviro.uji.es","description":"Atmospheric pressure readings in Pascal"},{"name":"Precipitation","definition":"http://www.senviro.uji.es","description":"Precipitation readings in mm"},{"name":"WindDirection","definition":"http://www.senviro.uji.es","description":"Wind direction in integer values (0-7)"},{"name":"WindSpeed","definition":"http://www.senviro.uji.es","description":"Wind speed readings in m/s"},{"name":"SoilTemperature","definition":"http://www.senviro.uji.es","description":"Soil temperature readings in °C"},{"name":"SoilHumidity","definition":"http://www.senviro.uji.es","description":"Soil moisture readings in m^3/m^3"},{"name":"Battery","definition":"http://www.senviro.uji.es","description":"Battery readings in %"}]

# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8082/FROST-Server/v1.0"

def insertSensors(dataArray):
    url = baseUrl + '/' + 'Sensors'
    # Create array with present sensors
    sensors = requests.get(url).json()
    sens = []
    for sen in sensors['value']:
        sens.append(sen['name'])
    print("Sensors present :", sens)

    # Insert sensors if they are not already present
    for i in dataArray:
        if i["name"] not in sens:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Sensor: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )

def insertObsProp(dataArray):
    # Create array with present observed properties
    url = baseUrl + '/' + 'ObservedProperties'
    obsProp = requests.get(url).json()
    props = []
    for prop in obsProp['value']:
        props.append(prop['name'])
    print("Observed properties present :", props)

    for i in dataArray:
        if i["name"] not in props:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Observed Properties: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )

def insertObsProp(dataArray):
    # Create array with present observed properties
    url = baseUrl + '/' + 'ObservedProperties'
    obsProp = requests.get(url).json()
    props = []
    for prop in obsProp['value']:
        props.append(prop['name'])
    print("Observed properties present :", props)

    for i in dataArray:
        if i["name"] not in props:
            try:
                req = requests.post(url, json = i)
                req.raise_for_status()
                print(req, "#### Observed Properties: ", i["name"], " inserted")
            except:
                print(req, "####", "Could not insert ", i["name"] )


insertSensors(sensorData)
insertObsProp(obsPropData)
