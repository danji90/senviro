library(dplyr)
library(anytime)
library(ggplot2)

sosString = "D:/Bulk/Uni/GitRepos/senviro/metrics/sos_1000_.csv"
frostString = "D:/Bulk/Uni/GitRepos/senviro/metrics/frost_1000_.csv"
sosIdleStr = "D:/Bulk/Uni/GitRepos/senviro/metrics/sosIdle.csv"
frostIdleStr = "D:/Bulk/Uni/GitRepos/senviro/metrics/frostIdle.csv"

sosData = read.csv(sosString, header = TRUE)
sosData$service = "52North-SOS"
sosData$request = "Active"
sosData$ID <- seq.int(nrow(sosData))

sosIdle = read.csv(sosIdleStr, header = TRUE)
sosIdle$service = "52North-SOS"
sosIdle$request = "Idle"
sosIdle$ID <- seq.int(nrow(sosIdle))

frostData = read.csv(frostString, header = TRUE)
frostData$service = "FROST"
frostData$request = "Active"
frostData$ID <- seq.int(nrow(frostData))

frostIdle = read.csv(frostIdleStr, header = TRUE)
frostIdle$service = "FROST"
frostIdle$request = "Idle"
frostIdle$ID <- seq.int(nrow(frostIdle))

dfFinal = rbind(sosData,frostData)

dfIdle = rbind(sosData,frostData,sosIdle,frostIdle)

sosDfIdle = rbind(sosData,sosIdle)

frostDfIdle = rbind(frostData,frostIdle)

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/cpu1000contrast.png", 
       ggplot(data=dfFinal,aes(x=ID, y=cpu_Percent)) + 
         ylim(0,100) +
         geom_line(aes(linetype=service)) + 
         # geom_point(aes(shape=service)) + 
         # scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c("solid","twodash")) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Seconds', y='CPU Usage [%]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/memory1000contrast.png", 
       ggplot(data=dfFinal,aes(x=ID, y=memory/1000000)) + 
         ggtitle("Container memory usage requesting 1000 observations") +
         ylim(2500,3500) + 
         geom_line(aes(linetype=service)) +
         # geom_point(aes(shape=service)) + 
         # scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c("solid","twodash")) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Seconds', y='Memory Usage [MB]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/cpuFrostDiff.png", 
       ggplot(data=frostDfIdle,aes(x=ID, y=cpu_Percent)) + 
         ylim(0,100) + 
         geom_line(aes(linetype=request)) + 
         # geom_point(aes(shape=service)) + 
         # scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         # scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Seconds', y='CPU Usage [%]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left",
               axis.text=element_text(size=12),
               axis.title=element_text(size=14),
               legend.text=element_text(size=14)), 
       width = 5, height = 4, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/cpuSosDiff.png", 
       ggplot(data=sosDfIdle,aes(x=ID, y=cpu_Percent)) + 
         ggtitle("Average container memory usage for observation retrieval") +
         ylim(0,100) + 
         geom_line(aes(linetype=request)) + 
         # geom_point(aes(shape=service)) + 
         # scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         # scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Seconds', y='CPU Usage [%]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left",
               axis.text=element_text(size=12),
               axis.title=element_text(size=14),
               legend.text=element_text(size=14)), 
       width = 5, height = 4, dpi = 300, units = "in", device='png')

# RAM

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/memFrostDiff.png", 
       ggplot(data=frostDfIdle,aes(x=ID, y=memory/1000000)) + 
         geom_line(aes(linetype=request)) + 
         # geom_point(aes(shape=service)) + 
         # scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         # scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Seconds', y='Memory Usage [MB]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left",
               axis.text=element_text(size=12),
               axis.title=element_text(size=14),
               legend.text=element_text(size=14)), 
       width = 5, height = 4, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/memSosDiff.png", 
       ggplot(data=sosDfIdle,aes(x=ID, y=memory/1000000)) + 
         geom_line(aes(linetype=request)) + 
         # geom_point(aes(shape=service)) + 
         # scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         # scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Seconds', y='Memory Usage [MB]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left",
               axis.text=element_text(size=12),
               axis.title=element_text(size=14),
               legend.text=element_text(size=14)), 
       width = 5, height = 4, dpi = 300, units = "in", device='png')



