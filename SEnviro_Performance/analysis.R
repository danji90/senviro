library(ggplot2)

# General Data
observations = c(1,100,200,400,500,600,800,1000)
breakPointsExtre = c(1,100,200,300,400,500,600,700,800,900,1000)
webServices = c(rep("52N-SOS",8), rep("FROST",8), rep("52N-SOS Helgoland",8),  rep("FROST (compressed)",8))

# Response Times Data
time_sos = c(260,161,168,201,236,203,280,324)
time_helgoSOS = c(138,180,211,208,199,235,401,294)
time_frost = c(185,251,238,285,336,436,381,410)
time_frostMin = c(169,150,189,204,228,253,280,272)

timesPlain = c(time_sos,time_frost)
timesMin = c(time_helgoSOS,time_frostMin)
times = c(timesPlain,timesMin)

respTimePlain = data.frame(ws=webServices[c(1:16)],obs=rep(observations,2),t=timesPlain)
respTimesMin = data.frame(ws=webServices[c(17:32)],obs=rep(observations,2),t=timesMin)
respTime = data.frame(ws=webServices,obs=rep(observations,4),t=times)




# Response Size Data
size_sos = c(0.566,2.54,4.38,8.1,454.23,545.02,726.61,908.19)
size_helgoSOS = c(0.34,2.56,4.8,9.29,11.54,13.79,18.28,22.77)
size_frost = c(0.717,49.9,99.42,198.39,247.87,297.37,396.34,495.31)
size_frostMin = c(0.567,8.55,16.64,32.8,40.88,48.96,65.12,81.28)

sizesPlain = c(size_sos,size_frost)
sizesMin = c(size_helgoSOS,size_frostMin)
sizes = c(sizesPlain,sizesMin)

respTimePlain = data.frame(ws=webServices[c(1:16)],obs=rep(observations,2),s=sizesPlain)
respTimesMin = data.frame(ws=webServices[c(17:32)],obs=rep(observations,2),s=sizesMin)
respSize = data.frame(ws=webServices,obs=observations,s=sizes)


# Analyses
time_frost - time_sos

mean(time_frost - time_sos)



