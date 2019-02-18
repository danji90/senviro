filePath = "D:/Bulk/Uni/GitRepos/senviro/metrics/frost_1000_.csv"

dat = read.csv(filePath, header = TRUE)

cpuAvg = mean(dat$cpu_Percent)
memory = mean(dat$memory)
memoryAvg = mean(dat$memoryPercent)
rxAvg = mean(dat$networkRX)
txAvg = mean(dat$networkTX)


cpuAvg
memory
memoryAvg
rxAvg
txAvg



