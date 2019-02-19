import requests
import json
import csv
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

refreshInterval = 1 #seconds

scheduler = BackgroundScheduler()
scheduler.start()

app_preCPU_total = 0.0
app_preCPU_system = 0.0
db_preCPU_total = 0.0
db_preCPU_system = 0.0
appCPU = 0.0
dbCPU = 0.0
cpuFinal = 0.0
appPreMemory = 0.0
dbPreMemory = 0.0
preNetworkRX = 0.0
preNetworkTX = 0.0


def extractData():

    global preMemory
    global preNetworkRX
    global preNetworkTX
    global cpuFinal
    global appMemory
    global dbMemory

    print("Getting data at ", datetime.datetime.now())
    # resp = requests.get(frost_url).json()
    appResp = requests.get("http://elcano.init.uji.es:8087/api/v2.0/stats/docker/b3a38f225eb5d106064e7f051565527e5d21aea9c697af33bd9701903ac1c06e?count=1").json()
    dbResp = requests.get("http://elcano.init.uji.es:8087/api/v2.0/stats/docker/0f5d9725ef7e0672a6eed50db2fafc247f7080b0c3ed331727bfd976871feb72?count=1").json()
    new = []

    appStats = appResp["/docker/b3a38f225eb5d106064e7f051565527e5d21aea9c697af33bd9701903ac1c06e"][0]
    dbStats = dbResp["/docker/0f5d9725ef7e0672a6eed50db2fafc247f7080b0c3ed331727bfd976871feb72"][0]

    def appCpuCalc(data):

        global app_preCPU_total
        global app_preCPU_system
        global appCPU

        cpuDelta = data["cpu"]["usage"]["total"] - app_preCPU_total
        systemDelta = data["cpu"]["usage"]["system"] - app_preCPU_system

        if  systemDelta > 0.0:
            appCPU = cpuDelta / systemDelta

        app_preCPU_total = data["cpu"]["usage"]["total"]
        app_preCPU_system = data["cpu"]["usage"]["system"]

        return appCPU

    def dbCpuCalc(data):

        global db_preCPU_total
        global db_preCPU_system
        global dbCPU

        cpuDelta = data["cpu"]["usage"]["total"] - db_preCPU_total
        systemDelta = data["cpu"]["usage"]["system"] - db_preCPU_system

        if  systemDelta > 0.0:
            dbCPU = cpuDelta / systemDelta

        db_preCPU_total = data["cpu"]["usage"]["total"]
        db_preCPU_system = data["cpu"]["usage"]["system"]

        return dbCPU

    memoryFinal = appStats["memory"]["usage"] + dbStats["memory"]["usage"]


    cpuFinal = appCpuCalc(appStats)+dbCpuCalc(dbStats)

    netWorkRXDelta = appStats["network"]["interfaces"][0]["rx_bytes"] - preNetworkRX
    netWorkTXDelta = appStats["network"]["interfaces"][0]["tx_bytes"] - preNetworkTX

    value = {"timestamp":appStats["timestamp"], "cpu_Percent":cpuFinal,"memory":memoryFinal, "memoryPercent":memoryFinal/2088427847.68, "networkRX":netWorkRXDelta, "networkTX":netWorkTXDelta, "rxTotal":appStats["network"]["interfaces"][0]["rx_bytes"],"txTotal":appStats["network"]["interfaces"][0]["tx_bytes"]}
    new.append(value)

    with open("sosMetrics.csv", "a") as f:
        w = csv.DictWriter(f,new[0].keys())
        w.writerows(new)

    print("App CPU: ", appCPU, "DB_CPU: ", dbCPU)
    print("Value extracted")

    # preCPU_total = appStats["cpu"]["usage"]["total"]
    # preCPU_system = appStats["cpu"]["usage"]["system"]
    preMemory = appStats["memory"]["usage"]
    preNetworkRX = appStats["network"]["interfaces"][0]["rx_bytes"]
    preNetworkTX = appStats["network"]["interfaces"][0]["tx_bytes"]

def main():
    headers = ["timestamp","cpu_Percent","memory","memoryPercent","networkRX","networkTX","rxTotal","txTotal"]
    with open("sosMetrics.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(headers)
    scheduler.add_job(extractData, 'interval', seconds = refreshInterval)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
