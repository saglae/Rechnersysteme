#!/bin/bash

#Achtung! Skript ist nicht funktionsfähig. SED ist zeilenbasiert und muss in der Kommandozeile eingefügt werden. 

path=/sys/devices/w1_bus_master1/28-00000a549a9e
#anzahl_nachkommastellen=3
 
#cat $path/w1_slave | grep 't=' | awk -F = '{print $2}'|cut -c 1-2
temperature=cat /sys/devices/w1_bus_master1/28-00000a549a9e
/w1_slave | grep 't=' | awk -F = '{print $2}' |sed 's/\(..\)\(..\)./\1.\2°C/'

# temperature_formatted=`sed 's/\(..\)\(..\)./\1.\2°C/' < $temperature`

cat temperature
#cat temperature_formatted

