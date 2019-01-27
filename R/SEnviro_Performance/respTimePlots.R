library(ggplot2)

# General Data
observations = c(rep(c(1,100,200,400,500,600,800,1000),4))
webService = c(rep("52N-SOS",8), rep("52N-SOS Helgoland",8), rep("FROST",8), rep("FROST (compressed)",8))

# Response Times Data
time_sos = c(260,161,168,201,236,203,280,324)
time_helgoSOS = c(138,180,211,208,199,235,401,294)
time_frost = c(185,251,238,285,336,436,381,410)
time_frostMin = c()

timesPlain = c(time_sos,time_frost)
timesMin = c(time_helgoSOS,time_frostMin)
times = c(timesPlain,timesMin)
  
respTimePlain = data.frame(webService,observations,timesPlain)
respTimesMin = data.frame(webService,observations,timesMin)
respTime = data.frame(webService,observations,times)




# Response Size Data
size_sos = c(0.566,2.54,4.38,8.1,454.23,545.02,726.61,908.19)
size_helgoSOS = c(0.34,2.56,4.8,9.29,11.54,13.79,18.28,22.77)
size_frost = c(0.717,49.9,99.42,198.39,247.87,297.37,396.34,495.31)
size_frostMin = c(0.567,8.55,16.64,32.8,40.88,48.96,65.12,81.28)

sizesPlain = c(size_sos,size_frost)
sizesMin = c(size_helgoSOS,size_frostMin)
sizes = c(sizesPlain,sizesMin)

respSize = data.frame(webService,observations,sizes)


# Plots

# Response Time
ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/imagesrespTimePlot.png", ggplot(data=respTime,aes(x=observations, y=times, group=webService)) + geom_line(aes(linetype=webService)) + geom_point(aes(shape=webService)) + scale_x_continuous(breaks = obsCount) + labs(x='Observations', y='Milliseconds [ms]'), width = 8, height = 4, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/imagesrespSizePlot.png", ggplot(data=respSize,aes(x=observations, y=sizes, group=webService)) + geom_line(aes(linetype=webService)) + geom_point(aes(shape=webService)) + scale_x_continuous(breaks = obsCount) + labs(x='Observations', y='Kilobytes [kb]') , width = 8, height = 4, dpi = 300, units = "in", device='png')

resSizePlot
