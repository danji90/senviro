import requests
import json
import csv
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

frost_url = "http://elcano.init.uji.es:8087/api/v1.0/containers/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a"

refreshInterval = 90 #seconds

scheduler = BackgroundScheduler()
scheduler.start()

preCPU_total = 0.0
preCPU_system = 0.0
# preMemoryUsage = 0.0
memoryLimit = 0.0



def firstExtract():

    global preCPU_total
    global preCPU_system
    global memoryLimit

    print("Getting data at ", datetime.datetime.now())
    # resp = requests.get(frost_url).json()
    resp = requests.get("http://elcano.init.uji.es:8087/api/v1.0/containers/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a").json()
    new = []

    preCPU_total = resp["stats"][0]["cpu"]["usage"]["total"]
    preCPU_system = resp["stats"][0]["cpu"]["usage"]["system"]
    # preMemory_usage = resp["stats"][0]["memory"]["usage"]
    memoryLimit = resp["spec"]["memory"]["limit"]

    for item in resp["stats"][1:59]:
        cpuDelta = item["cpu"]["usage"]["total"] - preCPU_total
        systemDelta = item["cpu"]["usage"]["system"] - preCPU_system
        memoryUsage = item["memory"]["usage"]


        if systemDelta > 0.0 and cpuDelta > 0.0:
            value = {"timestamp":item["timestamp"], "cpu_usage":(cpuDelta / systemDelta),"memory":memoryUsage/memoryLimit}
            new.append(value)

        preCPU_total = item["cpu"]["usage"]["total"]
        preCPU_system = item["cpu"]["usage"]["system"]
        memoryUsage = item["memory"]["usage"]

        print("cpuDelta: ", cpuDelta, "systemDelta: ", systemDelta, "memoryUsage: ", memoryUsage)

    with open("metrics.csv", "w") as f:
        w = csv.DictWriter(f,new[0].keys())
        w.writeheader()
        w.writerows(new)

def extractData():
    global preCPU_total
    global preCPU_system

    print("Getting data at ", datetime.datetime.now())
    # resp = requests.get(frost_url).json()
    resp = requests.get("http://elcano.init.uji.es:8087/api/v1.0/containers/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a").json()
    new = []

    # preCPU_total = resp["stats"][0]["cpu"]["usage"]["total"]
    # preCPU_system = resp["stats"][0]["cpu"]["usage"]["system"]
    memoryLimit = resp["spec"]["memory"]["limit"]

    for item in resp["stats"][1:59]:
        cpuDelta = item["cpu"]["usage"]["total"] - preCPU_total
        systemDelta = item["cpu"]["usage"]["system"] - preCPU_system
        memoryUsage = item["memory"]["usage"]


        if systemDelta > 0.0 and cpuDelta > 0.0:
            value = {"timestamp":item["timestamp"], "cpu_usage":(cpuDelta / systemDelta),"memory":(memoryUsage/memoryLimit)*100}
            new.append(value)

        preCPU_total = item["cpu"]["usage"]["total"]
        preCPU_system = item["cpu"]["usage"]["system"]
        memoryUsage = item["memory"]["usage"]

        print("cpuDelta: ", cpuDelta, "systemDelta: ", systemDelta, "memoryUsage: ", memoryUsage)

        with open("metrics.csv", "a") as f:
            w = csv.DictWriter(f,new[0].keys())
            w.writerows(new)

def main():
    firstExtract()
    scheduler.add_job(extractData, 'interval', seconds = refreshInterval)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
