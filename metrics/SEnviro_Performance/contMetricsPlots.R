library(ggplot2)

# General Data
observations = c(1,100,200,400,500,600,800,1000)
breakPointsExtre = c(1,100,200,300,400,500,600,700,800,900,1000)
webServices = c(rep("52N-SOS",8), rep("FROST",8))

# CPU Data
cpu_sos = c(4.56362,4.061076,5.941103,4.101744,4.098917,4.891219,5.167199,4.754338)
cpu_frost = c(28.02417,27.79759,36.92144,35.35104,31.78415,29.20752,37.9966,31.7985)

memory_sos = c(1.082397,1.082858,1.08334,1.083943,1.084413,1.084832,1.085033,1.085737) * 100
memory_frost = c(1.430068,1.430388,1.428887,1.421462,1.410519,1.384987,1.369538,1.377593143) * 100

memoryMB_sos = c(2736.235,2736.761,2737.451,2738.314,2738.987,2739.869,2740.689,2741.699)
memoryMB_frost = c(3292.553,3252.152,3235.036,3356.46,3339.015,3302.107,3334.228,3363.013)

rx_sos = c(55563.44,85758.64,63562.53,85239.97,81603.42,80062.66,86035.41,55624.07)
rx_frost = c(39765.89,293878.8,385053.8,471310.5,502368.8,573014.3,550962.8,593142)

tx_sos = c(111459,114252.5,111098.9,112425.8,108886.4,102989.1,114709.6,112435.5)
tx_frost = c(55297.28,1030404,1384252,1714001,1832846,2092936,2027332,2178644)

cpu = c(cpu_sos,cpu_frost)
memory = c(memory_sos,memory_frost)
memoryMB = c(memoryMB_sos,memoryMB_frost)
rx = c(rx_sos,rx_frost)
tx = c(tx_sos,tx_frost)

  
cpuDF = data.frame(ws=webServices,obs=rep(observations,2),cpu)
memoryMBDF = data.frame(ws=webServices,obs=rep(observations,2),memoryMB)
memoryDF = data.frame(ws=webServices,obs=rep(observations,2),memory)
rxDF = data.frame(ws=webServices,obs=rep(observations,2),rx)
txDF = data.frame(ws=webServices,obs=rep(observations,2),tx)
networkDF = data.frame(ws=webServices,obs=rep(observations,2),rx, tx)



ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/cpu.png", 
       ggplot(data=cpuDF,aes(x=obs, y=cpu)) + 
         ggtitle("Average container CPU usage for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='CPU Usage [%]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/memory.png", 
       ggplot(data=memoryDF,aes(x=obs, y=memory)) + 
         ggtitle("Average container memory usage for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='Memory Usage [%]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/memoryMB.png", 
       ggplot(data=memoryMBDF,aes(x=obs, y=memoryMB)) + 
         # ggtitle("Average container memory usage for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='Memory Usage [MB]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/rx.png", 
       ggplot(data=networkDF,aes(x=obs, y=rx)) + 
         ggtitle("Average received data (RX) per second for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='RX [bytes]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/tx.png", 
       ggplot(data=networkDF,aes(x=obs, y=tx)) + 
         ggtitle("Average transmitted data (TX) per second for observation retrieval") +
         geom_line(aes(linetype=ws)) + 
         geom_point(aes(shape=ws)) + 
         scale_x_continuous(breaks = observations) + 
         scale_linetype_manual("Web Services", values = c(1:4)) +
         scale_shape_manual("Web Services", values = c(15:18)) +
         labs(x='Observations', y='TX [bytes]') + 
         guides(guide_legend()) + 
         theme(plot.title = element_text(size = 15,hjust = 0.5),
               legend.key = element_blank(), 
               legend.position = "top", 
               legend.title = element_blank(),
               legend.box.just = "left"), 
       width = 8, height = 5, dpi = 300, units = "in", device='png')

# ggsave(filename = "D:/Bulk/Uni/UJI_2.0/MasterThesis/images/plots/rx.png", 
#        ggplot(data=networkDF,aes(x=obs, y=rx)) + 
#          ggtitle("Average received data (RX) and transmitted data (TX) per second for observation retrieval") +
#          geom_line(aes(linetype=ws)) + 
#          geom_point(aes(shape=ws)) + 
#          scale_x_continuous(breaks = observations) + 
#          scale_linetype_manual("Web Services", values = c(1:4)) +
#          scale_shape_manual("Web Services", values = c(15:18)) +
#          labs(x='Observations', y='RX/TX [bytes]') + 
#          guides(guide_legend()) + 
#          theme(plot.title = element_text(size = 15,hjust = 0.5),
#                legend.key = element_blank(), 
#                legend.position = "top", 
#                legend.title = element_blank(),
#                legend.box.just = "left"), 
#        width = 8, height = 5, dpi = 300, units = "in", device='png')
