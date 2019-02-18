library(dplyr)
library(anytime)

dataString = "D:/Bulk/Uni/GitRepos/senviro/metrics/sosMetrics.csv"

data = read.csv(dataString, header = TRUE)

data$ID <- seq.int(nrow(data))
time = anytime(as.factor(data$timestamp))
cpu = data$cpu_Percent
memory = data$memory
memoryPercent = data$memoryPercent*100
networkRX = data$networkRX
networkTX = data$networkTX
rxTotal = data$rxTotal
txTotal = data$txTotal

par(mfrow=c(2,2))
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_cpu.png", width = 600, height = 500)
plot(data$ID,cpu, type="l", xlab="Request Count", ylab="CPU usage [%]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_memory.png", width = 600, height = 500)
plot(data$ID,memoryPercent, type="l", xlab="Request Count", ylab="Memory usage [%]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_rx.png", width = 600, height = 500)
plot(data$ID,networkRX, type="l", xlab="Request Count", ylab="Received data [bytes]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_tx.png", width = 600, height = 500)
plot(data$ID,networkTX, type="l",xlab="Request Count", ylab="Transmitted data [bytes]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_rxTot.png", width = 600, height = 500)
plot(data$ID,rxTotal, type="l",xlab="Request Count", ylab="Transmitted data [bytes]")
dev.off()
png("D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/output/1000_txTot.png", width = 600, height = 500)
plot(data$ID,txTotal, type="l",xlab="Request Count", ylab="Transmitted data [bytes]")
dev.off()

