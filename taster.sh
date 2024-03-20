#!/bin/bash

echo 21 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio21/direction


echo 13 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio13/direction

while true;
do
if grep -q 1 /sys/class/gpio/gpio13/value; then echo 1 > /sys/class/gpio/gpio21/value; else echo 0 > /sys/class/gpio/gpio21/value; fi
done  

