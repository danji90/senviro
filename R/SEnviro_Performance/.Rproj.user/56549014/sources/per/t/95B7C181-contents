frost1000 = read.csv("RAW/FROST_1000.csv", header = TRUE)

frost1000CPU = dplyr::filter(frost1000, grepl('CPU', label))
plot(FROST1000CPU$timeStamp,FROST1000CPU$elapsed, type = "l")


frost1000memory = dplyr::filter(frost1000, grepl('Memory', label))
plot(frost1000memory$timeStamp,frost1000memory$elapsed, type = "l")


frost1000network = dplyr::filter(frost1000, grepl('Network', label))
plot(frost1000network$timeStamp,frost1000network$elapsed, type = "l")


frost1000disk = dplyr::filter(frost1000, grepl('Disk', label))
plot(frost1000disk$timeStamp,frost1000disk$elapsed, type = "l")


frost1000final = data.frame(frost1000CPU$timeStamp,frost1000CPU$elapsed, frost1000memory$elapsed, frost1000network$elapsed, frost1000disk$elapsed)
