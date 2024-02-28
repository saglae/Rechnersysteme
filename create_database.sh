#!/bin/bash
 
#Früher!

#rrdtool create /home/glaesser/temperature --step 5 \
#DS:temp1:GAUGE:600:-30:100\  #-30°C bis 100 °C erfassbar
#RRA:AVERAGE:0.5:1:17280 \    # 4 Durchschnittswerte  #Einen Tag im 5s Takt
#RRA:AVERAGE:0.5:12:43200 \    # Immer 12 Werte zusammenfassen: 1 Monat
#RRA:AVERAGE:0.5:120:52560 \    #  Immer 120 Werte zusammen: 1 Jahr
#RRA:AVERAGE:0.5:17280:7300 \	# Immer 17280 (also Tage):  Wenn über 1 Jahr
#RRA:MIN:0.5:17280:7300 \
#RRA:MAX:0.5:17280:7300 \

rrdtool create /home/glaesser/temperature1.rrd --step 5 \
DS:temp1:GAUGE:600:-30:100 \
RRA:AVERAGE:0.5:5s:1d \
RRA:AVERAGE:0.5:1m:30d \
RRA:AVERAGE:0.5:10m:1y \
RRA:AVERAGE:0.5:1d:20y \
RRA:MIN:0.5:1d:20y \
RRA:MAX:0.5:1d:20y

