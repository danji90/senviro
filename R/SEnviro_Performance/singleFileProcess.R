final = data.frame(matrix(ncol = 7, nrow = 0))

dataString = "./Raw/frost_100_.jmx"

data = read.csv(dataString, header = TRUE)

query = tools::file_path_sans_ext(dataString)

cpu = dplyr::filter(data, grepl('CPU', label))

memory = dplyr::filter(data, grepl('Memory', label))

network = dplyr::filter(data, grepl('Network', label))

disk = dplyr::filter(data, grepl('Disk', label))

new = data.frame(ID = seq.int(nrow(cpu)), cpu$timeStamp,cpu$elapsed/1000, memory$elapsed/100, network$elapsed/1000, disk$elapsed/1000)
new = cbind(rep(query, nrow(new)), new)

final <<- rbind(final,new)

colnames(final)=c("Query", "Timestep", "Time", "CPU", "Memory", "Network", "Disk")

plot(final$Time,final$Disk, type="l")

