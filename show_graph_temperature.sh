#!/bin/bash 

filename="/home/glaesser/temperature1.rrd"

rrdtool graph temperature1.png \
		--imgformat 'PNG' \
		--width 640 \
		--height 440 \
		--start -1hour \
		--end now \
		--vertical-label "Grad Celsius" \
		--alt-autoscale \
		--title Temperatur \
		DEF:temp1=$filename:temp1:AVERAGE \
		AREA:temp1#FFFFFF: \
		LINE1:temp1#FF0000:'Temperatur DS18B20' \
		GPRINT:temp1:MIN:"Min\\: %3.2lf °C " \
		GPRINT:temp1:MAX:"Max\\: %3.2lf °C " \
		GPRINT:temp1:AVERAGE:"Avg\\: %3.2lf °C " \
		GPRINT:temp1:LAST:"Aktuell\\: %3.2lf °C " 

sudo cp /home/glaesser/temperature1.png /var/www/html

