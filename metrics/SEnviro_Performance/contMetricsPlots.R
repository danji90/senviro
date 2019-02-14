library(ggplot2)

# General Data
observations = c(1,100,200,400,500,600,800,1000)
breakPointsExtre = c(1,100,200,300,400,500,600,700,800,900,1000)
webServices = c(rep("52N-SOS",8), rep("FROST",8))

# CPU Data
cpu_sos = c(2.631539,3.083289,2.591387,2.635106,2.789394,2.848171,3.013961,2.67153)
cpu_frost = c(4.42405,12.06288,14.84101,17.00324,18.8907,20.97674,20.90836,22.31597)

memory_sos = c(1.082397,1.082858,1.08334,1.083943,1.084413,1.084832,1.085033,1.085737) * 100
memory_frost = c(1.430068,1.430388,1.428887,1.421462,1.410519,1.384987,1.369538,1.377593143) * 100

rx_sos = c(55563.44,85758.64,63562.53,85239.97,81603.42,80062.66,86035.41,55624.07)
rx_frost = c(39765.89,293878.8,385053.8,471310.5,502368.8,573014.3,550962.8,593142)

tx_sos = c(111459,114252.5,111098.9,112425.8,108886.4,102989.1,114709.6,112435.5)
tx_frost = c(55297.28,1030404,1384252,1714001,1832846,2092936,2027332,2178644)

cpu = c(cpu_sos,cpu_frost)
memory = c(memory_sos,memory_frost)
rx = c(rx_sos,rx_frost)
tx = c(tx_sos,tx_frost)

  
cpuDF = data.frame(ws=webServices,obs=rep(observations,2),cpu)
memoryDF = data.frame(ws=webServices,obs=rep(observations,2),memory)
rxDF = data.frame(ws=webServices,obs=rep(observations,2),rx)
txDF = data.frame(ws=webServices,obs=rep(observations,2),tx)
networkDF = data.frame(ws=webServices,obs=rep(observations,2),rx, tx)



# Plots

# Response Time
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
