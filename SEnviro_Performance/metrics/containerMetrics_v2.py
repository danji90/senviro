import requests
import json
import csv
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

frost_url = "http://elcano.init.uji.es:8087/api/v1.0/containers/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a"

refreshInterval = 1 #seconds

scheduler = BackgroundScheduler()
scheduler.start()

preCPU_total = 0.0
preCPU_system = 0.0
preMemory = 0.0
preNetwork = 0.0
# memoryLimit = 0.0

def firstExtract():

    global preCPU_total
    global preCPU_system
    global preMemory

    print("Getting data at ", datetime.datetime.now())
    # resp = requests.get(frost_url).json()
    resp = requests.get("http://elcano.init.uji.es:8087/api/v2.0/stats/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a?count=1").json()
    new = []

    stats = resp["/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a"][0]

    cpuDelta = stats["cpu"]["usage"]["total"] - preCPU_total
    systemDelta = stats["cpu"]["usage"]["system"] - preCPU_system
    # memoryDelta = stats["memory"]["usage"] - preMemory

    if systemDelta > 0.0 and cpuDelta > 0.0:
        value = {"timestamp":stats["timestamp"], "cpu_Percent":(cpuDelta / systemDelta),"memory":stats["memory"]["usage"], "memoryPercent":(stats["memory"]["usage"])/2088427847.68, "networkRX":stats["network"]["interfaces"][0]["rx_bytes"], "networkTX":stats["network"]["interfaces"][0]["tx_bytes"]}
        new.append(value)

        with open("metrics.csv", "w") as f:
            w = csv.DictWriter(f,new[0].keys())
            w.writeheader()
            w.writerows(new)

    print(new)

    preCPU_total = stats["cpu"]["usage"]["total"]
    preCPU_system = stats["cpu"]["usage"]["system"]
    preMemory = stats["memory"]["usage"]


def extractData():

    global preCPU_total
    global preCPU_system
    global preMemory

    print("Getting data at ", datetime.datetime.now())
    # resp = requests.get(frost_url).json()
    resp = requests.get("http://elcano.init.uji.es:8087/api/v2.0/stats/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a?count=1").json()
    new = []

    stats = resp["/docker/770a8312ed0381458f375459e1ebe447866bd5677bbd8267f4acf5aa12655d2a"][0]

    cpuDelta = stats["cpu"]["usage"]["total"] - preCPU_total
    systemDelta = stats["cpu"]["usage"]["system"] - preCPU_system
    # memoryDelta = stats["memory"]["usage"] - preMemory

    if systemDelta > 0.0 and cpuDelta > 0.0:
        value = {"timestamp":stats["timestamp"], "cpu_Percent":(cpuDelta / systemDelta),"memory":stats["memory"]["usage"], "memoryPercent":(stats["memory"]["usage"])/2088427847.68, "networkRX":stats["network"]["interfaces"][0]["rx_bytes"], "networkTX":stats["network"]["interfaces"][0]["tx_bytes"]}
        new.append(value)

        with open("metrics.csv", "a") as f:
            w = csv.DictWriter(f,new[0].keys())
            w.writerows(new)

    print(new)

    preCPU_total = stats["cpu"]["usage"]["total"]
    preCPU_system = stats["cpu"]["usage"]["system"]
    preMemory = stats["memory"]["usage"]

def main():
    firstExtract()
    scheduler.add_job(extractData, 'interval', seconds = refreshInterval)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
