import RPi.GPIO as GPIO
import sys
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
	pin =  15 # pin 11 on the RP board
	GPIO.setup(pin, GPIO.OUT)
	state = 0
	GPIO.output(pin, (GPIO.LOW if state == 0 else GPIO.HIGH))
	GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, (GPIO.LOW if 0 == 0 else GPIO.HIGH))
finally:
	 GPIO.cleanup()
   