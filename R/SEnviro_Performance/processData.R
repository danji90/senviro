library(dplyr)

files <- list.files(path="./Raw", pattern="*.jmx", full.names=TRUE, recursive=FALSE)

final = data.frame(matrix(ncol = 7, nrow = 0))

lapply(files, function(data) {
  query = tools::file_path_sans_ext(data)
  
  data = read.csv(data, header = TRUE)
  
  cpu = dplyr::filter(data, grepl('CPU', label))
  
  memory = dplyr::filter(data, grepl('Memory', label))
  
  network = dplyr::filter(data, grepl('Network', label))
  
  disk = dplyr::filter(data, grepl('Disk', label))
  
  new = data.frame(ID = seq.int(nrow(cpu)), cpu$timeStamp,cpu$elapsed/1000, memory$elapsed/1000, network$elapsed/1000, disk$elapsed/1000)
  new = cbind(rep(query, nrow(new)), new)
  # assign('final',final,envir=.GlobalEnv)
  final <<- rbind(final,new)
})

colnames(final)=c("Query", "Timestep", "Time", "CPU", "Memory", "Network", "Disk")

plot(final$Timestep,final$CPU, type="l")

write.csv(final, file = "metrics.csv",row.names=FALSE, col.names=TRUE, sep=",")



