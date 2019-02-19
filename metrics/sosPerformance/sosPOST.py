import requests
import json
import sys
import ast
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

with open('sos1000.json') as json_data:
    postFile = json.load(json_data)

refreshInterval = 1 #seconds

scheduler = BackgroundScheduler()
scheduler.start()

# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8084/52n-sos-webapp/service"

def getObservation():
    global postFile

    try:
        resp = requests.post(baseUrl, json = postFile)
        # msg = ast.literal_eval(resp.content.decode('utf-8'))
        # resp.raise_for_status()
        print("#### Request posted at ", datetime.datetime.now())

        json_data = json.loads(resp.text)

        with open("output.json", "a") as f:
            json.dump(json_data, f)
            f.write("\n")


    except:
        err = ast.literal_eval(resp.content.decode('utf-8'))
        print(resp, "####", "Could not get observations! Error: ", err)


# getObservation()

def main():

    start = time.time()
    runtime = 180 # 3min
    scheduler.add_job(getObservation, 'interval', seconds = refreshInterval)
    while True:
        time.sleep(1)
        if time.time() > start + runtime : break


if __name__ == "__main__":
    main()
