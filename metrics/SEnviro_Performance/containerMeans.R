filePath = "D:/Bulk/Uni/GitRepos/senviro/metrics/sos_1000_.csv"

dat = read.csv(filePath, header = TRUE)

cpuAvg = mean(dat$cpu_Percent)
memory = mean(dat$memory)/1000000
memoryAvg = mean(dat$memoryPercent)
rxAvg = mean(dat$networkRX)
txAvg = mean(dat$networkTX)


cpuAvg
memory
max(dat$cpu_Percent)
min(dat$cpu_Percent)



