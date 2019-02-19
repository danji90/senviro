library(dplyr)
library(anytime)

sosString = "D:/Bulk/Uni/GitRepos/senviro/metrics/sosMetrics.csv"
frostString = "D:/Bulk/Uni/GitRepos/senviro/metrics/frostMetrics.csv"

sosData = read.csv(dataString, header = TRUE)

data$ID <- seq.int(nrow(data))
time = as.POSIXlt(data$timestamp, "CET", "%Y-%m-%dT%H:%M:%S")
hms = as.POSIXct(format(time, format = "%H:%M:%S"), format = "%H:%M:%S")
cpu = data$cpu_Percent
memory = data$memory
memoryPercent = data$memoryPercent*100
networkRX = data$networkRX/1000
networkTX = data$networkTX/1000
rxTotal = data$rxTotal/1000
txTotal = data$txTotal/1000

png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_cpu.png", width = 600, height = 500)
plot(data$ID,cpu, type="l", xlab="Seconds", ylab="CPU usage [%]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_memory.png", width = 600, height = 500)
plot(data$ID,memoryPercent, type="l", xlab="Seconds", ylab="Memory usage [%]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_rx.png", width = 600, height = 500)
plot(data$ID,networkRX, type="l", xlab="Seconds", ylab="Received inflow [kilobytes]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_tx.png", width = 600, height = 500)
plot(data$ID,networkTX, type="l",xlab="Seconds", ylab="Transmitted outflow [kilobytes]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_rxTot.png", width = 600, height = 500)
plot(data$ID,rxTotal, type="l",xlab="Seconds", ylab="Received data [kilobytes]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_txTot.png", width = 600, height = 500)
plot(data$ID,txTotal, type="l",xlab="Seconds", ylab="Transmitted data [kilobytes]")
dev.off()

