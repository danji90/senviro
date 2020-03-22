library(ggplot2)

# General Data
observations = c(1,100,200,400,500,600,800,1000)
breakPointsExtre = c(1,100,200,300,400,500,600,700,800,900,1000)
webServices = c(rep("52N-SOS",8), rep("FROST",8), rep("52N-SOS Helgoland",8),  rep("FROST (reduced)",8))

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
size_sos = c(1.25,114,228,456,570,684,912,1110)
size_helgoSOS = c(0.34,2.56,4.8,9.29,11.54,13.79,18.28,22.77)
size_frost = c(0.593,56,111,223,279,334,446,557 )
size_frostMin = c(0.567,8.55,16.64,32.8,40.88,48.96,65.12,81.28)

sizesPlain = c(size_sos,size_frost)
sizesMin = c(size_helgoSOS,size_frostMin)
sizes = c(sizesPlain,sizesMin)

respSizePlain = data.frame(ws=webServices[c(1:16)],obs=rep(observations,2),s=sizesPlain)
respSizeMin = data.frame(ws=webServices[c(17:32)],obs=rep(observations,2),s=sizesMin)
respSize = data.frame(ws=webServices,obs=observations,s=sizes)


# Plots

# Response Time
ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/respTimePlot.png", 
       ggplot(data=respTime,aes(x=obs, y=t)) + 
         ggtitle("Average HTTP response times for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='Milliseconds [ms]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

# Response Time
ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/respTimePlotPlain.png", 
       ggplot(data=respTimePlain,aes(x=obs, y=t)) + 
         ggtitle("Average HTTP response times for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='Milliseconds [ms]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/respSizePlot.png", 
       ggplot(data=respSize,aes(x=obs, y=s)) + 
         ggtitle("Average HTTP response size for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='Kilobytes [kb]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/respSizePlotPlain.png", 
       ggplot(data=respSizePlain,aes(x=obs, y=s)) + 
         ggtitle("Average HTTP response size for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='Kilobytes [kb]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

  

