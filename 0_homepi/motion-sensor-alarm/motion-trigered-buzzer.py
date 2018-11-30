import RPi.GPIO as GPIO
import time
import os
import sys
import re
import urllib2
from BeautifulSoup import BeautifulSoup
import subprocess


GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN) 
GPIO.setup(21, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT) 

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(20):
            GPIO.output(21, True)
            time.sleep(0.5) 
            GPIO.output(21, False)
            GPIO.output(15, True)
            print("motion detected....")
	    break 
except:
    GPIO.cleanup()
   