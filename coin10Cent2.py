#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os
import json
import requests
import pyqrcode          #https://pypi.org/project/PyQRCode/#description @raspberrypi:~/Downloads/PyQRCode-1.2.1 $ sudo python setup.py install
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def create_lnurlw():
    data = {
        "title": "10Cent_Entsorgung",
        "min_withdrawable": 100 * inserted_coins,
        "max_withdrawable": 100 * inserted_coins,
        "uses": 1,
        "wait_time": 10,
        "is_unique": True,
    }
    response = requests.post(
        url="https://legend.lnbits.com/withdraw/api/v1/links/",
        headers={"X-Api-Key": "fuck_off_EZB"},
        data=json.dumps(data),
    )
    res_json = response.json()
    if res_json.get("detail"):
        errormessage = res_json.get("detail")
        print("Error: " + errormessage)
    else:
        return res_json


while True:
	GPIO.wait_for_edge(21, GPIO.FALLING)	
	inserted_coins = os.path.getsize('amount.txt')
	if inserted_coins == 0:
		print("0 x 10Cent ergibt 0 Sats :-) ")
		time.sleep(2)
		continue
	res_json = create_lnurlw()	
	url = pyqrcode.create(res_json.get("lnurl"))
	url.svg('uca-url.svg', scale=5)
	url.eps('uca-url.eps', scale=1)
	print(url.terminal(quiet_zone=1))
	time.sleep(4)
	open("amount.txt", 'w').close()	
