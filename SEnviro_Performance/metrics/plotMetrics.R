library(dplyr)
library(anytime)

dataString = "D:/Bulk/Uni/GitRepos/senviro/SEnviro_Performance/metrics/metrics.csv"

data = read.csv(dataString, header = TRUE)

time = anytime(as.factor(data$timestamp))
cpu = data$cpu_Percent
memory = data$memory
memoryPercent = data$memoryPercent
networkRX = data$networkRX
networkTX = data$networkTX

par(mfrow=c(3,2))
plot(time,cpu, type="l")
plot(time,memory, type="l")
plot(time,memoryPercent, type="l")
plot(time,networkRX, type="l")
plot(time,networkTX, type="l")

