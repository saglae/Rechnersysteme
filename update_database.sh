#!/bin/bash

while true; do
	sleep 5

	value=`cat /sys/devices/w1_bus_master1/28-00000a549a9e/w1_slave | grep 't=' | awk -F = '{print $2}' |sed 's/\(..\)\(..\)./\1.\2/'`
	echo $value
	rrdupdate /var/www/html/temperature1.rrd N:$value
done
# N: Aktueller Zeitstempel
