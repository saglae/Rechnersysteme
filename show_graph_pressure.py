#!/usr/bin/python3 

import rrdtool

filename = "/var/www/html/temperature_pressure.rrd"

ret = rrdtool.graph ('-',
		'--imgformat', 'PNG',
		'--width', '640',
		'--height', '400',
		'--start', 'now-1hour',
		'--end', 'now',
		'--vertical-label', "Grad Celsius",
		'--alt-autoscale',
		'--title', 'Temperatur',
		'DEF:pressure1='+filename+':temp1:AVERAGE',
		'AREA:temp1#ADD8E6:',
		'LINE1:temp1#006400:Temperatur DS18B20',
		'GPRINT:temp1:MIN:Min\\: %3.2lf °C',
		'GPRINT:temp1:MAX:Max\\: %3.2lf °C',
		'GPRINT:temp1:AVERAGE:Avg\\: %3.2lf °C',
		'GPRINT:temp1:LAST:Aktuell\\: %3.2lf °C') 



