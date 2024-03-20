#!/usr/bin/python3

import spidev
spi = spidev.SpiDev()
spi.open(0,0)

# spi.xfer([array of bytes],frequenz)

frequency = 6.4e+6
leds = {"1": [100,0,0], "2": [0,100,0], "3": [0,0,100], "4": [100,100,0], "5": [0,100,100]}


while True: 
	for led in leds: 
		red =  leds[led][0]
		green = leds[led][1]
		blue =  leds[led][2]
		
		#Decode! 


		bytes_to_send = []
		for colour in {green, red, blue}:
			for bit in range(7,-1,-1):		#Wichtig! Reihenfolge beachten
				if ((colour >> bit) & 1) == 0:   #True wenn Wert ungleich 0
					bytes_to_send.append(0x80)
				else:
					bytes_to_send.append(0x78)

		spi.xfer(bytes_to_send,int(frequency))
		#print(bytes_to_send)
	#print("-------------------------")
