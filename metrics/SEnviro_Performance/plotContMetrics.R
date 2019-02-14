library(dplyr)
library(anytime)

dataString = "D:/Bulk/Uni/GitRepos/senviro/metrics/sos_1000_.csv"

data = read.csv(dataString, header = TRUE)

time = anytime(as.factor(data$timestamp))
cpu = data$cpu_Percent
memory = data$memory
memoryPercent = data$memoryPercent
networkRX = data$networkRX
networkTX = data$networkTX

par(mfrow=c(2,2))
plot(time,cpu, type="l", xlab="Time [minutes past the hour]", ylab="CPU usage [%]")
plot(time,memoryPercent, type="l", xlab="Time [minutes past the hour]", ylab="Memory usage [%]")
plot(time,networkRX, type="l", xlab="Time [minutes past the hour]", ylab="Received data [bytes]")
plot(time,networkTX, type="l",xlab="Time [minutes past the hour]", ylab="Transmitted data [bytes]")

