filePath = "D:/Bulk/Uni/GitRepos/senviro/metrics/sos_1000_.csv"

dat = read.csv(filePath, header = TRUE)

cpuAvg = mean(dat$cpu_Percent)
memoryAvg = mean(dat$memoryPercent)
rxAvg = mean(dat$networkRX)
txAvg = mean(dat$networkTX)

cpuAvg
memoryAvg
rxAvg
txAvg



