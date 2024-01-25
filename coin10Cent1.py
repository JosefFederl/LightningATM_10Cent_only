#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	GPIO.wait_for_edge(6, GPIO.FALLING)	
	f = open("amount.txt", "a")	
	f.write("1")
	f.flush()
	os.system('clear')
	print(os.path.getsize('amount.txt'), " x 100 Sats")
	f.close()
	time.sleep(0.1)
