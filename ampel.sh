#!/bin/bash

if ! test -e /sys/class/gpio/gpio16; then echo 16 > /sys/class/gpio/export; fi
if ! test -e /sys/class/gpio/gpio20; then echo 20 > /sys/class/gpio/export; fi
if ! test -e /sys/class/gpio/gpio21; then echo 21 > /sys/class/gpio/export; fi


echo out > /sys/class/gpio/gpio16/direction
echo out > /sys/class/gpio/gpio20/direction
echo out > /sys/class/gpio/gpio21/direction

echo 0 > /sys/class/gpio/gpio16/value
echo 0 > /sys/class/gpio/gpio20/value
echo 0 > /sys/class/gpio/gpio21/value



while true;
do
	sleep 2
	echo 1 > /sys/class/gpio/gpio16/value
	echo 0 > /sys/class/gpio/gpio20/value
	echo 0 > /sys/class/gpio/gpio21/value 

	sleep 2
	echo 1 > /sys/class/gpio/gpio16/value
	echo 1 > /sys/class/gpio/gpio20/value
	echo 0 > /sys/class/gpio/gpio21/value   

	sleep 2
	echo 0 > /sys/class/gpio/gpio16/value
	echo 0 > /sys/class/gpio/gpio20/value
	echo 1 > /sys/class/gpio/gpio21/value  

	sleep 2
	echo 0 > /sys/class/gpio/gpio16/value
	echo 1 > /sys/class/gpio/gpio20/value
	echo 0 > /sys/class/gpio/gpio21/value  

done
